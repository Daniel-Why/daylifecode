#数据清洗+特征识别，生成npy和csv文件
import os,time
os.chdir("D:\Personal\daylifecode\machine_Learning\mouse_tracker_slide_captcha")
os.system("python clean_data_step_01.py")
print("step 01 finished!")
time.sleep(0.5)
os.system("python clean_data_step_02.py")
print("step 02 finished!")
time.sleep(0.5)
os.system("python extract_feature.py")
print("extract_feature finished!")

