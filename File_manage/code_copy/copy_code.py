## 遍历文档中的代码，并粘贴到一个文档中，用于软件著作权申请等等相关场景
import os
os.chdir(".\shooting")
file_path_list = []
path= '.'
file_count = 0
import os
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        filepath = os.path.join(root, name)
        file_path_list.append(filepath)
        file_count += 1
print(file_count)
#print(file_path_list)

newfile_path = "../code.txt"
nf = open(newfile_path,"w",encoding='utf-8')
count = 0

for n in file_path_list:
    try:
        of = open(n,"r",encoding='utf-8')
        for i in of.readlines():
            nf.write(i)
        of.close()
        count +=1
        print("{}.{} 完成！".format(count,n))
    except:
        count +=1
        print("{}.{} 失败！".format(count,n))
        continue
    else:
        continue

nf.close()



