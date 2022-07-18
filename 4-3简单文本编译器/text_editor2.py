import tkinter as tk
import webbrowser


def click_info(event):
    vlabel.config(text="您的坐标为(" + str(event.x) + ',' + str(event.y) + ")位置单击了一下")


win = tk.Tk()
win.title('测试鼠标事件')
win.geometry("300x300")

vlabel = tk.Label(text='', bg="green", fg="white", width=50, font=("宋体", 12))
vlabel.pack(side=tk.LEFT, anchor=tk.N)
win.bind('<Button-1>', click_info)
win.mainloop()




win.mainloop()

