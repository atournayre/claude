# Kyutai TTS - Notifications Vocales pour Claude Code

Service de synthèse vocale (Text-to-Speech) basé sur Kyutai TTS pour les notifications Claude Code.

## Vue d'ensemble

**Kyutai TTS** est un modèle open-source de synthèse vocale qui génère des notifications vocales naturelles en français et anglais pour Claude Code.

### Caractéristiques

- **Modèle**: `kyutai/tts-1.6b-en_fr` (1.6B paramètres)
- **Langues**: Français, Anglais
- **Latence**: 220-350ms
- **GPU**: NVIDIA requis (8GB+ VRAM)
- **Qualité**: Voix naturelle, streaming audio
- **API**: Compatible OpenAI TTS API

## Prérequis

- Ubuntu/Debian Linux
- Docker 20.10+
- GPU NVIDIA avec 8GB+ VRAM
- Driver NVIDIA 470+
- 20GB espace disque libre

## Installation

### Installation automatique

```bash
cd ~/.claude/scripts/kyutai-tts-installer
./install.sh
```

Le script effectue:

1. ✓ Vérification Docker + GPU NVIDIA
2. ✓ Installation nvidia-container-toolkit (sudo requis)
3. ✓ Clone repository Kyutai TTS API dans `~/.local/share/kyutai-tts`
4. ✓ Configuration port 9876 (évite conflits)
5. ✓ Build container Docker (~10 min, 7.5GB)
6. ✓ Création service systemd user (auto-start au boot)
7. ✓ Démarrage API
8. ✓ Copie wrapper notification dans `~/.claude/scripts/`

### Structure après installation

```
~/.local/share/kyutai-tts/         # Installation API
├── docker-compose.yaml
├── dockerfile
├── api_server.py
├── tts_runner.py
├── test_tts.py
├── cache/                         # Modèles Hugging Face (2GB)
├── input/
├── output/
└── scripts/

~/.config/systemd/user/
└── kyutai-tts.service             # Service auto-start

~/.claude/scripts/
├── kyutai-tts-installer/          # Installer (réutilisable)
│   ├── install.sh
│   ├── notification-kyutai.py
│   ├── Dockerfile
│   ├── tts_runner.py
│   ├── test_tts.py
│   └── README.md
└── notification-kyutai.py         # Hook Claude Code
```

## Configuration Claude Code

Le script d'installation configure automatiquement `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [{"type": "command", "command": "~/.claude/scripts/notification-kyutai.py"}]
      },
      {
        "matcher": "idle_prompt",
        "hooks": [{"type": "command", "command": "~/.claude/scripts/notification-kyutai.py"}]
      },
      {
        "matcher": "auth_success",
        "hooks": [{"type": "command", "command": "~/.claude/scripts/notification-kyutai.py"}]
      },
      {
        "matcher": "elicitation_dialog",
        "hooks": [{"type": "command", "command": "~/.claude/scripts/notification-kyutai.py"}]
      }
    ]
  }
}
```

### Messages vocaux

| Type notification     | Phrase vocale                   |
|----------------------|----------------------------------|
| `permission_prompt`  | "Demande de permission"         |
| `idle_prompt`        | "En attente de votre réponse"   |
| `auth_success`       | "Authentification réussie"      |
| `elicitation_dialog` | "Information requise"           |

### Voix disponibles

Le système utilise des voix françaises du dataset CML-TTS pour un accent français européen.

| Nom    | Source CML                                | Caractéristiques          |
|--------|-------------------------------------------|---------------------------|
| alloy  | `cml-tts/fr/12977_10625_000037-0001.wav` | Voix neutre, claire       |
| echo   | `cml-tts/fr/1406_1028_000009-0003.wav`   | Voix douce, posée         |
| fable  | `cml-tts/fr/10087_11650_000028-0002.wav` | Voix narrative            |
| **onyx** | `cml-tts/fr/10177_10625_000134-0003.wav` | **Voix française recommandée** |
| nova   | `cml-tts/fr/12977_10625_000037-0001.wav` | Voix énergique            |
| shimmer | `cml-tts/fr/1406_1028_000009-0003.wav`  | Voix chaleureuse          |

**Voix par défaut**: `onyx` (accent français européen)

#### Changer la voix

**Méthode 1: Configuration Claude Code (recommandée)**

Ajouter dans `~/.claude/settings.json`:

```json
{
  "env": {
    "KYUTAI_VOICE": "onyx",
    "ENGINEER_NAME": "Aurélien"
  }
}
```

Redémarrer Claude Code pour appliquer les changements.

**Méthode 2: Variable d'environnement shell**

Ajouter dans `~/.bashrc` ou `~/.zshrc`:

```bash
export KYUTAI_VOICE="onyx"  # ou alloy, echo, fable, nova, shimmer
export ENGINEER_NAME="Aurélien"
```

Puis recharger:
```bash
source ~/.bashrc
```

**Méthode 3: Modifier le script directement**

Éditer `~/.claude/scripts/notification-kyutai.py`:

```python
DEFAULT_VOICE = os.getenv("KYUTAI_VOICE", "onyx")  # Changer "onyx" ici
```

#### Tester les voix

```bash
# Tester toutes les voix
for voice in alloy echo fable onyx nova shimmer; do
  echo "Test: $voice"
  curl -X POST http://localhost:9876/v1/audio/speech \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"tts-1\",\"input\":\"Bonjour, je suis la voix $voice\",\"voice\":\"$voice\",\"response_format\":\"wav\"}" \
    --output "/tmp/test-$voice.wav"
  paplay "/tmp/test-$voice.wav"
  sleep 2
