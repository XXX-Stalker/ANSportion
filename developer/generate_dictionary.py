import itertools
import threading
import time

def generate_dictionary(start_len, end_len, use_letters, use_numbers, use_symbols, filename, suffix, thread_count):
    # 定义字符集
    characters = ""
    if use_letters:
        characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        characters += "0123456789"
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"

    # 打开文件准备写入
    with open(f"{filename}.{suffix}", "w") as file:
        # 定义每个线程的任务
        def worker(start, end):
            for length in range(start, end + 1):
                for combination in itertools.product(characters, repeat=length):
                    file.write("".join(combination) + "\n")

        # 创建线程
        threads = []
        step = (end_len - start_len + 1) // thread_count
        for i in range(thread_count):
            start = start_len + i * step
            end = start_len + (i + 1) * step - 1 if i < thread_count - 1 else end_len
            thread = threading.Thread(target=worker, args=(start, end))
            threads.append(thread)
            thread.start()

        # 等待所有线程完成
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    # 用户输入
    start_len = int(input("请输入起始文字位数: "))
    end_len = int(input("请输入结束文字位数: "))
    use_letters = input("是否包含字母? (y/n): ").lower() == 'y'
    use_numbers = input("是否包含数字? (y/n): ").lower() == 'y'
    use_symbols = input("是否包含符号? (y/n): ").lower() == 'y'
    thread_count = int(input("请输入线程数: "))
    filename = input("请输入保存的文件名: ")
    suffix = input("请输入文件后缀 (例如: txt): ")

    # 开始生成字典
    print("开始生成字典...")
    start_time = time.time()
    generate_dictionary(start_len, end_len, use_letters, use_numbers, use_symbols, filename, suffix, thread_count)
    end_time = time.time()
    print(f"字典生成完成，耗时: {end_time - start_time:.2f} 秒")