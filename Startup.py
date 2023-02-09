import os

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
f=open("/XuiBackUp/config.txt","w")

f.writelines(chid+'\n'+Name+'\n'+FileAddres)
f.close()


f=open("/etc/systemd/system/x-uiAutoBackup.service","w")
f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /XuiBackUp/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")
f.close()

os.system("systemctl daemon-reload")
os.system("sudo systemctl start x-uiAutoBackup")
os.system("systemctl enable x-uiAutoBackup")