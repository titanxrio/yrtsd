import requests #line:1
import tkinter as tk #line:2
from tkinter import messagebox #line:3
BG_COLOR ="#0f0f0f"#line:6
FG_COLOR ="#00ffe1"#line:7
INPUT_BG ="#1a1a1a"#line:8
BTN_BG ="#00ffe1"#line:9
BTN_FG ="#000000"#line:10
FONT_MAIN =("Consolas",16 )#line:11
FONT_TITLE =("Consolas",20 ,"bold")#line:12
FONT_RESULT =("Consolas",12 )#line:13
def check_bin ():#line:16
    OOOO0OO0OO0OO0OOO =entry .get ().strip ()#line:17
    if len (OOOO0OO0OO0OO0OOO )!=6 or not OOOO0OO0OO0OO0OOO .isdigit ():#line:18
        messagebox .showerror ("ERROR","Enter a valid 6-digit BIN.")#line:19
        return #line:20
    OO0O0000O0OO00O0O =f"https://lookup.binlist.net/{OOOO0OO0OO0OO0OOO}"#line:22
    try :#line:23
        O0OO00OOO00O0O0OO =requests .get (OO0O0000O0OO00O0O )#line:24
        OOOOO0OOOO0OO0O0O =O0OO00OOO00O0O0OO .json ()#line:25
        OOO0O0OOOO000000O =OOOOO0OOOO0OO0O0O .get ("scheme","Unknown").title ()#line:27
        O0O0OO0OOOO00O000 =OOOOO0OOOO0OO0O0O .get ("type","Unknown").title ()#line:28
        OO00O0OOOOOO00O0O =OOOOO0OOOO0OO0O0O .get ("brand","N/A")#line:29
        OOO0000O0O0O00OOO =OOOOO0OOOO0OO0O0O .get ("bank",{}).get ("name","Unknown")#line:30
        O00000OO0O0000O0O =OOOOO0OOOO0OO0O0O .get ("country",{}).get ("name","Unknown")#line:31
        OOO00OO0OO000OOOO =OOOOO0OOOO0OO0O0O .get ("country",{}).get ("emoji","")#line:32
        OO0OO000000OO0O0O =OOOOO0OOOO0OO0O0O .get ("bank",{}).get ("url","N/A")#line:33
        OOOOOOO0OOO0OO00O =f"""
[ BIN INFO ]
• Scheme      : {OOO0O0OOOO000000O}
• Card Type   : {O0O0OO0OOOO00O000}
• Brand       : {OO00O0OOOOOO00O0O}
• Bank        : {OOO0000O0O0O00OOO}
• Country     : {O00000OO0O0000O0O} {OOO00OO0OO000OOOO}
• Bank Site   : {OO0OO000000OO0O0O}
"""#line:43
        result_label .config (text =OOOOOOO0OOO0OO00O )#line:44
    except Exception as OOOOOO0O0OO0O000O :#line:45
        messagebox .showerror ("API ERROR",f"Failed to fetch BIN data:\n{OOOOOO0O0OO0O000O}")#line:46
root =tk .Tk ()#line:49
root .title ("BIN CHECKER discord.gg/shitty")#line:50
root .geometry ("540x400")#line:51
root .configure (bg =BG_COLOR )#line:52
root .resizable (False ,False )#line:53
title =tk .Label (root ,text ="💳 BIN CHECKER",font =FONT_TITLE ,fg =FG_COLOR ,bg =BG_COLOR )#line:56
title .pack (pady =20 )#line:57
entry =tk .Entry (root ,font =FONT_MAIN ,justify ="center",bg =INPUT_BG ,fg ="white",insertbackground ="white")#line:60
entry .pack (pady =10 ,ipadx =30 ,ipady =5 )#line:61
btn =tk .Button (root ,text ="Check BIN",command =check_bin ,font =FONT_MAIN ,bg =BTN_BG ,fg =BTN_FG ,cursor ="hand2")#line:64
btn .pack (pady =15 )#line:65
result_label =tk .Label (root ,text ="",font =FONT_RESULT ,fg ="white",bg =BG_COLOR ,justify ="left")#line:68
result_label .pack (pady =20 )#line:69
root .mainloop ()#line:72
