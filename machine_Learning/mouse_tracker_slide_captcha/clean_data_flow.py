#数据清洗+特征识别，生成npy和csv文件
import os,time
data_type=int(input("生成训练集（1）还是测试集（2）:"))
if data_type == 1:
    data_type = "train"
    data_name = "train_data"
elif data_type == 2:
    data_type = "test"
    data_name = "test_data"
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
os.system("python clean_data_step_01.py {}".format(data_type))
print("step 01 finished!")
time.sleep(0.5)
os.system("python clean_data_step_02.py")
print("step 02 finished!")
time.sleep(0.5)
os.system("python extract_feature.py {}".format(data_name))
print("{} extract_feature finished!".format(data_name))

