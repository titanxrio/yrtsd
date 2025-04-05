import requests
import datetime
import time
import os

# === TITAN POWER CONFIG ===
WEBHOOK_URL = "https://discord.com/api/webhooks/1358124469067186447/DDiDvX9gqcd36joxXLWDeYvGGNN-q9PIwFS6rTkN4XUipbYkChULOmnsoMPElRkf_y-T"
USERNAME = "Titan WebSender"
AVATAR_URL = "https://i.imgur.com/YOUR_AVATAR.png"  # Optional – kannst du frei ändern
MESSAGE = "🔥 [TS] Another Webhook drop. Dominanz läuft."
DELAY = 1  # Sekunden zwischen den Nachrichten

# === STYLED OUTPUT ===
def timestamp():
    return datetime.datetime.now().strftime("[%H:%M:%S | %d-%m-%Y]")

# === WEBHOOK ATTACK ===
def send_webhook(msg):
    payload = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "content": f"{timestamp()} [>] {msg}"
    }
    r = requests.post(WEBHOOK_URL, json=payload)
    if r.status_code == 204:
        print(f"{timestamp()} [✓] Webhook message sent.")
    else:
        print(f"{timestamp()} [✘] Failed. Status Code: {r.status_code}")

# === RUN MODE ===
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("╔═════════════════════════════╗")
    print("║     ⚡ Titan WebSender ⚡     ║")
    print("╚═════════════════════════════╝\n")

    counter = 1
    while True:
        send_webhook(f"{MESSAGE} #{counter}")
        counter += 1
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
