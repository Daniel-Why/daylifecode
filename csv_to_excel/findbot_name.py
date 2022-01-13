# 提取UA中关于Bot的字段
import re
import csv
import os

def re_filter(org_text):#提取org_text中的IP
    re_patten=r'[\S]*((S|s)pider|(B|b)ot)[^(\s\/)]*'
    it=re.finditer(re_patten,org_text)
    finished_list=[]
    for match in it:
        get_name=match.group()
        finished_list.append(get_name)
    if finished_list == []:
        finished_list.append("zzzzzzz")
    return finished_list

def split_blank(org_text):
    split_result = []
    split_result.append(org_text.split(" ",1)[0])

    return split_result

os.chdir(r'D:\Personal\daylifecode\csv_to_excel\ua_ip')
excel_path="new.csv"
row_list=[]
count = 0
with open("UA_name_org.csv") as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    for row in f_csv:
        org_text=row[0]
        #bot_tag=re_filter(org_text)
        bot_tag=split_blank(org_text)
        #print(bot_tag)
        new_row = []
        new_row.extend(row)
        new_row.extend(bot_tag)
        
        #print(new_row)
        row_list.append(new_row)
        count += 1
        print("记录完成数：{}".format(count),end="\r")

with open(excel_path,"w",newline = '') as csvfile:
    header_list=["ua","ip","Bot name"]
    f_csv=csv.writer(csvfile)
    f_csv.writerow(header_list)
    f_csv.writerows(row_list)
    print("######finish######")