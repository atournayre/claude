#!/usr/bin/env python3
import json
import sys
import subprocess
from pathlib import Path

def get_last_assistant_message(transcript_path):
    """Extrait dernier message assistant du transcript."""
    try:
        with open(transcript_path) as f:
            data = json.load(f)

        # Messages en ordre inverse
        for msg in reversed(data.get("messages", [])):
            if msg.get("role") == "assistant":
                # Extraire texte (ignorer tool calls)
                for block in msg.get("content", []):
                    if block.get("type") == "text":
                        return block.get("text", "").strip()

        return None
    except Exception:
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

    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
