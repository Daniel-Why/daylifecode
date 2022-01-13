# 爬取 udger.com 中的表格

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re,random,time

def replace_space(bot_name):
    if re.search(" ",bot_name):
        para = bot_name.replace(" ","%20")
        return para
    else:
        return bot_name

def crawler_web(bot_name):
    para =  replace_space(bot_name)
    url = "https://udger.com/resources/ua-list/bot-detail?bot="+para
    print(url)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    r = requests.get(url,headers=headers)
    demo = r.text

    soup = BeautifulSoup(demo,"lxml")

    table =soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    file_path="./web_crawler_for_work/ua_list/UA_list_crawlers/"+bot_name+".csv"
    df.to_csv(file_path,header=["type","content"],index=True)

def main():
    list = open("./web_crawler_for_work/ua_list/UA_list_crawlers/bot_list.txt",mode="r")
    finish= open("./web_crawler_for_work/ua_list/UA_list_crawlers/finish.txt",mode="r+")
    finish.seek(0,2)
    count=len(list.readlines())
    list.seek(0,0)
    print("start") 
    for i in range(count):
        orgin_name=list.readline()
        bot_name = orgin_name.replace("\n","")
        print(bot_name)
        crawler_web(bot_name)
        print("-----"+ str(i+403) + ": "+ bot_name +" done"+"-------")
        finish.write(str(i+403) + ": "+ bot_name +" done\n")
        time.sleep(random.randint(1,10))
         
    list.close()
    finish.close()

main()