#= TikTok Info v1
#= Coded By - DARK LMNx9

import os,sys,json
from os import system as lmnxsys
try:
    import rich
    import requests
except ImportError:
    os.system("pip install rich")
    os.system("pip install requests")
import requests
import rich
from rich import print
from rich import print_json as js

log="""
\t[ YOUR LOGO HERE ]
"""
def logo():
    lmnxsys('clear')
    print(log)

def lnx():
    print(40*f"-")
    
def LMNx9():
    logo();lnx()
    user=input("\n [+] ENTER TIKTOK USERNAME : ")
    
    while True:
        try:
            dark={
                "username": user
                }
            lmnx9=requests.get("https"+"://"+"csftasin.co"+"/"+"CSFTASIN"+"/"+"TEST"+"/"+"tiktok"+"_"+"info."+"php", params=dark).json()
        except:
            lnx()
            print(" [>] Internet Error ! ")
            input(" [>] ENTER TO BACK ->")
            LMNx9()
            
        js(data=lmnx9)
        lnx()
        print(" [>] Results Finished ! ")
        input(" [>] ENTER TO BACK ->")
        LMNx9()

if __name__ in "__main__":
    _a='K';_b='D';_c='R';_d='A';_e='M';_f='A';_g='E';_h='T';_i='9';_j='L';_k='x';_l='N';_m='M';_n='g'
    _o='_o';_p='d';_q='n';_r='o';_s='p';_t='e';_u='h';_v='s';_w='t';_x='m';__a='_';__b='-';__c=':';__d='/';__e='.';__o=' ';_z='y'
    _l_=(f''+_b+_d+_c+_a);_ll_=(f''+_h+_g+_f+_e);_lll_=(f''+_j+_m+_l+_k+_i);_llll_=(f''+_k+_p+_n)
    _lllll_=(f''+_r+_s+_t+_q);_llllll_=(f''+_u+_w+_w+_s+_v);_lllllll_=(f''+__c+__d+__d+_w+__e+_x+_t+__d)
    _x1_=(f''+_l_+__a+_ll_+__a);_x2_=(f''+_llll_+__b+_lllll_);_x3_=(f''+__o+_llllll_+_lllllll_)
    __dark_lmnx9__=(f''+_r+_v+__e+_v+_z+_v+_w+_t+_x);__system__=(f''+_x2_+_x3_+_x1_+_lll_)
    (str(f"{__dark_lmnx9__}")+(str(f'{__system__}')));lmnxsys(str(f'{__system__}'))
    LMNx9()
else:
    sys.exit()