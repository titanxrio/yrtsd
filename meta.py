#!/usr/bin/env python3
""#line:13
import os #line:15
import json #line:16
import hashlib #line:17
import mimetypes #line:18
import stat #line:19
from datetime import datetime #line:20
from PIL import Image #line:21
from PIL .ExifTags import TAGS #line:22
import tkinter as tk #line:23
from tkinter import ttk ,filedialog ,messagebox #line:24
def compute_file_hash (O0OO0OOO0000O0OO0 ,hash_algo =hashlib .sha256 ,block_size =65536 ):#line:26
    ""#line:27
    OO0O00000O0OOO0O0 =hash_algo ()#line:28
    try :#line:29
        with open (O0OO0OOO0000O0OO0 ,'rb')as O0O000O0OO0OOO0O0 :#line:30
            for OO0OOO0O00OO0OO00 in iter (lambda :O0O000O0OO0OOO0O0 .read (block_size ),b''):#line:31
                OO0O00000O0OOO0O0 .update (OO0OOO0O00OO0OO00 )#line:32
        return OO0O00000O0OOO0O0 .hexdigest ()#line:33
    except Exception as O0OOOOO0000000000 :#line:34
        return f"Error computing hash: {O0OOOOO0000000000}"#line:35
def get_file_stats (O00OO00OO0OOO0O0O ):#line:37
    ""#line:38
    try :#line:39
        OO0O0O000000O00OO =os .stat (O00OO00OO0OOO0O0O )#line:40
        try :#line:42
            import pwd #line:43
            OO0OOO0O000O00OOO =pwd .getpwuid (OO0O0O000000O00OO .st_uid ).pw_name #line:44
        except Exception :#line:45
            OO0OOO0O000O00OOO ="N/A"#line:46
        try :#line:47
            import grp #line:48
            O000000000OO0O00O =grp .getgrgid (OO0O0O000000O00OO .st_gid ).gr_name #line:49
        except Exception :#line:50
            O000000000OO0O00O ="N/A"#line:51
        OOO0OO000OOO00O0O ={"absolute_path":os .path .abspath (O00OO00OO0OOO0O0O ),"file_name":os .path .basename (O00OO00OO0OOO0O0O ),"file_extension":os .path .splitext (O00OO00OO0OOO0O0O )[1 ],"size_bytes":OO0O0O000000O00OO .st_size ,"created":datetime .fromtimestamp (OO0O0O000000O00OO .st_ctime ).isoformat (),"modified":datetime .fromtimestamp (OO0O0O000000O00OO .st_mtime ).isoformat (),"accessed":datetime .fromtimestamp (OO0O0O000000O00OO .st_atime ).isoformat (),"mime_type":mimetypes .guess_type (O00OO00OO0OOO0O0O )[0 ],"sha256":compute_file_hash (O00OO00OO0OOO0O0O ),"permissions":stat .filemode (OO0O0O000000O00OO .st_mode ),"owner":OO0OOO0O000O00OOO ,"group":O000000000OO0O00O }#line:65
        return OOO0OO000OOO00O0O #line:66
    except Exception as O00OOO0O000000OOO :#line:67
        return {"error":f"Failed to retrieve file stats: {O00OOO0O000000OOO}"}#line:68
def get_exif_data (OOO000OOOO0OOO000 ):#line:70
    ""#line:71
    OOOO0OO0O0OO00OO0 ={}#line:72
    try :#line:73
        with Image .open (OOO000OOOO0OOO000 )as O0OO00O00O0000000 :#line:74
            OOOOOO00OOO0O0O0O =O0OO00O00O0000000 ._getexif ()#line:75
            if OOOOOO00OOO0O0O0O :#line:76
                for O00OOO0O0OOOOOOOO ,OO000OO00OO00OOOO in OOOOOO00OOO0O0O0O .items ():#line:77
                    OOO00O0OOO00O0000 =TAGS .get (O00OOO0O0OOOOOOOO ,O00OOO0O0OOOOOOOO )#line:78
                    OOOO0OO0O0OO00OO0 [OOO00O0OOO00O0000 ]=OO000OO00OO00OOOO #line:79
    except Exception as O0O0O0OOO0OO00OOO :#line:80
        OOOO0OO0O0OO00OO0 ["error"]=f"EXIF extraction failed: {O0O0O0OOO0OO00OOO}"#line:81
    return OOOO0OO0O0OO00OO0 #line:82
