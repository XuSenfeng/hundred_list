import tkinter as tk

win = tk.Tk()
win.title("这是一个测试窗口")

win.geometry('380x200')
var = tk.IntVar()

vlabel = tk.Label(win, text='', width=60, bg='white', fg='black', font=("宋体", 14))
vlabel.pack()


def ck_select():
    if var.get() == 1:
        vlabel.config(text="你已成年")
    else:
        vlabel.config(text="你未成年")


ck1 = tk.Checkbutton(win, text="满十八岁", onvalue=1, offvalue=0, variable=var,
                     command=ck_select)
ck1.pack()
win.mainloop()


