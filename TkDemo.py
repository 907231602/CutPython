
#参考：https://segmentfault.com/q/1010000005048090
import tkinter as tk
from tkinter import filedialog

#弹框选择图片
root = tk.Tk()

root.withdraw()
fpath = filedialog.askopenfilename()
print(fpath)