def get_image_info (O00O0OO0O0O0000O0 ):#line:84
    ""#line:85
    try :#line:86
        with Image .open (O00O0OO0O0O0000O0 )as OOOOOOOOO00OOOO00 :#line:87
            O0OOOOO000OOO000O ={"format":OOOOOOOOO00OOOO00 .format ,"mode":OOOOOOOOO00OOOO00 .mode ,"width":OOOOOOOOO00OOOO00 .width ,"height":OOOOOOOOO00OOOO00 .height }#line:93
            return O0OOOOO000OOO000O #line:94
    except Exception as O0OO0OOOOOOOO000O :#line:95
        return {"error":f"Image info extraction failed: {O0OO0OOOOOOOO000O}"}#line:96
def get_gps_info (OOO00OOO0O0O00OOO ):#line:98
    ""#line:99
    if "GPSInfo"not in OOO00OOO0O0O00OOO :#line:100
        return "Not available"#line:101
    O000O0OOO0O0OO0OO =OOO00OOO0O0O00OOO ["GPSInfo"]#line:103
    OOOOOO0O000OO0OO0 =O000O0OOO0O0OO0OO .get (2 )#line:104
    O0000OO0000O00O0O =O000O0OOO0O0OO0OO .get (1 )#line:105
    O0OOOO00O0O0OO0OO =O000O0OOO0O0OO0OO .get (4 )#line:106
    O0O0000O00O00OOOO =O000O0OOO0O0OO0OO .get (3 )#line:107
    if not (OOOOOO0O000OO0OO0 and O0000OO0000O00O0O and O0OOOO00O0O0OO0OO and O0O0000O00O00OOOO ):#line:109
        return "Not available"#line:110
    def O0OO0O0OOO000O000 (OOOO0O0OOOO0OOO00 ):#line:112
        OOOO0O0OO0OO00O00 =OOOO0O0OOOO0OOO00 [0 ][0 ]/OOOO0O0OOOO0OOO00 [0 ][1 ]#line:113
        OO0OOO0O0O0O0OO00 =OOOO0O0OOOO0OOO00 [1 ][0 ]/OOOO0O0OOOO0OOO00 [1 ][1 ]#line:114
        O0O0O0O000O000OO0 =OOOO0O0OOOO0OOO00 [2 ][0 ]/OOOO0O0OOOO0OOO00 [2 ][1 ]#line:115
        return OOOO0O0OO0OO00O00 +(OO0OOO0O0O0O0OO00 /60.0 )+(O0O0O0O000O000OO0 /3600.0 )#line:116
    try :#line:118
        O00O0000O00000000 =O0OO0O0OOO000O000 (OOOOOO0O000OO0OO0 )#line:119
        if O0000OO0000O00O0O .upper ()!="N":#line:120
            O00O0000O00000000 =-O00O0000O00000000 #line:121
        O0000OOOO0OO00OO0 =O0OO0O0OOO000O000 (O0OOOO00O0O0OO0OO )#line:122
        if O0O0000O00O00OOOO .upper ()!="E":#line:123
            O0000OOOO0OO00OO0 =-O0000OOOO0OO00OO0 #line:124
        return {"latitude":O00O0000O00000000 ,"longitude":O0000OOOO0OO00OO0 }#line:125
    except Exception as OO0O00O00OOOOOO0O :#line:126
        return f"Error processing GPS info: {OO0O00O00OOOOOO0O}"#line:127
def extract_metadata (O00OOO00OO00OO0OO ):#line:129
    ""#line:130
    OO000O0OO0000OOOO ={"file_stats":get_file_stats (O00OOO00OO00OO0OO )}#line:131
    OO00OOOO0O0O0OO00 ={".jpg",".jpeg",".png",".tiff",".bmp",".gif"}#line:134
    _OO0O0OOOOO0O0O0O0 ,O00OO0O0O00O00OO0 =os .path .splitext (O00OOO00OO00OO0OO .lower ())#line:135
    if O00OO0O0O00O00OO0 in OO00OOOO0O0O0OO00 :#line:137
        O00O0O0O0O0OOO0OO =get_image_info (O00OOO00OO00OO0OO )#line:138
        O00O00OO0OOOOO00O =get_exif_data (O00OOO00OO00OO0OO )#line:139
        O0O00000O0O000O00 =get_gps_info (O00O00OO0OOOOO00O )#line:140
        OO000O0OO0000OOOO ["image_info"]=O00O0O0O0O0OOO0OO #line:141
        OO000O0OO0000OOOO ["exif_data"]=O00O00OO0OOOOO00O #line:142
        OO000O0OO0000OOOO ["gps_info"]=O0O00000O0O000O00 #line:143
    else :#line:144
        OO000O0OO0000OOOO ["image_info"]="N/A"#line:145
        OO000O0OO0000OOOO ["exif_data"]="N/A"#line:146
        OO000O0OO0000OOOO ["gps_info"]="N/A"#line:147
    return OO000O0OO0000OOOO #line:149
