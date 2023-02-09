import os

f=open("/etc/systemd/system/x-uiAutoBackup.service","w")
f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /XuiBackUp/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=x-ui Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")
f.close()

os.system("systemctl daemon-reload")
os.system("sudo systemctl start x-uiAutoBackup")
os.system("systemctl enable x-uiAutoBackup")