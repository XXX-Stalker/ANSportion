import subprocess

def wifi_5_main():
    def get_connected_devices():
        # 执行 arp -a 命令
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        
        # 解析命令输出
        lines = result.stdout.split('\n')
        devices = []
        
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                ip_address = parts[0]
                mac_address = parts[1]
                device_name = parts[2] if len(parts) > 2 else 'Unknown'
                devices.append({
                    'IP Address': ip_address,
                    'MAC Address': mac_address,
                    'Device Name': device_name
                })
        
        return devices

    # 获取并打印连接设备的信息
    connected_devices = get_connected_devices()
    for device in connected_devices:
        print(f"IP Address: {device['IP Address']}, MAC Address: {device['MAC Address']}, Device Name: {device['Device Name']}")