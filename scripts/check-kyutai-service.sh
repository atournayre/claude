#!/bin/bash

API_URL="http://localhost:9876/v1/audio/speech"
TEMP_FILE="/tmp/claude-startup-${$}.wav"
CONTAINER_NAME="kyutai-tts-gpu"
MAX_RETRIES=10
RETRY_DELAY=2

# Fonction pour tester l'API
test_api() {
    curl -s --connect-timeout 3 -X POST "$API_URL" \
        -H "Content-Type: application/json" \
        -d '{"input": "Claude démarré", "voice": "'"${KYUTAI_VOICE:-onyx}"'", "model": "tts-1", "response_format": "wav", "language": "'"${KYUTAI_LANGUAGE:-fr}"'"}' \
        -o "$TEMP_FILE" -w "%{http_code}" 2>/dev/null
}

# Fonction pour attendre que l'API soit prête
wait_for_api() {
    for i in $(seq 1 $MAX_RETRIES); do
        response=$(test_api)
        if [ "$response" = "200" ]; then
            echo "$response"
            return 0
        fi
        sleep $RETRY_DELAY
    done
    echo "$response"
    return 1
}

# 1. Vérifier si le container tourne
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "🔄 Démarrage du service Kyutai TTS..."
    if ! docker start "$CONTAINER_NAME" 2>/dev/null; then
        echo "❌ Erreur: Container $CONTAINER_NAME non trouvé"
        echo "   Créer avec: docker compose up -d kyutai"
        exit 1
    fi
    echo "⏳ Attente du service (max ${MAX_RETRIES}x${RETRY_DELAY}s)..."
    response=$(wait_for_api)
else
    # 2. Tester l'API
    response=$(test_api)
fi

# 3. Si erreur 500, nettoyer le cache GPU et réessayer
if [ "$response" = "500" ]; then
    echo "🔧 Nettoyage cache GPU..."
    docker exec "$CONTAINER_NAME" rm -rf /tmp/torchinductor_root /root/.triton 2>/dev/null
    docker restart "$CONTAINER_NAME" 2>/dev/null
    echo "⏳ Attente du service (max ${MAX_RETRIES}x${RETRY_DELAY}s)..."
    response=$(wait_for_api)
fi

# 4. Jouer le son si OK
if [ "$response" = "200" ] && [ -f "$TEMP_FILE" ] && [ -s "$TEMP_FILE" ]; then
    aplay -q "$TEMP_FILE" 2>/dev/null || paplay "$TEMP_FILE" 2>/dev/null || ffplay -nodisp -autoexit -loglevel quiet "$TEMP_FILE" 2>/dev/null || true
    rm -f "$TEMP_FILE"
    exit 0
else
    rm -f "$TEMP_FILE"
    echo "❌ Erreur: Service Kyutai TTS indisponible (HTTP $response)"
    echo "   URL: $API_URL"
    echo "   Logs: docker logs $CONTAINER_NAME"
    exit 1
fi
