# 提取验证码验证数据，包括机器人与否、验证成功与否、数据获取时间、鼠标移动数据，并生成csv
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

def clean_data_step01(data_row):
            # 将“success”、“fail”转换成 1或0，将坐标和时间戳转换成int
            old_data01 = data_row[:2]#列表 "是否是bot|验证成功与否|验证数据获取时间错"
            old_data02 = data_row[2:]#列表 "[x0,y0,时间戳],[x1,y1,时间戳]..."
            new_data = []
            # 将“success”、“fail”转换成 1或0
            check_result_list = []
            if old_data01[0] == "success":
                captcha_result = 1
                check_time = int(old_data01[1])
                check_result_list.append(captcha_result)
                check_result_list.append(check_time)
            elif old_data01[0] == "fail":
                captcha_result = 0
                check_time = int(old_data01[1])
                check_result_list.append(captcha_result)
                check_result_list.append(check_time)
            # 将坐标和时间戳转换成int
            #coords_array = []
            #for coord_list_str in old_data02:
            #    new_coord_list=[]
            #    coord_list=coord_list_str.split(",")
            #    for i in coord_list:
            #        #i.replace(" ","")
            #        new_coord_list.append(int(i))
            #    coords_array.append(new_coord_list)#转换为int的坐标数据

            # 重新组合数据
            new_data.extend(check_result_list)
            #new_data.extend(coords_array)  
            new_data.extend(old_data02)  
            return new_data  


def mouse_data_clean(file_route_list,data_type):#human:0;bot:1;unknow:2
    clean_data_list =[]
    for f in file_route_list:
        input_list = []
        input_list.append(data_type)
        csv_lines = read_lines(f)#原始数据格式，用“|”分隔，例："验证成功与否|验证数据获取时间错|[x0,y0,时间戳]|[x1,y1,时间戳]|..."
        for csv_line in csv_lines:
            new_csv_line =csv_line.split("|")
            del new_csv_line[-1] #删除数据众最后一个空值，最后一个原始字符串为“|”,split后为空值
            new_data = clean_data_step01(new_csv_line)# 将“success”、“fail”转换成 1或0，将坐标和时间戳转换成int
            input_list.extend(new_data)
        clean_data_list.append(input_list)   
    return clean_data_list


if __name__ == '__main__':

    os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
    excel_path=".\clean_data\clean_data_step_01.csv"
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
