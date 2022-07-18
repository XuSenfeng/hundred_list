# 打开一个文本编译器
# 添加一个右侧滚轮
# 添加文字
# 添加标签的作用
import tkinter as tk
import webbrowser

win = tk.Tk()
win.title('Text')
simtext = tk.Text(win, font=("宋体", 12), width=50, height=10)
simtext.pack(side=tk.LEFT, fill=tk.Y)
simtext.insert(tk.INSERT, '这是一个测试，阿巴阿巴！')
# 取出文字的一部分 小数点前是行 之后是列
print(simtext.get(1.0, 1.6))
# 对单个字添加标签
simtext.mark_set('marktest', '1.4')
simtext.insert("marktest", '小')

# 在两个值之间添加一个标签
simtext.tag_add('tag_test', '1.0', '1.7', '1.10', '1.12')
simtext.tag_config('tag_test', background='yellow', foreground='red')
simtext.insert(tk.END, '\n测试：单机打开百度网站')

simtext.tag_add("tag_baidu", '2.5', '2.11')
simtext.tag_config('tag_baidu', foreground="blue", underline=True)


def openbaidu(event):
    webbrowser.open('http://www.baidu.com')


simtext.tag_bind('tag_baidu', '<Button-1>', openbaidu)

# 设置一个滑动滚轮
scroll_obj = tk.Scrollbar(win)
scroll_obj.pack(side=tk.RIGHT, fill=tk.Y)
scroll_obj.config(command=simtext.yview())
simtext.config(yscrollcommand=scroll_obj.set)

win.mainloop()

