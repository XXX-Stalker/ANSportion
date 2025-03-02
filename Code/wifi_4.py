import pywifi
from pywifi import const
import time
import sys

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    # 断开当前连接
    iface.disconnect()
    time.sleep(1)
    
    # 检查是否已经连接到指定的Wi-Fi
    if iface.status() == const.IFACE_CONNECTED and iface.ssid() == ssid:
        print(f"已连接到 {ssid}")
        return True
    
    # 如果没有连接，则尝试连接
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(5)  # 等待连接
    
    # 检查连接状态
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
                # 如果连接失败，可以选择重试或者退出
                print("尝试重新连接...")
                continue
            # 如果已连接，则保持程序运行以维持连接状态
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print("用户手动终止程序。")