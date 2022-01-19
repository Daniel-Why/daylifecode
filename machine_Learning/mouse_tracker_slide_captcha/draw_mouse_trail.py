
#%%
import csv
from os import name
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd

def mouseData_to_nparry(mouse_data):#将数据转换为 int
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
    #plt.savefig(str(n)+".png")
#%%
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
clean_data_S01 = csv.reader(open(r".\clean_data\clean_data_step_02.csv"))
n=1
for i,rows in enumerate(clean_data_S01):
    if i != 0:
        mouse_data = rows
        print(n)
        if rows[0] == "1":
            #print("Bot")
            continue
        elif rows[0] == "0":
            print("Human")
            #continue
        coords_nparry = mouseData_to_nparry(mouse_data)
        draw_mouse_trail(coords_nparry)
        n +=1
# %%
