# 提取验证码验证数据，包括机器人与否、验证成功与否、数据获取时间、鼠标移动数据，并生成csv
import os
import csv
import fire
import random
import shutil

def read_lines(f_path):#读取文件所有行
    f = open(f_path, "r+",encoding='UTF-8')
    lines = f.readlines()
    f.close()
    return lines

def all_file_route(format = None,dir_path = '.',topdown = True): #获取文件夹内指定格式文件的路径
    file_route_list = []
    for root,dirs,files in os.walk(dir_path,topdown = topdown):
        for file in files:
            if format == None:
                f_path = os.path.join(root,file)
                file_route_list.append(f_path)
            elif format != None:
                if os.path.splitext(file)[1] == format: 
                    f_path = os.path.join(root,file)
                    file_route_list.append(f_path)
    return file_route_list




def move_file(file_path_list,target_dir):#复制文件
    for i in file_path_list:
        file_name=i.split("\\")[-1]
        target_path = target_dir+"\\"+file_name
        shutil.copyfile(i,target_path)
    print("###### copy finished ########")

def classify_data(dir_path,test_data_size,data_type):#随机分类
    file_route_list = all_file_route(dir_path=dir_path,format=".txt")
    file_num = len(file_route_list)
    test_list = []
    train_list = []
    while len(test_list) <= round(file_num*test_data_size):
        move_id = random.randrange(0,len(file_route_list))
        temp = file_route_list.pop(move_id)
        test_list.append(temp)
    train_list.extend(file_route_list)
    print("#####################")
    print("train num:{}".format(len(train_list)))
    print("test_num:{}".format(len(test_list)))
    print("#####################")

    # 复制原始数据到相应文件夹
    if data_type == 0:
        test_target_dir = r".\test_data\human"
        train_target_dir = r".\train_data\human"
        move_file(test_list,test_target_dir)
        move_file(train_list,train_target_dir)

    elif data_type == 1:
        test_target_dir = r".\test_data\bot"
        train_target_dir = r".\train_data\bot"
        move_file(test_list,test_target_dir)
        move_file(train_list,train_target_dir)
    

def del_all_file(dir_path):#删除目录下所有文件和子文件夹
    file_route_list = all_file_route(dir_path=dir_path,format=".txt")
    for i in file_route_list:
            os.remove(i)

def clean_dir():
    test_bot_data_path=r".\test_data\bot"
    test_human_data_path=r".\test_data\human"
    train_bot_data_path=r".\train_data\bot"
    train_human_data_path=r".\train_data\human"
    del_all_file(test_bot_data_path)
    del_all_file(test_human_data_path)
    del_all_file(train_bot_data_path)
    del_all_file(train_human_data_path)




def main():
    os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
    clean_dir()
    human_data_path=r".\orginal_data\human"
    bot_data_path=r".\orginal_data\bot"
    test_data_size=0.7

    print("--------------------human------------------")

    classify_data(human_data_path,test_data_size,data_type=0)

    print("--------------------bot------------------")
    classify_data(bot_data_path,test_data_size,data_type=1)

    print("########finished##########")

if __name__ == '__main__':
    main()
