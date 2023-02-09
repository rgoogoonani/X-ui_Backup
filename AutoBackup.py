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
from pathlib import Path

f=open("/etc/systemd/system/x-uiAutoBackup.service","w")
f.writelines("[Unit]\nDescription=x-ui Auto Backup\nAfter=network-online.target\nAfter=dbus.service\n\n[Service]\nType=forking\nExecStart=python3 "+Path.cwd()+"/AutoBackup.py\nExecReload=pkill python3\n\n[Install]\nWantedBy=multi-user.target")
f.close()

try:
    f=open("config.txt","r+")
except:
    f=open("config.txt","w")
    f.close()
    f=open("config.txt","r+")
chid=""
Name=""
FileAddres=""

lines=f.readlines()
if len(lines)>0:
    print(lines)
    chid=lines[0].replace('\n','').replace('\r','')
    Name=lines[1].replace('\n','').replace('\r','')
    FileAddres=lines[2].replace('\n','').replace('\r','')
    f.close()
else:
    f.close()
    chid=input("Chatid : ")
    if chid=="":
        chid="189875244"
    print(chid)
    #-------------------------------------------------------------------
    Name=input("Server Name : ")
    print(Name)
    #-------------------------------------------------------------------
    FileAddres=input("File Addres : ")
    if FileAddres=="":
        FileAddres="/etc/x-ui-english/x-ui-english.db"
    print(FileAddres)
    f=open("config.txt","w")

    f.writelines(chid+'\n'+Name+'\n'+FileAddres)
    f.close()


spl1=FileAddres.split("/")
t=len(spl1)-1
FileName=spl1[t]
print("Uploading : "+FileName)

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
    print("uploaded")
os.system("sudo systemctl start x-uiAutoBackup")
os.system("systemctl enable x-uiAutoBackup")
while True:
    upload()
    time.sleep(60)