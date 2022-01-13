from selenium.webdriver import Firefox
path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
driver = Firefox(executable_path=path)
driver.get("https://user-agents.net/download?browser=beamrise&browser_type=browser")