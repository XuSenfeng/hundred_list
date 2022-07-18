import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


def close_win():
    if messagebox.askokcancel("退出提示", '确定退出吗'):
        win.destroy()


def set_line_number(event=None):
    row, col = simtext.index(tk.END).split('.')
    line = '\n'.join([str(i) for i in range(1, int(row))])
    text_line.config(state=tk.NORMAL)
    text_line.delete('1.0', tk.END)
    # 从第一行写起
    text_line.insert('1.0', line)
    # 不能写入文本
    text_line.config(state=tk.DISABLED)


def creat_new(event=None):
    win.title("简单的编译器--新文件(未命名)")
    simtext.delete("1.0", tk.END)
    set_line_number(event=None)


def open_file(event=None):
    # 打开一个文件
    global filename
    # 从文件选择窗口得到文件名
    filename = filedialog.askopenfile(defaultextension=".txt")

    if filename == "":
        filename = None
    else:
        win.title("简单编译器--" + os.path.basename(filename))
        simtext.delete("1.0", tk.END)
        with open(filename, 'r') as f:
            simtext.insert('1.0', f.read())
            set_line_number()

def save_file(event=None):
    # 检查有没有文件名
    global filename
    try:
        with open(filename, 'w') as f:
            msg = simtext.get("1.0", tk.END)
            f.write(msg)
    except:
        saveas()


def saveas(event=None):
    # 让用户输入问文件名 如果没有输入为前者 输入了就为后者
    fname = filedialog.asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global filename
    filename = fname
    with open(fname, 'w') as f:
        msg = simtext.get(1.0, tk.END)
        f.write(msg)
    win.title("简单编辑器--" + os.path.basename(fname))


def copy():
    simtext.event_gengrate("<<Copy>>")


def cut():
    simtext.event_gengrate("<<Cut>>")


def paste():
    simtext.event_gengrate("<<Paste>>")


def redo():
    simtext.event_gengrate("<<Redo>>")


def undo():
    simtext.event_gengrate("<<Undo>>")


def selectAll():
    simtext.event_gengrate("<<SelectAll>>")


def search(event=None):
    def do_search(ignore_case):
        key = e_search.get()
        simtext.tag_remove("tag_search", '1.0', tk.END)
        start_pos = 1.0
        vcount = 0
        while True:
            # 开始寻找忽略大小写
            start_pos = simtext.search(key, start_pos, nocase=ignore_case, stopindex=tk.END)
            if not start_pos:
                break
            print(start_pos, len(key))
            end_pos = '{}+{} chars'.format(start_pos, len(key))
            # 给找到的文字添加标签
            simtext.tag_add('tag_search', start_pos, end_pos)
            vcount += 1
            start_pos = end_pos

        simtext.tag_config("tag_search", background='yellow')
        messagebox.showinfo('查找', '共查找到%d个“%s”' % (vcount, key))
        win_search.focus_set()

    win_search = tk.Toplevel(win)
    win_search.title("搜索对话框")
    win_search.geometry("400x60+280+200")
    win_search.resizable(False, False)

    label_searck = tk.Label(win_search, text="请输入要查找的内容")
    label_searck.grid(row=0, column=0, sticky=tk.E)

    e_search = tk.Entry(win_search, width=30)
    e_search.grid(row=0, column=1, padx=2, pady=2, sticky=tk.E)
    ignore_case = tk.IntVar()
    but_search = tk.Button(win_search, text="查找",
                           command=lambda: do_search(ignore_case.get()))
    but_search.grid(row=0, column=2, padx=2, pady=0)
    ck_case = tk.Checkbutton(win_search, text='忽略大小写', variable=ignore_case, onvalue=1,
                             offvalue=0)
    ck_case.grid(row=1, column=1, sticky=tk.W, padx=2, pady=2)

    def close_win_search():
        simtext.tag_remove("tag_search", '1.0', tk.END)

        win_search.destroy()

    win_search.protocol('WM_DELETE_WINDOW', close_win_search)
    return


def create_menu():
    menu_obj = tk.Menu(win)
    menu_file = tk.Menu(menu_obj, tearoff=0)
    menu_obj.add_cascade(label='文件操作', menu=menu_file)

    menu_file.add_command(label='新建', command=creat_new, accelerator='Ctrl + N')
    menu_file.bind_all('<Control-N>', func=creat_new)
    menu_file.add_command(label='打开', command=open_file, accelerator='Ctrl + O')
    menu_file.bind_all('<Control-O>', func=open_file)
    menu_file.add_command(label='保存', command=save_file, accelerator='Ctrl + N')
    menu_file.bind_all('<Control-N>', func=save_file)
    menu_file.add_command(label='另存为', command=saveas, accelerator='Ctrl + Shift + N')

    menu_edit = tk.Menu(menu_obj, tearoff=0)
    menu_obj.add_cascade(label='编辑操作', menu=menu_edit)
    menu_edit.add_command(label='复制', command=copy, accelerator='Ctrl + C')
    menu_edit.add_command(label='粘贴', command=paste, accelerator='Ctrl + V')
    menu_edit.add_command(label='剪切', command=cut, accelerator='Ctrl + X')
    menu_edit.add_separator()
    menu_edit.add_command(label='撤销', command=undo, accelerator='Ctrl + Z')
    menu_edit.add_command(label='恢复', command=redo, accelerator='Ctrl + Y')
    menu_edit.add_separator()
    menu_edit.add_command(label='全选', command=selectAll, accelerator='Ctrl + C')
    menu_edit.add_command(label='查找', command=search, accelerator='Ctrl + F')
    menu_file.bind_all('<Control-F>', func=search)
    win.config(menu=menu_obj)


def creat_popup_menu():
    pop_menu = tk.Menu(simtext, tearoff=0)
    for name, comm in zip(['复制', '粘贴', '剪切', '撤销', '恢复'],
                          [copy, paste, cut, undo, redo]):
        pop_menu.add_command(label=name, command=comm)
    pop_menu.add_separator()
    pop_menu.add_command(label='全选', command=selectAll)
    simtext.bind('<Button-3>', lambda event: pop_menu.tk_popup(event.x_root, event.y_root))


if __name__ == '__main__':
    filename = ''
    win = tk.Tk()
    win.geometry('800x600+180+60')
    win.title("简单的编译器")
    win.protocol("WM_DELETE_WINDOW", close_win)
    create_menu()

    text_line = tk.Text(win, width=3)
    text_line.pack(side=tk.LEFT, fill=tk.Y)

    simtext = tk.Text(win, wrap=tk.WORD, undo=True)
    simtext.pack(expand=True, fill=tk.BOTH)

    scroll_obj = tk.Scrollbar(simtext)
    scroll_obj.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_obj.config(command=simtext.yview)

    simtext.config(yscrollcommand=scroll_obj.set)

    simtext.bind_all('<Any-KeyPress>', set_line_number)
    creat_popup_menu()
    win.mainloop()





