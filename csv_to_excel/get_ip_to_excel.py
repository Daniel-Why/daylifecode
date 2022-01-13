# 提取csv中的部分IP，存入新的excel
import os
import common_use_function as cf
import re
def tag_content(tag):#找出对应tag的行
    tag_list=cf.lines_tag_reading(csv_lines,tag)
    tag_content = tag_list[1][0].split(",",2)[-1].replace("\n","").replace('"',"")
    #print(tag_content)
    return tag_content


def re_filter(org_text):#提取org_text中的IP
    re_patten=r'((\d{1,3}\.){3}(\d{1,6})(.(\d{1,3}\.){1,3}(\d{1,3}))?)'
    it=re.finditer(re_patten,org_text)
    finished_list=[]
    for match in it: 
        get_ip=match.group()
        if len(get_ip)>15:#原数据中有同样的IP重复粘连两次的显现，这里需要去重
            get_ip=get_ip[:(int(len(get_ip)/2))]
        else:
            pass
        finished_list.append(get_ip)
    #print(finished_list)
    return(finished_list)



os.chdir('D:\Personal\daylifecode\csv_to_excel')
excel_path="ip_list.xls"
file_route_list = cf.all_file_route(format='.csv')#找出所有看的csv
cf.create_excel(excel_path)
new_workbook,new_worksheet=cf.read_excel(excel_path)
start_row = 1
num = 1
header_row = ["Bot 名称","IP"]#输入表头
cf.write_excel(new_worksheet,excel_list=header_row,start_row = 0,start_column = 0,sort_by_column = False)
print("#####start######")
for f in file_route_list:
    print(f)
    csv_lines = cf.read_lines(f)
    file_name=f.split("\\")[-1].split(".")[0]

    print("#####{}.{}#####".format(num,file_name))

    ip_index_list,ip_list=cf.lines_tag_reading(csv_lines,"Walk from")#找出"Useragentstring"
    num_2 = 1
    for i in ip_list:
        ip_detail=(i.split(",",2)[-1])
        #print(ip_detail)
        get_ip_list = re_filter(ip_detail)
        for ip in get_ip_list:
            row_list=[]
            row_list.append(file_name)
            row_list.append(ip)
            cf.write_excel(new_worksheet,row_list,start_row = start_row,start_column = 0,sort_by_column = False)
            start_row += 1
        print("完成数：{}".format(num_2),end="\r")
        num_2 += 1
    
    num += 1

cf.save_excel(new_workbook,excel_path = excel_path)