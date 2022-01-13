from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re,random,time
from fake_useragent import UserAgent

def getSoup(url,encoding="gb2312",**params):
    #print(params)
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
    proxies_url_before = "http://www.66ip.cn/areaindex_3/{}.html"
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
    ref='https://myip.ms/browse/blacklist/Blacklist_IP_Blacklist_IP_Addresses_Live_Database_Real-time'
    ip_list = getProxyList()
    ip_list=["http://58.20.235.180:9091","http://223.96.90.216:8085","http://120.79.163.155:808","http://39.104.177.233:9080","http://221.4.245.242:9091","http://122.9.101.6:8888","http://112.13.183.101:9091","http://1.117.100.196:7788","http://27.42.168.46:55481","http://113.120.60.241:43136","http://223.96.90.216:8085","http://223.96.90.216:8085","http://36.134.91.82:8888","http://124.204.33.162:8000","http://219.143.207.45:800","http://106.15.193.237:8088","http://218.59.193.14:38640","http://219.143.207.45:800","http://221.4.241.198:9091","http://106.12.80.219:8080","http://114.104.139.30:9005"]
    #print(ip_list)
    #ip_list=["http://221.238.207.34:8000"]
    params = dict(
        headers = {'User-Agent': ua.random,"referer":ref},
        proxies = {'http': random.choice(ip_list)}
    )
    print(params["proxies"])
    return params


###############################################


def str_switch(target_name):
    if re.search(" ",target_name):
        para = target_name.replace(" ","-")
        return para.lower()
    else:
        return target_name.lower()

def get_and_save(target_name,url):
    params = getParams()
    soup = getSoup(url,**params)
    print(soup)
    table =soup.find_all('table')#[17]
    print(table)
    df = pd.read_html(str(table))[0]
    file_path="./web_crawler_for_work/proxy_ip/myips/"+target_name+".csv"
    df.to_csv(file_path,index=True)

def crawler_web(target_name):
    #para =  str_switch(target_name)
    url = "https://myip.ms/browse/blacklist/{}/usrs/1".format(target_name)
    print(url)
    try:
        get_and_save(target_name,url)
    except:
        retry_result =""
        print("retry")
        retry_num = 1
        while retry_result != "done" and retry_num != 6:
            try:
                print("!!!!! retry:{} !!!!!!".format(str(retry_num)))
                get_and_save(target_name,url)            
            except:
                retry_num = retry_num + 1
                print("retry error-----")
                retry_result = "error"
            else:
                retry_result = "done" 
        return retry_result
    else:
        print("-----{}:done-----".format(target_name))
        return "done"

def main():
    print("start") 
    for i in range(1,2):
        finish= open("./web_crawler_for_work/proxy_ip/myips/finish.txt",mode="r+")
        finish.seek(0,2)
        target_name = str(i)
        print("#####{}:start#####".format(target_name))
        crawler_result = crawler_web(target_name)
        if crawler_result == "done":
            finish.write(str(i) + ": done\n")
            print("-----{}:done-----".format(target_name))  
        else: 
            finish.write(str(i) + ": error\n")
            print("-----{}:error-----".format(target_name))
        time.sleep(random.randint(1,5))
        finish.close()

main()