done
```

#### Ajouter de nouvelles voix françaises

Le dataset CML-TTS contient 382 voix françaises. Pour en ajouter :

1. Lister les voix disponibles:
```bash
docker exec kyutai-tts-gpu python3 -c "
from huggingface_hub import list_repo_files
files = list_repo_files('kyutai/tts-voices', repo_type='model')
french_voices = [f for f in files if 'cml-tts/fr/' in f and f.endswith('.safetensors')]
for v in french_voices[:20]:
    print(v)
"
```

2. Télécharger une voix:
```bash
docker exec kyutai-tts-gpu python3 -c "
from huggingface_hub import hf_hub_download
import os
os.environ['HF_HOME'] = '/app/cache'
hf_hub_download(
    repo_id='kyutai/tts-voices',
    filename='cml-tts/fr/VOTRE_VOIX.wav.1e68beda@240.safetensors'
)
"
```

3. Modifier le mapping dans `~/.local/share/kyutai-tts/api_server.py`:
```python
voice_mapping = {
    "alloy": "cml-tts/fr/VOTRE_NOUVELLE_VOIX.wav",
    # ...
}
```

4. Redémarrer le service:
```bash
systemctl --user restart kyutai-tts
```

### Personnalisation

**Option 1: Messages par défaut**

Modifier `~/.claude/scripts/notification-kyutai.py`:

```python
DEFAULT_MESSAGES = {
    "permission_prompt": "Votre message personnalisé",
    "idle_prompt": "En attente",
    ...
}
```

**Option 2: Message custom dans hook**

Le script lit le champ `message` du JSON si présent:

```json
{
  "notification_type": "permission_prompt",
  "message": "Attention requise immédiatement"
}
```

**Option 3: Variables d'environnement**

**Via Claude Code settings.json** (recommandé):
```json
{
  "env": {
    "KYUTAI_VOICE": "onyx",
    "ENGINEER_NAME": "Aurélien"
  }
}
```

**Via shell** (`~/.bashrc`):
```bash
export KYUTAI_VOICE="onyx"
export ENGINEER_NAME="Aurélien"
```

Le script utilise ces variables pour:
- `KYUTAI_VOICE`: Choix de la voix (onyx, alloy, echo, fable, nova, shimmer)
- `ENGINEER_NAME`: Personnalisation messages (30% du temps) - "Aurélien, demande de permission"

## Gestion du service

### Commandes systemd

```bash
# Démarrer
systemctl --user start kyutai-tts

# Arrêter
systemctl --user stop kyutai-tts

# Redémarrer
systemctl --user restart kyutai-tts

# Statut
systemctl --user status kyutai-tts

# Logs temps réel
journalctl --user -fu kyutai-tts

# Désactiver auto-start
systemctl --user disable kyutai-tts

# Réactiver auto-start
systemctl --user enable kyutai-tts
```

### Commandes Docker

```bash
cd ~/.local/share/kyutai-tts

# Voir logs container
docker compose logs -f

# Redémarrer container
docker compose restart

# Stopper container
docker compose down

# Rebuild après modification
docker compose build --no-cache
docker compose up -d
```

## Tests

### Test API directement

```bash
# Health check
curl http://localhost:9876/health

# Générer audio WAV
curl -X POST http://localhost:9876/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"model":"tts-1","input":"Bonjour monde","voice":"alloy","response_format":"wav"}' \
  --output test.wav

# Écouter résultat (avec paplay)
paplay test.wav
```

### Test wrapper notification

```bash
# Test simple
echo '{"notification_type":"permission_prompt"}' | \
  ~/.claude/scripts/notification-kyutai.py

# Test avec message custom
echo '{"notification_type":"idle_prompt","message":"Action requise"}' | \
  ~/.claude/scripts/notification-kyutai.py

# Test avec ENGINEER_NAME
ENGINEER_NAME="Aurélien" echo '{"notification_type":"auth_success"}' | \
  ~/.claude/scripts/notification-kyutai.py
```

Les notifications sont loguées dans `~/.claude/logs/kyutai-notifications.jsonl`.

### Test via Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="dummy",
    base_url="http://localhost:9876/v1"
)

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Demande de permission",
    response_format="mp3"
)

with open("notification.mp3", "wb") as f:
    f.write(response.content)
```

