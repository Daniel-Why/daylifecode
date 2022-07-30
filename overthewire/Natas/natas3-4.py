from selenium import webdriver
# <chrome_options>
chrome_options = webdriver.ChromeOptions()#headless模式
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--referer=http://natas5.natas.labs.overthewire.org/")


# <webdriver>
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

# <user/password/natas_id>
username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
natas_id = "4"

# <get url>
url="http://{}:{}@natas{}.natas.labs.overthewire.org/".format(username,password,natas_id)
browser.get(url)

# <main>

content = browser.page_source
print(content)

