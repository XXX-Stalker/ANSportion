#库导入
import os
from colorama import init, Fore

#自定义导入文字
ANSportion1 = """
        _    _   _ ____                   _   _
       / \  | \ | / ___| _ __   ___  _ __| |_(_) ___  _ __  
      / _ \ |  \| \___ \| '_ \ / _ \| '__| __| |/ _ \| '_ \ 
     / ___ \| |\  |___) | |_) | (_) | |  | |_| | (_) | | | |
    /_/   \_\_| \_|____/| .__/ \___/|_|   \__|_|\___/|_| |_|
                        |_|
-----------------------------------------------------------------
                        XXX_Stalker
                    版本 Version: 1.1.0
-----------------------------------------------------------------"""
ANSportion2 = """注意!!!:
需要联网，否则部分功能不能使用!

加入我们吧,我们需要你
Join us, we need you
QQ:991478664

=================================================================
输入 'help' 即可查看帮助
=================================================================
输入 'about' 即可查看关于我们的基本信息
================================================================="""
help = """
================================ help ================================
help     ---   View Help                                          查看帮助
exit     ---   exit the program                                   退出程序
ins l    ---   install the latest version of the program          安装所有第三方依赖库
cls      ---   clear screen                                       清屏
about    ---   About                                              关于我们
log      ---   Check log                                          查看日志
log all  ---   Check all log                                      查看所有日志
open ANS ---   Open ANSportion.py                                 打开一个新的ANSportion
cmd      ---   Open cmd                                           打开cmd
----------------------------------------------------------------------
check    ---   check                                              查看
attack   ---   attack                                             攻击
wifi     ---   Wi-Fi                                              Wi-Fi
listen   ---   listen                                             监听
port     ---   port                                               端口
crawler  ---   crawler                                            爬虫
server   ---   server                                             服务器
======================================================================
"""
about = """
================================ about ================================
团队名:
XXX_Stalker

制作者名单:
YoMon                 前后端

QQ:991478664
下载地址: https://gitcode.com/XXX_Stalker/ANSportion
Bilibili地址: https://space.bilibili.com/3546822658231133?spm_id_from=333.337.0.0
=======================================================================
"""
check_help = """
                            ____ _               _    
                           / ___| |__   ___  ___| | __
                          | |   | '_ \ / _ \/ __| |/ /
                          | |___| | | |  __/ (__|   < 
                           \____|_| |_|\___|\___|_|\_\ 
====================================== check ======================================
1   ---   Check your various IP addresses.                           查看自己的各个IP
2   ---   Check the hardware information of the IP host              查看IP主机的各种硬件信息
3   ---   View IP Geolocation                                        查看IP的地理信息
4   ---   Is the IP a valid IP?                                      IP是否为有效IP
===================================================================================
"""
attack_help = """
                        _   _   _             _    
                       / \ | |_| |_ __ _  ___| | __
                      / _ \| __| __/ _` |/ __| |/ /
                     / ___ \ |_| || (_| | (__|   <
                    /_/   \_\__|\__\__,_|\___|_|\_\ 
================================ attack ================================
1   ---   DDOS attack                    DDOS攻击
========================================================================
"""
wifi_help = """
                         __        ___       _____ ___ 
                         \ \      / (_)     |  ___|_ _|
                          \ \ /\ / /| |_____| |_   | |
                           \ V  V / | |_____|  _|  | |
                            \_/\_/  |_|     |_|   |___|
======================================= wifi =======================================
1   ---   Connect to WiFi                                               连接WiFi
2   ---   WiFi hack                                                     WiFi破解
3   ---   Scan surrounding WiFi                                         扫描周围WiFi
4   ---   Unlimited WiFi connection                                     无限连接WiFi
5   ---   Check the IP address of the current network connection        查看当前网络连接的IP
====================================================================================
"""
listen_help = """
                             _     _     _
                            | |   (_)___| |_ ___ _ __
                            | |   | / __| __/ _ \ '_ \ 
                            | |___| \__ \ ||  __/ | | |
                            |_____|_|___/\__\___|_| |_|
===================================== listen =====================================
1   ---   Monitor the port status of the IP host                 监听IP主机的端口状态
==================================================================================
"""
port_help = """
                                      ____            _   
                                     |  _ \ ___  _ __| |_
                                     | |_) / _ \| '__| __|
                                     |  __/ (_) | |  | |_
                                     |_|   \___/|_|   \__|
============================================= port =============================================
1   ---   Check the open ports of the IP                             扫描IP的指定范围的开放端口
2   ---   Check if the port is open                                  扫描指定端口是否开放
3   ---   Scan the specified range of IP ports for occupancy         扫描IP的指定范围端口是否被占用
================================================================================================
"""
crawler_help = """
                     ____                    _
                    / ___|_ __ __ ___      _| | ___ _ __
                   | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
                   | |___| | | (_| |\ V  V /| |  __/ |
                    \____|_|  \__,_| \_/\_/ |_|\___|_|
================================= crawler =================================
1   ---   Crawling the source code of a website                 爬取网站的源代码
2   ---   Crawling website status                               爬取网站状态
3   ---   Crawling the real IP of the website.                  爬取网站真实IP
===========================================================================
"""
server_help = """
                     ____
                    / ___|  ___ _ ____   _____ _ __
                    \___ \ / _ \ '__\ \ / / _ \ '__|
                     ___) |  __/ |   \ V /  __/ |
                    |____/ \___|_|    \_/ \___|_|
================================= server =================================
1   ---   Create a server (website)                             创建一个服务器(网站)
2   ---   Create a download file server (website)               创建一个下载文件服务器(网站)
==========================================================================
"""

