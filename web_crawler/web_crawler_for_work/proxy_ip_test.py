from multiprocessing.dummy import Pool as ThreadPool
import requests
def test_proxy_ip1(https, address):
    test_urld = 'http://api.ipify.org/'
    test_urls = 'https://api.ipify.org/'
    proxies = {https: address, }
    if https == 'http':
        test_url = test_urld
    elif https == 'https':
        test_url = test_urls
    else:
        return ''
    url = ''
    try:
        res = requests.get(url=test_url, proxies=proxies, timeout=8)
        if res.status_code == 200:
            string = str(res.content.decode("utf-8"))
            print(res)
            if address.find(string) != -1:
                # 包含，匿名
                #url = '1|' + address
                print(str(address) + 'success')
                url = address
            else:
                # 不包含，返回IP不对，不匿名
                #url = '0|' + address
                print("不匿名")
                print("res:"+res)
                url = "error"
        else:
            #url = '2|' + address
            print(address + ' Failed')
            url ="error"
    except:
        #url = '3|' + address
        print(address + ' Errored')
        url = "error"
    else:
        if url != "" or url != "error":
            print(str(url))
            tested_ip_pool.write(url+"\n")

def test_ip(url):
    https = url.split(':', 1)[0]
    test_proxy_ip1(https, url)
    #print("httpurl:"+httpurl)




# 线程数量
threads_num = 10
# 并行任务池
test_thread_pool = ThreadPool(threads_num)
test_ip_list = open("./web_crawler_for_work/test_proxyip_pool.txt",mode="r")
tested_ip_pool= open("./web_crawler_for_work/can_be_used_proxyip_pool.txt",mode="r+")
tested_ip_pool.seek(0,2)
ip_list=[]
for i in test_ip_list:
    url = i.replace("\n","")
    ip_list.append(url)
test_thread_pool.map(test_ip, ip_list)
test_ip_list.close()
tested_ip_pool.close()