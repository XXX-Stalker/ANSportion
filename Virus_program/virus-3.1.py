from cryptography.fernet import Fernet

def load_key():
    """
    从文件中加载密钥
    """
    return open("secret.key", "rb").read()

def decrypt_file(file_name, key):
    """
    解密指定文件
    """
    f = Fernet(key)
    with open(file_name, "rb") as file:
        # 读取加密文件内容
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name[:-10], "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # 加载密钥
    key = load_key()
    # 指定要解密的文件路径
    file_path = "example.txt.encrypted"
    decrypt_file(file_path, key)
    print(f"文件 {file_path} 已解密为 {file_path[:-10]}")