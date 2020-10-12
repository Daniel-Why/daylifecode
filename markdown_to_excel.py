# 获取文件夹及子文件夹内所有 .md 文件，并根据 .md 文件段落导入 excel
import xlwt
import xlrd
from xlutils.copy import copy
import os

def create_excel(excel_path = 'new_excel.xls'):#新建excel
    if os.path.exists(excel_path) == False:
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('sheet1')
        workbook.save(excel_path)
        print('新建文件成功')
    else:
        print('文件已存在')
def read_excel(excel_path = 'new_excel.xls'):#读取 excel
    workbook = xlrd.open_workbook(r'%s'%(excel_path))
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    return new_workbook,new_worksheet

def write_excel(new_worksheet,excel_list,start_row = 0,start_column = 0,sort_by_column = True):# 写入 excel，将列表写入 excel 的一列
    for i in excel_list:
        if sort_by_column == True:
            row_position = start_row + excel_list.index(i)
            column_position = start_column
            new_worksheet.write(row_position,column_position,i)
        elif sort_by_column == False:
            row_position = start_row
            column_position = start_column + excel_list.index(i)
            new_worksheet.write(row_position,column_position,i)

def save_excel(new_workbook,excel_path = 'new_excel.xls'):# 保存 excel
    new_workbook.save(r'%s'%(excel_path))
    print('写入完成!')

def all_file_route(format = None,dir_path = '.',topdown = True): #获取文件夹内指定格式文件的路径
    file_route_list = []
    for root,dirs,files in os.walk(dir_path,topdown = topdown):
        for file in files:
            if format == None:
                f_path = os.path.join(root,file)
                file_route_list.append(f_path)
            elif format != None:
                if os.path.splitext(file)[1] == format: 
                    f_path = os.path.join(root,file)
                    file_route_list.append(f_path)
    return file_route_list

def read_lines(f_path):#读取文件所有行
    f = open(f_path, "r+",encoding='UTF-8')
    lines = f.readlines()
    f.close()
    return lines

def lines_tag_reading(lines,tag):#读取列表含有特定字符的行，并生成位置列表和行列表
    tag_index_list = []
    tag_list = []
    for i in lines:
        if tag in i:
            l_t = lines.index(i)
            tag_index_list.append(l_t)
            tag_list.append(i)
    return tag_index_list,tag_list

def lines_between_tag_reading(lines,tag_index_list):#读取列表指定行之间的内容，并生成列表
    t_pointer = 0
    between_tag_text_list = []
    for a in tag_index_list:
        if t_pointer <= len(tag_index_list)-2:
            l_s = tag_index_list[t_pointer]
            l_e = tag_index_list[t_pointer+1]
        elif t_pointer == len(tag_index_list)-1:
            l_s = tag_index_list[t_pointer]
            l_e = None
        text_list = []
        for i in lines[l_s+1:l_e]:
            text_list.append(i)
        md_text = ''.join(text_list)
        #print(md_text)
        between_tag_text_list.append(md_text)
        t_pointer += 1
    return between_tag_text_list

#def main():
#    os.chdir('D://Personal//test//test2')
#    file_route_list = all_file_route(format='.md')
#    #print(file_route_list)
#    n = 0
#    create_excel()
#    new_workbook,new_worksheet = read_excel()
#    for i in file_route_list:
#        print(n+1)
#        lines = read_lines(i)
#        tool_name = lines[0]
#        tag_index_list,tag_list =lines_tag_reading(lines,tag='#')
#        #print(tag_index_list)
#        #print(tag_list)
#        #tag_list.insert(0,'###toolname')
#        between_tag_text_list = lines_between_tag_reading(lines,tag_index_list)
#        between_tag_text_list.insert(0,tool_name)
#        write_excel(new_worksheet,tag_list,sort_by_column=True)
#        write_excel(new_worksheet,between_tag_text_list,start_row=n+1,start_column=0,sort_by_column=True)
#        n += 1
#    save_excel(new_workbook)

def main():
    os.chdir('D://Personal//test//test2')
    file_route_list = all_file_route(format='.md')
    #print(file_route_list)
    create_excel()
    new_workbook,new_worksheet = read_excel()
    lines = read_lines("tool_list.md")
    tag_index_list,tag_list =lines_tag_reading(lines,tag='#')
    write_excel(new_worksheet,tag_list,sort_by_column=True)
    save_excel(new_workbook)
main()

