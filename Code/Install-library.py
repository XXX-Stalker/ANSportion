import os
print("开始安装依赖第三方库")
pywifi = input("是否下载 pywifi 库? (y/n):")
if pywifi in ["y","Y"]:
    os.system("pip install pywifi")
else:
    print("已取消下载")
requests = input("是否下载 requests 库? (y/n):")
if requests in ["y","Y"]:
    os.system("pip install requests")
else:
    print("已取消下载")
socket = input("是否下载 socket 库? (y/n):")
if socket in ["y","Y"]:
    os.system("pip install socket")
else:
    print("已取消下载")
signal = input("是否下载 signal 库? (y/n):")
if signal in ["y","Y"]:
    os.system("pip install signal")
else:
    print("已取消下载")
subprocess = input("是否下载 subprocess 库? (y/n):")
if subprocess in ["y","Y"]:
    os.system("pip install subprocess")
else:
    print("已取消下载")
validators = input("是否下载 validators 库? (y/n):")
if validators in ["y","Y"]:
    os.system("pip install validators")
else:
    print("已取消下载")
urllib3 = input("是否下载 urllib3 库? (y/n):")
if urllib3 in ["y","Y"]:
    os.system("pip install urllib3")
else:
    print("已取消下载")
tqdm = input("是否下载 tqdm 库? (y/n):")
if tqdm in ["y","Y"]:
    os.system("pip install tqdm")
else:
    print("已取消下载")
psutil = input("是否下载 psutil 库? (y/n):")
if psutil in ["y","Y"]:
    os.system("pip install psutil")
else:
    print("已取消下载")
ipaddress = input("是否下载 ipaddress 库? (y/n):")
if ipaddress in ["y","Y"]:
    os.system("pip install ipaddress")
else:
    print("已取消下载")
colorama = input("是否下载 colorama 库? (y/n):")
if colorama in ["y","Y"]:
    os.system("pip install colorama")
else:
    print("已取消下载")
print("安装完成")
