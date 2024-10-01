#Part 1
def is_valid_part(part):
    if not part.isdigit():
        return False
    num = int(part)
    if num < 0 or num > 255:
        return False
    if part[0] == '0' and len(part) > 1:
        return False
    return True

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True

#Part 2

def decimal_to_binary(n):
    if n == "":
        return 0
    if isinstance(n, str):
        n = int(n)
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    if b == "":
        return 0
    return int(b[0]) * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])

#Part 3

def ip_to_binary(ip):
    parts = ip.split('.')
    stripped_parts = [str(int(part)) for part in parts]
    if not is_valid_ip('.'.join(stripped_parts)):
        return "Invalid IP address"
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in stripped_parts]
    return '.'.join(binary_parts)

def binary_to_ip(binary):
    binary_parts = binary.split('.')
    if len(binary_parts) != 4:
        return "Invalid binary representation"
    decimal_parts = []
    for part in binary_parts:
        decimal_part = binary_to_decimal(part)
        decimal_parts.append(str(decimal_part))
    return '.'.join(decimal_parts)

def ip_convert(ip):
    ip = '.'.join(part.lstrip('0') or '0' for part in ip.split('.'))
    if is_valid_ip(ip):
        return ip_to_binary(ip)
    elif all(bit in '01.' for bit in ip) and ip.count('.') == 3:
        return binary_to_ip(ip)
    else:
        return "Invalid input"

print(ip_convert(input("Convert IP address from decimal to binary or from binary to decimal:")))