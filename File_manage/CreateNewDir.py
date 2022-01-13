#批量生成 filename 中的文件
import os
os.chdir('C://Users//Daniel.Why//Desktop//temp//2020-10-17')
aa = []
with open("filename.txt", "r", encoding='UTF-8') as f:
    for line in f.readlines():
        aa.append(line)
print(aa)

l = len(aa) 
for i in range(0, l):
    fname1 = aa[i].splitlines(False)
    fname = ''.join(fname1)
    fileName = fname
    pic = '{}\\pic'.format(fileName)
    os.mkdir(fileName)
    os.mkdir(pic)
