#计算轨迹特征

#%%
import os
import csv
import fire
from joblib import parallel_backend
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

# 判断鼠标移动次数数量
def extract_move_num(trace:np.ndarray):
    trace = trace.T
    move_num=len(trace[1])
    return move_num


# x坐标一阶差分
def extract_x_diff(trace:np.ndarray):
    trace = trace.T
    if len(trace[0]) >= 2:
        diff_list = []
        for i in range(0,len(trace[0])-1):
            diff = trace[0][i+1]-trace[0][i]
            diff_list.append(diff)
        diff_std = np.std(diff_list)     # 一阶差分的标准差
        diff_max = max(diff_list)   # 一阶差分的最大值
        diff_min = min(diff_list)   # 一阶差分的最小值

        diff_pd = pd.Series(diff_list)
        diff_skew = diff_pd.skew()  # 一阶差分的偏度
        return diff_std,diff_max,diff_min,diff_skew

    else:
        return 0,0,0,0
     
# y坐标一阶差分
def extract_y_diff(trace:np.ndarray):
    trace = trace.T
    if len(trace[1]) >= 2:
        diff_list = []
        for i in range(0,len(trace[1])-1):
            diff = trace[1][i+1]-trace[1][i]
            diff_list.append(diff)
        diff_std = np.std(diff_list)     # 一阶差分的标准
        diff_max = max(diff_list)   # 一阶差分的最大值
        diff_min = min(diff_list)   # 一阶差分的最小值
        diff_mean= np.mean(diff_list)    # 一阶差分的平均值

        diff_pd = pd.Series(diff_list)
        diff_skew = diff_pd.skew()  # 一阶差分的偏度

        return diff_std

    else:
        return 0

# t 时间的一阶差分
def extract_t_diff(trace:np.ndarray):
    trace = trace.T
    if len(trace[2]) >= 2:
        diff_list = []
        for i in range(0,len(trace[2])-1):
            diff = trace[2][i+1]-trace[2][i]
            diff_list.append(diff)
        diff_std = np.std(diff_list)     # 一阶差分的标准差
        diff_max = max(diff_list)   # 一阶差分的最大值
        diff_min = min(diff_list)   # 一阶差分的最小值
        diff_mean= np.mean(diff_list)    # 一阶差分的平均值
        
        if len(diff_list)>=3: # diff_list 少于3个值，偏度的返回值为 nan
            diff_pd = pd.Series(diff_list)
            diff_skew = diff_pd.skew()  # 一阶差分的偏度
        else:
            diff_skew = 0
        return diff_std,diff_mean

    else:
        return 0,0    

# 相邻点的一些特征
def extract_adjacent_point(trace:np.ndarray):
    trace = sorted(trace, key=lambda point: point[2])
    trace = np.array(trace)
    if len(trace.T[0]) >=2 :
        adj_point_dis_list = []
        adj_point_v_list = []

        for i in range(0,len(trace.T[0])-1):
            trace = trace
            adj_point_dis = ((trace[i+1][0]-trace[i][0])**2+(trace[i+1][1]-trace[i][1])**2)**0.5 #相邻点距离
            adj_point_dis_list.append(adj_point_dis)
            adj_point_v = adj_point_dis/(trace[i+1][2]-trace[i][2])#相邻点之间移动速度
            adj_point_v_list.append(adj_point_v)

        adj_point_dis_max = max(adj_point_dis_list) #所有相邻样本点距离最大值
        adj_point_v_std = np.std(adj_point_v_list)#相邻样本点速度的标准差
        adj_point_v_mean = np.mean(adj_point_v_list)#相邻样本点速度的平均值
        v_last = adj_point_v_list[-1]#轨迹最后两个相邻点的速度
        v_first = adj_point_v_list[0]#轨迹最后开始两个相邻点的速度


        # 速度差分
        diff_v_list=[]
        for i in range(0,len(adj_point_v_list)-1): 
            diff_v = adj_point_v_list[i+1]-adj_point_v_list[i]
            diff_v_list.append(diff_v)

        diff_v_std = np.std(diff_v_list)     # 一阶差分的标准差
        diff_v_max = max(diff_v_list)   # 一阶差分的最大值
        diff_v_min = min(diff_v_list)   # 一阶差分的最小值
        diff_v_mean= np.mean(diff_v_list)    # 一阶差分的平均值
        diff_v_median = np.median(diff_v_list) # 一阶差分的中值

        return adj_point_dis_max,adj_point_v_std,adj_point_v_mean,v_last,v_first,diff_v_std,diff_v_max,diff_v_min,diff_v_mean,diff_v_median

    else:
        return 0

