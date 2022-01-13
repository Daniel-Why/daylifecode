from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import lxml

chrome_options = webdriver.ChromeOptions()#headless模式
chrome_options.add_argument(r"--user-data-dir=C:\Users\Daniel.Why\AppData\Local\Google\Chrome\User Data\Default")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument("--proxy-server=http://206.253.164.101:80")
#browser_locale = 'fr'
#chrome_options.add_argument("--lang={}".format(browser_locale))
chrome_options.add_argument("--window-size=1920,1050")
chrome_options.add_argument("user-agent=test")


browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl ="http://10.100.1.3:9001/login.php" #"file:///D:/Personal/other_s_code/detect-headless-master/index.html"#"https://user-agents.net/"
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
browser.get(mainUrl)
time.sleep(1)
browser.switch_to_alert().accept()
html_source = browser.page_source
print(html_source)
#browser.find_element_by_link_text("Browsers").click()
#browser.find_element_by_link_text("1stBrowser").click()
#browser.implicitly_wait(10)
#browser.back()
#time.sleep(3)
#browser.quit()