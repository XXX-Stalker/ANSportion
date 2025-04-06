import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import signal

# 添加一个全局变量来控制扫描的停止
stop_scan = False

def signal_handler(sig, frame):
    global stop_scan
    print("\n用户手动终止扫描。")
    stop_scan = True

def is_port_open(ip, port):
    try:
        if stop_scan:
            return None
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None  # 捕获异常并返回 None，避免影响主线程

def scan_ports(ip, start_port, end_port, max_workers):
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(is_port_open, ip, port): port for port in range(start_port, end_port + 1)}
        for future in tqdm(as_completed(future_to_port), total=end_port - start_port + 1, desc="扫描进度", ncols=100):
            if stop_scan:
                break
            port = future_to_port[future]
            open_port = future.result()
            if open_port:
                open_ports.append(open_port)
    return open_ports

def port_1_main():
    global stop_scan
    signal.signal(signal.SIGINT, signal_handler)  # 注册信号处理函数
    ip = input("请输入要扫描的IP地址: ")
    try:
        print("端口范围: 1-65535")
        start_port = int(input("请输入起始端口: "))
        end_port = int(input("请输入结束端口: "))
        if start_port > end_port or start_port < 1 or end_port > 65535:
            raise ValueError("端口范围无效。")
        print("线程数量: 1-1000")
        max_workers = int(input("请输入线程数量: "))
        if max_workers < 1:
            raise ValueError("线程数量必须大于0")
        if max_workers > 1000:
            raise ValueError("线程数量必须小于1 000")
    except ValueError as e:
        print(f"输入错误: {e}")
        return

    print(f"扫描 {ip} 的端口 {start_port} 到 {end_port} ...")
    open_ports = scan_ports(ip, start_port, end_port, max_workers)
    if open_ports:
        print(f"开放的端口: {', '.join(map(str, open_ports))}")
    else:
        print("没有找到开放的端口。")