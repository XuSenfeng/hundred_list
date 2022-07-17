import tkinter as tk


win = tk.Tk()
win.title("这是一个测试窗口")

win.geometry('380x280')
var_label = tk.StringVar()

vlabel = tk.Label(win, text='', width=50, bg='white', fg='black', font=("宋体", 14),
                  height=1, textvariable=var_label)
vlabel.pack()
var = tk.StringVar()

lb = tk.Listbox(win, listvariable=var)


def display_select():
    try:
        print(lb.curselection())
        vsel = lb.get(lb.curselection())
        var_label.set("你的选择是" + vsel)

    except Exception as e:
        var_label.set('你尚未选择')


bt3 = tk.Button(win, text='显示选中', font=('Arial', 10), width=6, height=1, command=display_select)
bt3.pack()

var.set(('程序员', '架构师', '产品经理', '设计师'))
lb.pack()

vlist = ["python语言", 'c#语言', 'go语言', 'php语言']

for item in vlist:
    lb.insert('end', item)

lb.insert(0, '程序员爱编程')
lb.insert(3, '产品经理爱客户')
lb.delete(6)
win.mainloop()

