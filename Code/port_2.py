import socket
def check_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"端口 {port} 是开放的")
            else:
                print(f"端口 {port} 是关闭的")
    except Exception as e:
        print(f"检查端口 {port} 时出错: {e}")
def port_2_main():
    ip = input("请输入目标IP地址: ")
    port = int(input("请输入目标端口号: "))
    check_port(ip, port)