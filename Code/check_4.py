import socket
from urllib.parse import urlparse

def get_ips_from_url(url):
    # 解析URL，获取主机名
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        print("无效的URL")
        return
    try:
        # 获取所有IP地址
        ips = socket.getaddrinfo(hostname, None)
        unique_ips = set()
        # 提取并去重IP地址
        for ip in ips:
            unique_ips.add(ip[4][0])
        # 输出所有IP地址
        for ip in unique_ips:
            print(f"网站 {hostname} 的所有IP地址: {ip}")
    except socket.gaierror as e:
        print(f"无法解析域名: {e}")

def check_4_main():
    url = input("请输入网站的URL:")
    get_ips_from_url(url)