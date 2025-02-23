import socket
import threading
import tkinter as tk
from tkinter import ttk
import signal
import time
import sys
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
def monitor_host_ports(host, ports):
    results = []
    for port in ports:
        open_status = check_port(host, port)
        results.append((port, open_status))
    return results
def monitor_multiple_hosts_ports(hosts, ports):
    all_results = []
    for host in hosts:
        host_results = monitor_host_ports(host, ports)
        all_results.extend([(host, port, status) for port, status in host_results])
    return all_results
def update_gui(results):
    for row in treeview.get_children():
        treeview.delete(row)
    for result in results:
        if len(result) == 2:
            host, (port, status) = result
            treeview.insert("", "end", values=(host, port, status))
        elif len(result) == 3:
            host, port, status = result
            treeview.insert("", "end", values=(host, port, status))
def continuous_monitoring():
    global running
    while running:
        start_time = time.time()
        results = monitor_multiple_hosts_ports(hosts, ports)
        update_gui(results)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)
def handle_ctrl_c(signal, frame):
    print("接收到Ctrl+C，正在退出程序...")
    global running
    running = False
    global monitor_thread
    if monitor_thread.is_alive():
        monitor_thread.join(timeout=3)
        if monitor_thread.is_alive():
            print("监听线程未能及时停止，强制退出...")
            sys.exit(1)
    root.destroy()
    print("程序已成功退出。")
root = tk.Tk()
root.title("网络端口监听")
root.configure(bg='#333333')
treeview = ttk.Treeview(root, columns=("主机", "端口", "状态"), show="headings")
treeview.heading("主机", text="主机")
treeview.heading("端口", text="端口")
treeview.heading("状态", text="状态")
treeview.pack()
hosts_input = input("请输入要监听的主机，多个主机用逗号分隔: ")
hosts = [host.strip() for host in hosts_input.split(',')]
ports_input = input("请输入要监听的端口，多个端口用逗号分隔: ")
ports = [int(port.strip()) for port in ports_input.split(',')]
running = True
monitor_thread = threading.Thread(target=continuous_monitoring)
monitor_thread.start()
signal.signal(signal.SIGINT, handle_ctrl_c)
root.mainloop()
