#!/usr/bin/env python3
"""Notifier desktop via notify-send."""

import subprocess
from pathlib import Path


def _play_system_beep():
    """Joue un bip sonore système."""
    try:
        sound_files = [
            "/usr/share/sounds/freedesktop/stereo/message.oga",
            "/usr/share/sounds/freedesktop/stereo/complete.oga",
            "/usr/share/sounds/gnome/default/alerts/drip.ogg",
            "/usr/share/sounds/ubuntu/stereo/message.ogg",
        ]
        for sound in sound_files:
            if Path(sound).exists():
                subprocess.Popen(
                    ["paplay", sound],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                return
        # Fallback: beep terminal
        print("\a", end="", flush=True)
    except Exception:
        pass


def is_available():
    """Vérifie si notify-send est disponible."""
    try:
        return subprocess.run(["which", "notify-send"], capture_output=True).returncode == 0
    except Exception:
        return False


def notify(title, message, with_sound=True):
    """Envoie une notification desktop, optionnellement avec bip sonore."""
    try:
        if not is_available():
            return False

        subprocess.Popen(
            ["notify-send", "-u", "normal", "-i", "dialog-information", title, message],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if with_sound:
            _play_system_beep()

        return True

    except Exception:
        return False
