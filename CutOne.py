#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open("pic\login.png")
# 图片的宽度和高度
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''

#截取登录界面块
def cutPicLogin():
    x =782
    y =113
    w =292
    h =460
    region = im.crop((x, y, x + w, y + h))
    region.save("pic\loginTable.png")


#登录界面分块，version1,只能实现单个
def cropLogin():
    im=Image.open("pic\loginTable.png");
    im_size=im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    #把图片平均分成10块
    # 第1块
    w = im_size[0] / 2.0  #宽
    h = im_size[1] / 10.0 #长
    x = 0
    y = 0
    region = im.crop((x, y, x + w, y + h))
    region.save("pic\crop_average-1.png")

#登录界面分块，version2，for循环分块
def cropLogin2():
    im=Image.open("pic\loginTable.png");
    im_size=im.size;
    print("login图片宽度和高度分别是{}".format(im_size));
    #把图片平均分成10块
    # 第1块
    w = im_size[0] / 2.0  #宽
    h = im_size[1] / 10.0 #高
    x = 0                   #宽
    y = 0                   #高
    for i in range(10): #循环长度10次
        for j in range(2):  #循环宽度2次
            region = im.crop((x, y, x + w, y + h))
            region.save("pic\crop_average-%d-%d.png" % (i,j));
            x=x+w;
            y=y;
        x=0                 #高依次增加，宽度从0~~边界值
        y=y+h;

if __name__ == "__main__":
    cutPicLogin();
    cropLogin2();



