import tkinter as tk
from tkinter import PhotoImage

win = tk.Tk()
win.title("这是一个窗口")
win.geometry('300x200+30+20')

lb_test = tk.Label(win, text='这是一个窗口', font=('宋体', 12), bg='yellow', fg='red')
# 纵向边距
lb_test.pack(pady=2)
img = PhotoImage(file='./1.gif')

lb_img = tk.Label(win, image=img)
lb_img.pack(side=tk.BOTTOM)
win.mainloop()

