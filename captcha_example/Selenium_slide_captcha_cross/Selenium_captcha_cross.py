# 自动拖动滑动验证码
#!/usr/bin/env python
# encoding: utf-8

import re,os
import time
import random
import requests
from PIL import Image
from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from  io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains
from mouse_record import output_trace


#def get_merge_img(img_content,location_list,num):
#    '''
#    拼接图片
#    :param img_content:
#    :param location_list:
#    :param num:
#    :return:
#    '''
#    im = Image.open(img_content)
#    im_list_upper = []
#    im_list_done = []
#    for  location  in location_list:
#        # print(location)
#        if int(location['y']) == -58:
#            im_list_upper.append(im.crop((abs(int(location['x'])),58,abs(int(location['x']))+10,116)))
#        if int(location['y']) == 0:
#            im_list_done.append(im.crop((abs(int(location['x'])),0,abs(int(location['x']))+10,58)))
#
##create new image
#    new_im = Image.new('RGB',(260,116))
#    x_offset=0
#    for im in im_list_upper:
#        new_im.paste(im,(x_offset,0))
#        x_offset +=10
#
#    x_offset = 0
#    for im in im_list_done:
#        new_im.paste(im, (x_offset, 58))
#        x_offset += 10
#
#    return new_im


#def get_img(driver,div_class,num):
#    '''
#    获取图片
#    :param driver:
#    :param div_class:
#    :param num:
#    :return:
#    '''
#    background_imgs = driver.find_elements_by_class_name(div_class)
#    location_list = []
#    imge_url = ''
#    for img in background_imgs:
#
#        location = {}
#        imge_url = re.findall(r'background-image: url\(\"(.*?)\"\); background-position: (.*?)px (.*?)px;',img.get_attribute('style'))[0][0]
#        location['x'] = re.findall(r'background-image: url\(\"(.*?)\"\); background-position: (.*?)px (.*?)px;',img.get_attribute('style'))[0][1]
#        location['y'] = re.findall(r'background-image: url\(\"(.*?)\"\); background-position: (.*?)px (.*?)px;',img.get_attribute('style'))[0][2]
#
#        location_list.append(location)
#
#    response = requests.get(imge_url).content
#    img_content  = BytesIO(response)
#
#    image = get_merge_img(img_content,location_list,num)
#    image.save('{}.jpg'.format(num))
#    return image

#获取 Canvas 图片
def get_canv(driver,div_class,filename):
    driver.save_screenshot("f.png")
    imgelement=driver.find_element_by_class_name(div_class)
    #推动快的截图区间
    imgelement_block = driver.find_element_by_class_name("verify-sub-block")
     #刷新按钮的截图区间
    imgelement_refresh = driver.find_element_by_class_name("verify-refresh")
    size1 = imgelement_block.size
    size2 = imgelement_refresh.size
    location = imgelement.location
    size = imgelement.size
    rangle = (int(location['x']) + size1["width"],#减去推动块的 x 长度
            int(location['y']),
            int(location['x']) + size['width']-size2["width"],#减去刷新按钮的 x 长度
            int(location['y']) + size['height'],
            )
    i = Image.open("f.png")
    verifycodeimage = i.crop(rangle)
    #verifycodeimage=verifycodeimage.convert("RBG")
    verifycodeimage.save(filename+".png")
    im = Image.open(filename+".png")
    return im



# 查找缺口位置
def get_diff_location(image1,image2):
    '''
    通过像素对比 找到缺口位置
    :param image1:
    :param image2:
    :return:
    '''
    size = image1.size
    for x in range(1,size[0]):
        for y in range(1, size[1]):
            if is_similar(image1,image2,x,y) == False:
                #判断成立 表示xy这个点 两张图不一样
                print("different")
                return x
            else:
                pass

# 比较像素点
def is_similar(image1,image2,x,y):
    pixel1 = image1.getpixel((x,y))
    pixel2 = image2.getpixel((x,y))
    
    for i in range(0,3):
        pixel_result=[x,y]
        sub= abs(pixel1[i] - pixel2[i])
        pixel_result.append(sub)
        #print(pixel_result)
        if sub >=100:
            return False
    return True

