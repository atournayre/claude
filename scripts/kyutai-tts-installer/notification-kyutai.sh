#!/bin/bash

# Wrapper pour notifications Claude Code avec Kyutai TTS
# Lit le JSON depuis stdin et génère la parole via API Kyutai

API_URL="http://localhost:9876/v1/audio/speech"
TEMP_AUDIO="/tmp/claude-notification-$(date +%s).mp3"

# Lire input JSON
input=$(cat)
notification_type=$(echo "$input" | grep -oP '"notification_type":\s*"\K[^"]+')

# Mapper notification_type vers phrase française
case "$notification_type" in
  permission_prompt)
    text="Demande de permission"
    ;;
  idle_prompt)
    text="En attente de votre réponse"
    ;;
  auth_success)
    text="Authentification réussie"
    ;;
  elicitation_dialog)
    text="Information requise"
    ;;
  *)
    text="Notification"
    ;;
esac

# Appeler API Kyutai TTS
curl -s -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"tts-1\",\"input\":\"$text\",\"voice\":\"alloy\",\"response_format\":\"mp3\"}" \
  --output "$TEMP_AUDIO" 2>/dev/null

# Jouer audio
if [ -f "$TEMP_AUDIO" ]; then
  # Essayer ffplay d'abord, sinon paplay via conversion
  if command -v ffplay > /dev/null 2>&1; then
    ffplay -nodisp -autoexit -loglevel quiet "$TEMP_AUDIO" 2>/dev/null &
  elif command -v paplay > /dev/null 2>&1 && command -v ffmpeg > /dev/null 2>&1; then
    # Convertir MP3 en WAV puis jouer avec paplay
    ffmpeg -i "$TEMP_AUDIO" -f wav - 2>/dev/null | paplay 2>/dev/null &
  fi

  # Nettoyer fichier après 5 secondes
  (sleep 5 && rm -f "$TEMP_AUDIO") &
fi

exit 0
