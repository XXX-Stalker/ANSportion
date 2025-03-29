from PyInstaller.__main__ import run
def package_with_pyinstaller_api():
    opts = ["--onefile",
            "--icon", "picture/ANSportion.ico",
            "--name", "ANSportion1.1.6-Pro",
            
            "ANSportion.py",

            "Code/__init__.py",

            "Code/use_1.py",

            "Code/attack_1.py",
            "Code/attack_2.py",
            "Code/attack_3.py",

            "Code/check_1.py",
            "Code/check_2.py",
            "Code/check_3.py",
            "Code/check_4.py",
            "Code/check_5.py",
            "Code/check_6.py",

            "Code/crawler_1.py",
            "Code/crawler_2.py",

            "Code/port_1.py",
            "Code/port_2.py",

            "Code/server_1.py",
            "Code/server_2.py",

            "Code/listen_1.py",

            "Code/wifi_1.py",
            "Code/wifi_2.py",
            "Code/wifi_3.py",
            "Code/wifi_4.py",
            "Code/wifi_5.py"]
    try:
        run(opts)
        print("打包成功")
    except SystemExit as e:
        print("打包过程出错:", e)
if __name__ == "__main__":
    package_with_pyinstaller_api()