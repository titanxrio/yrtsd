import aiohttp
import asyncio
import colorama
from colorama import Fore, Style
import pyfiglet
import os

colorama.init(autoreset=True)

PLATFORMS = {
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitter/X": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Steam": "https://steamcommunity.com/id/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Medium": "https://medium.com/@{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "DeviantArt": "https://{}.deviantart.com/",
    "GitLab": "https://gitlab.com/{}",
    "CodePen": "https://codepen.io/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Replit": "https://replit.com/@{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "TripAdvisor": "https://tripadvisor.com/members/{}",
    "VSCO": "https://vsco.co/{}",
    "ProductHunt": "https://www.producthunt.com/@{}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def check_username(session, platform, url):
    try:
        async with session.get(url, headers=HEADERS, timeout=10) as resp:
            html = await resp.text()
            if resp.status == 404 or "not found" in html.lower():
                return platform, "✅ Free", url
            elif resp.status == 200:
                return platform, "❌ Taken", url
            else:
                return platform, f"⚠️ Error ({resp.status})", url
    except:
        return platform, "⚠️ Error", url

async def run_check(username):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for platform, url_template in PLATFORMS.items():
            url = url_template.format(username)
            tasks.append(check_username(session, platform, url))
        return await asyncio.gather(*tasks)

def print_banner():
    banner = pyfiglet.figlet_format("TITAN HUNTER V1", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "🔎 Scan any username across 25+ platforms\n")

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(Fore.GREEN + "[1] Start Scan")
        print(Fore.RED + "[0] Exit\n")

        choice = input(Fore.CYAN + "option: ").strip()
        
        if choice == "1":
            run_scan()
        elif choice == "0":
            print(Fore.MAGENTA + "\nSee you next time, Titan 👑")
            break
        else:
            print(Fore.RED + "\nInvalid option!")
            input(Fore.YELLOW + "Press Enter to return to menu...")

def run_scan():
    clear_screen()
    print_banner()
    username = input(Fore.GREEN + "username : ").strip()
    print(Fore.MAGENTA + f"\n[+] Scanning username '{username}'...\n")

    results = asyncio.run(run_check(username))

    for platform, status, url in results:
        color = Fore.GREEN if "Free" in status else Fore.RED if "Taken" in status else Fore.YELLOW
        print(f"{color}{platform:<15} ➜ {status:<10} ➜ {url}")

    print(Fore.CYAN + "\n✅ Scan complete.")
    input(Fore.YELLOW + "\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
