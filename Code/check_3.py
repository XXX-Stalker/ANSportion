import socket
from urllib.parse import urlparse

def get_ips_from_url(url, ip_version='both'):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        print("无效的URL")
        return
    try:
        if ip_version == 'v4':
            families = [socket.AF_INET]
        elif ip_version == 'v6':
            families = [socket.AF_INET6]
        else:
            families = [socket.AF_INET, socket.AF_INET6]
        unique_ips = set()
        for family in families:
            try:
                ips = socket.getaddrinfo(hostname, None, family=family)
                for ip in ips:
                    unique_ips.add(ip[4][0])
            except socket.gaierror:
                continue  # 如果某种地址族没有记录则跳过
        if not unique_ips:
            print(f"网站 {hostname} 没有找到{_get_version_desc(ip_version)}地址")
            return
        print(f"网站 {hostname} 的{_get_version_desc(ip_version)}地址:")
        for ip in unique_ips:
            print(f"  - {ip}")
    except Exception as e:
        print(f"解析域名时出错: {e}")

def _get_version_desc(ip_version):
    return {
        'v4': 'IPv4',
        'v6': 'IPv6',
        'both': 'IP'
    }.get(ip_version, 'IP')

def check_3_main():
    print("IP地址扫描工具")
    print("1. 扫描IPv4地址")
    print("2. 扫描IPv6地址")
    print("3. 扫描所有IP地址")
    while True:
        choice = input("请选择扫描类型(1/2/3): ").strip()
        if choice == '1':
            ip_version = 'v4'
            break
        elif choice == '2':
            ip_version = 'v6'
            break
        elif choice == '3':
            ip_version = 'both'
            break
        else:
            print("无效选择，请重新输入")
    while True:
        url = input("请输入网站的URL(例如: www.example.com): ").strip()
        if url:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            break
        else:
            print("URL不能为空，请重新输入")
    get_ips_from_url(url, ip_version)