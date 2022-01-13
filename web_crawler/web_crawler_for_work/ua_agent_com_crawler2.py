from bs4 import BeautifulSoup as bs
import requests
import csv
import re,random,time
from fake_useragent import UserAgent

def getSoup(url,encoding="utf-8",**params):
    print(params)
    reponse = requests.get(url,allow_redirects=False,**params)
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
    ref='https://user-agents.net/browsers'
    ip_list = getProxyList()
    params = dict(
        headers = {'User-Agent': ua.random,"referer":ref},
        proxies = {'http': random.choice(ip_list)}
    )
    return params


###############################################


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
    params = getParams()
    soup = getSoup(url,**params)
    print(soup)

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