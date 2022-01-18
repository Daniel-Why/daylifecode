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
    plt.gca().invert_yaxis()
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





#################################### 特征 ######################################3
# 完成验证时间
def extract_used_time(trace: np.ndarray):
    trace = trace.T
    used_time = trace[2].max() - trace[2].min()
    return used_time


# 提取平均速度
def extract_avg_speed(trace: np.ndarray):

    """
    提取平均速度,参数为一个numpy二维数组,大小是n*3:[[x,y,t],[x,y,t],...,[x,y,t]]
    """
    #trace = trace[:]
    path_length = 0
    x_t = trace[0][0]#t时刻的x值
    y_t = trace[0][1]#t时刻的y值
    for (x, y, t) in trace[1:]: #鼠标移动的距离
        path_length += math.sqrt((x_t - x) ** 2 + (y_t - y) ** 2)
        x_t = x
        y_t = y
    trace = trace.T #矩阵转置
    avg_speed = (path_length / (trace[2].max() - trace[2].min()))
    return avg_speed


# 提取最大速度
def extract_max_speed(trace: np.ndarray):

    trace = sorted(trace, key=lambda point: point[2])
    x_t = trace[0][0]
    y_t = trace[0][1]
    tt = trace[0][2]
    max_speed = 0.000001
    for p in trace[1:]:
        x = p[0]
        y = p[1]
        t = p[2]
        if tt > t:
            print("error:error:error:error:error:error:error:error:error:error:er")
            break
        speed = (math.sqrt((x_t - x) ** 2 + (y_t - y) ** 2) / (0.5 if t == tt else t - tt))
        max_speed = speed if max_speed < speed else max_speed
        x_t = x
        y_t = y
        tt = t
    return max_speed

# 提取最小速度
def extract_min_speed(trace: np.ndarray):
    trace = sorted(trace, key=lambda point: point[2])
    x_t = trace[0][0]
    y_t = trace[0][1]
    tt = trace[0][2]
    min_speed = 1000000000
    for p in trace[1:]:
        x = p[0]
        y = p[1]
        t = p[2]
        if tt > t:
            print("error:error:error:error:error:error:error:error:error:error:er")
            break
        speed = (math.sqrt((x_t - x) ** 2 + (y_t - y) ** 2) / (0.5 if t == tt else t - tt))
        if speed != 0.0:
            min_speed = speed if min_speed > speed else min_speed
        x_t = x
        y_t = y
        tt = t
    return min_speed

# 提取速度变化程度
def extract_speed_change_rate(trace: np.ndarray):
    trace = sorted(trace, key=lambda point: point[2])
    x_t = trace[0][0]
    y_t = trace[0][1]
    tt = trace[0][2]
    speeds = list()
    # for a in trace[1:]:
    #     print(a)
    for p in trace[1:]:
        x = p[0]
        y = p[1]
        t = p[2]
        if tt > t:
            print("error:error:error:error:error:error:error:error:error:error:er")
            break
        speeds.append(math.sqrt((x_t - x) ** 2 + (y_t - y) ** 2) / (0.5 if t == tt else t - tt))
        x_t = x
        y_t = y
        tt = t
    return np.var(np.array(speeds)) * len(trace)

# 判断x方向是否会重复轨迹
def extract_if_x_traceback(trace: np.ndarray):
    """
    判断是否会重复轨迹，以此区分部分机器，参数为一个numpy二维数组,大小是n*3:[[x,y,t],[x,y,t],...,[x,y,t]]
    注意：部分机器在x轴上为递增的，不会递减
    若有 返回1
    否则返回0
    """

    trace = trace.T
    cnt = 0
    if len(trace[0]) >= 2:
        for i in range(0, len(trace[0])-1):
            if trace[0][i] > trace[0][i + 1]:
                return 1

    else:
        return 0
    return cnt


# 判断y方向是否会重复轨迹
def extract_if_y_traceback(trace: np.ndarray):
    """
    判断是否会重复轨迹，以此区分部分机器，参数为一个numpy二维数组,大小是n*3:[[x,y,t],[x,y,t],...,[x,y,t]]
    注意：部分机器在x轴上为递增的，不会递减
    若有 返回1
    否则返回0
    """

    trace = trace.T
    cnt = 0
    if len(trace[1]) >= 2:
        for i in range(0, len(trace[1])-1):
            if trace[1][i] > trace[1][i + 1]:
                return 1

    else:
        return 0
    return cnt

# 判断x方向重复轨迹数量
def extract_x_traceback_num(trace:np.ndarray):
    trace = trace.T
    cnt = 0
    if len(trace[0]) >= 2:
        for i in range(0, len(trace[0])-1):
            if trace[0][i] > trace[0][i + 1]:
                cnt +=1

    else:
        return 0
    return cnt


# 判断y方向重复轨迹数量
def extract_y_traceback_num(trace:np.ndarray):
    trace = trace.T
    cnt = 0
    if len(trace[1]) >= 2:
        for i in range(0, len(trace[1])-1):
            if trace[1][i] > trace[1][i + 1]:
                cnt +=1

    else:
        return 0
    return cnt

###### 特征提取集合 #######
def extract_feature(trace:np.ndarray):
        
        #完成验证时间
        used_t = extract_used_time(coords_nparray)

        #速度平均值
        avg_s = extract_avg_speed(coords_nparray)

        #速度最大值
        max_s = extract_max_speed(coords_nparray)

        #速度最小值
        min_s = extract_min_speed(coords_nparray)
        
        #速度变化率
        speed_change_rate = extract_speed_change_rate(coords_nparray)

        #x方向是否有重复轨迹
        x_traceback = extract_if_x_traceback(coords_nparray)

        #y方向是否有重复轨迹
        y_traceback = extract_if_y_traceback(coords_nparray)

        # 判断x方向重复轨迹数量
        x_traceback_num = extract_x_traceback_num(coords_nparray)

        # 判断y方向重复轨迹数量
        y_traceback_num = extract_y_traceback_num(coords_nparray)
        return [used_t,avg_s,max_s,min_s,speed_change_rate,x_traceback,y_traceback,x_traceback_num,y_traceback_num]

#%% 主函数
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
clean_data_S02 = csv.reader(open(r".\clean_data\clean_data_step_02.csv"))
clean_data=[]
for i,data_row in enumerate(clean_data_S02):
    if i != 0:
        info_data = int_data(data_row[:3])
        coords_nparray = mouseData_to_nparry(data_row)
        
        #绘制鼠标轨迹
        #draw_mouse_trail(coords_nparray)

        #提取特征
        extract_feature_list = extract_feature(coords_nparray)

        mouse_data = []
        mouse_data.extend(info_data[:-1])
        mouse_data.extend(extract_feature_list)
        clean_data.append(mouse_data)
        print("{} row finished!".format(i))

# %% 数据存储为npy格式和csv格式
np_save_path = ".\clean_data\clean_data_step_03.npy"
save_npy(np_save_path,clean_data)

csv_save_path = ".\clean_data\clean_data_step_03.csv"
header_list=["Bot","captcha_result","used_t","avg_s","max_s","min_s","speed_change_rate","x_traceback","y_traceback","x_traceback_num","y_traceback_num"]
save_csv(csv_save_path,clean_data,header_list)

# %%
