import psutil
import socket

def list_all_interfaces():
    try:
        print("\n可用网络接口:")
        all_interfaces = psutil.net_if_addrs()
        
        for interface, addrs in all_interfaces.items():
            print(f"\n接口: {interface}")
            ipv4_addrs = []
            mac_addr = None
            
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ipv4_addrs.append(addr.address)
                elif addr.family == psutil.AF_LINK:
                    mac_addr = addr.address.upper()
            
            if ipv4_addrs:
                print("  IPv4地址:", ", ".join(ipv4_addrs))
            if mac_addr:
                print("  MAC地址:", mac_addr)
        print("\n")
    except Exception as e:
        print(f"获取网络接口信息时出错: {e}")

def check_4_main():
    list_all_interfaces()