import requests
import time
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Color presets
purple = Fore.MAGENTA
darkblue = Fore.BLUE
cyan = Fore.CYAN
grey = Fore.LIGHTBLACK_EX

sent_count = 0

def log(msg):
    now = datetime.now()
    time_str = f"{purple}[{cyan}{now.strftime('%H')}{purple}:{cyan}{now.strftime('%M')}{purple}:{cyan}{now.strftime('%S')} {purple}| {cyan}{now.strftime('%d-%m-%Y')}{purple}]{purple} [>{purple}] {darkblue}{msg}{Style.RESET_ALL}"
    print(time_str)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_header():
    print(purple + r""" 
____    __    ____  _______ .______    __    __    ______     ______    __  ___ 
\   \  /  \  /   / |   ____||   _  \  |  |  |  |  /  __  \   /  __  \  |  |/  / 
 \   \/    \/   /  |  |__   |  |_)  | |  |__|  | |  |  |  | |  |  |  | |  '  /  
  \            /   |   __|  |   _  <  |   __   | |  |  |  | |  |  |  | |    <   
   \    /\    /    |  |____ |  |_)  | |  |  |  | |  `--'  | |  `--'  | |  .  \  
    \__/  \__/     |_______||______/  |__|  |__|  \______/   \______/  |__|\__\ 
                                                                                
shitty hub<3
""" + Style.RESET_ALL)

def check_webhook(url):
    try:
        r = requests.get(url)
        return r.status_code == 200
    except:
        return False

def send_webhook(url, content):
    global sent_count
    payload = {"content": content}
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 204:
            sent_count += 1
            log("✅ message sent.")
        else:
            log(f"❌ Failed to send message ({r.status_code})")
    except Exception as e:
        log(f"💥 Error: {e}")

def ask(prompt):
    return input(purple + "[>" + cyan + f" {prompt} " + purple + ">> " + Style.RESET_ALL).strip()

def main():
    clear()
    ascii_header()
    
    webhook = ask("Enter the Webhook URL")
    if not webhook.startswith("https://discord.com/api/webhooks/"):
        log("❌ Invalid webhook format.")
        return
    if not check_webhook(webhook):
        log("❌ Webhook is not valid")
        return
    else:
        log("✅ Webhook valid ")

    spam_choice = ask("Do you want to spam messages? (y/n)").lower()
    message = ask("Enter your message")

    if spam_choice == 'y':
        try:
            amount = int(ask("How many times to send"))
        except:
            log(" Invalid number.")
            return

        log(f"🚀 Starting spam – {amount}x")
        for _ in range(amount):
            send_webhook(webhook, message)
            time.sleep(0.3)
    else:
        log("📨 Sending a single message ...")
        send_webhook(webhook, message)

    log("done<3")

if __name__ == "__main__":
    main()
