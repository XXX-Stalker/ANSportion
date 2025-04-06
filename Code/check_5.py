import platform
import os

def check_5_main():
    system = platform.system().lower()
    if system == "windows":
        command = "netsh interface ip show interfaces"
        os.system(command)
    elif system == "linux":
        command = "ip -o link"
        os.system(command)
    elif system == "darwin":
        command = "ifconfig -a"
        os.system(command)
    else:
        raise NotImplementedError(f"Unsupported platform: {system}")