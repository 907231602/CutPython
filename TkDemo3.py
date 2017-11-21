#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#参考：https://www.cnblogs.com/kaituorensheng/p/3287652.html
from  tkinter import *

root=Tk();
root.title("Hello");
root.geometry('300x200');
'''
Lable
    text　  要现实的文本
    bg　　  背景颜色
    font　  字体(颜色, 大小)
    width　 控件宽度
    height　控件高度
'''
l=Label(root,text="show",bg='green',font=('Arial',12),width=5,height=2);
l.pack(side=LEFT)
root.mainloop()
