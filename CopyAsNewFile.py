#批量生成复制并重命名文件
import os
import shutil
aa = []
with open("filename.txt", "r", encoding='UTF-8') as f:
    for line in f.readlines():
        aa.append(line)
print(aa)

fileSuffix = '.md'    #文件后缀
l = len(aa) 
for i in range(0, l):
    org_file = 'test.md'
    fname1 = aa[i].splitlines(False)
    fname = ''.join(fname1)
    fileName = fname + fileSuffix
    shutil.copyfile(org_file,fileName)

