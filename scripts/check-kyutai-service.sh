#!/bin/bash

API_URL="http://localhost:9876/v1/audio/speech"
TEMP_FILE="/tmp/claude-startup-${$}.wav"

# Test si le service répond
response=$(curl -s --connect-timeout 2 -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d '{"input": "Claude démarré", "voice": "'"${KYUTAI_VOICE:-onyx}"'"}' \
    -o "$TEMP_FILE" -w "%{http_code}" 2>/dev/null)

if [ "$response" = "200" ] && [ -f "$TEMP_FILE" ] && [ -s "$TEMP_FILE" ]; then
    # Service OK, jouer le son
    aplay -q "$TEMP_FILE" 2>/dev/null || paplay "$TEMP_FILE" 2>/dev/null || true
    rm -f "$TEMP_FILE"
    exit 0
else
    rm -f "$TEMP_FILE"
    echo "⚠️  Service Kyutai TTS non disponible sur $API_URL"
    echo "   Démarrer avec: docker compose up -d kyutai (ou équivalent)"
    exit 0
fi
