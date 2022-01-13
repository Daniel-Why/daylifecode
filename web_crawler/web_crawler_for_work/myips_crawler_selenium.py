import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re,random,time

def chrome_options():
    chrome_options = webdriver.ChromeOptions()#headless模式
    #chrome_options.add_argument(r"--user-data-dir=C:\Users\Daniel.Why\AppData\Local\Google\Chrome\User Data\Default")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--proxy-server=http://121.43.190.89:3128")
    return chrome_options

def openbrowser(chrome_options):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    mainUrl = "https://myip.ms/"
    browser.get(mainUrl)
    time.sleep(random.randint(2,5))
    #browser.find_element_by_link_text("Browsers").click()
    #time.sleep(random.randint(2,5))
    return browser

def save_to_csv(content,target_name):
    form = ["------"]
    for i in content:
        item = i.text
        form.append(item)
        #print(i)
    #print(form)
    file_path="./web_crawler_for_work/proxy_ip/myips/"+target_name+".csv"
    csv_title = [target_name]
    xml_df = pd.DataFrame(columns=csv_title,data=form)
    xml_df.to_csv(file_path,index=True)

def getinfo(browser,target_name):
    #browser.find_element_by_link_text(target_name).click()
    soup = bs(browser.page_source,"lxml")
    print(soup)
    content = soup.find("ul",class_="agents_list").find_all("a")
    save_to_csv(content,target_name)
    time.sleep(random.randint(4,15))
    browser.back()
    time.sleep(random.randint(2,5))


def main():
    #list = open("./web_crawler_for_work/ua_list/user_agent_com/user_agent_browser/list.txt",mode="r")
    finish= open("./web_crawler_for_work/proxy_ip/myips/finish.txt",mode="r+")
    finish.seek(0,2)
    #count=len(list.readlines())
    #list.seek(0,0)
    print("start") 
    browser = openbrowser(chrome_options())
    for i in range(1):
        target_name = str(i)
        print(target_name)
        getinfo(browser,target_name)
        print("-----"+ str(i+58) + ": "+ target_name +" done"+"-------")
        finish.write(str(i+58) + ": "+ target_name +" done\n")         
    #list.close()
    finish.close()
    browser.quit()

main()