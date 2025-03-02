import requests
import socket
import subprocess
import re
def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            data = response.json()
            return data.get('origin')
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"请求异常: {e}")
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error as e:
        print(f"获取本地 IP 时发生错误: {e}")
def get_gateway_ip_windows():
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        output = result.stdout
        pattern = r"默认网关.*?:\s*([\d\.]+)"
        match = re.search(pattern, output)
        if match:
            gateway_ip = match.group(1)
            return gateway_ip
        else:
            print("未找到默认网关信息。")
            return None
    except Exception as e:
        print(f"执行命令出错: {e}")
        return None
def check_1_main():
    gateway_ip = get_gateway_ip_windows()
    if gateway_ip:
        print(f"网关 IP 地址: {gateway_ip}")
    print("公网IP:", get_public_ip())
    print("局域网IP:", get_local_ip())