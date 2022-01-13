import requests
#from fake_useragent import UserAgent
url = "http://10.10.10.31/"
#ua = UserAgent(use_cache_server=False)
#ua = UserAgent()
#print(ua.ie)
headers = {
    'User-Agent':"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
}
strhtml = requests.get(url,headers=headers)
print(strhtml.status_code)
print(strhtml.text)