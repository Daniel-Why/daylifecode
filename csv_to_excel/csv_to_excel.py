# 提取csv中的部分表格，存入新的excel
import os
import common_use_function as cf

def tag_content(tag):#找出对应tag的行
    tag_list=cf.lines_tag_reading(csv_lines,tag)
    tag_content = tag_list[1][0].split(",",2)[-1].replace("\n","").replace('"',"")
    print(tag_content)
    return tag_content


os.chdir('D:\Personal\daylifecode\csv_to_excel')
excel_path = "ua2_list.xls"
file_route_list = cf.all_file_route(format='.csv')
cf.create_excel(excel_path)
new_workbook,new_worksheet=cf.read_excel(excel_path)
start_row = 1
num = 1
header_row = ["Bot","厂商","厂商","url","分类","a"]
cf.write_excel(new_worksheet,excel_list=header_row,start_row = start_row,start_column = 0,sort_by_column = False)
print("#####start######")
for f in file_route_list:
    csv_lines = cf.read_lines(f)
    file_name=f.split("\\")[-1].split(".")[0]

    print("#####{}.{}#####".format(num,file_name))

    pr_detail=tag_content("Producer")
    url_detail=tag_content("Bot URL")
    category_detail=tag_content("Category")
    ua_index_list,ua_list=cf.lines_tag_reading(csv_lines,"Useragentstring")#找出"Useragentstring"
    num_2 = 1
    for i in ua_list:
        row_list=[]
        row_list.append(file_name)
        row_list.append(pr_detail)
        row_list.append(url_detail)
        row_list.append(category_detail)
        ua_detail=(i.split(",",2)[-1])
        row_list.append(ua_detail.replace("\n","").replace('"',""))
        cf.write_excel(new_worksheet,excel_list=row_list,start_row = start_row,start_column = 0,sort_by_column = False)
        start_row += 1
        print("完成数：{}".format(num_2),end="\r")
        num_2 += 1
    
    num += 1

cf.save_excel(new_workbook,excel_path = excel_path)