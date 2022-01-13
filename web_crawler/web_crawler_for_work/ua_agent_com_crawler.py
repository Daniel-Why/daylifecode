from typing import ItemsView
from bs4 import BeautifulSoup
import requests
import csv
import re,random,time

def str_switch(target_name):
    if re.search(" ",target_name):
        para = target_name.replace(" ","-")
        return para.lower()
    else:
        return target_name.lower()

def crawler_web(target_name):
    para =  str_switch(target_name)
    url = "https://user-agents.net/browsers/"+para
    print(url)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0","Referer":"https://user-agents.net/browsers"}
    r = requests.get(url,headers=headers)
    demo = r.text

    soup = BeautifulSoup(demo,"lxml")
    content = soup.find("ul",class_="agents_list").find_all("a")
    print(type(content))
    form = []
    for i in content:
        item = i.text
        form.append(item)
        csv_titles=[target_name]
        file_path="./web_crawler_for_work/ua_list/UA_list_brower/"+target_name+".csv"
        with open(file_path,"w") as f:
            f_csv=csv.writer(f)
            f_csv.writerow(csv_titles)
            f_csv.writerows(form)


def main():
    list = open("./web_crawler_for_work/ua_list/UA_list_brower/browser_list.txt",mode="r")
    finish= open("./web_crawler_for_work/ua_list/UA_list_brower/finish.txt",mode="r+")
    finish.seek(0,2)
    count=len(list.readlines())
    list.seek(0,0)
    print("start") 
    for i in range(count):
        orgin_name=list.readline()
        target_name = orgin_name.replace("\n","")
        print(target_name)
        crawler_web(target_name)
        print("-----"+ str(i) + ": "+ target_name +" done"+"-------")
        finish.write(str(i) + ": "+ target_name +" done\n")
        time.sleep(random.randint(3,15))
         
    list.close()
    finish.close()

main()