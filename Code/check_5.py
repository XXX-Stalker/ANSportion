import psutil
import socket

def get_mac_by_ip(ip):
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == ip:
                for mac_addr in addrs:
                    if mac_addr.family == psutil.AF_LINK:
                        return mac_addr.address
    return None

def check_5_main():
    ip = input("请输入IP地址: ")
    mac = get_mac_by_ip(ip)
    print(f"IP: {ip}, MAC: {mac}")