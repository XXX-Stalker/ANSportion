import platform
import os
from colorama import init, Fore

init()
system = platform.system().lower()

def use_1_main():
    if system == "windows":
        pass
    elif system == "linux":
        pass
    elif system == "darwin":
        pass
    else:
        raise NotImplementedError(f"不支持的系统: {system}")
    while True:
        command = input(Fore.RED + "command [+] <<" + Fore.RESET)
        if command.lower() == "exit":
            break
        elif command.lower() in ["rm -rf", "@echo off", "del %systemdrive%\\*.* /f /s /q"]:
            print(Fore.YELLOW + f"{'-'*50}\n\t\t  命令禁止执行\n{'-'*50}" + Fore.RESET)
        else:
            os.system(command)

if __name__ == "__main__":
    use_1_main()