import socket
def get_website_ip(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None
if __name__ == '__main__':
    print("注意: 输入的时候仅需输入后面的域名\n例如: www.XXX.com")
    website_url = input("请输入网站域名:")
    website_ip = get_website_ip(website_url)
    if website_ip:
        print(f"{website_url} 的真实IP地址是：{website_ip}")
    else:
        print("无法获取网站的真实IP地址")
