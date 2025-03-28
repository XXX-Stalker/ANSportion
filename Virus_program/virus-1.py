import os
import shutil
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def copy_file_to_directory(source_file, destination_directory):
    if not os.path.isfile(source_file):
        logging.error(f"源文件 {source_file} 不存在")
        return
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
        logging.info(f"创建目标目录 {destination_directory}")
    destination_file = os.path.join(destination_directory, os.path.basename(source_file))
    try:
        shutil.copy(source_file, destination_file)
        logging.info(f"文件 {source_file} 已成功复制到 {destination_directory}")
    except Exception as e:
        logging.error(f"复制文件时出错: {e}")
source_file = "文件源"   #文件源
destination_directory = "文件目录"   #文件目标
copy_file_to_directory(source_file, destination_directory)
