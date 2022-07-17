import tkinter as tk
from tkinter import PhotoImage

win = tk.Tk()
win.title("这是一个测试窗口")

win.geometry('380x200')
var = tk.StringVar()

vlabel = tk.Label(win, text='', width=60, bg='white', fg='black', font=("宋体", 14))
vlabel.pack()


def rd_select():
    print(var.get())
    vlabel.config(text='你的选择是' + var.get())

var.set('0')
rb1 = tk.Radiobutton(win, text='Python语言', variable=var, value="Python语言",
                     command=rd_select)
rb1.pack()
rb2 = tk.Radiobutton(win, text='C语言', variable=var, value="C语言",
                     command=rd_select)
rb2.pack()
rb3 = tk.Radiobutton(win, text='Java语言', variable=var, value="Java语言",
                     command=rd_select)
rb3.pack()
print(var.get())
win.mainloop()


