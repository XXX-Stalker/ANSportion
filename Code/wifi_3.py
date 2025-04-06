import pywifi
import time
import sys
from threading import Thread

def animate_scanning():
    chars = "|/-\\"
    i = 0
    while getattr(animate_scanning, "running", True):
        sys.stdout.write(f"\r扫描中... {chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r扫描完成!          \n")

def wifi_3_main():
    time_stop = input("请输入扫描时间(秒，建议3-10): ")
    try:
        time_stop = int(time_stop)
    except ValueError:
        print("请输入有效的数字!")
        return
    animate_scanning.running = True
    t = Thread(target=animate_scanning)
    t.start()
    wifi_list = scan_wifi(time_stop)
    animate_scanning.running = False
    t.join()
    print("\n扫描结果:")
    for i, wifi in enumerate(wifi_list, 1):
        print(f"{i}. SSID: {wifi['ssid']} | 信号强度: {wifi['signal']}dBm | MAC: {wifi['address']}")

def scan_wifi(time_stop):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(time_stop)
    results = iface.scan_results()
    return [
        {'address': result.bssid, 
         'ssid': result.ssid, 
         'signal': result.signal}
        for result in results
    ]