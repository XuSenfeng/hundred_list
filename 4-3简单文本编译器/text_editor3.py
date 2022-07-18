import tkinter as tk
import webbrowser

win = tk.Tk()
win.title('图片-文字')

text_img = tk.Text(win, width=30, height=20)
img = tk.PhotoImage(file='./1.gif')
text_img.image_create(tk.END, image=img)
text_img.pack(side=tk.LEFT)
simtest = tk.Text(win, font=('宋体', 12), width=30, height=18)
simtest.pack(side=tk.LEFT, fill=tk.Y)
scorll_obj = tk.Scrollbar(win)
scorll_obj.pack(side=tk.RIGHT, fill=tk.Y)
scorll_obj.config(command=simtest.yview)
simtest.config(yscrollcommand=scorll_obj.set)
simtest.pack(side=tk.LEFT)
scorll_obj.pack(side=tk.LEFT, fill=tk.Y)
simtest.insert(tk.INSERT, "\n吊\n", 'tag_title')
simtest.tag_config("tag_title", font=('黑体', 20, 'bold'))
conten = """
经查，该护士为象山县第一人民医院儿科副护士长，2022年7月15日上午9时多，一名三岁患儿来象山县第一人民医院就诊，因病情严重，医院当即组织抢救，从上午11时许开始抢救，12:45时，因抢救无效，与家属解释后，家属签字同意放弃抢救。鉴于部分其他在场亲属的要求，医务人员仍继续实施心肺复苏等有关措施进行抢救，15:40时，宣布该患儿死亡。
"""
simtest.insert(tk.END, conten)

win.mainloop()

