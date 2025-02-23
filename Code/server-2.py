import http.server
import socketserver
import socket
import os

# 获取本地 IP 地址
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

local_ip = get_local_ip()
IP = local_ip

# 要下载的文件位于项目目录下的 code 文件夹中
DOWNLOAD_FOLDER = input("文件路径:")
FILE_NAME = input("文件名:")
port_input = input("请输入端口号:")
HTML_input = input("请输入存放HTML代码文件名:")

try:
    with open(HTML_input, 'rb') as file:
        html_content = file.read()
except FileNotFoundError:
    print(f"未找到 {HTML_input} 文件，请检查文件名和路径。")
    html_content = b"<html><body><h1>HTML file not found</h1></body></html>"

# 验证输入的端口号
def validate_port(port):
    try:
        port = int(port_input)
        if 1 <= port <= 65535:
            return port
        else:
            print("端口号必须在 1 到 65535 之间。")
            return None
    except ValueError:
        print("端口号必须是整数。")
        return None

# 防护路径遍历攻击
def is_safe_path(path):
    safe_base = os.path.abspath(DOWNLOAD_FOLDER)
    requested_path = os.path.abspath(os.path.join(DOWNLOAD_FOLDER, path))
    return requested_path.startswith(safe_base)

class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 打印客户端IP地址
        client_ip = self.client_address[0]
        print(f"客户端IP: {client_ip}")

        if self.path == '/':
            # 处理根路径请求，返回 HTML 页面
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content)
        elif self.path == '/download':
            # 处理下载请求，发送文件给用户
            if is_safe_path(FILE_NAME):
                try:
                    with open(os.path.join(DOWNLOAD_FOLDER, FILE_NAME), 'rb') as file:
                        self.send_response(200)
                        self.send_header("Content-type", "application/octet-stream")
                        self.send_header("Content-Disposition", f"attachment; filename={FILE_NAME}")
                        self.end_headers()
                        self.wfile.write(file.read())
                except FileNotFoundError:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"File not found.")
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Forbidden.")
        else:
            # 默认返回404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

def program():
    port = None
    while port is None:
        port = validate_port(port_input)

    # 创建TCP服务器实例
    with socketserver.TCPServer((IP, port), CustomHTTPRequestHandler) as httpd:
        print(f"服务器地址 (http://{IP}:{port}) \n服务器已启动!!!")
        httpd.serve_forever()

if __name__ == "__main__":
    program()
