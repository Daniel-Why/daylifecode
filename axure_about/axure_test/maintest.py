# TangGo 应用中心，下载、安装 自动化测试脚本
#%%
import time
import pyautogui as pya
import do_operations as do

print("开始")

pagelist = ['Badges','Bottom app bar','Bottom sheets','Buttons','Cards','Checkbox','Chips','Date pickers','Dialogs','Divider','Lists','Menus','Navigation bar','Navigation drawer','Navigation rail','Progress indicators','Radio button','Search','Sliders','Snackbar','Switch','Tabs','Text felds','Time pickers','Top app bar']
for i in pagelist:
    do.fine_click(r"asset\axure\01_add_page\1.jpg")
    do.typewords(i)
    do.keyboard_press()
    time.sleep(0.2)

print("完成")




# %%
