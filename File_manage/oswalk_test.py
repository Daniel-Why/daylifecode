import os
os.chdir('D://Personal//test//test1')
root_list = []
dir_list = []
file_list =[]
path= '.'
for root,dirs,files in os.walk(path,topdown=False):
    print(root)
    print(dirs)
    print(files)
    root_list.append(root)
    dir_list.append(dirs)
    file_list.append(files)

    #dir_path = os.path.join(root,dirs[0])
    file_path = os.path.join(root,files[0])
    #print("文件夹路径：{}".format(dir_path))
    print("文件路径：{}".format(file_path))
    break
    
    '''
    for d in dirs:
        dir_list.append(d)
    
    for f in files:
        file_list.append(f)
    '''
print("root列表：{}".format(root_list))   
print("文件夹列表：{}".format(dir_list))        
print("文件列表：{}".format(file_list))
