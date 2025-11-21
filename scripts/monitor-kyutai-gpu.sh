#!/bin/bash
# Vérifie l'accès GPU du conteneur Kyutai et notifie en cas d'erreur

CONTAINER_NAME="kyutai-tts-gpu"
NOTIFY_SCRIPT="$HOME/.claude/scripts/notification-kyutai.py"

# Test accès GPU dans le conteneur
if ! docker exec "$CONTAINER_NAME" nvidia-smi --query-gpu=name --format=csv,noheader &>/dev/null; then
    # Notification desktop persistante (critical = ne disparaît pas)
    notify-send -u critical -i dialog-error "Kyutai TTS" "Perte d'accès GPU - Redémarrage en cours..."
    # Notification vocale
    echo '{"notification_type": "error", "message": "Kyutai TTS a perdu accès au GPU, redémarrage en cours"}' | python3 "$NOTIFY_SCRIPT"

    # Redémarrer le conteneur
    docker restart "$CONTAINER_NAME"

    # Attendre et vérifier
    sleep 10
    if docker exec "$CONTAINER_NAME" nvidia-smi &>/dev/null; then
        notify-send -u normal -i dialog-information "Kyutai TTS" "Redémarré avec succès"
        echo '{"notification_type": "info", "message": "Kyutai TTS redémarré avec succès"}' | python3 "$NOTIFY_SCRIPT"
    else
        notify-send -u critical -i dialog-error "Kyutai TTS" "Échec du redémarrage - Intervention manuelle requise"
        echo '{"notification_type": "error", "message": "Échec du redémarrage de Kyutai TTS"}' | python3 "$NOTIFY_SCRIPT"
    fi
fi
