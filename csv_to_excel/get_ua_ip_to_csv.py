# 提取txt中的IP和ua，存入新的excel
import os
import common_use_function as cf
import csv
def tag_content(tag):#找出对应tag的行
    tag_list=cf.lines_tag_reading(csv_lines,tag)
    tag_content = tag_list[1][0].split(",",2)[-1].replace("\n","").replace('"',"")
    #print(tag_content)
    return tag_content



os.chdir(r'D:\Personal\daylifecode\csv_to_excel\ua_ip')
excel_path="ua_ip_list.csv"
file_route_list = cf.all_file_route(format='.txt')#找出所有看的csv
#cf.create_excel(excel_path)
#new_workbook,new_worksheet=cf.read_excel(excel_path)
start_row = 1
header_row = ["ua","IP"]#输入表头
#cf.write_excel(new_worksheet,excel_list=header_row,start_row = 0,start_column = 0,sort_by_column = False)
print("#####start######")
for f in file_route_list:
    input_list = []
    csv_lines = cf.read_lines(f)
    num = 1
    for org_line in csv_lines:
        tag = "#"
        line=org_line.replace("\n","")
        if tag in line:
           ua=line.split(" - ",1)[-1]
        else:
            row_list=[]
            row_list.append(ua)
            row_list.append(line)
            #cf.write_excel(new_worksheet,row_list,start_row = start_row,start_column = 0,sort_by_column = False)
            input_list.append(row_list)
            start_row += 1
            print("记录完成数：{}".format(start_row),end="\r")

with open(excel_path,"w",newline = '') as csvfile:
    header_list=["ua","ip"]
    f_csv=csv.writer(csvfile)
    f_csv.writerow(header_list)
    f_csv.writerows(input_list)
    print("######finish######")
#cf.save_excel(new_workbook,excel_path = excel_path)