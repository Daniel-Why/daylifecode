# 提取验证码验证数据，包括机器人与否、验证成功与否、数据获取时间、鼠标移动数据，并生成csv
import os
import csv
import fire
import numpy as np

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
            # 将坐标和时间戳转换成int
            coords_array = []
            for coord_list_str in data_row:
                new_coord_list=[]
                coord_list=coord_list_str.split(",")
                for i in coord_list:
                    #i.replace(" ","")
                    new_coord_list.append(int(i))
                coords_array.append(new_coord_list)#转换为int的坐标数据
            return coords_array  


def mouse_data_clean(file_route_list):#human:0;bot:1;unknow:2
    clean_data_list =[]
    for f in file_route_list:
        input_list = []
        csv_lines = read_lines(f)#原始数据格式，用“|”分隔，例："验证成功与否|验证数据获取时间错|[x0,y0,时间戳]|[x1,y1,时间戳]|..."
        for csv_line in csv_lines:
            new_csv_line =csv_line.split("|")
            del new_csv_line[-1] #删除数据众最后一个空值，最后一个原始字符串为“|”,split后为空值
            del new_csv_line[0] #删除数据验证成功与否
            del new_csv_line[0] #删除数据验证数据获取时间戳
            new_data = clean_data_step01(new_csv_line)# 将“success”、“fail”转换成 1或0，将坐标和时间戳转换成int
            input_list.extend(new_data)
        clean_data_list.append(input_list)   
    return clean_data_list

def delete_error_data(data_list): # 删除点击滑动块前的数据
    clean_data=[]
    for datas in data_list:
        for data in datas[:]:
            click_bar=(int(data[0]) >= 8 and int(data[0])<=50 and int(data[1]) >= 505 and int(data[1]) <=550)#鼠标位置是否在拖动快处
            if click_bar == False:
                datas.remove(data)
            elif click_bar == True:
                break
        clean_data.append(datas)
    return clean_data

def normalization_coords(data_list): # 归一化，转化为每一步增加的位移
    clean_data = []
    for datas in data_list:
        new_datas = ["0,0"]
        for i in range(0,len(datas)-1):
            new_data=[]
            x = datas[i+1][0]-datas[i][0]
            y = datas[i+1][1]-datas[i][1]
            #t = datas[i+1][2]-datas[i][2]
            new_data.append(x)
            new_data.append(y)
            #new_data.append(t)
            new_data="{},{}".format(x,y)
            new_datas.append(new_data)
        clean_data.append(new_datas)
    return clean_data

def save_npy(np_save_path,np_data):
    np.save(np_save_path,np_data)
    print("npy saved!!")


def save_csv(csv_save_path,csv_data,header_list=[]):
    with open(csv_save_path,"w",newline = '') as csvfile:
        f_csv=csv.writer(csvfile)
        f_csv.writerow(header_list)
        f_csv.writerows(csv_data)
        print("csv saved!!")


def main():
    os.chdir(r"D:\Personal\daylifecode\captcha_example\Selenium_slide_captcha_cross")
 
    
    trace_data_path=r".\mouse_record\orginal_data"

    trace_data_list = all_file_route(dir_path=trace_data_path,format='.txt')#找出所有的txt


    print(len(trace_data_list))

    print("#####start######")
    #整理录入坐标数据
    clean_data_step01 = mouse_data_clean(trace_data_list)
    clean_data_step02 = delete_error_data(clean_data_step01)
    clean_data = normalization_coords(clean_data_step02)

    data_name="trace_record"
    
    csv_save_path = ".\mouse_record\clean_data\{}.csv".format(data_name)
    header_list=[""]
    save_csv(csv_save_path,clean_data,header_list)


if __name__ == '__main__':
    fire.Fire(main)
