import requests
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"网站: {url} 发生错误: {e}")
        return None
url = input("请输入要爬取的网站URL: ")
choice = input("请选择操作1 - 打印到终端，2 - 保存到文件: ")
html_content = get_html_content(url)
if html_content:
    if choice == '1':
        print(html_content)
    elif choice == '2':
        file_name = input("请输入要保存的文件名: ")
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(html_content)
            print(f"内容已保存到 {file_name}")
        except IOError as e:
            print(f"保存文件时发生错误: {e}")
    else:
        print("无效的选择")