###################### 鼠标移动算法 ##########################
#注意:packages\selenium\webdriver\common\actions\pointer_input.py中DEFAULT_MOVE_DURATION 可修改鼠标每次移动间隔，以模拟真人移动时间，默认250
# 分段变加速运动
def get_track_01(x):
    v = 20
    tracks = []
    current = 0
    mid = x*7/10#到达mid值开始减速
    while current < x:
        coord=[]
        t_list = [17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 66, 18, 8, 37, 19]
        t= 0.001*random.choice(t_list)

        s_ylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, 2]
        s_y = random.choice(s_ylist)
        if current < mid:
            a = random.randint(400,800)
        else:
            a = -random.randint(800,1200)
            s_y = random.choice(s_ylist)
        #a = 20
        v0 = v
        #单位时间内位移公式
        s_x =v0*t+0.5*a*(t**2)
        #当前位移
        current = current+s_x
        coord.append(round(s_x))
        coord.append(round(s_y))
        tracks.append(coord)
        v = v0+a*t

    for i in range(3):
        tracks.append([-1,0])
    for i in range(3):
        tracks.append([2,0])
    print(tracks)
    return tracks
    
# 变加速运动
def get_track_02(x):
    v = 20
    tracks = []
    current = 0
    while current < x:
        coord=[]
        t_list = [17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 66, 18, 8, 37, 19]
        t= 0.001*random.choice(t_list)

        s_ylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, 2]
        s_y = random.choice(s_ylist)
        a = 300
        v0 = v
        #单位时间内位移公式
        s_x =v0*t+0.5*a*(t**2)
        #当前位移
        current = current+s_x
        coord.append(round(s_x))
        coord.append(round(s_y))
        tracks.append(coord)
        v = v0+a*t

    for i in range(3):
        tracks.append([-1,0])
    for i in range(3):
        tracks.append([2,0])
    print(tracks)
    return tracks

# 两点直线
def get_track_03(x):
    v = 20
    tracks = []
    tracks.append([0,0])
    tracks.append([x,0])
    print(tracks)
    return tracks

# 录屏轨迹
def get_track_04(x):
    tracks = output_trace.get_trace(x)
    print(tracks)
    return tracks

### 选择算法
def get_track(x,func_num=1):
    if func_num == 1:
        tracks = get_track_01(x)
    elif func_num == 2:
        tracks = get_track_02(x)
    elif func_num == 3:
        tracks = get_track_03(x)
    elif func_num == 4:
        tracks = get_track_04(x)
        
    return tracks
#########################滑块验证模块#####################
def main(driver,element):

    #1为完整图、2为有缺口图
    image1 = get_canv(driver,'org_pic',"1")
    image2 = get_canv(driver,'verify-img-canvas',"2")
    org_x = get_diff_location(image1,image2)

    #加上之前减去的推动块的x
    imgelement_block = driver.find_element_by_class_name("verify-sub-block")
    size1 = imgelement_block.size
    move_para = 3 #自定义参数，用于图像识别消减误差
    x = int(org_x+size1["width"]+move_para)
    print(x)


    tracks = get_track(x,4)
    ActionChains(driver).click_and_hold(element).perform()
    for coord in tracks:
        #packages\selenium\webdriver\common\actions\pointer_input.py中DEFAULT_MOVE_DURATION 可修改鼠标移动间隔 250
        ActionChains(driver).move_by_offset(xoffset=coord[0],yoffset=coord[1]).perform()
    ActionChains(driver).release(element).perform()
    time.sleep(0.5)

########################主函数################################
if __name__ == '__main__':
    os.chdir("D:\Personal\daylifecode\captcha_example\Selenium_slide_captcha_cross")
    
    #headless 参数
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1050")

    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('file:///D:/Personal/daylifecode/captcha_example/target_html/slide_captcha/slide_captcha.html')
    try:
        count = 1
        # waiting slidingVC loading
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'verify-move-block')))
        while count >0:
            main(driver,element)
            try:
                #succes = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="gt_ajax_tip gt_success"]')))
                locator = ("id","result")
                success = wait.until(EC.text_to_be_present_in_element(locator,"success"))
                if success:
                    print('恭喜你！识别成功...')
                    #count -=1
                    break
                
            except Exception as e:
                print('识别错误，继续')
                #count -=1
                #time.sleep(2)
                break

    finally:
        print("finish")
        driver.quit()
