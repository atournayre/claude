#!/bin/bash
set -e

echo "=========================================="
echo "Installation Kyutai TTS - Système Global"
echo "=========================================="
echo ""

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

INSTALL_DIR="$HOME/.local/share/kyutai-tts"
API_PORT=9876

# Fonction de log
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Vérifier si script exécuté avec sudo
if [ "$EUID" -eq 0 ]; then
    log_error "Ne pas exécuter ce script avec sudo"
    log_info "Le script demandera sudo uniquement quand nécessaire"
    exit 1
fi

echo "Étape 1/8: Vérification prérequis"
echo "-----------------------------------"

# Vérifier Docker
if ! command -v docker &> /dev/null; then
    log_error "Docker n'est pas installé"
    exit 1
fi
log_info "Docker: $(docker --version)"

# Vérifier GPU NVIDIA
if ! command -v nvidia-smi &> /dev/null; then
    log_error "nvidia-smi non trouvé - GPU NVIDIA requis"
    exit 1
fi
GPU_INFO=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader)
log_info "GPU: $GPU_INFO"

echo ""
echo "Étape 2/8: Installation nvidia-container-toolkit"
echo "-------------------------------------------------"

if ! dpkg -l | grep -q nvidia-container-toolkit; then
    log_info "Ajout dépôt NVIDIA (sudo requis)..."

    # Ajouter clé GPG NVIDIA
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
        sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

    # Ajouter dépôt NVIDIA
    curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
        sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list > /dev/null

    log_info "Installation nvidia-container-toolkit..."
    sudo apt-get update
    sudo apt-get install -y nvidia-container-toolkit

    log_info "Configuration Docker pour NVIDIA..."
    sudo nvidia-ctk runtime configure --runtime=docker
    sudo systemctl restart docker

    log_info "nvidia-container-toolkit installé"
else
    log_info "nvidia-container-toolkit déjà installé"
fi

echo ""
echo "Étape 3/8: Configuration répertoire installation"
echo "------------------------------------------------"

if [ -d "$INSTALL_DIR" ]; then
    log_warn "Répertoire $INSTALL_DIR existe déjà"
    read -p "Supprimer et réinstaller? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # Arrêter service si actif
        if systemctl --user is-active --quiet kyutai-tts.service 2>/dev/null; then
            log_info "Arrêt du service..."
            systemctl --user stop kyutai-tts.service
        fi

        # Nettoyer container et volumes Docker
        if [ -f "$INSTALL_DIR/docker-compose.yaml" ]; then
            log_info "Nettoyage containers Docker..."
            cd "$INSTALL_DIR"
            docker compose down -v 2>/dev/null || true
        fi

        # Supprimer répertoire (avec sudo si permissions insuffisantes)
        log_info "Suppression répertoire..."
        if ! rm -rf "$INSTALL_DIR" 2>/dev/null; then
            log_warn "Permissions insuffisantes, utilisation de sudo..."
            sudo rm -rf "$INSTALL_DIR"
        fi

        log_info "Répertoire supprimé"
    else
        log_error "Installation annulée"
        exit 1
    fi
fi

mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"
log_info "Répertoire créé: $INSTALL_DIR"

echo ""
echo "Étape 4/8: Téléchargement Kyutai TTS API"
echo "----------------------------------------"

git clone https://github.com/dwain-barnes/kyutai-tts-openai-api.git .
mkdir -p input output cache scripts

log_info "Repository cloné"

echo ""
echo "Étape 5/8: Configuration Docker Compose"
echo "---------------------------------------"

# Supprimer version obsolète
sed -i '/^version:/d' docker-compose.yaml

# Changer port
sed -i "s/- \"8000:8000\"/- \"$API_PORT:8000\"/" docker-compose.yaml

# Copier scripts personnalisés depuis le répertoire de l'installer
SCRIPT_DIR="$HOME/.claude/scripts/kyutai-tts-installer"
if [ -f "$SCRIPT_DIR/tts_runner.py" ]; then
    cp "$SCRIPT_DIR/tts_runner.py" .
    cp "$SCRIPT_DIR/test_tts.py" .
    cp "$SCRIPT_DIR/Dockerfile" ./dockerfile
    log_info "Scripts personnalisés copiés"
else
    log_warn "Scripts personnalisés non trouvés dans $SCRIPT_DIR"
    log_info "Utilisation des fichiers par défaut du repository"
