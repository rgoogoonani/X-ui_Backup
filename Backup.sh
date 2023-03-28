sudo apt update -y
sudo apt upgrade -y
sudo apt install python3.9 -y
sudo apt install python3-pip -y
sudo mkdir /XuiBackUp
cd /XuiBackUp
sudo wget https://raw.githubusercontent.com/rgoogoonani/X-ui_Backup/main/Startup.py
sudo wget https://raw.githubusercontent.com/rgoogoonani/X-ui_Backup/main/AutoBackup.py
sudo python3 /XuiBackUp/Startup.py
