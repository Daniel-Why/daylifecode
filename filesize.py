#获取文件夹内所有文件的大小，并导入excel
import common_use_function as cf
import os
def main():
    os.chdir('D://YZYTool//fixed1//swfdecompiler')
    file_route_list = cf.all_file_route()
    #print(file_route_list)
    n = 0
    cf.create_excel()
    new_workbook,new_worksheet = cf.read_excel()
    for i in file_route_list:
        print(n+1)
        file_size_list = []
        file_size = os.path.getsize(i)
        file_size_list.append(i)
        file_size_list.append(file_size)
        cf.write_excel(new_worksheet,file_size_list,start_row=n+1,start_column=0,sort_by_column=False)
        n += 1
    cf.save_excel(new_workbook)

main()