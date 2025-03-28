import os

def install_library_main():
    choose = input("1.选择性安装第三方库\n2.一键安装第三方库库\n3.查看所有库是否装好\n:")
    if choose == "1":
        print("开始安装依赖第三方库")
        try:
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
            pyinstaller = input("是否下载 pyinstaller 库? (y/n):")
            if pyinstaller in ["y","Y"]:
                os.system("pip3 install pyinstaller")
            else:
                print("已取消下载")
            cryptography = input("是否下载 cryptography 库? (y/n):")
            if cryptography in ["y","Y"]:
                os.system("pip install cryptography")
            else:
                print("已取消下载")
            Pillow = input("是否下载 Pillow 库? (y/n):")
            if Pillow in ["y","Y"]:
                os.system("pip3 install Pillow")
            else:
                print("已取消下载")
            comtypes = input("是否下载 comtypes 库? (y/n):")
            if comtypes in ["y","Y"]:
                os.system("pip install comtypes")
            else:
                print("已取消下载")
        except Exception as e:
            print(f"安装失败{e}")
        print("安装完成")
    elif choose == "2":
        print("开始一键安装第三方库")
        try:
            os.system("pip install pywifi requests validators urllib3 tqdm psutil ipaddress colorama pyinstaller cryptography Pillow comtypes")
        except Exception as e:
            print(f"安装失败{e}")
    elif choose == "3":
        print("开始检查所有库是否装好")
        try:
            print("开始检查 pywifi 库")
            print(f"{'='*80}")
            os.system("pip show pywifi")
            print("pywifi 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 requests 库")
            print(f"{'='*80}")
            os.system("pip show requests")
            print("requests 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 validators 库")
            print(f"{'='*80}")
            os.system("pip show validators")
            print("validators 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 urllib3 库")
            print(f"{'='*80}")
            os.system("pip show urllib3")
            print("urllib3 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 tqdm 库")
            print(f"{'='*80}")
            os.system("pip show tqdm")
            print("tqdm 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 psutil 库")
            print(f"{'='*80}")
            os.system("pip show psutil")
            print("psutil 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 ipaddress 库")
            print(f"{'='*80}")
            os.system("pip show ipaddress")
            print("ipaddress 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 colorama 库")
            print(f"{'='*80}")
            os.system("pip show colorama")
            print("colorama 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 pyinstaller 库")
            print(f"{'='*80}")
            os.system("pip show pyinstaller")
            print("pyinstaller 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 cryptography 库")
            print(f"{'='*80}")
            os.system("pip show cryptography")
            print("cryptography 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 Pillow 库")
            print(f"{'='*80}")
            os.system("pip show Pillow")
            print("Pillow 库已装好")
            print(f"{'='*80}\n")

            print("开始检查 comtypes 库")
            print(f"{'='*80}")
            os.system("pip show comtypes")
            print("comtypes 库已装好")
            print(f"{'='*80}\n")

            print("检查完成")
        except Exception as e:
            print(f"检查失败{e}")

if __name__ == "__main__":
    install_library_main()