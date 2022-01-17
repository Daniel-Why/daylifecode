from PIL import Image
import os
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
            is_similar(image1,image2,x,y)
            if is_similar(image1,image2,x,y) == False:
                #判断成立 表示xy这个点 两张图不一样
                print("different")
                return x
            else:
                pass


def is_similar(image1,image2,x,y):
    pixel1 = image1.getpixel((x,y))
    pixel2 = image2.getpixel((x,y))
    
    for i in range(0,4):
        pixel_result=[x,y]
        sub= abs(pixel1[i] - pixel2[i])
        pixel_result.append(sub)
        #print(pixel_result)
        if sub >=20:
            print("false")
            print(pixel_result)
            #return False
    return True

os.chdir("D:\Personal\daylifecode\mousetracker")
image1=Image.open("1.png")
image2=Image.open("2.png")
x = get_diff_location(image1,image2)
print(x)



