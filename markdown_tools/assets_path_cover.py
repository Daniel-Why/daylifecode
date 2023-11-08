import os,time
def files_path_list(target_path):#找到目标文件
    file_list =[] #['文件名', '绝对路径', '相对路径','最近修改时间']
    target_file_type = "md" # 后缀名
    for root,dirs,files in os.walk(target_path,topdown=False):
        #print(root)# 查询的根目录
        #print(dirs)# 根目录中的文件夹
        #print(files)# 根目录中的文件
        for f in files:
            if f.split('.')[-1] == target_file_type:
                file_ab_path = root +"\\"+ f
                # 将文件信息写入列表
                file_list.append(file_ab_path)#绝对路径
            else:
                continue
    return(file_list)



def keywords_cover(file_path,org_keywords,target_keywords):#替换字符串
    with open(file_path, "r", encoding='UTF-8') as f:#读取全文
        content = f.read()

    new_content =  content.replace(org_keywords,target_keywords)#替换字段
    with open(file_path, "w", encoding='UTF-8') as f:#保存全文
        content = f.write(new_content)
           

if __name__ == '__main__':
    file_path = r"E:\\Document\\notebook"#文件夹路径
    files_list = files_path_list(file_path)
    print(files_list)
    org_keywords = "E:\\Document\\notebook\\" # 需要替换的文本
    target_keywords = ".\\" # 替换为
    for file in files_list:
        keywords_cover(file,org_keywords,target_keywords)
        print("{} 替换完成".format(file))