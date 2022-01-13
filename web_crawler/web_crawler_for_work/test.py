from bs4 import BeautifulSoup as bs
import requests
import csv
import re,random,time
from fake_useragent import UserAgent
import time

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
    #ref='https://user-agents.net/browsers'
    #ip_list = getProxyList()
    ip_list=["http://58.20.235.180:9091","http://223.96.90.216:8085","http://120.79.163.155:808","http://39.104.177.233:9080","http://221.4.245.242:9091","http://122.9.101.6:8888","http://112.13.183.101:9091","http://1.117.100.196:7788","http://27.42.168.46:55481","http://113.120.60.241:43136","http://223.96.90.216:8085","http://223.96.90.216:8085","http://36.134.91.82:8888","http://124.204.33.162:8000","http://219.143.207.45:800","http://106.15.193.237:8088","http://218.59.193.14:38640","http://219.143.207.45:800","http://221.4.241.198:9091","http://106.12.80.219:8080","http://114.104.139.30:9005"]
    params = dict(
        headers = {'User-Agent': ua.random},
        proxies = {'http': random.choice(ip_list)}
    )
    return params


###############################################




def crawler_web(target_name):
    url = "https://dinasouregg.xyz/"
    print(url)
    params = getParams()
    time.sleep(1)
    soup = getSoup(url,**params)
    print(soup)



def main():
    crawler_web("")
main()