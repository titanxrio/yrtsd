import random
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system('cls')

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            # Identify Brand
            self.cardNumber = number
            self.__findBrand()
            # Luhn's Algorithm
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[!] {self.cardNumber} is a valid Store Card!'
                file = open("cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f'[?] {self.cardNumber} is not a valid Store Card!'
        else:
            return 'Not a valid Credit Card Number'
os.system('cls')
banner ='''
 ######  ##     ## #### ######## ######## ##    ##    ##     ## ##     ## ########  
##    ## ##     ##  ##     ##       ##     ##  ##     ##     ## ##     ## ##     ## 
##       ##     ##  ##     ##       ##      ####      ##     ## ##     ## ##     ## 
 ######  #########  ##     ##       ##       ##       ######### ##     ## ########  
      ## ##     ##  ##     ##       ##       ##       ##     ## ##     ## ##     ## 
##    ## ##     ##  ##     ##       ##       ##       ##     ## ##     ## ##     ## 
 ######  ##     ## ####    ##       ##       ##       ##     ##  #######  ########                                          
'''
print(Fore.CYAN + banner)
print(Fore.YELLOW + ' ')
print('Cards & Balance List:')
print('0.  < $1000 AMZ SC')
print('1.  $1000 AMZ SC')
print('2.  $2000 AMZ SC')
print('3.  $5000 AMZ SC')
print('4.  $7000 AMZ SC')
print('5.  $10.000 AMZ SC')
print('6.  $20.000 AMZ SC')
print('7.  $40.000 AMZ SC')
print('8.  $100.000 AMZ SC')
print('9.  AMZ Corporate Revolving SC')
print('10. Multifunction Discover Card')
print('11. BestBuy Storecard')
print('12. Target Storecard')
print('13. AMZ Visa Signature CC')
print('14. Amazon Standard 1-10K SC')
print('15. HQ BestBuy Storecard')
print('16. HQ Multifunction Discover Card')
print(' ')
whatcard = input("[?] What Card Do You Want To Generate? ")

whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input('[?] How many cards do you want to generate: ')
    time.sleep(0.8)
    print('[/] Starting')
    time.sleep(0.8)
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811425'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 2:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578114'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7)
        print(validator().validate(int(cc)))
if whatcard == 3:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578118'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7)
        print(validator().validate(int(cc)))
if whatcard == 4:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578114860'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 5:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '6045781123'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 6:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811496'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 7:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811436'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 8:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811318'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 0:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578112729'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 9:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578172729'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 10:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '601100351312'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 11:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '702126'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
if whatcard == 12:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '5859752142'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 13:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '414840'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
if whatcard == 14:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8)
        print(validator().validate(int(cc)))
if whatcard == 15:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '5859752142'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 16:
    howmany = input('[?] How many cards do you want to generate: ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '601120'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
print(' ')
print(' ')
print(Fore.CYAN + 'If the cards are Invalid, simply run the gen again!')
print(' ')
input('Press ENTER to exit')
