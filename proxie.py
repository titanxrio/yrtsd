import requests #line:1
import threading #line:2
import time #line:3
import os #line:4
from colorama import Fore ,Style ,init #line:5
init (autoreset =True )#line:7
valid_proxies =[]#line:9
proxy_sources ={"http":["https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"],"socks4":["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1000&country=all","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"],"socks5":["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1000&country=all","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"]}#line:24
def clear_screen ():#line:26
    os .system ('cls'if os .name =='nt'else 'clear')#line:27
def banner ():#line:29
    print (f"{Fore.MAGENTA}┌──────────────────────────────────────────────────┐")#line:30
    print (f"{Fore.MAGENTA}│        {Fore.CYAN}Shitty Proxy Scraper          {Fore.MAGENTA}")#line:31
    print (f"{Fore.MAGENTA}├──────────────────────────────────────────────────┤")#line:32
    print (f"{Fore.MAGENTA}│ {Fore.YELLOW}Proxy Types: {Fore.WHITE}http | socks4 | socks5                    {Fore.MAGENTA}")#line:33
    print (f"{Fore.MAGENTA}└──────────────────────────────────────────────────┘\n")#line:34
def scrape_proxies (OOOOOO00O0OO0O0OO ):#line:36
    OOO0O00OOO000O0OO =set ()#line:37
    if OOOOOO00O0OO0O0OO not in proxy_sources :#line:38
        print (f"{Fore.RED}[-] Ungültiger Proxy-Typ: {OOOOOO00O0OO0O0OO}")#line:39
        return []#line:40
    print (f"{Fore.CYAN}[+] Scraping {OOOOOO00O0OO0O0OO.upper()} Proxies...\n")#line:42
    for OOO000O00O0O0OOO0 in proxy_sources [OOOOOO00O0OO0O0OO ]:#line:43
        try :#line:44
            O0000OOO0O000O000 =requests .get (OOO000O00O0O0OOO0 ,timeout =5 )#line:45
            if O0000OOO0O000O000 .status_code ==200 :#line:46
                for OOOO0OO0OO000OO00 in O0000OOO0O000O000 .text .splitlines ():#line:47
                    if OOOO0OO0OO000OO00 .strip ():#line:48
                        OOO0O00OOO000O0OO .add (OOOO0OO0OO000OO00 .strip ())#line:49
        except Exception as OOO0O0OOO0O0OO0O0 :#line:50
            print (f"{Fore.RED}[-] Fehler bei {OOO000O00O0O0OOO0}: {OOO0O0OOO0O0OO0O0}")#line:51
    print (f"{Fore.GREEN}[✓] {len(OOO0O00OOO000O0OO)} Proxies gesammelt.\n")#line:53
    return list (OOO0O00OOO000O0OO )#line:54
def check_proxy (O00OOOOO00000O000 ,OOO00O0O00OOO0O00 ):#line:56
    O0OO00OO0000O00OO =f"{OOO00O0O00OOO0O00}://{O00OOOOO00000O000}"#line:57
    OOOOOOOOO000O00OO ={"http":O0OO00OO0000O00OO ,"https":O0OO00OO0000O00OO }#line:61
    try :#line:62
        OOO0O0OO000000O00 =requests .get ("http://httpbin.org/ip",proxies =OOOOOOOOO000O00OO ,timeout =3 )#line:63
        if OOO0O0OO000000O00 .status_code ==200 :#line:64
            print (f"{Fore.GREEN}[VALID]   {O00OOOOO00000O000}")#line:65
            valid_proxies .append (O00OOOOO00000O000 )#line:66
        else :#line:67
            print (f"{Fore.RED}[INVALID] {O00OOOOO00000O000}")#line:68
    except :#line:69
        print (f"{Fore.RED}[INVALID] {O00OOOOO00000O000}")#line:70
def check_all_proxies (O0O000000O0O0O0O0 ,O0OO0OO00OO0OOOO0 ):#line:72
    print (f"{Fore.CYAN}[~] Starte Live-Check...\n")#line:73
    OOOO00OOOO00OOO0O =[]#line:74
    for OO0OO000OOO000OO0 in O0O000000O0O0O0O0 :#line:76
        OOO000000OO00O0OO =threading .Thread (target =check_proxy ,args =(OO0OO000OOO000OO0 ,O0OO0OO00OO0OOOO0 ))#line:77
        OOO000000OO00O0OO .start ()#line:78
        OOOO00OOOO00OOO0O .append (OOO000000OO00O0OO )#line:79
        time .sleep (0.03 )#line:80
    for OOO000000OO00O0OO in OOOO00OOOO00OOO0O :#line:82
        OOO000000OO00O0OO .join ()#line:83
def save_to_file (O0OO0OO0OO00O0O00 ,O00OO000OOOOO000O ):#line:85
    O0O0OO0OO0O00000O =f"valid_{O00OO000OOOOO000O}_proxies.txt"#line:86
    with open (O0O0OO0OO0O00000O ,"w")as O0OO0OO00O00O0OO0 :#line:87
        for O0OO00O0OO0O0OOO0 in O0OO0OO0OO00O0O00 :#line:88
            O0OO0OO00O00O0OO0 .write (O0OO00O0OO0O0OOO0 +"\n")#line:89
    print (f"{Fore.CYAN}[✓] saved: {O0O0OO0OO0O00000O}")#line:90
def main ():#line:92
    clear_screen ()#line:93
    banner ()#line:94
    OO0000O0O00O0O0O0 =input (f"{Fore.YELLOW}[?] Proxy : ").lower ().strip ()#line:96
    O0O0OOO00000O00OO =scrape_proxies (OO0000O0O00O0O0O0 )#line:97
    if not O0O0OOO00000O00OO :#line:99
        print (f"{Fore.RED}[-] no proxies found ")#line:100
        return #line:101
    print (f"{Fore.BLUE}[+] first 10: \n")#line:103
    for O00O00O00OO0OO000 in O0O0OOO00000O00OO [:10 ]:#line:104
        print (f"  → {O00O00O00OO0OO000}")#line:105
    O0OO0OOO000OO00OO =input (f"\n{Fore.YELLOW}[?] check proxies? (j/n): ").lower ()#line:107
    if O0OO0OOO000OO00OO =="j":#line:108
        check_all_proxies (O0O0OOO00000O00OO ,OO0000O0O00O0O0O0 )#line:109
        print (f"\n{Fore.GREEN}[✓] valid Proxies ({len(valid_proxies)}):")#line:111
        for O0O000OOO0O00000O in valid_proxies :#line:112
            print (f"{Fore.GREEN}{O0O000OOO0O00000O}")#line:113
        O000OO00OO00O00OO =input (f"\n{Fore.YELLOW}[?] save valid proxies? (j/n): ").lower ()#line:115
        if O000OO00OO00O00OO =="j":#line:116
            save_to_file (valid_proxies ,OO0000O0O00O0O0O0 )#line:117
if __name__ =="__main__":#line:119
    main ()#line:120
