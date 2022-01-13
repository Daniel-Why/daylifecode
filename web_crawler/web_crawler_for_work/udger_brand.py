# 爬取 udger.com 中的表格

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re,random,time
from fake_useragent import UserAgent

def getSoup(url,encoding="utf-8",**params):
    print(params)
    reponse = requests.get(url,**params)
    reponse.encoding = encoding
    soup = bs(reponse.text,'lxml')
    return soup

def cssFind(movie,cssSelector,nth=1):
    if len(movie.select(cssSelector)) >= nth:
        return movie.select(cssSelector)[nth-1].text.strip()
    else:
        return ''

def getProxyList():
    proxies_url_before = "http://www.66ip.cn/areaindex_2/{}.html"
    proxies_url = proxies_url_before.format(random.randint(1,8))
    soup = getSoup(proxies_url)
    item_list = soup.select("table tr")[2:]
    proxies_list = []
    for item in item_list:
        ipAddress = cssFind(item, "td")
        ipPort = cssFind(item, "td", 2)
        proxies_list.append("http://{}:{}".format(ipAddress, ipPort))
    return proxies_list

def getParams():
    ua = UserAgent()
    ref='https://udger.com/resources/ua-list/devices-brand'
    ip_list = getProxyList()
    params = dict(
        #headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"},
        headers = {"User-Agent":ua.random,"referer":ref},
        proxies = {'http': random.choice(ip_list)}
    )
    return params


###############################################


def str_switch(target_name):
    if re.search(" ",target_name):
        para = target_name.replace(" ","_")
        return para.lower()
    else:
        return target_name.lower()

def crawler_web(target_name):
    para =  str_switch(target_name)
    url = "https://udger.com/resources/ua-list/devices-brand-detail?brand="+para
    print(url)
    params = getParams()
    soup = getSoup(url,**params)
    try:
        table =soup.find_all('table')[0]
        df = pd.read_html(str(table))[0]
        file_path="./web_crawler_for_work/ua_list/UA_list_brand/"+target_name+".csv"
        df.to_csv(file_path,header=["type","content"],index=True)
        return "done"
    except:
        return "error"


def main():
    list = open("./web_crawler_for_work/ua_list/UA_list_brand/list.txt",mode="r")
    finish= open("./web_crawler_for_work/ua_list/UA_list_brand/finish.txt",mode="r+")
    finish.seek(0,2)
    count=len(list.readlines())
    list.seek(0,0)
    print("-------start---------") 
    for i in range(count):
        orgin_name=list.readline()
        target_name = orgin_name.replace("\n","")
        print(target_name)
        crawler_result = crawler_web(target_name)
        if crawler_result == "done":
            print("-----"+ str(i+133) + ": "+ target_name +" done"+"-------")
            finish.write(str(i+133) + ": "+ target_name +" done\n")
        else: 
            print("-----"+ str(i+133) + ": "+ target_name +" error"+"-------")
            finish.write(str(i+133) + ": "+ target_name +" error\n")

        time.sleep(random.randint(3,10))
         
    list.close()
    finish.close()

main()