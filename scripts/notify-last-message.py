#!/usr/bin/env python3
import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime
import os

LOG_FILE = Path.home() / ".claude" / "logs" / "notify-errors.log"
# Activer/désactiver notification vocale des erreurs via variable d'environnement
NOTIFY_ERRORS = os.getenv("CLAUDE_NOTIFY_ERRORS", "false").lower() in ("true", "1", "yes")

def log_error(context, error):
    """Logue les erreurs dans un fichier dédié et notifie vocalement si activé."""
    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now().isoformat()} [{context}] {error}\n")
        if NOTIFY_ERRORS:
            notification_input = {
                "notification_type": "error",
                "message": f"Erreur dans {context}"
            }
            subprocess.run(
                [str(Path.home() / ".claude/scripts/notification-kyutai.py")],
                input=json.dumps(notification_input),
                text=True,
                capture_output=True
            )
    except Exception:
        pass

def get_last_assistant_message(transcript_path):
    """Extrait dernier message assistant du transcript JSONL."""
    try:
        messages = []
        with open(transcript_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    if entry.get("type") == "assistant":
                        messages.append(entry)
                except json.JSONDecodeError:
                    continue
        if not messages:
            return None
        last_msg = messages[-1]
        message_data = last_msg.get("message", {})
        for block in message_data.get("content", []):
            if block.get("type") == "text":
                return block.get("text", "").strip()
        return None
    except Exception as e:
        log_error("get_last_assistant_message", f"{type(e).__name__}: {e}")
        return None

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        transcript_path = input_data.get("transcript_path")

        if not transcript_path:
            sys.exit(0)

        message = get_last_assistant_message(transcript_path)

        if not message:
            sys.exit(0)

        # Tronquer si trop long (garde 200 premiers chars)
        if len(message) > 200:
            message = message[:200] + "..."

        # Appeler notification avec message custom
        notification_input = {
            "notification_type": "assistant_response",
            "message": message
        }

        subprocess.run(
            [str(Path.home() / ".claude/scripts/notification-kyutai.py")],
            input=json.dumps(notification_input),
            text=True,
            capture_output=True
        )

        sys.exit(0)

    except Exception as e:
        log_error("main", f"{type(e).__name__}: {e}")
        sys.exit(0)

if __name__ == "__main__":
    main()
