#批量生成 filename 中的文件
import os
aa = []
with open("filename.txt", "r", encoding='UTF-8') as f:
    for line in f.readlines():
        aa.append(line)
print(aa)

fileSuffix = '.md'    #文件后缀
l = len(aa) 
for i in range(0, l):
    fname1 = aa[i].splitlines(False)
    fname = ''.join(fname1)
    fileName = fname + fileSuffix
    fl= open(fileName,"w")
    fl.close()
