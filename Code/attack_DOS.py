import os
import sys

#所有初始化
version = "1.0.0"

title = f'''
M""""""'YMM MMP"""""YMM MP""""""`MM MMP"""""""MM M""""""""M M""""""""M MMP"""""""MM MM'""""'YMM M""MMMMM""M
M  mmmm. `M M' .mmm. `M M  mmmmm..M M' .mmmm  MM Mmmm  mmmM Mmmm  mmmM M' .mmmm  MM M' .mmm. `M M  MMMM' .M
M  MMMMM  M M  MMMMM  M M.      `YM M         `M MMMM  MMMM MMMM  MMMM M         `M M  MMMMMooM M       .MM
M  MMMMM  M M  MMMMM  M MMMMMMM.  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M  MMMMMMMM M  MMMb. YM
M  MMMM' .M M. `MMM' .M M. .MMM'  M M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM M. `MMM' .M M  MMMMb  M
M       .MM MMb     dMM Mb.     .dM M  MMMMM  MM MMMM  MMMM MMMM  MMMM M  MMMMM  MM MM.     .dM M  MMMMM  M
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMM MMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM

XXX_Stalker
当前版本: {version}
输入 'help' 查看帮助
{"=" * 107}'''

help = """
[帮助信息]
cls, clear --- 清屏
exit --- 退出程序

[攻击方式选择]
[1] --- 线程(thread dos)
[2] --- 多包(Multi-Packet dos)
[3] --- 代理(Agent dos)
"""

def attack_dos_main():
    os.system("cls" if os.name == 'nt' else "clear")
    print("[安全警告]")
    print("-" * 40)
    print("1. 请确保您有目标网站的访问授权")
    print("2. 高频dos可能导致IP被封禁")
    print("3. 按 Ctrl+C 停止攻击")
    print("4. 请使用 IPV4 地址, 否则其他 IP 不支持")
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
            while_input = input("DOS ATTACK <<")
            if while_input == "help":
                print(help)
            elif while_input in ["cls", "clear"]:
                os.system("cls" if os.name == 'nt' else "clear")
            elif while_input == "exit":
                print("已退出")
                break
            elif while_input == "1":
                from DOS.thread_dos import DOS_thread_dos_main
                DOS_thread_dos_main()
            elif while_input == "2":
                from DOS.Multi_Packet_dos import Multi_Packet_dos_main
                Multi_Packet_dos_main()
            elif while_input == "3":
                from DOS.Agent_dos import Agent_dos_main
                Agent_dos_main()
    else:
        print("已拒绝")
        os.system("cls" if os.name == 'nt' else "clear")
        sys.exit()
