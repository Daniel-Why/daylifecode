# 提取鼠标轨迹数据，生成轨迹csv
import os
import csv

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

def mouse_data_clean(file_route_list,data_type):#human:0;bot:1;unknow:2
    clean_data_list =[]
    for f in file_route_list:
        input_list = []
        input_list.append(data_type)
        csv_lines = read_lines(f)#原始数据格式，用“|”分隔，例："验证成功与否|验证数据获取时间错|[x0,y0,时间戳]|[x1,y1,时间戳]|..."
        for csv_line in csv_lines:
            new_csv_line =csv_line.split("|")
            input_list.extend(new_csv_line)
            #print(input_list)
        clean_data_list.append(input_list)  
        #print(clean_data_list)  
    return clean_data_list


if __name__ == '__main__':

    os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
    excel_path=".\clean_data\clean_data.csv"
    bot_data_path=r".\orginal_data\bot"
    human_data_path=".\orginal_data\human"
    humandata_list = all_file_route(dir_path=human_data_path,format='.txt')#找出所有的txt
    botdata_list = all_file_route(dir_path=bot_data_path,format='.txt')#找出所有的txt

    print("#####start######")
    #整理录入坐标数据
    bot_clean_data = mouse_data_clean(botdata_list,1)

    human_clean_data = mouse_data_clean(humandata_list,0)

    #合并数据
    clean_data = []
    clean_data.extend(bot_clean_data)
    clean_data.extend(human_clean_data)


    with open(excel_path,"w",newline = '') as csvfile:
        header_list=["Bot","captcha_result","check_time","mouse track"]
        f_csv=csv.writer(csvfile)
        f_csv.writerow(header_list)
        f_csv.writerows(clean_data)
        print("######finish######")
