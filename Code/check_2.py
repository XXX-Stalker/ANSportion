import requests

def get_ip_geolocation(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        geolocation_info = {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),
            "Timezone": data.get("timezone"),
            "ISP": data.get("org")
        }
        return geolocation_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation data: {e}")
        return None

def check_2_main():
    ip_address = input("请输入要查询的IP地址:")
    geolocation = get_ip_geolocation(ip_address)
    if geolocation:
        print("IP地理位置信息:")
        for key, value in geolocation.items():
            print(f"{key}: {value}")
    else:
        print("无法获取IP的地理位置信息")