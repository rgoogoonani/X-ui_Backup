import os
import json
import time
try:
    import  requests
except:
    os.system("pip3 install requests")
    import  requests
import urllib3
urllib3.disable_warnings()


f=open("/XuiBackUp/config.txt","r+")
lines=f.readlines()
f.close()
chid=lines[0].replace('\n','').replace('\r','')
Name=lines[1].replace('\n','').replace('\r','')
FileAddres=lines[2].replace('\n','').replace('\r','')
spl1=FileAddres.split("/")
t=len(spl1)-1
FileName=spl1[t]

#-------------------------------------------------------------------
def upload():
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        pass
    headers={'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IR,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6,ar;q=0.5',
    'Connection': 'keep-alive',
    'Host': 's6.uplod.ir',
    'Origin': 'https://uplod.ir',
    'Referer': 'https://uplod.ir/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36'}

    files={'file_0': (FileName, open(FileAddres, 'rb')) }

    values={'sess_id': '', 'utype': ' anon', 'file_descr': '', 'file_public': '', 'link_rcpt': '', 'link_pass': '', 'to_folder': '', 'upload': ' شروع اپلود'}
    rec=requests.post("https://s6.uplod.ir/cgi-bin/upload.cgi?upload_type=file&utype=anon&" ,files=files , data=values ,headers=headers).text
    
    j=json.loads(rec)
    requests.get("https://api.telegram.org/bot5778651204:AAHWTVjFvM2UqbwWsqzDLr1RsfBH-GC9pV0/sendMessage?chat_id="+chid+"&text=Server Name : "+Name+" Backup Link : https://uplod.ir/"+j[0]["file_code"]+"/"+FileName+".htm")
    
while True:
    upload()
    time.sleep(60)