#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.parse

API_BASE = "https://api.telegram.org/bot{token}/sendMessage"


def main():
    if len(sys.argv) < 2:
        print("Usage: notify_telegram.py '<message>'", file=sys.stderr)
        sys.exit(1)

    message = sys.argv[1]

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("[notify_telegram] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set", file=sys.stderr)
        sys.exit(2)

    url = API_BASE.format(token=token)
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    data_encoded = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data=data_encoded, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8")
            print(body)
    except Exception as e:
        print(f"[notify_telegram] Error sending message: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
