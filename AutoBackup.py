import os
import zipfile
import requests
import json
import time

MAX_SIZE = 49 * 1024 * 1024

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config['telegram_token']
CHAT_ID = config['telegram_chat_id']
FOLDER_PATH = config['backup_folder']
ZIP_NAME = config['zip_file_name']
HTTP_PROXY = config.get('http_proxy', '')

proxies = {}
if HTTP_PROXY:
    proxies = {
        'http': HTTP_PROXY,
        'https': HTTP_PROXY
    }

def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

def split_file(file_path, part_size):
    parts = []
    with open(file_path, 'rb') as f:
        i = 0
        while True:
            chunk = f.read(part_size)
            if not chunk:
                break
            part_file = f'{file_path}.part{i:03d}'
            with open(part_file, 'wb') as pf:
                pf.write(chunk)
            parts.append(part_file)
            i += 1
    return parts

def send_files_to_telegram(file_list):
    message = f'بکاپ پوشه "{FOLDER_PATH}" ارسال می‌شود. تعداد فایل‌ها: {len(file_list)}'
    requests.post(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
        data={'chat_id': CHAT_ID, 'text': message},
        proxies=proxies
    )

    for file_path in file_list:
        with open(file_path, 'rb') as f:
            response = requests.post(
                f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument',
                data={'chat_id': CHAT_ID},
                files={'document': f},
                proxies=proxies
            )
        if response.status_code != 200:
            print(f'ارسال فایل {file_path} با خطا مواجه شد.')

def main():
    if os.path.exists(ZIP_NAME):
        os.remove(ZIP_NAME)

    zip_folder(FOLDER_PATH, ZIP_NAME)
    zip_size = os.path.getsize(ZIP_NAME)

    if zip_size <= MAX_SIZE:
        send_files_to_telegram([ZIP_NAME])
    else:
        parts = split_file(ZIP_NAME, MAX_SIZE)
        send_files_to_telegram(parts)
        for p in parts:
            os.remove(p)
    os.remove(ZIP_NAME)

if __name__ == '__main__':
    while True:
    	main()
    	time.sleep(120)