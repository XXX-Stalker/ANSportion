import subprocess
import platform

def get_connected_devices():
    system = platform.system()
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    
    lines = result.stdout.split('\n')
    devices = []
    
    for line in lines:
        parts = line.split()
        if system == "Darwin":  # macOS
            if len(parts) >= 4:
                ip_address = parts[1].strip("()")
                mac_address = parts[3]
                device_name = "Unknown"
                devices.append({
                    'IP Address': ip_address,
                    'MAC Address': mac_address,
                    'Device Name': device_name
                })
        else:  # Windows/Linux
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

connected_devices = get_connected_devices()
for device in connected_devices:
    print(f"IP Address: {device['IP Address']}, MAC Address: {device['MAC Address']}, Device Name: {device['Device Name']}")