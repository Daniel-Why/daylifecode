#批量生成复制并重命名文件
import os
import shutil
def scan_file_list(file_dir): #读取目标文件夹内所有除了 .py 文件
    aa=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.LRF':
                aa.append(os.path.join(file))
    return aa

# filePrefix = '.md'    #文件后缀
os.chdir('C://Users//D2010//Desktop//tmp')

aa = scan_file_list('.')

l = len(aa) 
for i in range(0, l):
    fname1 = aa[i].splitlines(False)
    fname = ''.join(fname1)
    org_file = fname
    fileName = fname[:-3]+'mp4'
    shutil.copyfile(org_file,fileName)
