import socket
import threading
from tqdm import tqdm

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex((ip, port)) == 0

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with tqdm(total=end_port - start_port + 1, desc="Scanning ports") as pbar:
        def worker(port):
            if check_port(ip, port):
                open_ports.append(port)
            pbar.update(1)

        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=worker, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    return open_ports

def main():
    ip = input("请输入要扫描的IP地址: ")
    start_port = int(input("请输入起始端口号: "))
    end_port = int(input("请输入结束端口号: "))

    open_ports = scan_ports(ip, start_port, end_port)
    if open_ports:
        print(f"以下端口被占用: {open_ports}")
    else:
        print("没有发现被占用的端口。")

if __name__ == "__main__":
    main()
