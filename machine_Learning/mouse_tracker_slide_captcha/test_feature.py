#用于测试提取一些特征
#计算轨迹特征

#%%
import os
import csv
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt

#将数据转换为 int
def int_data(data_row):
    new_data_row = []
    for i in data_row:
        new_data_row.append(int(i))
    return new_data_row


#将数据坐标转换为 int 和np.array
def mouseData_to_nparry(mouse_data):
    ## 清洗坐标数据
    coords_array = []
    for coord in mouse_data[3:]:
        coord_list = coord.split(",")
        new_coord_list=[]
        for i in coord_list:
            if i != "":
                i.replace(" ","")
                new_coord_list.append(int(i))
        coords_array.append(new_coord_list)
    coords_nparray =  np.array(coords_array)
    return coords_nparray



#绘制鼠标轨迹
def draw_mouse_trail(coords_nparry):
    coords_obj = pd.DataFrame(coords_nparry)
    #plt.gca().invert_yaxis()
    plt.plot(coords_obj[0],coords_obj[1])
    plt.show()


def save_npy(np_save_path,np_data):
    np.save(np_save_path,np_data)
    print("npy saved!!")


def save_csv(csv_save_path,csv_data,header_list=[]):
    with open(csv_save_path,"w",newline = '') as csvfile:
        f_csv=csv.writer(csvfile)
        f_csv.writerow(header_list)
        f_csv.writerows(csv_data)
        print("csv saved!!")


######################### 一些数据测试不用于特征提取 #############################
def x_move_diff(trace:np.ndarray):
    trace = trace.T
    move_diff_data = []
    diff_arrays=[]
    if len(trace[0]) >= 2:
        for i in range(0, len(trace[0])-1):
            diff_array = []
            move_diff = trace[0][i+1]-trace[0][i]
            diff_array.append(trace[2][i])
            diff_array.append(move_diff)
            move_diff_data.append(move_diff)
            diff_arrays.append(diff_array)
        return move_diff_data,diff_arrays




#%% 主函数
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
clean_data_S02 = csv.reader(open(r".\clean_data\clean_data_step_02.csv"))
test_datas =[]
for i,data_row in enumerate(clean_data_S02):
    if i != 0 and data_row[0] =="0":
        info_data = int_data(data_row[:3])
        coords_nparray = mouseData_to_nparry(data_row)

        ####### 一些测试
        test_data,diff_array = x_move_diff(coords_nparray)
        test_datas.append(test_data)


        test_datas_nparray =  np.array(diff_array)
        draw_mouse_trail(test_datas_nparray)

        print("{} row finished!".format(i))

# %% 数据存储为npy格式和csv格式

csv_save_path = r".\clean_data\test_feature_data.csv"
header_list=["1","2","3"]
save_csv(csv_save_path,test_datas,header_list)

# %%
