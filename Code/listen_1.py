import socket
import threading
import tkinter as tk
from tkinter import ttk
import signal
import time
import sys

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

# 更新GUI显示
def update_gui(treeview, results):
    for row in treeview.get_children():
        treeview.delete(row)
    for result in results:
        if len(result) == 2:
            host, (port, status) = result
            treeview.insert("", "end", values=(host, port, status))
        elif len(result) == 3:
            host, port, status = result
            treeview.insert("", "end", values=(host, port, status))

# 持续监控线程
def continuous_monitoring(hosts, ports, treeview):
    global running
    while running:
        start_time = time.time()
        results = monitor_multiple_hosts_ports(hosts, ports)
        update_gui(treeview, results)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)

# 处理Ctrl+C退出
def handle_ctrl_c(signal, frame):
    print("接收到Ctrl+C，正在退出程序...")
    global running
    running = False
    global monitor_thread
    if monitor_thread.is_alive():
        monitor_thread.join(timeout=3)
        if monitor_thread.is_alive():
            print("监听线程未能及时停止，强制退出...")
            from tkinter import root
            root.destroy()
            sys.exit()
    print("程序已成功退出")

# 主函数，用于启动程序
def listen_1_main(hosts_input=None, ports_input=None):
    global running
    global monitor_thread
    running = True

    # 如果没有提供输入，则通过用户输入获取
    if hosts_input is None:
        hosts_input = input("请输入要监听的主机，多个主机用逗号分隔: ")
    if ports_input is None:
        ports_input = input("请输入要监听的端口，多个端口用逗号分隔: ")

    # 解析主机和端口
    hosts = [host.strip() for host in hosts_input.split(',')]
    ports = [int(port.strip()) for port in ports_input.split(',')]

    # 初始化GUI
    root = tk.Tk()
    root.title("网络端口监听")
    root.configure(bg='#333333')
    treeview = ttk.Treeview(root, columns=("主机", "端口", "状态"), show="headings")
    treeview.heading("主机", text="主机")
    treeview.heading("端口", text="端口")
    treeview.heading("状态", text="状态")
    treeview.pack()

    # 启动监控线程
    monitor_thread = threading.Thread(target=continuous_monitoring, args=(hosts, ports, treeview))
    monitor_thread.start()

    # 注册信号处理函数
    signal.signal(signal.SIGINT, handle_ctrl_c)

    # 启动GUI主循环
    try:
        root.mainloop()
    except KeyboardInterrupt:
        handle_ctrl_c(None, None)