#!/usr/bin/python
# -*- coding:utf-8 -*-
import cv2
from PIL import Image
import time
import shutil
import os
 
 
 
DATA = input('请输入要放大的图片名称(JPG文件名称必须使用数字或英文)：')
Multiple = int(input('请输入要放大的图片的倍数(必须大于1)：'))
DATA_file = input('请输入要图片要保存的图片名称：')
print('开始放大....')
os.mkdir('DATA') # 新建
#读取图片  要放大的图片
src = cv2.imread(DATA)
# 用来读取原图片的像素RGB颜色值  先读取图片文件
IMG = Image.open(DATA)
#获取图像大小  获取图像的大写XY也是颠倒过来的
y, x = src.shape[:2]
 
# 临时装饰器
List_elements = []
for YY in range(y):   # 获取图片的Y轴有多少像素  也相当于长度
    '''意思：循环读取图片的每一个像素点的RGB值 并以列表的形式存储起来'''
    if int(len(List_elements)) >= 2:   # 每次循环完毕后要将列表的值恢复无
        List_elements = []
    for XX in range(x):  # 获取图片的X轴有多少像素   也相当于宽度
        # IMG.getpixel((a, aa))  用来获取图片某位置的RGB像素值  提示：获取的值 对应 BGR  是RGB反过来的
        List_elements = List_elements + [list(IMG.getpixel((XX, YY)))]  # 读取某坐标的像素值并将元组为列表进行存储
    NAME = open(f"DATA/{YY}", 'w')  # 存储
    NAME.write(str(List_elements))  # 将列表转为字符串保存
    NAME.close()
 
time.sleep(2)  # 延迟一下 ，防止文件加载过慢读取错误
 
# 图像缩放  要将原图进行翻倍放大  然后在原图的基础上进行绘图
result = cv2.resize(src, (x*Multiple,y*Multiple))
 
for RGB_DATA_Y in range(y):  # 循环所有文件 Y有多少像素 就有多少个RGB颜色文件
    '''循环读取刚刚存储的RGB颜色文件 并循环进行绘制 以倍数进行绘图 确保无损放大'''
    NAME_ = eval(open(f'DATA/{RGB_DATA_Y}', 'r', encoding='utf-8').read())  # 读取文件并转为列表
    for RGB_DATA_X in range(len(NAME_)):  # 获取 文件内有多少个子列表
        '''
        因为通过getpixel 获取出来的颜色是反过来的 RGB 也就是 BGR  
        在颜色文件内的数值也是反过来的，所以在这里读取的时候要将其颠倒一下，反向转换一下
        '''
        _DATA = NAME_[RGB_DATA_X]
        _DATA.reverse()
 
        '''
        当前这个模块是核心模块 主要是用来读取并绘制出原图的倍数 
        原理：
        result[1,1] = [255,255,255]    填充 图片的第一个像素为白色   [255,255,255] 是RGB的白色颜色数值
        result[0:2,0:4] = [255,255,255]      填充图片 X轴从0像素到2像素为白色  Y轴从0像素到4像素为白色  
        '''
        try:
            result[RGB_DATA_Y*Multiple:RGB_DATA_Y*Multiple+Multiple,RGB_DATA_X*Multiple:RGB_DATA_X*Multiple+Multiple] = _DATA
        except:pass
# 写入保存图像
cv2.imwrite(DATA_file, result)
print('完成....')
try:
    shutil.rmtree("DATA") # 删除文件夹和文件
except:pass