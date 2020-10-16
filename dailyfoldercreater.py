import os #每天生成一个以日期命名的文件夹，并将之前的空文件夹删除。
import datetime
os.chdir('C:\\Users\\Daniel.Why\\Desktop\\temp')
f_path = '.'
today = datetime.date.today()
print("today is %s"%(today))
newfileName = str(today)
newfilePath = '{0}\\{1}'.format(f_path,newfileName)
folder_list=os.listdir(f_path)
print(folder_list)
for i in folder_list:
    try:
        if not os.listdir(i):# 非空为真，如果不为空则...
            print('{} 是一个空文件夹'.format(i))
            os.removedirs(i)
            print('{} 已删除'.format(i))
    except:
        pass
new_folder_list=os.listdir(f_path)
if newfileName in new_folder_list:
    print('{} folder is already exist!'.format(newfileName))
else:
    os.mkdir(newfilePath)

