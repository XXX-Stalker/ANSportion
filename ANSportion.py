#库导入
import os
from colorama import init, Fore
import sys
import time
import platform
import subprocess

#自定义导入文字
ANSportion1_0 = """    _    _   _ ____                   _   _               ____"""

ANSportion1_1 = """   / \  | \ | / ___| _ __   ___  _ __| |_(_) ___  _ __   |  _ \ _ __ ___  """

ANSportion1_2 = """  / _ \ |  \| \___ \| '_ \ / _ \| '__| __| |/ _ \| '_ \  | |_) | '__/ _ \ """

ANSportion1_3 = """ / ___ \| |\  |___) | |_) | (_) | |  | |_| | (_) | | | | |  __/| | | (_) |"""

ANSportion1_4 = """/_/   \_\_| \_|____/| .__/ \___/|_|   \__|_|\___/|_| |_| |_|   |_|  \___/ """

ANSportion1_5 = """                    |_|"""

ANSportion2 = """
----------------------------------------------------------------------------
                                XXX_Stalker
                         版本 Version: 1.1.6 - pro
----------------------------------------------------------------------------
切记不可用于任何非法用途！！!
"""

ANSportion3 = """注意!!!:
需要联网，否则部分功能不能使用!

粉丝群: QQ:991478664

=================================================================
输入 'help' 即可查看帮助
=================================================================
输入 'about' 即可查看关于我们的基本信息
================================================================="""

help = """
                       _   _ _____ _     ____  
                      | | | | ____| |   |  _ \ 
                      | |_| |  _| | |   | |_) |
                      |  _  | |___| |___|  __/ 
                      |_| |_|_____|_____|_|    
================================ help ================================
help     ---   View Help                                          查看帮助
exit     ---   exit the program                                   退出程序
cls      ---   clear screen                                       清屏
about    ---   About                                              关于我们
log      ---   Check log                                          查看日志
log all  ---   Check all log                                      查看所有日志
open p   ---   Open end point                                     打开终端
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
YoMon                 前端/后端
GHO高泽林GAO          测试

QQ:991478664
GitCode: https://gitcode.com/XXX_Stalker/ANSportion
GitHub: https://github.com/XXX-Stalker/ANSportion
=======================================================================
"""

check_help = """
                            ____ _               _    
                           / ___| |__   ___  ___| | __
                          | |   | '_ \ / _ \/ __| |/ /
                          | |___| | | |  __/ (__|   < 
                           \____|_| |_|\___|\___|_|\_\ 
====================================== check ======================================
1   ---   Check your various IP addresses                           查看自己的各个IP
2   ---   View IP Geolocation                                       查看IP的地理信息
3   ---   Check if the IP is a valid IP                             查看IP是否为有效IP
4   ---   Crawling the real IP of the website                       查看网站真实IP
5   ---   Check the Mac address of the IP                           查看IP的Mac地址
6   ---   View network interface information                        查看网络接口信息
===================================================================================
"""

attack_help = """
                        _   _   _             _    
                       / \ | |_| |_ __ _  ___| | __
                      / _ \| __| __/ _` |/ __| |/ /
                     / ___ \ |_| || (_| | (__|   <
                    /_/   \_\__|\__\__,_|\___|_|\_\ 
================================ attack ================================
1   ---   DDOS attack                                  DDOS攻击
2   ---   DDOS attack                                  DDOS代理攻击
3   ---   SMS bombardment                              短信轰炸
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
====================================== listen ======================================
1   ---   Monitor the port status of the IP host                 监听IP主机的端口状态
====================================================================================
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
================================================================================================
"""

crawler_help = """
                       ____                    _
                      / ___|_ __ __ ___      _| | ___ _ __
                     | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
                     | |___| | | (_| |\ V  V /| |  __/ |
                      \____|_|  \__,_| \_/\_/ |_|\___|_|
=================================== crawler ===================================
1   ---   Crawling the source code of a website                 爬取网站的源代码
2   ---   Crawling website status                               爬取网站状态
===============================================================================
"""

server_help = """
                              ____
                             / ___|  ___ _ ____   _____ _ __
                             \___ \ / _ \ '__\ \ / / _ \ '__|
                              ___) |  __/ |   \ V /  __/ |
                             |____/ \___|_|    \_/ \___|_|
========================================== server ==========================================
1   ---   Create a server (website)                             创建一个服务器(网站)
2   ---   Create a download file server (website)               创建一个下载文件服务器(网站)
============================================================================================
"""

#所有初始化
system = platform.system()
init()
ANSportion_print_time_1 = 0.2
# 获取当前工作目录的绝对路径
current_file_path = os.path.abspath(__file__)

