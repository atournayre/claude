#!/usr/bin/env python3
"""Notifier TTS via Kyutai."""

import os
import subprocess
from datetime import datetime
from pathlib import Path
import requests

API_URL = "http://localhost:9876/v1/audio/speech"
DEFAULT_VOICE = os.getenv("KYUTAI_VOICE", "onyx")
DEFAULT_LANGUAGE = os.getenv("KYUTAI_LANGUAGE", "fr")


def is_available():
    """Vérifie si le service TTS Kyutai est disponible."""
    try:
        response = requests.get("http://localhost:9876/health", timeout=2)
        return response.status_code == 200
    except Exception:
        return False


def notify(message):
    """Génère et joue la notification TTS."""
    try:
        temp_audio = f"/tmp/claude-notification-{datetime.now().timestamp()}.wav"

        response = requests.post(
            API_URL,
            json={
                "model": "tts-1",
                "input": message,
                "voice": DEFAULT_VOICE,
                "response_format": "wav",
                "language": DEFAULT_LANGUAGE
            },
            timeout=10
        )

        if response.status_code != 200:
            return False

        with open(temp_audio, "wb") as f:
            f.write(response.content)

        # Jouer l'audio
        if subprocess.run(["which", "ffplay"], capture_output=True).returncode == 0:
            subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", temp_audio],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        elif subprocess.run(["which", "paplay"], capture_output=True).returncode == 0:
            subprocess.Popen(
                ["paplay", temp_audio],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        # Nettoyer après 5 secondes
        subprocess.Popen(
            ["sh", "-c", f"sleep 5 && rm -f {temp_audio}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True

    except Exception:
        return False
