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

lines = ""
with open("/XuiBackUp/config.txt","r+") as f :
    lines=f.read().split("\n")
    lines=[i.replace("\r","") for i in lines]
chid=lines[0]
Name=lines[1]
FileAddres=lines[2]
spl1=FileAddres.split("/")
t=len(spl1)-1
FileName=spl1[t]

#-------------------------------------------------------------------
def upload():
    
    requests.get("https://api.telegram.org/bot5778651204:AAHWTVjFvM2UqbwWsqzDLr1RsfBH-GC9pV0/sendDocument?chat_id="+chid+"&caption=Server Name : "+Name,files={'document': (FileName, open(FileAddres, 'rb'))})
    print("uploaded")
while True:
    upload()
    time.sleep(60)