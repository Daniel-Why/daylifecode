# 获取文件夹及子文件夹内所有 .md 文件，并根据 .md 文件段落导入 excel,需要md 内容大纲都相同。按一列条目一列条目写入
import xlwt
import xlrd
from xlutils.copy import copy
import os
import common_use_function as cf
def main():
    os.chdir('D://YZYImage_full//md//operating_systems')
    file_route_list = cf.all_file_route(format='.md')
    tool_name_list = []
    orgin_tag_list = []
    for i in file_route_list:
        lines = cf.read_lines(i)
        lines.pop()
        tag = "#"
        tag_index_list,tag_list =cf.lines_tag_reading(lines,tag=tag)
        tool_name_list.append(tag_list[0])
        for a in tag_list[1:]:
            if a not in orgin_tag_list:
                orgin_tag_list.append(a)
    print(len(orgin_tag_list))
    print(orgin_tag_list)
    n = 0
    cf.create_excel()
    new_workbook,new_worksheet = cf.read_excel()
    cf.write_excel(new_worksheet,orgin_tag_list,start_row=0,start_column=1,sort_by_column=False)
    cf.write_excel(new_worksheet,tool_name_list,start_row=1,start_column=0,sort_by_column=True)
    for m in orgin_tag_list:
        tag_content_list = []
        n_f = 0
        for i in file_route_list:
            lines = cf.read_lines(i)
            lines.pop()
            tool_name = lines[0]
            if m in lines:
                m_pointer = lines.index(m)
                m_pointer = m_pointer+1
                m_son_list = [] 
                while tag not in lines[m_pointer] and m_pointer < len(lines):
                    m_son_list.append(lines[m_pointer])
                    m_pointer = m_pointer + 1
                    if m_pointer >= len(lines):
                        break
                m_son_text = ''.join(m_son_list)
                tag_content_list.append(m_son_text)
            elif m not in lines:
                tag_content_list.append(" ")
            n_f = n_f + 0
        # print(tag_content_list)
        cf.write_excel(new_worksheet,tag_content_list,start_row=1,start_column=n+1,sort_by_column=True)       
        print("\r —————— 已完成条目数：{}。————————".format(n+1),end='')
        n += 1
    cf.save_excel(new_workbook)
main()