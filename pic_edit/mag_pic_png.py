#!/usr/bin/python
# -*- coding:utf-8 -*-
import cv2
from PIL import Image
import time
import shutil
import os
 
 
 
DATA = input('请输入要放大的图片名称(PNG文件名称必须使用数字或英文)：')
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
 
# 模板
# 图像缩放  要将原图进行翻倍放大  然后在原图的基础上进行绘图
result = cv2.resize(src, (x*Multiple,y*Multiple))
# 写入保存图像 - 模板图片不用管
cv2.imwrite('8UY88767.png', result)
 
 
 
# 临时装饰器
List_elements = []
# 存储文件的个数 后期读取方便，不会错读取
Number_documents = 0
 
for YY in range(y):   # 获取图片的Y轴有多少像素  也相当于长度
    '''意思：循环读取图片的每一个像素点的RGBA值 并以列表的形式存储起来'''
    if int(len(List_elements)) >= 2:   # 每次循环完毕后要将列表的值恢复无
        List_elements = []
    for XX in range(x):  # 获取图片的X轴有多少像素   也相当于宽度
        # IMG.getpixel((a, aa))  用来获取图片某位置的RGBA像素值
        List_elements = List_elements + [IMG.getpixel((XX, YY))]*Multiple   # 读取某坐标的像素值并将元组为列表进行存储   Multiple是倍数
    for a in range(Multiple):    # Multiple是倍数  如果是2倍 则生成两个同样的颜色文件   在后期进行单行输出多次 确保以像素点进行放大
        NAME = open(f"DATA/{Number_documents}", 'w')  # 存储
        NAME.write(str(List_elements))  # 将列表转为字符串保存
        NAME.close()
        Number_documents = Number_documents + 1
 
time.sleep(1)   # 延迟一下 ，防止文件加载过慢读取错误
 
DATA_ = list()  # 定义需要处理的数据列表
for a in range(Number_documents):
    NAME = open(f"DATA/{a}", 'r').read()  # 读取颜色文件
    NAME = list(eval(NAME))   # 将颜色文件转换为列表
    for aa in range(len(NAME)):  # 循环读取列表的颜色值
        DATA_.append(NAME[aa])    # 将颜色值保存到数据列表
 
# 打开写入模板图片
IMG_2 = Image.open('8UY88767.png')
# 转化为RGBA
RGBA_IMG = IMG_2.convert("RGBA")
RGBA_IMG.putdata(DATA_)  # 写入图片
RGBA_IMG.save(DATA_file, "PNG")  # 保存图片
print('完成....')
try:
    shutil.rmtree("DATA") # 删除文件夹和文件
except:pass
try:
    os.remove("8UY88767.png") # 删除文件
except:pass