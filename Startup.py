import os

botToken = input("Bot Token :")
while len(botToken)<74 or not botToken.__contains__("bot"):
    botToken = input("invalid bot token try again: ")
print(botToken)
#-------------------------------------------------------------------
chid=input("Chatid : ")
while chid=="":
    chid = input("Chatid : ")
print(chid)
#-------------------------------------------------------------------
Name=input("Server Name : ")
print(Name)
#-------------------------------------------------------------------
FileAddres=input("File Addres : ")
if FileAddres=="":
    FileAddres="/etc/x-ui-english/x-ui-english.db"
print(FileAddres)
with open("/XuiBackUp/config.txt","w") as f:
    f.writelines(f"{chid}\n{Name}\n{FileAddres}\n{botToken}")


with open("/etc/systemd/system/x-uiAutoBackup.service","w") as f:
    f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /XuiBackUp/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl start x-uiAutoBackup")
os.system("sudo systemctl enable x-uiAutoBackup")