# 用于文件迁移时的比对，尽量减少未修改文件的迁移，通过文件修改时间来判断是否有修改

import os,time
from prettytable import PrettyTable
import shutil

# 清洗文件夹地址，去掉多余符号
def clear_path(target_path):
    # 清洗地址，去掉多余的"\"
    if target_path[-1] != "\\":
        target_path = target_path
    else:
        target_path = target_path[:-1]
    return target_path

# 美化表格
def pretty_list(table_list,table_title):
    table_target_file = PrettyTable(table_title)
    for fl in table_list:
        table_target_file.add_row(fl)
    print(table_target_file)

# 遍历指定目录下，文件夹的所有文件，并获取文件的创建、修改时间
## 提取文件的创建时间、修改时间
def getFileTime(file_ab_path):
    file_time_list  = []
    # 获取创建时间
    #file_time_list.append(os.path.getctime(file_ab_path)) 
    # 获取最近修改时间
    file_time_list.append(os.path.getmtime(file_ab_path))
    # 获取最近访问时间
    #file_time_list.append(os.path.getatime(file_ab_path))

    return file_time_list
## 将时间戳格式化为可读时间
def stamp2structTime(stamp_time):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(stamp_time)))


## 判断目标文件夹绝对路径的字符串长度，用于后面提取文件的相对路径
def tp_string_len(target_path):
    if target_path[-1] != "\\":
        tp_string_len = len(target_path)
    else:
        tp_string_len = len(target_path)-1
    return tp_string_len


## 遍历指定路径下的文件，并提取文件名、绝对路径、相对路径及修改时间
def files_path_list(target_path):
    #root_list = []
    #dir_list = []
    file_list =[] #['文件名', '绝对路径', '相对路径','最近修改时间']
    for root,dirs,files in os.walk(target_path,topdown=False):
        #print(root)# 查询的根目录
        #print(dirs)# 根目录中的文件夹
        #print(files)# 根目录中的文件
        for f in files:
            f_data_list = []
            tp_len=tp_string_len(target_path)
            file_ab_path = root +"\\"+ f
            file_rel_path = file_ab_path[tp_len:]
            # 将文件信息写入列表
            f_data_list.append(f)#文件名
            f_data_list.append(file_ab_path )#绝对路径
            f_data_list.append(file_rel_path)#相对路径

            # 获取文件修改时间
            for file_time in getFileTime(file_ab_path):
                f_data_list.append(file_time)

            file_list.append(f_data_list)
    return(file_list)


# 对比相对路径下的文件，判断哪些文件需要迁移
def compare_files(org_file_list,target_file_list):
    for o_file in org_file_list:
        file_state = "添加"
        for t_file in target_file_list:
            try:
                t_file.index(o_file[2])
            except:
                continue
            if o_file[3] != t_file[3]:
                file_state = "变更"
            else:
                file_state = "保持"
            break
        o_file.append(file_state)
    for t_file in target_file_list:
        file_state = "移除"
        t_file.append(file_state)
        org_file_list.append(t_file)
    return org_file_list

# 执行迁移操作

## 选择更新模式
def update_file_mode(target_path,file_states_list):
    mode_id = input(
        '''请选择更新模式：
            1.添加、更新文件的同时删除目标文件夹中多余的文件
            2.仅添加和更新文件，不删除多余文件
        '''
    )
    update_file_list = file_states_list.copy()
    if mode_id == "1":
        pass
    elif mode_id == "2":
        for file in file_states_list:
            if file[-1] == "移除":
                print(file)
                update_file_list.remove(file)
            else:
                pass

    pretty_list(update_file_list,['文件名', '绝对路径', '相对路径','最近修改时间','状态'])
    update_files(target_path,update_file_list)

## 判断文件夹是否存在，不存在则创建文件夹
def folder_exists(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

## 执行迁移操作
def update_files(target_path,file_states_list):
    print("开始更新...")
    for file in file_states_list:
        if file[-1]=="保持":#不更新文件
            pass
        elif file[-1]=="添加":
            #文件需要添加到的相对路径
            target_folder_path = (target_path+file[2])[:-len(file[0])]
            #print(target_folder_path)
            # 判断文件夹是否存在，不存在则创建文件夹
            folder_exists(target_folder_path)
            # shutil.copy2 能够对文件进行复制，同时不会修改文件的修改时间等属性
            shutil.copy2(file[1],target_path+file[2])
        elif file[-1]=="变更":
            shutil.copy2(file[1],target_path+file[2])
        elif file[-1]=="移除":
            os.remove(target_path+file[2])
        #file_states_list.remove(file)
    print("完成更新")


# 主程序
if __name__ == '__main__':
    
    org_path = input("请输入原文件夹地址:")
    target_path=input("请输入目标文件夹地址:")

    #org_path = r"E:\personal\daliy_code\daylifecode\File_manage\file_updat_check\test_file\org"
    #target_path = r"E:\personal\daliy_code\daylifecode\File_manage\file_updat_check\test_file\trans2"

    # 清洗地址
    org_path = clear_path(org_path)
    target_path=clear_path(target_path)


    # 提取文件信息
    ## 源目录
    org_file_list = files_path_list(org_path)
    print("源目录文件列表：")
    pretty_list(org_file_list,['文件名', '绝对路径', '相对路径','最近修改时间'])

    ## 目标目录
    target_file_list = files_path_list(target_path)
    print("目标目录文件列表：")
    pretty_list(target_file_list,['文件名', '绝对路径', '相对路径','最近修改时间'])



    # 比较原始文件夹和目标文件夹中的文件，列出文件更新状态
    file_states_list = compare_files(org_file_list,target_file_list)
    
    # 显示文件变更状态表格
    print("文件更新状态：")
    pretty_list(file_states_list,['文件名', '绝对路径', '相对路径','最近修改时间','状态'])

    

    # 执行操作
    update_file_mode(target_path,file_states_list)