import pywifi
from pywifi import const
import time
def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # 等待扫描完成
    results = iface.scan_results()
    wifi_list = []
    for result in results:
        info = {
            'address': result.bssid,
            'ssid': result.ssid,
            'signal': result.signal
        }
        wifi_list.append(info)
    return wifi_list
def wifi_3_main():
    wifi_list = scan_wifi()
    for wifi in wifi_list:
        print(f"Address: {wifi['address']}, SSID: {wifi['ssid']}, Signal: {wifi['signal']}")