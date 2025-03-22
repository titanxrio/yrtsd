#!/usr/bin/env python3
""#line:12
import random #line:14
import colorama #line:15
from colorama import Fore ,Style #line:16
colorama .init (autoreset =True )#line:18
def compute_check_digit (O0OOOO00O0O00OO0O ):#line:21
    ""#line:24
    OOO0OOOO0O00OO0O0 =[int (O0OO0OO00O0000000 )for O0OO0OO00O0000000 in O0OOOO00O0O00OO0O ]#line:25
    OO0OO0000000O000O =len (OOO0OOOO0O00OO0O0 )%2 #line:26
    O0OOOOOO0OOO0O000 =0 #line:27
    for O0O0O0O000OOOO0O0 ,O0O000OO0000O0OO0 in enumerate (OOO0OOOO0O00OO0O0 ):#line:28
        if O0O0O0O000OOOO0O0 %2 ==OO0OO0000000O000O :#line:29
            O000OO0OOO00000O0 =O0O000OO0000O0OO0 *2 #line:30
            if O000OO0OOO00000O0 >9 :#line:31
                O000OO0OOO00000O0 -=9 #line:32
            O0OOOOOO0OOO0O000 +=O000OO0OOO00000O0 #line:33
        else :#line:34
            O0OOOOOO0OOO0O000 +=O0O000OO0000O0OO0 #line:35
    O0OO0OOOOOOO00OO0 =(10 -(O0OOOOOO0OOO0O000 %10 ))%10 #line:36
    return str (O0OO0OOOOOOO00OO0 )#line:37
class Validator :#line:40
    def __init__ (O00O00000OO0000O0 ):#line:41
        O00O00000OO0000O0 .card_number =None #line:42
        O00O00000OO0000O0 .brand =None #line:43
    def _find_brand (O0OOO00OO0O00O0OO ):#line:45
        O0000O0O0000O000O =O0OOO00OO0O00O0OO .card_number #line:46
        if O0000O0O0000O000O .startswith (('34','37')):#line:47
            O0OOO00OO0O00O0OO .brand ='American Express'#line:48
        elif O0000O0O0000O000O [:3 ]in ['300','301','302','303','304','305']:#line:49
            O0OOO00OO0O00O0OO .brand ='Diners Club - Carte Blanche'#line:50
        elif O0000O0O0000O000O .startswith ('36'):#line:51
            O0OOO00OO0O00O0OO .brand ='Diners Club - International'#line:52
        elif O0000O0O0000O000O .startswith ('54'):#line:53
            O0OOO00OO0O00O0OO .brand ='Diners Club - USA & Canada'#line:54
        elif (O0000O0O0000O000O .startswith ('6011')or O0000O0O0000O000O [:3 ]in ['644','645','646','647','648','649']or O0000O0O0000O000O .startswith ('65')or O0000O0O0000O000O [:6 ]in [str (O0OOOO0O00OOOO0OO )for O0OOOO0O00OOOO0OO in range (622126 ,622926 )]):#line:58
            O0OOO00OO0O00O0OO .brand ='Discover'#line:59
        elif O0000O0O0000O000O [:3 ]in ['637','638','639']:#line:60
            O0OOO00OO0O00O0OO .brand ='InstaPayment'#line:61
        elif O0000O0O0000O000O [:4 ]in [str (OOO00000OOO00000O )for OOO00000OOO00000O in range (3528 ,3590 )]:#line:62
            O0OOO00OO0O00O0OO .brand ='JCB'#line:63
        elif O0000O0O0000O000O [:4 ]in ['5018','5020','5038','5893','6304','6759','6761','6762','6763']:#line:64
            O0OOO00OO0O00O0OO .brand ='Maestro'#line:65
        elif (O0000O0O0000O000O .startswith (('51','52','53','54','55'))or O0000O0O0000O000O [:6 ]in [str (O000O0OO00000O0O0 )for O000O0OO00000O0O0 in range (222100 ,272100 )]):#line:67
            O0OOO00OO0O00O0OO .brand ='MasterCard'#line:68
        elif (O0000O0O0000O000O [:4 ]in ['4026','4508','4844','4913','4917']or O0000O0O0000O000O [:6 ]=='417500'):#line:70
            O0OOO00OO0O00O0OO .brand ='VISA Electron'#line:71
        elif O0000O0O0000O000O .startswith ('4'):#line:72
            O0OOO00OO0O00O0OO .brand ='VISA'#line:73
        else :#line:74
            O0OOO00OO0O00O0OO .brand ='Unknown Brand'#line:75
    def validate (OO00OOOO00OOOOO0O ,O00OO0O00OOOOOOO0 ):#line:77
        ""#line:81
        if O00OO0O00OOOOOOO0 is None or isinstance (O00OO0O00OOOOOOO0 ,(bool ,float )):#line:82
            return None #line:83
        O00OO0O00OOOOOOO0 =''.join (str (O00OO0O00OOOOOOO0 ).strip ().split ())#line:84
        if O00OO0O00OOOOOOO0 .isdigit ()and 13 <=len (O00OO0O00OOOOOOO0 )<=19 :#line:85
            OO00OOOO00OOOOO0O .card_number =O00OO0O00OOOOOOO0 #line:86
            OO00OOOO00OOOOO0O ._find_brand ()#line:87
            OO000000OOOO00OO0 =int (O00OO0O00OOOOOOO0 [-1 ])#line:89
            O0O0OO0OOO00OOO0O =[int (OOOOOOO000O00O0O0 )for OOOOOOO000O00O0O0 in reversed (O00OO0O00OOOOOOO0 [:-1 ])]#line:90
            O0O0OO0OOO00OOO0O =[OOO0OO0O0O00OO0O0 if OO00O0O0OOO000OO0 %2 !=0 else 2 *OOO0OO0O0O00OO0O0 for OO00O0O0OOO000OO0 ,OOO0OO0O0O00OO0O0 in enumerate (O0O0OO0OOO00OOO0O )]#line:91
            O0O0OO0OOO00OOO0O =[OOO0O0O0OOO0O0OOO if OOO0O0O0OOO0O0OOO <=9 else OOO0O0O0OOO0O0OOO -9 for OOO0O0O0OOO0O0OOO in O0O0OO0OOO00OOO0O ]#line:92
            OOOO00O0OO00O00OO =sum (O0O0OO0OOO00OOO0O )#line:93
            OOOO00O0OO00O00OO =(OOOO00O0OO00O00OO *9 )%10 #line:94
            if OOOO00O0OO00O00OO ==OO000000OOOO00OO0 :#line:95
                return Fore .GREEN +f"+ {O00OO0O00OOOOOOO0} ({OO00OOOO00OOOOO0O.brand})"+Style .RESET_ALL #line:96
        return None #line:97
