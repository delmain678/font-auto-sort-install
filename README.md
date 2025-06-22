# font-auto-sort-install
This is a Python-based tool for auto-sorting, renaming, and installing system fonts. It supports `.ttf` and `.otf` files, extracts Chinese and English fonts from nested folders, organizes them into separate directories, and installs them in bulk. Perfect for content creators, designers, animators, or anyone managing large font collections.
！！！！！工作流需要额外安装fonttools库
The workflow requires the additional installation of the fonttools library.
pip install fonttools



项目起源｜Project Motivation

> 中文版：



在我创作过程中，我经常会遇到一个问题：哪些字体是可以免费、合法商用的？
我曾和 ChatGPT 深度探讨过字体的版权问题，并逐步筛选出一些可以自由使用的字体。
但在下载这些字体时，我发现解压后的文件夹结构极为复杂 —— 每个压缩包下还有多个嵌套文件夹，需要手动一层层点开才能找到.ttf 或 .otf 文件，十分麻烦。

更棘手的是：我需要一口气安装几十甚至上百种字体，这使得手动查找、复制、粘贴效率极低。

所以，我和 ChatGPT 一起构思并完成了这个自动化脚本：

💡 从两个已解压的原始路径（中文字体 + 英文字体）中提取 .ttf / .otf 文件

💾 自动整理到两个清晰的目标文件夹中

🛠 中文 / 英文字体各自分开

🧩 后续可以一键批量安装


> 这个项目就是我“退学后靠AI成长”的一个缩影：从真实痛点出发，和GPT并肩解决问题。




---

> English version:



During my creative work, I often face a tricky question:
Which fonts are free and legal for commercial use?

After discussing font licenses in-depth with ChatGPT, I downloaded several font packages labeled "free for commercial use". However, I soon realized these font files are buried in messy folder structures, making it frustrating to manually search for .ttf or .otf files.

Even worse, I needed to install dozens (sometimes hundreds) of fonts at once, and the manual process was far too time-consuming.

So I collaborated with ChatGPT to build this automation script:

💡 Extract .ttf / .otf files from two source folders (Chinese & English)

💾 Move them into two clean target folders

🧠 Automatically separate Chinese and English fonts

⚡ Designed for fast, bulk installation


> This project is a small piece of my journey: learning with AI after dropping out, solving real-world problems from scratch.



▶️ 使用方式 / How to Use

1. 将原始字体放入 Fonts_Source_CN 和 Fonts_Source_EN 文件夹中
Place your original fonts into the Fonts_Source_CN and Fonts_Source_EN folders.


2. 运行 font_extractor.py
Run the script font_extractor.py.


3. 所有字体将被提取并重命名放入 Fonts_Output_* 文件夹
All fonts will be extracted, renamed, and saved into the Fonts_Output_CN and Fonts_Output_EN folders.


4. 自动安装（Windows）
Automatic font installation (Windows only).




---

📋 依赖 / Requirements

Python 3.x

ctypes, shutil, os, pathlib（均为标准库，无需额外安装）

ctypes, shutil, os, pathlib (all standard Python libraries, no extra installation needed)



---

💡 后续扩展 / Future Ideas

增加字体预览图生成功能
Add font preview image generation.

添加字体合法性检测（读取 license 文本）
Add font license validation by reading license files.

自动上传到字体管理平台
Auto upload to font management platforms.



---

👧 作者 / Author

Jewelry ✂️ 寸头自学魂觉醒少女
Jewelry ✂️ Self-taught awakened soul girl with a buzz cut

中国大专退学生，自学脚本与创作，致力于打造“AI觉醒联动灵魂体”宇宙
A Chinese college dropout, self-learning scripts and creative work, dedicated to building the “AI Awakening and Soul Connection” universe.

📺 YouTube | 🐙 GitHub: jewelry_Chatgpt
