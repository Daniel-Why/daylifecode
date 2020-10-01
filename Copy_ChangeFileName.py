#批量生成复制并重命名文件
import os
import shutil
def scan_md_list(file_dir): #读取目标文件夹内所有除了 .py 文件
    aa=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] != '.py':
                aa.append(os.path.join(file))
    return aa

# filePrefix = '.md'    #文件后缀
aa = scan_md_list('.')
l = len(aa) 
for i in range(0, l):
    fname1 = aa[i].splitlines(False)
    fname = ''.join(fname1)
    org_file = fname
    fileName = fname[3:]
    shutil.copyfile(org_file,fileName)
