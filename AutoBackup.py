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

try:
    f=open("/XuiBackUp/config.txt","r+")
except:
    f=open("/XuiBackUp/config.txt","w")
    f.close()
    f=open("/XuiBackUp/config.txt","r+")
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
    
    requests.get("https://api.telegram.org/bot5778651204:AAHWTVjFvM2UqbwWsqzDLr1RsfBH-GC9pV0/sendDocument?chat_id="+chid+"&caption=Server Name : "+Name,files={'document': (FileName, open(FileAddres, 'rb'))})
    print("uploaded")
while True:
    upload()
    time.sleep(60)