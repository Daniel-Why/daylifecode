import os,time
os.chdir("D:\Personal\daylifecode\captcha_example\Selenium_slide_captcha_cross")
for i in range(11):
    time.sleep(1)
    print("##########{}##########".format(i))
    os.system("python Selenium_captcha_cross.py")
    print("##########{}##########".format("finish"))
    time.sleep(0.5)