import socket
import threading
import time
import sys
import os

# 检测操作系统
is_windows = os.name == "nt"
is_linux = os.name == "posix" and sys.platform.startswith("linux")
is_macos = os.name == "posix" and sys.platform.startswith("darwin")

# 定义全局变量
running = False
monitor_thread = None

# 检查单个端口是否开放
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        return False
    except Exception:
        return False
    finally:
        sock.close()

# 监控单个主机的多个端口
def monitor_host_ports(host, ports):
    results = []
    for port in ports:
        open_status = check_port(host, port)
        results.append((port, open_status))
    return results

# 监控多个主机的多个端口
def monitor_multiple_hosts_ports(hosts, ports):
    all_results = []
    for host in hosts:
        host_results = monitor_host_ports(host, ports)
        all_results.extend([(host, port, status) for port, status in host_results])
    return all_results

# 在终端中实时显示结果
def display_results(results):
    # 清除终端内容
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

    # 打印结果
    print(f"{'主机':<15} {'端口':<5} {'状态':<8}")
    print("-" * 30)
    for host, port, status in results:
        status_text = "开放" if status else "关闭"
        print(f"{host:<15} {port:<5} {status_text:<8}")

# 持续监控线程
def continuous_monitoring(hosts, ports):
    global running
    while running:
        start_time = time.time()
        results = monitor_multiple_hosts_ports(hosts, ports)
        display_results(results)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)

# 处理Ctrl+C退出
def handle_ctrl_c(signal, frame):
    global running
    print("\n接收到Ctrl+C，正在退出程序...")
    running = False  # 设置全局变量，通知线程停止运行

    # 等待线程结束
    if monitor_thread is not None and monitor_thread.is_alive():
        monitor_thread.join(timeout=5)  # 设置超时时间，避免阻塞
        if monitor_thread.is_alive():
            print("监听线程未能及时停止，强制退出...")
            sys.exit(1)  # 强制退出程序
    print("程序已成功退出")

# 主函数，用于启动程序
def listen_1_main():
    global running
    global monitor_thread
    running = True

    # 如果没有提供输入，则通过用户输入获取
    hosts_input = input("请输入要监听的主机，多个主机用逗号分隔: ")
    ports_input = input("请输入要监听的端口，多个端口用逗号分隔: ")

    # 解析主机和端口
    hosts = [host.strip() for host in hosts_input.split(',')]
    ports = [int(port.strip()) for port in ports_input.split(',')]

    # 启动监控线程
    monitor_thread = threading.Thread(target=continuous_monitoring, args=(hosts, ports))
    monitor_thread.start()

    # 注册信号处理函数
    import signal
    signal.signal(signal.SIGINT, handle_ctrl_c)

    # 阻塞主线程，直到用户中断
    try:
        while running:
            time.sleep(1)  # 主线程保持运行，等待线程结束
    except KeyboardInterrupt:
        handle_ctrl_c(None, None)  # 捕获主线程的 KeyboardInterrupt