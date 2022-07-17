# 设置一个滑动的滑块
import tkinter as tk


win = tk.Tk()
win.title("这是一个测试窗口")

win.geometry('380x280')

var = tk.IntVar()
vlabel = tk.Label(win, text='', width=60, bg='white', fg='black', font=('宋体', 14))
vlabel.pack()


def s_select(v):
    vlabel.config(text='现在的选择数值是：' + v)


# 设置进度条 数值起始终止 水平显示 竖直为VERTICAL
s = tk.Scale(win, label='数值', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,
             tickinterval=2, resolution=0.01, command=s_select)
s.pack()
win.mainloop()

