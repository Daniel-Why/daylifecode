#查询文件夹名称及大小，并存入excel
import xlwt
import xlrd
from xlutils.copy import copy
import os
def folder_name_size(origin_path):
    folder_list=os.listdir(origin_path)
    print("文件列表：{}".format(folder_list))
    folder_size = []
    for i in folder_list:
        new_path = '{0}\\{1}\\zip'.format(origin_path,i)
        new_file_list=os.listdir(new_path)
        print(new_file_list)
        i_size = 0
        file_size = []
        for n in new_file_list:
            file_path = '{0}\\{1}'.format(new_path,n)
            n_size = int(os.path.getsize(file_path))
            file_size.append(n_size)
            print(file_size)
        for l in range(0,len(file_size)):
            i_size = i_size + file_size[l]
        folder_size.append(i_size) 
    print("文件大小：{}".format(folder_size))
    return folder_list,folder_size
def create_excel():#新建excel
    if os.path.exists('tool_info.xls') == False:
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('tool_info')
        worksheet.write(0,1,'tool_size')
        worksheet.write(0,0,'tool_name')
        workbook.save('tool_info.xls')
        print('新建文件成功')
    else:
        print('文件已存在')
def write_excel_from_list(column_1_list,column_2_list,excel_path = 'tool_info.xls'):#插入excel
    workbook = xlrd.open_workbook(r'%s'%(excel_path))
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    #获取list长度
    l_1 = len(column_1_list)
    l_2 = len(column_2_list)
    #写入数据
    for i in range(0,l_1):
        list_text = column_1_list[i]
        new_worksheet.write(i+1,0,list_text)
    for i in range(0,l_2):
        list_text = column_2_list[i]
        new_worksheet.write(i+1,1,list_text)    
    # 保存
    new_workbook.save(r'%s'%(excel_path))
    print('写入完成!')
def main():
    origin_path = 'D://YZYTool//fixed1'
    os.chdir(origin_path)
    folder_list,folder_size = folder_name_size(origin_path)
    create_excel()
    write_excel_from_list(column_1_list=folder_list,column_2_list = folder_size)

main()
