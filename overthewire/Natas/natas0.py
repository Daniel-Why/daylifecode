from selenium import webdriver
# chrome_options
chrome_options = webdriver.ChromeOptions()#headless模式
chrome_options.add_argument("--headless")

# main
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

# user/password/natas_id
username = "natas0"
password = "natas0"
natas_id = "0"

# get url
url="http://{}:{}@natas{}.natas.labs.overthewire.org/".format(username,password,natas_id)
browser.get(url)

# detail
content = browser.page_source
print(content)

