# 布局
import tkinter as tk

win = tk.Tk()
win.title("测试布局")

win.geometry('300x100')
# 添加容器
# frame1 = tk.Frame(win)
#
# bt1 = tk.Button(frame1, text='左边', width=8)
# # 在容器的坐车间距为2
# bt1.pack(side=tk.LEFT, padx=2)
# bt2 = tk.Button(frame1, text='中间', width=8)
# bt2.pack(side=tk.LEFT, padx=2)
# bt3 = tk.Button(frame1, text='右边', width=8)
# bt3.pack(side=tk.LEFT, padx=2)
# frame1.pack(side=tk.LEFT, fill=tk.Y, padx=6)

frame2 = tk.Frame(win)
labl1 = tk.Label(frame2, bg='green', width=8, text='顶部')
labl1.pack(side=tk.BOTTOM, anchor=tk.E, fill=tk.Y, padx=2)
labl1 = tk.Label(frame2, bg='green', width=8, text='中部')
labl1.pack(side=tk.LEFT, anchor=tk.E, fill=tk.Y, padx=2)
labl1 = tk.Label(frame2, bg='green', width=8, text='下部')
labl1.pack(side=tk.TOP, anchor=tk.E, fill=tk.Y, padx=2)
frame2.pack(side=tk.BOTTOM, fill=tk.Y)


win.mainloop()



