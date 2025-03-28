from cryptography.fernet import Fernet

def generate_key():
    """
    生成一个密钥并保存到文件中
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    从文件中加载密钥
    """
    return open("secret.key", "rb").read()

def encrypt_file(file_name, key):
    """
    加密指定文件
    """
    f = Fernet(key)
    with open(file_name, "rb") as file:
        # 读取文件内容
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    # 生成并保存密钥
    generate_key()
    # 加载密钥
    key = load_key()
    # 指定要加密的文件路径
    file_path = "example.txt"
    encrypt_file(file_path, key)
    print(f"文件 {file_path} 已加密为 {file_path}.encrypted")