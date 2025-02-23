import requests
import validators
import time
def check_website_status(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    if not validators.url(url):
        print(f"{url} 不是合法的网址格式，请重新输入。")
        return
    try:
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        end_time = time.time()
        response_time = end_time - start_time
        print("-" * 50)
        print(f"网站: {url}")
        print(f"状态码: {response.status_code}")
        print(f"响应时间: {response_time:.2f} 秒")
        print("-" * 50)
    except requests.exceptions.Timeout:
        print(f"{'-' * 50}\n网站: {url} 请求超时\n{'-' * 50}")
    except requests.exceptions.ConnectionError:
        print(f"{'-' * 50}\n网站: {url} 连接失败\n{'-' * 50}")
    except requests.exceptions.RequestException as e:
        print(f"{'-' * 50}\n网站: {url} 发生错误:{e}\n{'-' * 50}")
if __name__ == "__main__":
    websites = input("请输入要检查的网站URL:").split()
    for site in websites:
        check_website_status(site)