# 相邻点角度序列
def extract_adjacent_angle(trace:np.ndarray):
    trace = sorted(trace, key=lambda point: point[2])
    trace = np.array(trace)
    if len(trace.T[0]) >=3 :
        adj_point_angle_list = []
        for i in range(1,len(trace.T[0])-1):
            a = ((trace[i+1][0]-trace[i-1][0])**2+(trace[i+1][1]-trace[i-1][1])**2)**0.5 #三角形底边
            b = ((trace[i][0]-trace[i-1][0])**2+(trace[i][1]-trace[i-1][1])**2)**0.5 #前相邻点距离
            c = ((trace[i+1][0]-trace[i][0])**2+(trace[i+1][1]-trace[i][1])**2)**0.5 #后相邻点距离

            if b*c !=0: # 去掉三点在同一位置的情况
                cos_A = (a*a-b*b-c*c)/(-2*b*c)

                if cos_A <=1 and cos_A >= -1:#由于浮点数不精确，有时Cos_A的返回值会稍稍大于1或小于-1，这里需要判断此类异常值，并修正。
                    cos_A = cos_A
                elif cos_A >=1:
                    cos_A = 1
                elif cos_A <=-1:
                    cos_A = -1

                angle_A = math.acos(cos_A)
                adj_point_angle_list.append(angle_A)
        angle_std = np.std(adj_point_angle_list)     # 角度序列的标准差
        if len(adj_point_angle_list)>=4: # adj_point_angle_list 少于4个值，偏度的返回值为 nan
            angle_pd = pd.Series(adj_point_angle_list)   
            angle_kurt = angle_pd.kurt() # 角度序列峰度
        else:
            angle_kurt = 0

        return angle_std,angle_kurt

    else:
        return 0,0

# 相邻点围成的三角形的凹凸情况
def extract_adjacent_angle_type(trace:np.ndarray):
    trace = sorted(trace, key=lambda point: point[2])
    trace = np.array(trace)
    if len(trace.T[0]) >=3 :
        adj_point_angle_list = []
        up_num = 0
        down_num = 0
        parallel_num = 0
        for i in range(1,len(trace.T[0])-1):
            k = (trace[i+1][1]-trace[i-1][1])/(trace[i+1][0]-trace[i-1][0])
            b = trace[i+1][1]-k*trace[i+1][0]
            check_y=k*(trace[i+1][0])+b
            if trace[i][1]>check_y:
                up_num += 1
            elif trace[i][1]<check_y:
                down_num +=1
            elif trace[i][1]==check_y:
                parallel_num +=1

        angle_tupe_sum=up_num+down_num+parallel_num
        if angle_tupe_sum != 0:
            return up_num/angle_tupe_sum,down_num/angle_tupe_sum,parallel_num/angle_tupe_sum
        else:
            return 0,0,0
    else:
        return 0,0,0


###### 特征提取集合 #######
def extract_feature(trace:np.ndarray):
     
    #完成验证时间
    used_t = extract_used_time(trace)

    #速度平均值
    avg_s = extract_avg_speed(trace)

    #速度最大值
    max_s = extract_max_speed(trace)

    #速度最小值
    min_s = extract_min_speed(trace)

    
    #速度变化率
    speed_change_rate = extract_speed_change_rate(trace)

    # x方向是否有重复轨迹
    #x_traceback = extract_if_x_traceback(coords_nparray)

    # y方向是否有重复轨迹
    #y_traceback = extract_if_y_traceback(coords_nparray)

    # 判断x方向重复轨迹数量
    x_traceback_num = extract_x_traceback_num(trace)

    # 判断y方向重复轨迹数量
    y_traceback_num = extract_y_traceback_num(trace)

    # 判断鼠标移动次数数量
    move_num = extract_move_num(trace)
    
    # x 方向差分
    diff_x_std,diff_x_max,diff_x_min,diff_x_skew= extract_x_diff(trace)

    # y 方向差分
    diff_y_std = extract_y_diff(trace)

    # t 方向差分
    diff_t_std,diff_t_mean = extract_t_diff(trace)

    # 相邻点的一些特征
    adj_point_dis_max,adj_point_v_std,adj_point_v_mean,v_last,v_first,diff_v_std,diff_v_max,diff_v_min,diff_v_mean,diff_v_median=extract_adjacent_point(trace)
    
    # 相邻点角度序列
    angle_std,angle_kurt=extract_adjacent_angle(trace)

    # 相邻点围成的三角形的凹凸情况
    up_num,down_num,parallel_num = extract_adjacent_angle_type(trace)


    return [avg_s,max_s,min_s,speed_change_rate,x_traceback_num,y_traceback_num,move_num,diff_x_std,diff_x_max,diff_x_min,diff_x_skew,diff_y_std,diff_t_mean,diff_t_std,adj_point_dis_max,adj_point_v_std,adj_point_v_mean,v_last,v_first,diff_v_std,diff_v_max,diff_v_min,diff_v_mean,diff_v_median,angle_std,angle_kurt,up_num,down_num,parallel_num]

def main(data_name="train_data"):
    #%% 主函数
    os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
    clean_data_S02 = csv.reader(open(r".\clean_data\clean_data_step_02.csv"))
    clean_data=[]
    test_datas =[]
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
    np_save_path = ".\clean_data\{}.npy".format(data_name)
    save_npy(np_save_path,clean_data)
    
    csv_save_path = ".\clean_data\{}.csv".format(data_name)
    header_list=["Bot","captcha_result","avg_s","max_s","min_s","speed_change_rate","x_traceback_num","y_traceback_num","move_num","diff_x_std","diff_x_max","diff_x_min","diff_x_skew","diff_y_std","diff_t_mean","diff_t_std","adj_point_dis_max","adj_point_v_std","adj_point_v_mean","v_last","v_first","diff_v_std","diff_v_max","diff_v_min","diff_v_mean","diff_v_median","angle_std","angle_kurt","up_num","down_num","parallel_num"]
    save_csv(csv_save_path,clean_data,header_list)
    
    # %%
if __name__ == '__main__':
    fire.Fire(main)