#程序代码函数主体
def program_code_body():
    while True:
        try:
            program_input = input(Fore.MAGENTA + f'ANSportion-PRO [+ {system} +] <<' + Fore.RESET)
            if program_input == "help":#系统指令 提供帮助
                print(help)
            elif program_input == "exit":#系统指令 退出程序
                sys.exit()
            elif program_input == "cls":#系统指令 清屏
                os.system("cls" if os.name == 'nt' else 'clear')
            elif program_input == "about":#系统指令 关于我们
                print(about)
            elif program_input == "open p":#系统指令 调用系统对应终端
                from Code.use_1 import use_1_main
                use_1_main()
            elif program_input == "log":#查看更新日志
                if os.path.exists("更新日志1.ans"):
                    with open("更新日志1.ans", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print(f"{'=' * 65}\n更新日志内容:")
                    print(log_content,f"\n{'=' * 65}")
                else:
                    print("更新日志文件不存在。")
            elif program_input == "log all":#查看所有的更新日志
                if os.path.exists("更新日志2.ans"):
                    with open("更新日志2.ans", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print(f"{'=' * 65}\n更新日志内容:")
                    print(log_content, f"\n{'=' * 65}")
                else:
                    print("更新日志文件不存在。")
            elif program_input == "check l":#查看指定的库是否安装
                check_l = input("请输入要检查的库名:")
                import importlib.util
                def is_library_installed(library_name):
                    spec = importlib.util.find_spec(library_name)
                    return spec is not None
                library_name = check_l
                if is_library_installed(library_name):
                    print(f"{library_name} 已安装")
                else:
                    print(f"{library_name} 未安装")

            elif program_input == "check":#工具包指令 使用工具包
                print(check_help)
                program_check = input(":")
                if program_check == "1":#工具包指令 查看自己的各个IP
                    from Code.check_1 import check_1_main
                    check_1_main()
                elif program_check == "2":#工具包指令 查看IP的地理信息
                    from Code.check_2 import check_2_main
                    check_2_main()
                elif program_check == "3":#工具包指令 查看IP是否为有效IP
                    from Code.check_3 import check_3_main
                    check_3_main()
                elif program_check == "4":#工具包指令 查看网站真实IP
                    from Code.check_4 import check_4_main
                    check_4_main()
                elif program_check == "5":#工具包指令 查看IP的Mac地址
                    from Code.check_5 import check_5_main
                    check_5_main()
                elif program_check == "6":#工具包指令 查看网络接口信息
                    from Code.check_6 import check_6_main
                    check_6_main()

            elif program_input == "attack":
                print(attack_help)
                program_attack = input(":")
                if program_attack == "1":#工具包指令 DDOS攻击
                    from Code.attack_1 import attack_1_main
                    attack_1_main()
                elif program_attack == "2":#工具包指令 DDOS代理攻击
                    from Code.attack_2 import attack_2_main
                    attack_2_main()
                elif program_attack == "3":#工具包指令 短信轰炸
                    from Code.attack_3 import attack_3_main
                    attack_3_main()

            elif program_input == "wifi":
                print(wifi_help)
                program_wifi = input(":")
                if program_wifi == "1":#工具包指令 连接Wi-Fi
                    from Code.wifi_1 import wifi_1_main
                    wifi_1_main()
                elif program_wifi == "2":#工具包指令 WiFi破解
                    from Code.wifi_2 import wifi_2_main
                    wifi_2_main()
                elif program_wifi == "3":#工具包指令 扫描周围WiFi
                    from Code.wifi_3 import wifi_3_main
                    wifi_3_main()
                elif program_wifi == "4":#工具包指令 无限连接Wi-Fi
                    from Code.wifi_4 import wifi_4_main
                    wifi_4_main()
                elif program_wifi == "5":#工具包指令 查看当前网络连接的IP
                    from Code.wifi_5 import wifi_5_main
                    wifi_5_main()

            elif program_input == "listen":
                print(listen_help)
                program_listen = input(":")
                if program_listen == "1":#工具包指令 监听IP主机的端口状态
                    from Code.listen_1 import listen_1_main
                    listen_1_main()
            
            elif program_input == "port":
                print(port_help)
                program_port = input(":")
                if program_port == "1":#工具包指令 查看IP开放端口
                    from Code.port_1 import port_1_main
                    port_1_main()
                elif program_port == "2":#工具包指令 查看端口是否开放工具包指令
                    from Code.port_2 import port_2_main
                    port_2_main()
            
            elif program_input == "crawler":
                print(crawler_help)
                program_crawler = input(":")
                if program_crawler == "1":#工具包指令 爬取网站的源代码
                    from Code.crawler_1 import crawler_1_main
                    crawler_1_main()
                elif program_crawler == "2":#工具包指令 爬取网站状态
                    from Code.crawler_2 import crawler_2_main
                    crawler_2_main()
            
            elif program_input == "server":
                print(server_help)
                program_server = input(":")
                if program_server == "1":#工具包指令 创建一个服务器(网站)
                    from Code.server_1 import server_1_main
                    server_1_main()
                elif program_server == "2":#工具包指令 创建一个下载文件服务器(网站)
                    from Code.server_2 import server_2_main
                    server_2_main()

        except Exception as e:
            print(f"发生错误:\n{e}")

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else 'clear')
    print("<ANSportion> 正在运行...")
    os.system("cls" if os.name == 'nt' else 'clear')
    print("正在检查当前系统")
    os.system("cls" if os.name == 'nt' else 'clear')
    print(f"当前系统为: {system}")
    os.system("cls" if os.name == 'nt' else 'clear')
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_0 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_1 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_2 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_3 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_4 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion1_5 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.YELLOW + ANSportion2 + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    print(Fore.CYAN + f"当前工作目录所在的绝对路径: {current_file_path}" + Fore.RESET)
    time.sleep(ANSportion_print_time_1)
    if os.path.exists("更新日志1.ans"):
        with open("更新日志1.ans", 'r', encoding='utf-8') as file:
            log_content = file.read()
        print(Fore.CYAN + f"更新日志1:\n{'=' * 65}\n更新日志内容:" + Fore.RESET)
        print(Fore.CYAN + log_content,f"\n{'=' * 65}" + Fore.RESET)
    else:
        print("更新日志文件不存在。")
    print(ANSportion3)
    program_code_body()
