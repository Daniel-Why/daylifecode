# 爬取本地 html 数据
from bs4 import BeautifulSoup
import re
path = r"script/data1.html"
htmlfile = open(path,"r",encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle,"lxml")
result=soup.find_all("span",class_="mat-checkbox-label")
result_list = []
for i in result:
    item = str(i.text)
    new_item=item.replace("\n","").replace("\xa0",",")
    result_list.append(new_item)

print(result_list)
with open("result.md","w",encoding="utf-8") as f:
    for n in result_list:
        f.write(n)
f.close()
    