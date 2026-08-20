import ctypes
import subprocess
import time

CREATE_SUSPENDED = 0x00000004
PAGE_EXECUTE_READWRITE = 0x40

TARGET_PROCESS = "Crackme3.exe"

MEMORY_PATCHES = {
    0x004013EA: b"\x74",  
    0x004013F1: b"\x74", 
    0x004013FD: b"\x74",  
    0x0040140C: b"\x74", 
    0x00401419: b"\x74",  
    0x00401423: b"\x74",  
    0x0040142A: b"\x74",  
    0x00401437: b"\x74",  
    0x00401405: b"\x75",
}

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", ctypes.c_void_p),
        ("hThread", ctypes.c_void_p),
        ("dwProcessId", ctypes.c_ulong),
        ("dwThreadId", ctypes.c_ulong)
    ]

class STARTUPINFO(ctypes.Structure):
    _fields_ = [
        ("cb", ctypes.c_ulong), ("lpReserved", ctypes.c_char_p), ("lpDesktop", ctypes.c_char_p),
        ("lpTitle", ctypes.c_char_p), ("dwX", ctypes.c_ulong), ("dwY", ctypes.c_ulong),
        ("dwXSize", ctypes.c_ulong), ("dwYSize", ctypes.c_ulong), ("dwXCountChars", ctypes.c_ulong),
        ("dwYCountChars", ctypes.c_ulong), ("dwFillAttribute", ctypes.c_ulong), ("dwFlags", ctypes.c_ulong),
        ("wShowWindow", ctypes.c_ushort), ("cbReserved2", ctypes.c_ushort), ("lpReserved2", ctypes.c_char_p),
        ("hStdInput", ctypes.c_void_p), ("hStdOutput", ctypes.c_void_p), ("hStdError", ctypes.c_void_p)
    ]

def launch_and_patch():
    si = STARTUPINFO()
    si.cb = ctypes.sizeof(si)
    pi = PROCESS_INFORMATION()

    print(f"[*] Запуск {TARGET_PROCESS} в режиме SUSPENDED...")
    success = ctypes.windll.kernel32.CreateProcessA(
        None, TARGET_PROCESS.encode('ascii'), None, None, False,
        CREATE_SUSPENDED, None, None, ctypes.byref(si), ctypes.byref(pi)
    )

    if not success:
        print(f"[!] Не удалось запустить процесс. Ошибка: {ctypes.windll.kernel32.GetLastError()}")
        return

    h_process = pi.hProcess
    h_thread = pi.hThread

    kernel32 = ctypes.windll.kernel32
    for addr, data in MEMORY_PATCHES.items():
        old_protect = ctypes.c_ulong(0)
        data_len = len(data)
        bytes_written = ctypes.c_size_t(0)

        kernel32.VirtualProtectEx(h_process, addr, data_len, PAGE_EXECUTE_READWRITE, ctypes.byref(old_protect))
        
        res = kernel32.WriteProcessMemory(h_process, addr, data, data_len, ctypes.byref(bytes_written))
        
        kernel32.VirtualProtectEx(h_process, addr, data_len, old_protect, ctypes.byref(old_protect))

        if res:
            print(f"[+] Память по адресу 0x{addr:X} успешно изменена на {data.hex().upper()}")
        else:
            print(f"[!] Ошибка записи по адресу 0x{addr:X}. Код: {kernel32.GetLastError()}")

    print("[*] Возобновление потока...")
    kernel32.ResumeThread(h_thread)

    kernel32.CloseHandle(h_thread)
    kernel32.CloseHandle(h_process)
    print("[+++] Лоадер отработал успешно!")

if __name__ == "__main__":
    launch_and_patch()
