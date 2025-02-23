import socket
import psutil
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None
def get_hardware_info():
    info = {
        "CPU": {
            "物理核心": psutil.cpu_count(logical=False),
            "总颜色": psutil.cpu_count(logical=True),
            "最大频率": f"{psutil.cpu_freq().max:.2f} MHz",
            "最小频率": f"{psutil.cpu_freq().min:.2f} MHz",
            "当前频率": f"{psutil.cpu_freq().current:.2f} MHz",
            "每核CPU使用率": [f"Core {i}: {usage}%" for i, usage in enumerate(psutil.cpu_percent(percpu=True, interval=1))],
            "总CPU使用率": f"{psutil.cpu_percent()}%"
        },
        "记忆": {
            "共计": f"{psutil.virtual_memory().total / (1024.0 **3):.2f} GB",
            "可用": f"{psutil.virtual_memory().available / (1024.0 **3):.2f} GB",
            "用过的": f"{psutil.virtual_memory().used / (1024.0 **3):.2f} GB",
            "百分比": f"{psutil.virtual_memory().percent}%"
        },
        "磁盘": {
            "共计": f"{psutil.disk_usage('/').total / (1024.0 **3):.2f} GB",
            "用过的": f"{psutil.disk_usage('/').used / (1024.0 **3):.2f} GB",
            "自由": f"{psutil.disk_usage('/').free / (1024.0 **3):.2f} GB",
            "百分比": f"{psutil.disk_usage('/').percent}%"
        },
        "网络": {
            "IP地址": get_ip_address(),
            "MAC地址": psutil.net_if_addrs()['eth0'][0].address if 'eth0' in psutil.net_if_addrs() else "没有找到"
        }
    }
    return info
def print_hardware_info(info):
    """打印硬件信息"""
    print("硬件信息:")
    for category, details in info.items():
        print(f"\n{category}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
def main():
    ip_address = input("输入要监控的计算机的IP地址(本机留空): ").strip()
    if not ip_address:
        ip_address = get_ip_address()
        if not ip_address:
            print("获取IP地址失败。")
            return
    print(f"监控IP的硬件信息: {ip_address}")
    info = get_hardware_info()
    print_hardware_info(info)
if __name__ == "__main__":
    main()
