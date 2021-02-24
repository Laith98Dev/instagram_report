import os

lib = input("""

[1] Download lib & update

[2] pass

[+] Please Choice >> """)

if lib == "1":

    os.system('pip install requests')

    os.system('pip install datetime')

    os.system('pip install colorama')

    os.system('cls' if os.name == 'nt' else 'clear')

    pass

else:

    os.system('cls' if os.name == 'nt' else 'clear')

    pass

import requests

import json

import secrets

from colorama import Fore, Style

from time import sleep

from datetime import datetime

try:

    os.system('color')

except:

    pass

r       = requests.Session()

G       = Fore.GREEN

R       = Fore.RED

Y       = Fore.YELLOW

a       = 0

b       = 0

c       = 0

d       = 0

e       = 0

f       = 0

g       = 0

h       = 0

z       = 0

cookie  = secrets.token_hex(8)*2

time_now= int(datetime.now().timestamp())

banner = (G+"""

[!] Coded By : @o_7ay on Telegram

 ___ _   _ ____ _____  _    ____  _____ ____   ___  ____ _____ 

|_ _| \ | / ___|_   _|/ \  |  _ \| ____|  _ \ / _ \|  _ \_   _|

 | ||  \| \___ \ | | / _ \ | |_) |  _| | |_) | | | | |_) || |  

 | || |\  |___) || |/ ___ \|  _ <| |___|  __/| |_| |  _ < | |  

|___|_| \_|____/ |_/_/   \_\_| \_\_____|_|    \___/|_| \_\|_|                          

"""+Style.RESET_ALL)

print(banner)

print(G+"="*37+Style.RESET_ALL)

def Secure():

    global cookie_jar, csrf_token

    ig_nrcb = cookie_jar['ig_nrcb']

    ig_did = cookie_jar['ig_did']

    mid = cookie_jar['mid']

    sec_url='https://www.instagram.com'+json_login['checkpoint_url']

    head2 = {

        "accept": "*/*",

        "accept-encoding": "gzip, deflate, br",

        "accept-language": "en-US,en;q=0.9",

        "content-type": "application/x-www-form-urlencoded",

        "cookie": 'ig_did='+ig_did+'; ig_nrcb='+ig_nrcb+'; csrftoken='+csrf_token+'; mid='+mid,

        "origin": "https://www.instagram.com",

        "referer": 'https://instagram.com'+json_login['checkpoint_url'],

        "sec-fetch-dest": "empty",

        "sec-fetch-mode": "cors",

        "sec-fetch-site": "same-origin",

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",

        "x-csrftoken": csrf_token,

        "x-ig-app-id": "936619743392459",

        "x-ig-www-claim": "0",

        "x-instagram-ajax": "e8e20d8ba618",

        "x-requested-with": "XMLHttpRequest"

    }

    code =input(Y+'[+] '+json.loads(requests.post(sec_url, headers=head2, data={'choice': '1'}).text)['extraData']['content'][1]['text']+' : '+Style.RESET_ALL)

    if json.loads(requests.post(sec_url, headers=head2, data={'security_code': code}).text)['type']=='CHALLENGE_REDIRECTION':

        login2 = requests.post(log_url, data=payload, headers=head)

        print(G+'[-] Login Done'+Style.RESET_ALL)

        pass

    else:

        print(R+'[!] Login Failed'+Style.RESET_ALL)

        sleep(3)

        exit()

option = input(G+"""

[1] Use one Insta Account

[2] Use Unlimited Account

[+] Enter one option : """)

print(G+"="*37+Style.RESET_ALL)

