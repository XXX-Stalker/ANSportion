import requests
import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_ip_info(ip):
    if not validate_ip(ip):
        return "输入的 IP 地址不合法，请输入有效的 IP 地址。"
    api_url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
    try:
        response = requests.get(api_url, timeout=5)  # 设置超时时间为 5 秒
        response.raise_for_status()  # 检查 HTTP 状态码
        data = response.json()
        if data['status'] == 'success':
            return data
        else:
            return f"查询失败，原因：{data['message']}"
    except requests.exceptions.RequestException as e:
        return f"请求失败，错误信息：{str(e)}"

def check_2_main():
    ip = input("请输入 IP 地址:")
    ip_info = get_ip_info(ip)
    if isinstance(ip_info, dict):
        print("IP 信息：")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print(ip_info)