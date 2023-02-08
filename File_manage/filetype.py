#查看文件夹内所有文件类型
import os
def scan_file_list(file_dir): #读取目标文件夹内所有文件
    aa=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_type= os.path.splitext(file)[1]
            if file_type not in aa:
                aa.append(file_type)
    return aa
def main():
    os.chdir(r'E:\personal\daliy_code\temp\file_updat_check\test_file')
    aa = scan_file_list(".")
    print(aa)

main()