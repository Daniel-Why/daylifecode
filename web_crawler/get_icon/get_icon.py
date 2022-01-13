from bs4 import BeautifulSoup as bs
import requests
import csv
import os
import re,random,time
from fake_useragent import UserAgent
from multiprocessing import Process, Queue
import os, time, random


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
def url_clean(url):
    tag_index=url.find("/",8)
    if tag_index != -1:
        cleaned_url = url[:tag_index]
    else:
        cleaned_url = url
    return cleaned_url

def str_switch(url,suffix):
    new_url = url + "/" + suffix
    return new_url


def crawler_web(bot_name,org_url):
    #url = "https://www.baidu.com/3favicon.ico"#"https://user-agents.net/browsers/"+para
    cleaned_url = url_clean(org_url)
    suffix_list = ["favicon.ico","favicon.png","favicon.jpg","favicon.jpeg"]
    for suffix in suffix_list:
        url= str_switch(cleaned_url,suffix)
        print(url)
        #params = getParams()
        #response = requests.get(url,allow_redirects=False,**params)
        try:
            response = requests.get(url)
        except:
            #if suffix != suffix_list[-1]:
            print("connect error")
            continue
        else:
            img = response.content
            if b"html" in img[:300] or response.status_code==404 or img == b'':
                print("type error")
                continue
            else:
                file_path = "./"+ bot_name+".png"
                with open( file_path,'wb' ) as f:
                    f.write(img)
                return file_path

def get_image(row,f_csv):
    row_list = []
    new_row = []
    bot_name = row[0]
    org_url = row[1]
    file_path = crawler_web(bot_name,org_url)
    new_row.extend(row)
    new_row.append(file_path)
    row_list.append(new_row)
    f_csv.writerows(row_list)
    return new_row

def SaveAsCsv(file_path,title_list,row_list):
    with open(file_path,"w",encoding='utf-8') as nf:
        nf_csv=csv.writer(nf)
        nf_csv.writerow(title_list)
        nf_csv.writerows(row_list)

def main():
    os.chdir("D:\Personal\daylifecode\web_crawler\get_icon\pic")
    new_row_list=[]
    n = 0

    new_file_path = "newPic.csv"
    title_list = ["bot name","url","file path"]
    with open(new_file_path,"w",encoding='utf-8') as nf:    
        nf_csv=csv.writer(nf)
        nf_csv.writerow(title_list)

        with open("pic.csv","r",encoding="UTF-8") as f:
            reader = csv.reader(f)
            for row in reader:
                new_row = get_image(row,nf_csv)
                new_row_list.append(new_row)
                n += 1
                print(n)
    #new_file_path = "newPic.csv"
    #title_list = ["bot name","url","file path"]
    #SaveAsCsv(new_file_path,title_list,new_row_list)
    print("done!")



    
if __name__ == "__main__":
    main()