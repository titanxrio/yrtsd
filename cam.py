import requests, re, colorama, time
from requests.structures import CaseInsensitiveDict
from colorama import Fore, Style

colorama.init(autoreset=True)

def print_with_delay(text, delay=0.2, color=Fore.MAGENTA):
    """Gibt den übergebenen Text zeilenweise in einer festen Farbe mit Verzögerung aus."""
    for line in text.splitlines():
        print(color + line + Style.RESET_ALL)
        time.sleep(delay)

titan_ascii = r"""
███████ ██   ██ ██ ████████ ████████ ██    ██      ██████  █████  ███    ███ ███████ 
██      ██   ██ ██    ██       ██     ██  ██      ██      ██   ██ ████  ████ ██      
███████ ███████ ██    ██       ██      ████       ██      ███████ ██ ████ ██ ███████ 
     ██ ██   ██ ██    ██       ██       ██        ██      ██   ██ ██  ██  ██      ██ 
███████ ██   ██ ██    ██       ██       ██         ██████ ██   ██ ██      ██ ███████ 
"""
print(titan_ascii)

time.sleep(1.5)

url = "http://www.insecam.org/en/jsoncountries/"
headers = CaseInsensitiveDict({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.insecam.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

try:
    resp = requests.get(url, headers=headers)
    data = resp.json()
    countries = data['countries']
except Exception as e:
    print(Fore.RED + "Fehler beim Laden der Länder: " + str(e))
    exit()

for key, value in countries.items():
    line = f'Code : ({key}) - {value["country"]} / ({value["count"]})'
    print_with_delay(line)

try:
    country = input("Code(##) : ")
    res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers)
        find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
        for ip in find_ip:
            print_with_delay(ip, delay=0.2)
except Exception as e:
    print(Fore.RED + "Ein Fehler ist aufgetreten: " + str(e))
