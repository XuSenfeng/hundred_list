import tkinter as tk


win = tk.Tk()
win.title('place布局设置')
win.geometry('360x320')

img = tk.PhotoImage(file='./1.gif')
label_img = tk.Label(win, width=100, height=100, image=img)
# 设置为左上角占用两列
label_img.grid(row=0, column=0, rowspan=2, padx=10, pady=20)

label1 = tk.Label(win, text='地点')
# 设置为第一行第一列左侧
label1.grid(row=0, column=1, sticky=tk.W)

label2 = tk.Label(win, text='内容')
label2.grid(row=1, column=1, sticky=tk.W)

e1 = tk.Entry(win)
e1.grid(row=0, column=2, sticky=tk.W)
e2 = tk.Entry(win)
e2.grid(row=1, column=2, sticky=tk.W)

label3 = tk.Label(win, text='简介')
label3.grid(row=2, column=0, sticky=tk.W, padx=5)

text1 = tk.Text(win, width=45, height=10)

text1.grid(row=3, column=0, sticky=tk.W+tk.N, columnspan=3, padx=10, pady=10)

win.mainloop()







