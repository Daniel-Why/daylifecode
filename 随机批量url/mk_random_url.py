import random

def random_url():
    base_str="abcdefghijklmnopqrstuvwsxy0123456789"
    st2=""
    str_length = len(base_str)-1
    for i in range(992):
        st2 = st2 + base_str[random.randint(0,str_length)]
    url = "http://www."+st2+".com"
    return url

def create_url_list(file_name):
    n = 0
    file = open(file_name,"w")
    for i in range(10000):
        url = random_url()
        file.write(url+"\n")
        n=n+1
        print(n)
    file.close

def main():
    for i in range(10):
        file_name = "./test"+str(i)+".txt"
        create_url_list(file_name)

main()
