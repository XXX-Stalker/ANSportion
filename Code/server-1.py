import http.server
import socketserver
import socket
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
local_ip = get_local_ip()
IP = local_ip
def program():
    while True:
        PORT = input("请输入端口号：")
        try:
            PORT = int(PORT)
            break
        except ValueError:
            print("端口号必须是整数，请重新输入。")
    HTML_file = input("请输入存放HTML代码文件名：")
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # 打印客户端IP地址
            client_ip = self.client_address[0]
            print(f"客户端IP: {client_ip}")
            # 读取HTML文件内容
            try:
                with open(HTML_file, 'rb') as file:  # 使用'rb'模式以二进制方式读取文件
                    html_content = file.read()
            except FileNotFoundError:
                html_content = b"<html><body><h1>The server needs to continue debugging</h1></body></html>"  # 使用字节串
            # 发送HTTP响应
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content)  # 直接写入字节串
    # 创建TCP服务器实例
    with socketserver.TCPServer((IP, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"服务器地址 (http://{IP}:{PORT}) \n服务器已启动!!!")
        httpd.serve_forever()
if __name__ == "__main__":
    program()