def print_banner ():#line:100
    OOOO0O0O0000OOO00 =r"""

███████╗██╗  ██╗██╗████████╗████████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
██╔════╝██║  ██║██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
███████╗███████║██║   ██║      ██║    ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
╚════██║██╔══██║██║   ██║      ██║     ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
███████║██║  ██║██║   ██║      ██║      ██║       ╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                              
    """#line:110
    print (Fore .CYAN +OOOO0O0O0000OOO00 +Style .RESET_ALL )#line:111
    print (Fore .YELLOW +"             TITAN SERVICE STORECARD GENERATOR"+Style .RESET_ALL )#line:112
    print (Fore .YELLOW +"       goated tools<3 by titan. gg.shitty"+Style .RESET_ALL )#line:113
    print (Fore .CYAN +"="*60 +Style .RESET_ALL )#line:114
    print ("\n~ Status:      working ig")#line:115
    print ("~ Creator:     Titan")#line:116
    print ("~ Server:      discord.gg/shitty\n")#line:117
def display_menu ():#line:120
    OOO0O0OOO00OOOOOO ={1 :{"desc":"$1,000 Storecard","bin":"60457811425","extra_digits":5 },2 :{"desc":"$2,000 Storecard","bin":"604578114","extra_digits":7 },3 :{"desc":"$5,000 Storecard","bin":"604578118","extra_digits":7 },4 :{"desc":"$10,000 Storecard","bin":"6045781123","extra_digits":6 }}#line:126
    print (Fore .BLUE +"\nWähle die sc:"+Style .RESET_ALL )#line:127
    for OO0O0O0O000O0O0O0 ,O0O00O0O000O0O0O0 in OOO0O0OOO00OOOOOO .items ():#line:128
        print (Fore .MAGENTA +f"[ {OO0O0O0O000O0O0O0} ] "+Fore .YELLOW +f"{O0O00O0O000O0O0O0['desc']}"+Style .RESET_ALL )#line:129
    try :#line:130
        OO00000O0O0OOOOO0 =int (input ("\n- option: "))#line:131
    except ValueError :#line:132
        print (Fore .RED +"Ungültige Eingabe!"+Style .RESET_ALL )#line:133
        return None ,None ,None #line:134
    if OO00000O0O0OOOOO0 not in OOO0O0OOO00OOOOOO :#line:136
        print (Fore .RED +"Diese Option exestiert nd"+Style .RESET_ALL )#line:137
        return None ,None ,None #line:138
    try :#line:140
        OOO0OO0O000O0OOOO =int (input ("- Wie viele Storecards generieren? "))#line:141
    except ValueError :#line:142
        print (Fore .RED +"Bitte eine gültige zahl..."+Style .RESET_ALL )#line:143
        return None ,None ,None #line:144
    return OOO0O0OOO00OOOOOO [OO00000O0O0OOOOO0 ]["bin"],OOO0O0OOO00OOOOOO [OO00000O0O0OOOOO0 ]["extra_digits"],OOO0OO0O000O0OOOO #line:146
