import re

def replace_image_path(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'!\[.*?\]\((C:/Users/D2010/AppData/Roaming/Typora/typora-user-images/.*?)\)'
    new_content = re.sub(pattern, lambda x: x.group(0).replace('C:/Users/D2010/AppData/Roaming/Typora/typora-user-images/', './../assets/article_data/Pman002/pic/'), content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# 使用方法：将下面的路径替换为你的markdown文件路径
markdown_file_path = r'notebook\[Pman002]功能.md'
replace_image_path(markdown_file_path)