folder = "Code/"

init()
#程序代码函数主体
def program_code_body():
    while True:
        try:
            program_input = input(Fore.MAGENTA + 'ANSportion [+] <<' + Fore.RESET)
            if program_input == "help":#系统指令 提供帮助
                print(help)
            if program_input == "exit":#系统指令 退出程序
                import sys
                sys.exit()
            if program_input == "ins l":#系统指令 安装所有第三方依赖库
                import subprocess
                subprocess.call(f"python {folder}Install-library.py", shell=True)
            if program_input == "cls":#系统指令 清屏
                os.system("cls" if os.name == 'nt' else 'clear')
            if program_input == "about":#系统指令 关于我们
                print(about)
            if program_input in ["command", "cmd"]:#系统指令 使用cmd
                os.system("cls" if os.name == 'nt' else 'clear')
                while True:
                    command = input(Fore.RED + "command [+] <<" + Fore.RESET)
                    if command == "exit":
                        break
                    os.system(command)
            if program_input == "log":#查看更新日志
                if os.path.exists("更新日志1.txt"):
                    with open("更新日志1.txt", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print("==================================================================\n更新日志内容:")
                    print(log_content,"\n==================================================================")
                else:
                    print("更新日志文件不存在。")
            if program_input == "log all":#查看所有的更新日志
                if os.path.exists("更新日志2.txt"):
                    with open("更新日志2.txt", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print("==================================================================\n更新日志内容:")
                    print(log_content,"\n==================================================================")
                else:
                    print("更新日志文件不存在。")
            if program_input in ["open ANS", "open ans"]:
                import subprocess
                subprocess.call(f"python {folder}ANSportion.py")

            if program_input == "check":#工具包指令 使用工具包
                print(check_help)
                program_check = input(":")
                if program_check == "1":#工具包指令 查看自己的各个IP
                    import subprocess
                    subprocess.call(f"python {folder}check-1.py", shell=True)
                if program_check == "2":#工具包指令 查看IP主机的各种硬件信息
                    import subprocess
                    subprocess.call(f"python {folder}check-2.py", shell=True)
                if program_check == "3":#工具包指令 查看IP的地理信息
                    import subprocess
                    subprocess.call(f"python {folder}check-3.py", shell=True)
                if program_check == "4":#工具包指令 IP是否为有效IP
                    import subprocess
                    subprocess.call(f"python {folder}check-4.py", shell=True)

            if program_input == "attack":
                print(attack_help)
                program_attack = input(":")
                if program_attack == "1":#工具包指令 DDOS攻击
                    import subprocess
                    subprocess.call(f"python {folder}attack-1.py", shell=True)

            if program_input == "wifi":
                print(wifi_help)
                program_wifi = input(":")
                if program_wifi == "1":#工具包指令 连接Wi-Fi
                    import subprocess
                    subprocess.call(f"python {folder}wifi-1.py", shell=True)
                if program_wifi == "2":#工具包指令 WiFi破解
                    import subprocess
                    subprocess.call(f"python {folder}wifi-2.py", shell=True)
                if program_wifi == "3":#工具包指令 扫描周围WiFi
                    import subprocess
                    subprocess.call(f"python {folder}wifi-3.py", shell=True)
                if program_wifi == "4":#工具包指令 无限连接Wi-Fi
                    import subprocess
                    subprocess.call(f"python {folder}wifi-4.py", shell=True)
                if program_wifi == "5":#工具包指令 查看当前网络连接的IP
                    import subprocess
                    subprocess.call(f"python {folder}wifi-5.py", shell=True)

            if program_input == "listen":
                print(listen_help)
                program_listen = input(":")
                if program_listen == "1":#工具包指令 监听IP主机的端口状态
                    import subprocess
                    subprocess.call(f"python {folder}listen-1.py", shell=True)
            
            if program_input == "port":
                print(port_help)
                program_port = input(":")
                if program_port == "1":#工具包指令 查看IP开放端口
                    import subprocess
                    subprocess.call(f"python {folder}port-1.py", shell=True)
                if program_port == "2":#工具包指令 查看端口是否开放工具包指令
                    import subprocess
                    subprocess.call(f"python {folder}port-2.py", shell=True)
                if program_port == "3":#工具包指令 查看IP开放端口是否被占用
                    import subprocess
                    subprocess.call(f"python {folder}port-3.py", shell=True)
            
            if program_input == "crawler":
                print(crawler_help)
                program_crawler = input(":")
                if program_crawler == "1":#工具包指令 爬取网站的源代码
                    import subprocess
                    subprocess.call(f"python {folder}crawler-1.py", shell=True)
                if program_crawler == "2":#工具包指令 查看网站状态
                    import subprocess
                    subprocess.call(f"python {folder}crawler-2.py", shell=True)
                if program_crawler == "3":#工具包指令 查看网站真实IP
                    import subprocess
                    subprocess.call(f"python {folder}crawler-3.py", shell=True)
            
            if program_input == "server":
                print(server_help)
                program_server = input(":")
                if program_server == "1":#工具包指令 创建一个服务器(网站)
                    import subprocess
                    subprocess.call(f"python {folder}server-1.py")
                if program_server == "2":#工具包指令 创建一个下载文件服务器(网站)
                    import subprocess
                    subprocess.call(f"python {folder}server-2.py")

        except KeyboardInterrupt:
            import sys
            os.system('cls')
            print("用户手动终止程序")
            sys.exit()
        except Exception as e:
            print(f"发生错误:\n{e}")

if __name__ == "__main__":
    os.system("cls")
    print("<ANSportion> 正在运行...")
    os.system("cls")
    print("正在检查当前系统")
    import platform
    system = platform.system()
    os.system("cls")
    print(f"当前系统为: {system}")
    if system == "Windows":
        os.system("cls")
        print(Fore.YELLOW + ANSportion1 + Fore.RESET)   
        if os.path.exists("更新日志1.txt"):
            with open("更新日志1.txt", 'r', encoding='utf-8') as file:
                log_content = file.read()
            print(Fore.CYAN + "更新日志1:\n==================================================================\n更新日志内容:" + Fore.RESET)
            print(Fore.CYAN + log_content,"\n==================================================================" + Fore.RESET)
        else:
            print("更新日志文件不存在。")
        print(ANSportion2)
        program_code_body()
    else:
        print("请使用Windows系统运行此程序，否则部分功能不支持")
        os.system("clear")
        print(Fore.YELLOW + ANSportion1 + Fore.RESET)   
        if os.path.exists("更新日志1.txt"):
            with open("更新日志1.txt", 'r', encoding='utf-8') as file:
                log_content = file.read()
            print(Fore.CYAN + "更新日志1:\n==================================================================\n更新日志内容:" + Fore.RESET)
            print(Fore.CYAN + log_content,"\n==================================================================" + Fore.RESET)
        else:
            print("更新日志文件不存在。")
        print(ANSportion2)
        program_code_body()
