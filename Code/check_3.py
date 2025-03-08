import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    else:
        return False

def check_3_main():
    ip = input("IP:")
    test_ips = [ip]
    for ip in test_ips:
        print(f"IP地址 {ip} 是否有效: {is_valid_ipv4(ip)}")