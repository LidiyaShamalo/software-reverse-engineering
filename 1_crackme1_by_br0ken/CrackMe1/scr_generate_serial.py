import sys

def generate_serial(name):
    if not (2 <= len(name) <= 10):
        print("[-] Ошибка: Длина имени должна быть от 2 до 10 символов!")
        return None
        
    serial_num = 0
    name_bytes = list(name.encode('utf-8'))
    name_bytes.append(0) 

    for i in range(len(name_bytes)):
        char_val = name_bytes[i]
        
        if char_val > 127:
            char_val -= 256
            
        serial_num = (serial_num + char_val - 1) & 0xFFFFFFFF
        
    if serial_num > 0x7FFFFFFF:
        serial_num -= 0x100000000
        
    return serial_num

name_input = "Velana" 
serial = generate_serial(name_input)
print(f"Name: {name_input} -> Serial: {serial}")
