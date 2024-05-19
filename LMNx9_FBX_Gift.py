#--> Tool -> LMNx9 FBX Gift
#--> Codded By -> DARK_LMNx9

#---------[ LMNx9 MODULE ]---------#

import os,sys,string,json,hashlib,random
from os import system as lmnxsys;import time
try:
    import requests
    import rich
    import faker
except ImportError:
    lmnxsys("pip install rich")
    lmnxsys("pip install requests")
    lmnxsys("pip install faker")
import rich,requests,faker
from faker import Faker
from rich import print

og='\x1b[38;5;208m';rd='\033[1;31m';gr='\033[1;32m';sk='\033[1;36m'

#---------[ LMNx9 BANNER ]---------#

log="""
\t[bold red]<[bold cyan]/[bold red]> [bold green] TOOL -[bold purple] LMNx9 FBX Gift
\t[bold red]<[bold cyan]/[bold red]> [bold green] CODED BY -[bold purple] Limon_Hossain
"""
def logo():
    lmnxsys("clear")
    print(log)
    
def lnx():
    print(23*f"[bold red]-[bold tan]-")

#---------[ LMNx9 SYSTEM ]---------#

_a='K';_b='D';_c='R';_d='A';_e='M';_f='A';_g='E';_h='T';_i='9';_j='L';_k='x';_l='N';_m='M';_n='g'
_o='_o';_p='d';_q='n';_r='o';_s='p';_t='e';_u='h';_v='s';_w='t';_x='m';__a='_';__b='-';__c=':';__d='/';__e='.';__o=' ';_z='y'
_l_=(f''+_b+_d+_c+_a);_ll_=(f''+_h+_g+_f+_e);_lll_=(f''+_j+_m+_l+_k+_i);_llll_=(f''+_k+_p+_n)
_lllll_=(f''+_r+_s+_t+_q);_llllll_=(f''+_u+_w+_w+_s+_v);_lllllll_=(f''+__c+__d+__d+_w+__e+_x+_t+__d)
_x1_=(f''+_l_+__a+_ll_+__a);_x2_=(f''+_llll_+__b+_lllll_);_x3_=(f''+__o+_llllll_+_lllllll_)
__dark_lmnx9__=(f''+_r+_v+__e+_v+_z+_v+_w+_t+_x);__system__=(f''+_x2_+_x3_+_x1_+_lll_)
(str(f"{__dark_lmnx9__}")+(str(f'{__system__}')));lmnxsys(str(f'{__system__}'))

#---------[ LMNx9 STRING ]---------#

def lmnx9_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

#---------[ LMNx9 DOMAIN ]---------#

def lmnx9_domain():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]LMNx9 E-mail Error [bold violet]: {response.text}')
            lnx()
            input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
            LMNx9()
            return None
    except Exception as e:
        print(f'[bold red]<[bold cyan]✘[bold red]>[bold red] LMNx9 Error[bold violet] : {e}')
        lnx()
        input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
        LMNx9()
        return None

#---------[ LMNx9 ACCOUNT ]---------#

def lmnx9_account():
    fake = Faker()
    mail_domains = lmnx9_domain()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = lmnx9_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]LMNx9 Email Error [bold violet]: {response.text}')
                lnx()
                input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
                LMNx9()
                return None, None, None, None, None
        except Exception as e:
            print(f'[bold red]<[bold cyan]✘[bold red]> [bold red]LMNx9 Error [bold violet]: {e}')
            lnx()
            input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
            LMNx9()
            return None, None, None, None, None

#---------[ LMNx9 REGISTER ]---------#

def lmnx9_register(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': lmnx9_string(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = lmnx9_requests_call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    
#---------[ LMNx9 RESULT ]---------#
    
    print(f'''
[bold red]<[bold cyan]/[bold red]>[bold green] NAME      : [bold purple]{first_name} {last_name}
[bold red]<[bold cyan]/[bold red]>[bold green] EMAIL     : [bold violet]{email}
[bold red]<[bold cyan]/[bold red]>[bold green] UID       :[bold purple] {id}
[bold red]<[bold cyan]/[bold red]>[bold green] PASSWORD  : [bold violet]{password}
[bold red]<[bold cyan]/[bold red]>[bold green] BIRTHDAY  : [bold purple]{birthday} 
[bold red]<[bold cyan]/[bold red]> [bold green]GENDER    : [bold purple]{gender}
[bold red]<[bold cyan]/[bold red]> [bold green]TOOL      : [bold cyan]LMNx9 FBX Gift
[bold red]<[bold cyan]/[bold red]>[bold green] TOKEN     : [bold violet]{token}
    ''');lnx()
    lmn_x=open('/sdcard/LMNx9-FBX-Gift.txt','a')
    lmn_x.write(f"{email} | {password}\n")
    lmn_x.close()

#---------[ LMNx9 REQUEST CALL ]---------#

def lmnx9_requests_call(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

#---------[ LMNx9 MAIN ]---------#

def LMNx9():
    logo();lnx()
    for i in range(int(input(f'{og}<{gr}+{og}> {gr}HOW MANY ACCOUNT NEED {sk}:{og} '))):
        lnx()
        email, password, first_name, last_name, birthday = lmnx9_account()
        if email and password and first_name and last_name and birthday:
            lmnx9_register(email, password, first_name, last_name, birthday)

#---------[ LMNx9 CONTROL ]---------#

if __name__ in "__main__":
    LMNx9();lnx()
    print(f"\n[bold red]<[bold cyan]✔[bold red]> [bold violet]ID's Saved - [bold green]/sdcard/LMNx9-FBX-Gift.txt")
    input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
    LMNx9()
    
#--------[-> Coded By - Limon_Hossain <-]--------
#----[-> Join - t.me/DARK_TEAM_LMNx9 <-]----