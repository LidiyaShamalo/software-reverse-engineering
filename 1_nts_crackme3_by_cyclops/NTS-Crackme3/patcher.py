import os
import shutil

TARGET_FILE = "Crackme3.exe"
BACKUP_FILE = "NTS-Crackme3.bak"

PATCHES = {
    0x13EA: b"\x74",  
    0x13F1: b"\x74", 
    0x13FD: b"\x74",  
    0x140C: b"\x74", 
    0x1419: b"\x74",  
    0x1423: b"\x74",  
    0x142A: b"\x74",  
    0x1437: b"\x74",  
    0x1405: b"\x75",  
}

def create_patch():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Файл {TARGET_FILE} не найден в текущей папке.")
        return

    if not os.path.exists(BACKUP_FILE):
        shutil.copyfile(TARGET_FILE, BACKUP_FILE)
        print(f"[+] Создан бэкап оригинального файла: {BACKUP_FILE}")

    try:
        with open(TARGET_FILE, "r+b") as f:
            for offset, new_bytes in PATCHES.items():
                f.seek(offset)          
                f.write(new_bytes)      
                print(f"[+] Смещение 0x{offset:X} успешно пропатчено байтами: {new_bytes.hex().upper()}")
        print("[+++] Файл полностью пропатчен!")
    except Exception as e:
        print(f"[!] Произошла ошибка: {e}")

if __name__ == "__main__":
    create_patch()
