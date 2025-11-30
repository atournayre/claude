#!/usr/bin/env python3
"""Dispatcher de notifications Claude Code.

Logique :
- Son muted → notification desktop (sans bip)
- TTS disponible + son actif → TTS Kyutai
- TTS indisponible + son actif → notification desktop + bip
"""

import json
import os
import random
import subprocess
import sys
from pathlib import Path

# Ajouter le répertoire notifiers au path
sys.path.insert(0, str(Path(__file__).parent / "notifiers"))

import desktop
from importlib import import_module

# Import dynamique pour éviter erreur si requests non installé
try:
    tts_kyutai = import_module("tts-kyutai")
except Exception:
    tts_kyutai = None

LOG_DIR = Path.home() / ".claude" / "logs"

DEFAULT_MESSAGES = {
    "permission_prompt": "Demande de permission",
    "idle_prompt": "En attente de votre réponse",
    "auth_success": "Authentification réussie",
    "elicitation_dialog": "Information requise"
}


def is_audio_muted():
    """Vérifie si le son système est muted (PulseAudio/PipeWire)."""
    try:
        result = subprocess.run(
            ["pactl", "get-sink-mute", "@DEFAULT_SINK@"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            return "yes" in result.stdout.lower()
    except Exception:
        pass
    return False


def get_message(input_data):
    """Détermine le message à afficher/prononcer."""
    if custom_message := input_data.get("message"):
        text = custom_message
    else:
        notification_type = input_data.get("notification_type", "unknown")
        text = DEFAULT_MESSAGES.get(notification_type, "Notification")

    engineer_name = os.getenv("ENGINEER_NAME", "").strip()
    if engineer_name and random.random() < 0.3:
        text = f"{engineer_name}, {text}"

    return text


def log_notification(input_data):
    """Logue la notification dans un fichier JSONL."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        log_file = LOG_DIR / "notifications.jsonl"
        with open(log_file, "a") as f:
            json.dump(input_data, f)
            f.write("\n")
    except Exception:
        pass


def dispatch(input_data):
    """Dispatch la notification vers le bon notifier."""
    message = get_message(input_data)
    notification_type = input_data.get("notification_type", "Claude Code")
    title = f"Claude Code - {notification_type}"

    # Son muted → desktop sans bip
    if is_audio_muted():
        desktop.notify(title, message, with_sound=False)
        return

    # TTS disponible → TTS
    if tts_kyutai and tts_kyutai.is_available():
        if tts_kyutai.notify(message):
            return

    # Fallback → desktop avec bip
    desktop.notify(title, message, with_sound=True)


def main():
    try:
        input_data = json.loads(sys.stdin.read())
        log_notification(input_data)
        dispatch(input_data)
        sys.exit(0)
    except json.JSONDecodeError:
        sys.exit(0)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
