import os
import shutil
import ctypes
from pathlib import Path

# ========== 🔧 路径配置（手动修改）==========
# ⚠️ 请根据你自己电脑的路径进行修改！
# Configure your own paths here before running the script

# 中文字体源文件夹路径（含子目录）
# Source folder for Chinese fonts (may contain subfolders)
source_cn_path = "路径/到/你的/Fonts_Source_CN"

# 英文字体源文件夹路径
# Source folder for English fonts
source_en_path = "路径/到/你的/Fonts_Source_EN"

# 中文字体提取目标文件夹
# Target folder for extracted Chinese fonts
target_cn_path = "路径/到/你的/Fonts_Output_CN"

# 英文字体提取目标文件夹
# Target folder for extracted English fonts
target_en_path = "路径/到/你的/Fonts_Output_EN"

# ========== 支持的字体扩展名 ==========
# Supported font file extensions
font_extensions = ['.ttf', '.otf']

# 自动创建输出文件夹（避免报错）
# Automatically create target folders if they don't exist
os.makedirs(target_cn_path, exist_ok=True)
os.makedirs(target_en_path, exist_ok=True)

def extract_fonts(source_folder, target_folder, tag):
    """
    提取字体文件并重命名为带标签的新文件名
    Extract font files and rename them with a tag
    """
    success_count = 0
    for root, _, files in os.walk(source_folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in font_extensions:
                source_path = os.path.join(root, file)
                new_filename = os.path.splitext(file)[0] + f'_{tag}' + ext
                target_path = os.path.join(target_folder, new_filename)
                shutil.copy2(source_path, target_path)
                print(f'[✔] Copied: {new_filename}')
                success_count += 1
    return success_count

def install_fonts(folder_path):
    """
    安装字体文件（仅限 Windows 系统）
    Install fonts (Windows only)
    """
    installed_count = 0
    for file in os.listdir(folder_path):
        if file.endswith('.ttf') or file.endswith('.otf'):
            font_path = os.path.join(folder_path, file)
            try:
                ctypes.windll.gdi32.AddFontResourceW(font_path)
                print(f'[✔] Installed: {file}')
                installed_count += 1
            except Exception as e:
                print(f'[✘] Install failed: {file}, Reason: {e}')
    return installed_count

# ========== 主流程 ==========
# Main execution flow
if __name__ == "__main__":
    print("\n📦 Step 1: Extracting fonts... / 提取字体中...\n")

    cn_count = extract_fonts(source_cn_path, target_cn_path, "OpenSource_CommercialUse")
    en_count = extract_fonts(source_en_path, target_en_path, "OpenSource_CommercialUse")

    print(f"\n✅ CN fonts extracted 中文字体提取数量: {cn_count}")
    print(f"✅ EN fonts extracted 英文字体提取数量: {en_count}")

    print("\n🛠 Step 2: Installing fonts... / 安装字体中...\n")

    cn_installed = install_fonts(target_cn_path)
    en_installed = install_fonts(target_en_path)

    print(f"\n🎉 Done! 安装完成！")
    print(f"✅ CN Installed 中文已安装: {cn_installed}")
    print(f"✅ EN Installed 英文已安装: {en_installed}")