fi

log_info "Port API configuré: $API_PORT"

echo ""
echo "Étape 6/8: Build container Docker (5-10 min)"
echo "--------------------------------------------"

docker compose build

log_info "Container built: $(docker images | grep kyutai-tts | awk '{print $3}')"

echo ""
echo "Étape 7/8: Création service systemd"
echo "-----------------------------------"

SERVICE_FILE="$HOME/.config/systemd/user/kyutai-tts.service"
mkdir -p "$HOME/.config/systemd/user"

cat > "$SERVICE_FILE" << EOF
[Unit]
Description=Kyutai TTS OpenAI-Compatible API

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=$INSTALL_DIR
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
EOF

log_info "Service systemd créé: $SERVICE_FILE"

# Activer service
systemctl --user daemon-reload
systemctl --user enable kyutai-tts.service
log_info "Service activé au démarrage"

echo ""
echo "Étape 8/8: Démarrage service"
echo "---------------------------"

systemctl --user start kyutai-tts.service
sleep 5

# Vérifier statut
if systemctl --user is-active --quiet kyutai-tts.service; then
    log_info "Service démarré avec succès"

    # Attendre que API soit prête
    log_info "Attente démarrage API..."
    for i in {1..30}; do
        if curl -s http://localhost:$API_PORT/health > /dev/null 2>&1; then
            log_info "API prête sur http://localhost:$API_PORT"
            break
        fi
        sleep 2
    done
else
    log_error "Échec démarrage service"
    log_info "Logs: journalctl --user -u kyutai-tts.service"
    exit 1
fi

# Copier wrapper notification dans .claude/scripts
CLAUDE_SCRIPT_DIR="$HOME/.claude/scripts"
if [ -d "$CLAUDE_SCRIPT_DIR" ]; then
    cp "$SCRIPT_DIR/notification-kyutai.sh" "$CLAUDE_SCRIPT_DIR/"
    chmod +x "$CLAUDE_SCRIPT_DIR/notification-kyutai.sh"
    log_info "Wrapper notification copié: $CLAUDE_SCRIPT_DIR/notification-kyutai.sh"
fi

echo ""
echo "=========================================="
echo "Installation terminée avec succès!"
echo "=========================================="
echo ""
log_info "Service: systemctl --user status kyutai-tts.service"
log_info "Logs: journalctl --user -fu kyutai-tts.service"
log_info "API: http://localhost:$API_PORT"
log_info "Docs: http://localhost:$API_PORT/docs"
echo ""
log_info "Pour activer dans Claude Code, modifier ~/.claude/settings.json:"
echo ""
echo "  \"Notification\": ["
echo "    {"
echo "      \"matcher\": \"permission_prompt\","
echo "      \"hooks\": [{\"type\": \"command\", \"command\": \"~/.claude/scripts/notification-kyutai.sh\"}]"
echo "    },"
echo "    {"
echo "      \"matcher\": \"idle_prompt\","
echo "      \"hooks\": [{\"type\": \"command\", \"command\": \"~/.claude/scripts/notification-kyutai.sh\"}]"
echo "    },"
echo "    {"
echo "      \"matcher\": \"auth_success\","
echo "      \"hooks\": [{\"type\": \"command\", \"command\": \"~/.claude/scripts/notification-kyutai.sh\"}]"
echo "    },"
echo "    {"
echo "      \"matcher\": \"elicitation_dialog\","
echo "      \"hooks\": [{\"type\": \"command\", \"command\": \"~/.claude/scripts/notification-kyutai.sh\"}]"
echo "    }"
echo "  ]"
echo ""
log_info "Test API:"
echo "curl -X POST http://localhost:$API_PORT/v1/audio/speech \\"
echo "  -H 'Content-Type: application/json' \\"
echo "  -d '{\"model\":\"tts-1\",\"input\":\"Bonjour\",\"voice\":\"alloy\"}' \\"
echo "  --output test.mp3"
echo ""
log_info "Commandes systemd:"
echo "  systemctl --user start kyutai-tts    # Démarrer"
echo "  systemctl --user stop kyutai-tts     # Arrêter"
echo "  systemctl --user restart kyutai-tts  # Redémarrer"
echo "  systemctl --user status kyutai-tts   # Statut"
echo ""
