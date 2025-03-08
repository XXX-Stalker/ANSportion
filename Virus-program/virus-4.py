from pywifi import PyWiFi, const

def disconnect_wifi():
    # 创建一个PyWiFi对象
    wifi = PyWiFi()
    # 获取第一个无线网卡接口
    iface = wifi.interfaces()[0]
    # 断开当前WiFi连接
    iface.disconnect()
    # 检查网卡是否处于断开状态
    if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        print(f"无线网卡 {iface.name()} 已断开!")
    else:
        print(f"无线网卡 {iface.name()} 未成功断开!")

def main():
    while True:
        disconnect_wifi()

if __name__ == "__main__":
    main()