#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#自己搞的
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog


class MainWindow:
    def buttonListener1(self, event):
        fpath = filedialog.askopenfilename()
        print(fpath)
        #tkinter.messagebox.showinfo("messagebox", "this is button 1 dialog")


    def __init__(self):
        self.frame = Tk()

        self.button1 = Button(self.frame, text="button1", width=10, height=5)


        self.button1.grid(row=0, column=0, padx=5, pady=5)


        self.button1.bind("<ButtonRelease-1>", self.buttonListener1)

        self.frame.mainloop()


window = MainWindow()