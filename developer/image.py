from PIL import Image
import os
import sys

def convert_image(input_path, output_path, output_format):
    try:
        # 打开图片
        with Image.open(input_path) as img:
            # 获取图片的原始格式
            original_format = img.format
            print(f"原始图片格式：{original_format}")
            # 转换图片格式
            img.save(output_path, format=output_format.upper())
            print(f"图片已成功转换为 {output_format.upper()} 格式，保存到 {output_path}")
    except Exception as e:
        print(f"转换失败：{e}")

def main():
    input_path = input("请输入图片的完整路径：")
    output_format = input("请输入目标格式（如 ICO, JPG, PNG 等）：").strip().upper()
    # 检查文件是否存在
    if not os.path.isfile(input_path):
        print("错误：输入的文件不存在！")
        sys.exit(1)
    # 检查输出格式是否支持
    supported_formats = ["ICO", "JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF"]
    if output_format not in supported_formats:
        print(f"错误：不支持的格式 {output_format}。支持的格式有：{', '.join(supported_formats)}")
        sys.exit(1)
    # 构造输出路径
    output_path = os.path.splitext(input_path)[0] + f".{output_format.lower()}"
    # 调用转换函数
    convert_image(input_path, output_path, output_format)

if __name__ == "__main__":
    main()