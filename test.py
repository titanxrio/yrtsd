import random
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def clear_console():
    print('\033c', end='')

def banner():
    print(Fore.CYAN + Style.BRIGHT + """

████████╗██╗████████╗ █████╗ ███╗   ██╗███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗
╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝
   ██║   ██║   ██║   ███████║██╔██╗ ██║███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  
   ██║   ██║   ██║   ██╔══██║██║╚██╗██║╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  
   ██║   ██║   ██║   ██║  ██║██║ ╚████║███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗
   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝
                                                                                                                                                                                                                                        
    """)
    print(Fore.MAGENTA + "~ amazon Sc Gen + checker")
    print(Fore.YELLOW + "~ Discord: discord.gg/shitty")
    print(Fore.BLUE + "~ Created by: titan<3 \n")

class Validator:
    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        cn = self.cardNumber
        if cn.startswith(('34', '37')):
            self.Brand = 'American Express'
        elif cn.startswith(('300', '301', '302', '303', '304', '305')):
            self.Brand = 'Diners Club - Carte Blanche'
        elif cn.startswith('36'):
            self.Brand = 'Diners Club - International'
        elif cn.startswith('54'):
            self.Brand = 'Diners Club - USA & Canada'
        elif cn.startswith(('6011',)) or cn[:3] in ['644', '645', '646', '647', '648', '649'] or cn.startswith('65') or cn[:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif cn.startswith(('637', '638', '639')):
            self.Brand = 'InstaPayment'
        elif cn[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif cn.startswith(('5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763')):
            self.Brand = 'Maestro'
        elif cn[:2] in ['51', '52', '53', '54', '55'] or cn[:6] in [str(x) for x in range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif cn[:4] in ['4026', '4508', '4844', '4913', '4917'] or cn.startswith('417500'):
            self.Brand = 'VISA Electron'
        elif cn.startswith('4'):
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        try:
            number = ''.join(x for x in str(number).strip() if x.isdigit())
            if not number or not (13 <= len(number) <= 19):
                return Fore.RED + "✖ Invalid input"
            self.cardNumber = number
            self.__findBrand()
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            checksum = (sum(base) * 9) % 10
            if checksum == lastDigit:
                return Fore.GREEN + f"✔ VALID | {number} | Brand: {self.Brand}"
            else:
                return Fore.RED + f"✖ INVALID | {number}"
        except:
            return Fore.RED + "✖ ERROR"

def generate_cards(prefix, total_digits, amount):
    for _ in range(amount):
        remaining_digits = total_digits - len(prefix) - 1
        rand_digits = ''.join(random.choice("0123456789") for _ in range(remaining_digits))
        base = prefix + rand_digits
        check_digit = get_check_digit(base)
        full_card = base + str(check_digit)
        print(Validator().validate(full_card))

def get_check_digit(number):
    base = [int(x) for x in reversed(number)]
    base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
    base = [x if x <= 9 else x - 9 for x in base]
    checksum = sum(base)
    return (10 - (checksum % 10)) % 10

def main():
    while True:
        clear_console()
        banner()
        print(Fore.CYAN + "\n[ 1 ] $1,000 Storecard")
        print("[ 2 ] $2,000 Storecard")
        print("[ 3 ] $5,000 Storecard")
        print("[ 4 ] $10,000 Storecard")
        print("[ 0 ] Exit")
        try:
            choice = int(input(Fore.YELLOW + "\n> Your choice: "))
            if choice == 0:
                print(Fore.RED + "Exiting... Peace.")
                break
            amount = int(input(Fore.GREEN + "- How many cards to generate? "))
            print(Fore.MAGENTA + "\n----- Generating Storecards -----\n")
            if choice == 1:
                generate_cards("60457811425", 16, amount)
            elif choice == 2:
                generate_cards("604578114", 16, amount)
            elif choice == 3:
                generate_cards("604578118", 16, amount)
            elif choice == 4:
                generate_cards("6045781123", 16, amount)
            else:
                print(Fore.RED + "Invalid selection.")
        except ValueError:
            print(Fore.RED + "❗ Input error. Use numbers only.")
        input(Fore.YELLOW + "\nPress ENTER to return to the menu...")

if __name__ == "__main__":
    main()
