#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipOcr

#参考：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html#.E9.80.9A.E7.94.A8.E6.96.87.E5.AD.97.E8.AF.86.E5.88.AB
""" 你的 APPID AK SK """
APP_ID = '10404372'
API_KEY = 'RM3BV3tnAnKjoKVCkyBbOTVO'
SECRET_KEY = 'U7atOte4w1llvWGM0N2w81kkQmjlWuTD'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 调用通用文字识别接口
for i in range(10):
    for j in range(2):
        result = aipOcr.basicGeneral(get_file_content('pic\\crop_average-%d-%d.png'%(i,j)))
        print(result)