if option == '1':

    username = input(Y+'[+] Enter Insta UserName : ')

    password = input(Y+'[+] Enter Insta Password : ')

    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {

        "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",

        'x-csrftoken': 'missing',

        'mid': cookie

    }

    data = {

        'username':f'{username}',

        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}',

        'queryParams': '{}',

        'optIntoOneTap': 'false'

    }

    login = r.post(url, headers=headers, data=data)

    json_login = json.loads(login.text)

    cookies = login.cookies

    cookie_jar = cookies.get_dict()

    try:

        csrf_token = cookie_jar['csrftoken']

    except:

        csrf_token = cookie

    try:

        if 'userId' in login.text:

            r.headers.update({'X-CSRFToken': cookies['csrftoken']})

            print(G+'[-] Login Done'+Style.RESET_ALL)

            pass

        else:

            print(R+'[-] Login Failed'+Style.RESET_ALL)

            sleep(2)

            exit()

    except:

        try:

            if json_login["message"]=="checkpoint_required":

                Secure()

        except KeyError:

            try:

                if json_login["message"]=="checkpoint_required":

                    Secure()

            except:

                print(R+'[-] Login Failed'+Style.RESET_ALL)

                sleep(2)

                exit()

    #########################################################

    TA = input(Y+'[+] Enter User Target : ')

    SL = int(input('[+] Enter Sleep : '))

    R1 = int(input('[+] Enter Count of spam : '))

    R2 = int(input('[+] Enter Count of Harassment : '))

    R3 = int(input('[+] Enter Count of Sale drugs : '))

    R4 = int(input('[+] Enter Count of Violence : '))

    R5 = int(input('[+] Enter Count of Nudity : '))

    R6 = int(input('[+] Enter Count of Hate : '))

    R7 = int(input('[+] Enter Count of Self injury : '))

    R8 = int(input('[+] Enter Count of Me : '))

    print(Style.RESET_ALL)

    #########################################################

    url_id = 'https://www.instagram.com/{}/?__a=1'.format(TA)

    req = r.get(url_id).json()

    idd = str(req['logging_page_id'])

    TA_ID = idd.split('_')[1]

    for i in range(R1):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'1','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            a +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R2):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'7','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            b +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R3):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'3','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            c +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R4):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'5','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            d +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R5):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'4','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            e +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R6):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'6','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            f +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R7):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'2','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            g +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

    for i in range(R8):

        url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

        data1 = {'source_name':'','reason_id':'8','frx_context':''}

        report = r.post(url1,data=data1)

        if '"status": "ok"' in report.text:

            h +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        else:

            z +=1

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

        sleep(SL)

        

elif option == '2':

    #########################################################

    TA = input(Y+'[+] Enter User Target : ')

    R1 = int(input('[+] Enter Count of spam : '))

    R2 = int(input('[+] Enter Count of Harassment : '))

    R3 = int(input('[+] Enter Count of Sale drugs : '))

    R4 = int(input('[+] Enter Count of Violence : '))

    R5 = int(input('[+] Enter Count of Nudity : '))

    R6 = int(input('[+] Enter Count of Hate : '))

    R7 = int(input('[+] Enter Count of Self injury : '))

    R8 = int(input('[+] Enter Count of Me : '))

    print(Style.RESET_ALL)

    #########################################################

    for x in open('Accounts.txt','r').read().splitlines():

        username = x.split(":")[0]

        password = x.split(":")[1]

        url = 'https://www.instagram.com/accounts/login/ajax/'

        headers = {

            "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",

            'x-csrftoken': 'missing',

            'mid': cookie

        }

        data = {

            'username':f'{username}',

            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}',

            'queryParams': '{}',

            'optIntoOneTap': 'false'

        }

        print(Y+f'[-] {username}:{password}'+Style.RESET_ALL)

        login = r.post(url, headers=headers, data=data)

        json_login = json.loads(login.text)

        cookies = login.cookies

        cookie_jar = cookies.get_dict()

        try:

            csrf_token = cookie_jar['csrftoken']

        except:

            csrf_token = cookie

        try:

            if 'userId' in login.text:

                r.headers.update({'X-CSRFToken': cookies['csrftoken']})

                print(G+'[-] Login Done'+Style.RESET_ALL)

                pass

            else:

                print(R+'[-] Login Failed'+Style.RESET_ALL)

                sleep(2)

                exit()

        except:

            try:

                if json_login["message"]=="checkpoint_required":

                    Secure()

            except KeyError:

                try:

                    if json_login["message"]=="checkpoint_required":

                        Secure()

                except:

                    print(R+'[-] Login Failed'+Style.RESET_ALL)

                    sleep(2)

                    exit()

        url_id = 'https://www.instagram.com/{}/?__a=1'.format(TA)

        req = r.get(url_id).json()

        idd = str(req['logging_page_id'])

        TA_ID = idd.split('_')[1]

        for i in range(R1):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'1','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                a +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R2):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'7','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                b +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R3):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'3','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                c +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R4):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'5','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                d +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R5):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'4','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                e +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R6):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'6','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                f +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R7):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'2','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                g +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        for i in range(R8):

            url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)

            data1 = {'source_name':'','reason_id':'8','frx_context':''}

            report = r.post(url1,data=data1)

            if '"status": "ok"' in report.text:

                h +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            else:

                z +=1

                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'{banner}\n==============[Free By @O0Dev on Tele]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')

            sleep(0.5)

        url_out = 'https://www.instagram.com/accounts/logout/ajax/'

        data_out = {

            'one_tap_app_login': '0'

        }

        hed_out = {

            "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",

            'x-csrftoken': csrf_token,

            'mid': cookie

        }

        sleep(2)

        logout = r.post(url_out, headers=hed_out, data=data_out)

        if logout.status_code == 200:

            pass

        else:

            print(R+f'[!] Error In logout from [{username}:{passwors}]'+Style.RESET_ALL)
