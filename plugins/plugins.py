file_path = f"plugins/plugins_list.txt"

def run_plugins(target_line):
    def check_line_in_file(file_path, target_line):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() == target_line:
                        return True
            return False
        except FileNotFoundError:
            print(f"文件 {file_path} 不存在")
            return False
    
    if check_line_in_file(file_path, target_line):
        print(f"正在打开插件包 {target_line}...")
        module_name = f"plugins.{target_line}_guide"
        try:
            import importlib
            module = importlib.import_module(module_name)
            plugin_func = module.RUN
            plugin_func()
        except ImportError as e:
            print(f"无法打开插件包 {target_line}: {e}")
        except AttributeError:
            print(f"插件包 {target_line} 中没有找到 RUN 函数")
    else:
        pass