import pywifi
from pywifi import const
import time

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    if iface.status() == const.IFACE_CONNECTED and iface.ssid() == ssid:
        print(f"已连接到 {ssid}")
        return True
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:
        print(f"成功连接到 {ssid}")
        return True
    else:
        print(f"无法连接到 {ssid}")
        return False

def wifi_4_main():
    ssid = input("请输入 Wi-Fi 名称: ")
    password = input("请输入 Wi-Fi 密码: ")
    try:
        while True:
            if not connect_to_wifi(ssid, password):
                print("尝试重新连接...")
                continue
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print("用户手动终止程序")