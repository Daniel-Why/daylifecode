#%%
import time
import pyautogui as pya



#%% 单一步骤

## 定位多个

def all_location(img_path,confidence=0.8):
    return pya.locateAllOnScreen(img_path,confidence)


## 精细定位
def fine_location(img_path,box=None):
    location = pya.locateCenterOnScreen(img_path,confidence=0.8,region=box)
    if location != None:
        return location
    else:
        return 0

# 鼠标点击
def mouse_click(location=None,click_times=1,LorR="left"):
    if location != None:
        pya.click(location.x,location.y,clicks=click_times,interval=0.2,duration=0.2,button=LorR)
        time.sleep(0.1)
    else:
        pya.click(clicks=click_times,interval=0.2,duration=0.2,button=LorR)
        time.sleep(0.1)


# 输入
def typewords(words):
    pya.typewrite(words)

# 鼠标移动(绝对位置)
def mouse_move(location,duration = 0.25):
    pya.moveTo(location.x,location.y,duration)


def mouse_moveRel(x,y,duration = 0.25):
    pya.moveRel(x,y,duration)

# 敲击键盘
def keyboard_press(the_key = "enter"):
    pya.press(the_key)

#%% 组合步骤
# 精细定位单击
def fine_click(img_path,box=None):
    location=fine_location(img_path,box)
    if location != 0:
        mouse_click(location)
    else:
        pass

# 点击并输入
def fine_cleck_A_input(img_path,input_words,box=None):
    location=fine_location(img_path,box)
    if location != 0:
        mouse_click(location)
        typewords(input_words)
    else:
        print("Error: 目标不存在")
        pass

def move_to(img_path):
    location = fine_location(img_path)
    mouse_move(location)
    time.sleep(1)