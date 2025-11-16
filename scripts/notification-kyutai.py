#!/usr/bin/env python3

import json
import os
import sys
import subprocess
import random
from pathlib import Path
from datetime import datetime
import requests

API_URL = "http://localhost:9876/v1/audio/speech"
LOG_DIR = Path.home() / ".claude" / "logs"

# Voix par défaut (peut être surchargée par KYUTAI_VOICE)
# Voix disponibles: alloy, echo, fable, onyx (recommandée), nova, shimmer
DEFAULT_VOICE = os.getenv("KYUTAI_VOICE", "onyx")

# Messages par défaut par type
DEFAULT_MESSAGES = {
    "permission_prompt": "Demande de permission",
    "idle_prompt": "En attente de votre réponse",
    "auth_success": "Authentification réussie",
    "elicitation_dialog": "Information requise"
}

def get_message(input_data):
    """Détermine le message à prononcer."""
    # 1. Priorité: message custom du JSON
    if custom_message := input_data.get("message"):
        text = custom_message
    # 2. Sinon: message par défaut selon notification_type
    else:
        notification_type = input_data.get("notification_type", "unknown")
        text = DEFAULT_MESSAGES.get(notification_type, "Notification")

    # 3. Optionnel: personnaliser avec ENGINEER_NAME (30% chance)
    engineer_name = os.getenv("ENGINEER_NAME", "").strip()
    if engineer_name and random.random() < 0.3:
        text = f"{engineer_name}, {text}"

    return text

def generate_speech(text):
    """Appelle API Kyutai TTS et retourne le chemin du fichier audio."""
    try:
        temp_audio = f"/tmp/claude-notification-{datetime.now().timestamp()}.wav"

        response = requests.post(
            API_URL,
            json={
                "model": "tts-1",
                "input": text,
                "voice": DEFAULT_VOICE,
                "response_format": "wav"
            },
            timeout=10
        )

        if response.status_code == 200:
            with open(temp_audio, "wb") as f:
                f.write(response.content)
            return temp_audio

    except Exception:
        pass  # Fail silently

    return None

def play_audio(audio_file):
    """Joue le fichier audio et le nettoie après."""
    if not audio_file or not Path(audio_file).exists():
        return

    try:
        # Essayer ffplay d'abord
        if subprocess.run(["which", "ffplay"], capture_output=True).returncode == 0:
            subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", audio_file],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        # Sinon paplay directement (WAV)
        elif subprocess.run(["which", "paplay"], capture_output=True).returncode == 0:
            subprocess.Popen(
                ["paplay", audio_file],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        # Nettoyer après 5 secondes
        subprocess.Popen(
            ["sh", "-c", f"sleep 5 && rm -f {audio_file}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:
        pass  # Fail silently

def log_notification(input_data):
    """Logue la notification dans un fichier JSONL."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        log_file = LOG_DIR / "kyutai-notifications.jsonl"

        with open(log_file, "a") as f:
            json.dump(input_data, f)
            f.write("\n")

    except Exception:
        pass  # Fail silently

def main():
    try:
        # Lire JSON depuis stdin
        input_data = json.loads(sys.stdin.read())

        # Logger la notification
        log_notification(input_data)

        # Déterminer le message
        message = get_message(input_data)

        # Générer et jouer l'audio
        audio_file = generate_speech(message)
        play_audio(audio_file)

        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)  # Fail silently
    except Exception:
        sys.exit(0)  # Fail silently

if __name__ == "__main__":
    main()
