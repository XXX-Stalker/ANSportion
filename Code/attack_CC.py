import os
import sys

#所有初始化
with open("CC\\CC_version.txt", "r") as f:
    version = f.read()
    

title = f"""
 _____  _____    ___ _____ _____ ___  _____  _   __
/  __ \/  __ \  / _ \_   _|_   _/ _ \/  __ \| | / /
| /  \/| /  \/ / /_\ \| |   | |/ /_\ \ /  \/| |/ / 
| |    | |     |  _  || |   | ||  _  | |    |    \ 
| \__/\| \__/\ | | | || |   | || | | | \__/\| |\  \ 
 \____/ \____/ \_| |_/\_/   \_/\_| |_/\____/\_| \_/

XXX_Stalker
当前版本: {version}
输入 'help' 查看帮助
{"=" * 52}"""

help = """
[帮助信息]
cls, clear --- 清屏
exit --- 退出程序

[攻击方式选择]
[1] --- cc
[2] --- 线程(thread cc)
"""

def attack_cc_main():
    os.system("cls" if os.name == 'nt' else "clear")
    print("[安全警告]")
    print("-" * 40)
    print("1. 请确保您有目标网站的访问授权")
    print("2. 高频cc可能导致IP被封禁")
    print("3. 按 Ctrl+C 停止攻击")
    print("-" * 40)
    print("\n[重要法律声明]")
    print("=" * 50)
    print("根据 - 中华人民共和国刑法 - 第285、286条规定:")
    print("- 未经授权对计算机系统实施攻击可处5年以下有期徒刑")
    print("- 造成严重后果者可处5年以上有期徒刑")
    print("=" * 50)
    confirm = input("\n您确认已获得合法授权且了解法律风险吗？(y/n): ")
    if confirm in ['y', 'yes']:
        os.system("cls" if os.name == 'nt' else "clear")
        print(title)
        while True:
            while_input = input("CC ATTACK <<")
            if while_input == "help":
                print(help)
            elif while_input in ["cls", "clear"]:
                os.system("cls" if os.name == 'nt' else "clear")
            elif while_input == "exit":
                print("已退出")
                break
            elif while_input == "1":
                from CC.cc import cc_main
                cc_main()
            elif while_input == "2":
                from CC.thread_cc import thread_cc_main
                thread_cc_main()
    elif confirm in ['n', 'no']:
        print("已拒绝")
        sys.exit()