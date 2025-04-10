import json
import os
import getpass
import platform

def save_config(config_data, path='config.json'):
    with open(path, 'w') as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)
    print("تنظیمات با موفقیت در config.json ذخیره شد.")

def add_to_startup(script_path):
    system_type = platform.system()
    user = getpass.getuser()

    if system_type == "Linux":
        service_name = "xui_backup_autorun.service"
        service_content = f"""[Unit]
Description=Auto Backup Script for X-ui
After=network.target

[Service]
ExecStart=/usr/bin/python3 {script_path}
Restart=on-failure
User={user}
WorkingDirectory={os.path.dirname(script_path)}

[Install]
WantedBy=multi-user.target
"""
        service_path = f"/etc/systemd/system/{service_name}"

        try:
            with open(service_name, 'w') as f:
                f.write(service_content)
            os.system(f"sudo mv {service_name} {service_path}")
            os.system(f"sudo systemctl daemon-reexec")
            os.system(f"sudo systemctl daemon-reload")
            os.system(f"sudo systemctl enable {service_name}")
            print(f"سرویس استارت‌آپ با نام {service_name} با موفقیت ایجاد شد.")
        except PermissionError:
            print("خطا: دسترسی root نیاز است. لطفاً اسکریپت را با sudo اجرا کنید.")
    else:
        print("فعلاً فقط از سیستم‌های لینوکسی پشتیبانی می‌شود.")

def main():
    print("تنظیمات ارسال بکاپ به تلگرام\n")

    telegram_token = input("توکن ربات تلگرام را وارد کنید: ").strip()
    telegram_chat_id = input("شناسه چت تلگرام را وارد کنید: ").strip()
    backup_folder = input("مسیر پوشه‌ای که باید بکاپ گرفته شود را وارد کنید: ").strip()
    zip_file_name = input("نام فایل زیپ (مثلاً backup.zip): ").strip()

    use_proxy = input("آیا می‌خواهید از پروکسی HTTP استفاده کنید؟ (y/n): ").strip().lower()
    http_proxy = ""
    if use_proxy == "y":
        http_proxy = input("آدرس پروکسی HTTP را وارد کنید (مثلاً http://127.0.0.1:8080): ").strip()

    config = {
        "telegram_token": telegram_token,
        "telegram_chat_id": telegram_chat_id,
        "backup_folder": backup_folder,
        "zip_file_name": zip_file_name,
        "http_proxy": http_proxy
    }

    save_config(config)
    script_path = os.path.abspath("AutoBackup.py")
    add_to_startup(script_path)

if __name__ == '__main__':
    main()