import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not pattern.match(ip):
        return False
    parts = ip.split('.')
    for part in parts:
        try:
            num = int(part)
            if not 0 <= num <= 255:
                return False
        except ValueError:
            return False
    return True

def is_valid_ipv6(ip):
    pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,6}::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}$')
    return bool(pattern.match(ip))

def check_ip_address(ip):
    if ':' in ip:
        return 'IPv6', is_valid_ipv6(ip)
    else:
        return 'IPv4', is_valid_ipv4(ip)

def check_2_main():
    print("IP地址验证工具")
    print("1. 验证单个IP地址")
    print("2. 批量验证IP地址")
    while True:
        choice = input("请选择模式(1/2): ").strip()
        if choice in ('1', '2'):
            break
        print("无效输入，请重新选择")
    if choice == '1':
        while True:
            ip = input("请输入要验证的IP地址: ").strip()
            if ip:
                ip_type, is_valid = check_ip_address(ip)
                print(f"IP地址 {ip} 类型: {ip_type}, 有效性: {'有效' if is_valid else '无效'}")
                break
            print("IP地址不能为空，请重新输入")
    else:
        print("请输入多个IP地址，用空格或逗号分隔:")
        ips_input = input("IP地址列表: ").strip()
        separators = re.compile(r'[,\s]+')
        ips = separators.split(ips_input)
        print("\n验证结果:")
        for ip in ips:
            if ip:
                ip_type, is_valid = check_ip_address(ip)
                print(f"{ip:<20} 类型: {ip_type:<5} 有效性: {'有效' if is_valid else '无效'}")