#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#参考：https://www.cnblogs.com/baijifeilong/p/3707393.html
import tkinter
from tkinter import filedialog

def openfile():
    r = filedialog.askopenfilename(title='打开文件')
    print(r)
def savefile():
    r = filedialog.asksaveasfilename(title='保存文件', initialdir='d:\mywork', initialfile='hello.py')
    print(r)

root = tkinter.Tk()
btn1 = tkinter.Button(root, text='File Open', command=openfile)
btn2 = tkinter.Button(root, text='File Save', command=savefile)

btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()