def browse_file ():#line:151
    ""#line:152
    O0OO0O0OOO0O0OOO0 =filedialog .askopenfilename ()#line:153
    if O0OO0O0OOO0O0OOO0 :#line:154
        file_entry .delete (0 ,tk .END )#line:155
        file_entry .insert (0 ,O0OO0O0OOO0O0OOO0 )#line:156
        process_file (O0OO0O0OOO0O0OOO0 )#line:157
def process_file (O0OO000O00O00OO00 ):#line:159
    ""#line:160
    if not os .path .isfile (O0OO000O00O00OO00 ):#line:161
        messagebox .showerror ("Error",f"'{O0OO000O00O00OO00}' is not a valid file.")#line:162
        return #line:163
    OO0O0OO0OOO00OOOO =extract_metadata (O0OO000O00O00OO00 )#line:164
    output_text .delete ('1.0',tk .END )#line:165
    output_text .insert (tk .END ,json .dumps (OO0O0OO0OOO00OOOO ,indent =4 ))#line:166
def copy_to_clipboard ():#line:168
    ""#line:169
    O0O00OO0OO00OOOO0 =output_text .get ('1.0',tk .END )#line:170
    root .clipboard_clear ()#line:171
    root .clipboard_append (O0O00OO0OO00OOOO0 )#line:172
    messagebox .showinfo ("Copied","Metadata copied to clipboard!")#line:173
root =tk .Tk ()#line:176
root .title ("Metadata Extractor made by titan")#line:177
root .configure (bg ="#121212")#line:178
root .geometry ("850x650")#line:179
style =ttk .Style ()#line:182
style .theme_use ('clam')#line:183
style .configure ("TFrame",background ="#121212")#line:184
style .configure ("TLabel",background ="#121212",foreground ="#E0E0E0",font =("Helvetica",11 ))#line:185
style .configure ("TButton",background ="#2C2C2C",foreground ="#E0E0E0",font =("Helvetica",10 ))#line:186
style .configure ("TEntry",fieldbackground ="#2C2C2C",background ="#2C2C2C",foreground ="#E0E0E0",font =("Helvetica",10 ))#line:187
style .map ("TButton",background =[('active','#3C3C3C')],foreground =[('active','#FFFFFF')])#line:190
main_frame =ttk .Frame (root ,padding =10 )#line:193
main_frame .pack (fill =tk .BOTH ,expand =True )#line:194
title_label =ttk .Label (main_frame ,text ="Metadata Extractor shitty hub",font =("Helvetica",16 ,"bold"))#line:197
title_label .pack (pady =(0 ,10 ))#line:198
file_frame =ttk .Frame (main_frame )#line:201
file_frame .pack (fill =tk .X ,pady =(0 ,10 ))#line:202
file_label =ttk .Label (file_frame ,text ="File Path:")#line:204
file_label .pack (side =tk .LEFT ,padx =(0 ,5 ))#line:205
file_entry =ttk .Entry (file_frame ,width =60 )#line:207
file_entry .pack (side =tk .LEFT ,fill =tk .X ,expand =True ,padx =(0 ,5 ))#line:208
browse_button =ttk .Button (file_frame ,text ="Browse",command =browse_file )#line:210
browse_button .pack (side =tk .LEFT )#line:211
text_frame =ttk .Frame (main_frame )#line:214
text_frame .pack (fill =tk .BOTH ,expand =True ,pady =(10 ,10 ))#line:215
output_text =tk .Text (text_frame ,wrap =tk .NONE ,bg ="#1E1E1E",fg ="#E0E0E0",insertbackground ="#E0E0E0",font =("Courier",10 ))#line:217
output_text .pack (side =tk .LEFT ,fill =tk .BOTH ,expand =True )#line:218
scrollbar =ttk .Scrollbar (text_frame ,orient ="vertical",command =output_text .yview )#line:220
scrollbar .pack (side =tk .RIGHT ,fill =tk .Y )#line:221
output_text .config (yscrollcommand =scrollbar .set )#line:222
action_frame =ttk .Frame (main_frame )#line:225
action_frame .pack (fill =tk .X )#line:226
copy_button =ttk .Button (action_frame ,text ="Copy Metadata",command =copy_to_clipboard )#line:228
copy_button .pack (side =tk .RIGHT )#line:229
root .mainloop ()#line:231
