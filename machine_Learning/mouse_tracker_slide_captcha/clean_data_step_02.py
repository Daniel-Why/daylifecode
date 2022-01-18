#%%
#删除点击拖动快，开始滑动之前的数据
import os
import csv

os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
clean_data_S01 = csv.reader(open(r".\clean_data\clean_data_step_01.csv"))
clean_data=[]
for i,data_row in enumerate(clean_data_S01):
    if i != 0:
        info_data = data_row[:3]
        mouse_data = data_row[3:]

        #删除点击拖动快，开始滑动之前的数据
        for data in mouse_data[:]:
            data_to_list=data.split(",")
            #print(data)
            click_bar=(int(data_to_list[0]) >= 8 and int(data_to_list[0])<=50 and int(data_to_list[1]) >= 505 and int(data_to_list[1]) <=550)#鼠标位置是否在拖动快处
            if click_bar == False:
                mouse_data.remove(data)
            elif click_bar == True:
                break
        info_data.extend(mouse_data)
        clean_data.append(info_data)
#%%
excel_path = ".\clean_data\clean_data_step_02.csv"

with open(excel_path,"w",newline = '') as csvfile:
    header_list=["Bot","captcha_result","check_time","mouse track"]
    f_csv=csv.writer(csvfile)
    f_csv.writerow(header_list)
    f_csv.writerows(clean_data)
    print("######finish######")
            
        



#%%