## API Reference

### Endpoint: POST /v1/audio/speech

**Paramètres:**
- `model`: "tts-1" ou "tts-1-hd"
- `input`: Texte (1-4096 caractères)
- `voice`: alloy, echo, fable, onyx, nova, shimmer
- `response_format`: mp3, wav, flac, aac, opus, pcm
- `speed`: 0.25-4.0 (optionnel)

**Exemple:**
```bash
curl -X POST http://localhost:9876/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "Authentification réussie",
    "voice": "alloy",
    "response_format": "wav",
    "speed": 1.0
  }' \
  --output audio.wav
```

### Endpoint: GET /v1/models

Liste modèles disponibles.

### Endpoint: GET /health

Health check service.

**Réponse:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "cuda_available": true,
  "device": "cuda",
  "service": "kyutai-tts-openai-compatible-cached"
}
```

## Performance

### Métriques attendues

- **Latence première génération**: ~2-5s (téléchargement modèle)
- **Latence suivantes**: ~220-350ms
- **VRAM utilisée**: ~2-3GB
- **RAM système**: ~4GB
- **Taille cache modèles**: ~2GB
- **Taille image Docker**: ~7.5GB

### Optimisations

**Pré-charger modèles au démarrage:**

Modifier `~/.local/share/kyutai-tts/docker-compose.yaml`:
```yaml
command: sh -c "python test_tts.py && python api_server.py"
```

**Augmenter timeout systemd:**

Modifier `~/.config/systemd/user/kyutai-tts.service`:
```ini
[Service]
TimeoutStartSec=300
```

## Troubleshooting

### Service ne démarre pas

```bash
# Vérifier logs
journalctl --user -u kyutai-tts -n 50

# Vérifier Docker
docker ps -a | grep kyutai

# Tester manuellement
cd ~/.local/share/kyutai-tts
docker compose up
```

### Erreur GPU

```bash
# Vérifier NVIDIA runtime
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi

# Réinstaller nvidia-container-toolkit
sudo apt-get purge nvidia-container-toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### API ne répond pas

```bash
# Vérifier port disponible
ss -tuln | grep 9876

# Tester depuis container
docker exec kyutai-tts-gpu curl http://localhost:8000/health

# Vérifier logs API
cd ~/.local/share/kyutai-tts
docker compose logs -f
```

### Audio ne joue pas

```bash
# Vérifier paplay installé
command -v paplay || sudo apt-get install -y pulseaudio-utils

# Tester sortie audio
paplay /usr/share/sounds/freedesktop/stereo/complete.oga

# Test génération WAV
curl -X POST http://localhost:9876/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"model":"tts-1","input":"Test","response_format":"wav"}' \
  --output /tmp/test.wav
paplay /tmp/test.wav
```

### Permissions cache Docker

Si erreurs de permissions dans le cache:

```bash
# Arrêter service
systemctl --user stop kyutai-tts

# Nettoyer containers et volumes
cd ~/.local/share/kyutai-tts
docker compose down -v

# Supprimer cache avec sudo si nécessaire
sudo rm -rf ~/.local/share/kyutai-tts/cache

# Redémarrer
systemctl --user start kyutai-tts
```

## Réinstallation

```bash
# Exécuter installer (gère automatiquement le nettoyage)
cd ~/.claude/scripts/kyutai-tts-installer
./install.sh
```

Le script propose de supprimer l'installation existante et nettoie automatiquement:
- Service systemd
- Containers Docker
- Fichiers avec permissions root (via sudo)

## Désinstallation

```bash
# Stopper et désactiver service
systemctl --user stop kyutai-tts
systemctl --user disable kyutai-tts

# Supprimer service
rm ~/.config/systemd/user/kyutai-tts.service
systemctl --user daemon-reload

# Supprimer container et image
cd ~/.local/share/kyutai-tts
docker compose down -v
docker rmi kyutai-tts:latest

# Supprimer fichiers
sudo rm -rf ~/.local/share/kyutai-tts
rm ~/.claude/scripts/notification-kyutai.py
rm ~/.claude/logs/kyutai-notifications.jsonl

# Restaurer ancien hook (optionnel)
# Modifier ~/.claude/settings.json
```

## Licence

- Code API wrapper: MIT
- Modèles Kyutai TTS: CC-BY 4.0
- Moshi package: Apache 2.0

## Support

- **API wrapper**: https://github.com/dwain-barnes/kyutai-tts-openai-api
- **Kyutai Labs**: https://github.com/kyutai-labs
- **Documentation Kyutai**: https://kyutai.org/next/tts
- **Modèle Hugging Face**: https://huggingface.co/kyutai/tts-1.6b-en_fr

## Références

- [Documentation Claude Code Hooks](../docs/claude/hooks.md)
- [Installation nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- [Docker Compose](https://docs.docker.com/compose/)
- [Systemd User Services](https://wiki.archlinux.org/title/Systemd/User)
