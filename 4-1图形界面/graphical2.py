import tkinter as tk

win = tk.Tk()
win.title("这是一个测试窗口")

win.geometry('380x200')
var = tk.StringVar()

vflog = 0


def click():
    global vflog
    if vflog == 0:
        vflog = 1
        var.set('你单机了按钮')

    else:
        vflog = 0
        var.set('')


bt = tk.Button(win, text='测 试', font=('Arial', 12), width=6, height=1, command=click)
bt.pack()
valbell = tk.Label(win, textvariable=var, font=('Arial', 12), bg='green', fg='red', width=50,
                   height=2)
# 设置输入窗口
e1 = tk.Entry(win, show=None, font=('宋体', 12))
e2 = tk.Entry(win, show='*', font=('Arial', 12))
e1.pack()
e2.pack()

valbell.pack()
win.mainloop()