def generate_cards (O00OOO00O00O00O00 ,OOO0OOO000OO0O000 ,OOOOO0000O0OO00OO ):#line:149
    ""#line:153
    OO0OOO0OOOOO0000O ="0123456789"#line:154
    O0OOOOOO00OO0O000 =[]#line:155
    for _O000OO0000O00OO00 in range (OOOOO0000O0OO00OO ):#line:156
        if OOO0OOO000OO0O000 >1 :#line:158
            O0O0OOO0O0OO00O0O =''.join (random .choice (OO0OOO0OOOOO0000O )for _OO00000OO0O000O0O in range (OOO0OOO000OO0O000 -1 ))#line:159
        else :#line:160
            O0O0OOO0O0OO00O0O =""#line:161
        O0000O0O0O0OOO0O0 =O00OOO00O00O00O00 +O0O0OOO0O0OO00O0O #line:162
        OOOOOOO00OOO0OO00 =compute_check_digit (O0000O0O0O0OOO0O0 )#line:163
        O0O00O00O00O00O00 =O0000O0O0O0OOO0O0 +OOOOOOO00OOO0OO00 #line:164
        O0OOOOOO00OO0O000 .append (O0O00O00O00O00O00 )#line:165
    return O0OOOOOO00OO0O000 #line:166
def main ():#line:169
    print_banner ()#line:170
    OO000OO00OO0O0000 ,O00O0O0OO0OOO0O00 ,O0OOOOOO0O000OO0O =display_menu ()#line:171
    if not all ([OO000OO00OO0O0000 ,O00O0O0OO0OOO0O00 ,O0OOOOOO0O000OO0O ]):#line:172
        return #line:173
    print ("\n"+Fore .CYAN +"----- Storecards -----\n"+Style .RESET_ALL )#line:175
    OO000O00000OOO000 =generate_cards (OO000OO00OO0O0000 ,O00O0O0OO0OOO0O00 ,O0OOOOOO0O000OO0O )#line:176
    OOO00OOO0O00OO0O0 =Validator ()#line:177
    O0O0000O00O0O000O =0 #line:180
    for O0000O00O0OOOOOO0 in OO000O00000OOO000 :#line:181
        O0000OO00O0OO000O =OOO00OOO0O00OO0O0 .validate (O0000O00O0OOOOOO0 )#line:182
        if O0000OO00O0OO000O :#line:183
            print (O0000OO00O0OO000O )#line:184
            O0O0000O00O0O000O +=1 #line:185
    print (Fore .CYAN +f"\n----- Generiert: {O0O0000O00O0O000O} valide Storecard(s) -----"+Style .RESET_ALL )#line:187
    input (Fore .YELLOW +"\nDrücke Enter zum Beenden..."+Style .RESET_ALL )#line:188
if __name__ =="__main__":#line:191
    main ()#line:192
