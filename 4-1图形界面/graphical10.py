import tkinter as tk


def cal_command(event):
    but_text = event.widget['text']
    if but_text == '=':
        try:
            result_num = str(eval(show_text.get()))
            but_text_new = result_num
        except:
            show_text.set('录入有误， 请单击C清除')
            return

    elif but_text == 'C':
        but_text_new = ''
    else:
        but_text_new = show_text.get() + but_text

    show_text.set(but_text_new)

def layout():
    txt = ['7', '8', '9', '+', 'C', '4', '5', '6', '-', '%', '1', '2', '3', '*', '=', '0', '.', '/']
    but_index = 0
    for i in range(1, 5):
        if but_index >= 18:
            break
        for j in range(0, 5):
            if but_index >= 18:
                break
            bt = tk.Button(text=txt[but_index], width=12, height=1)

            if txt[but_index] == '=':
                bt.config(width=12, height=3)
                bt.grid(row=i, column=j, rowspan=2)

            elif txt[but_index] == '0':
                bt.config(width=25)
                bt.grid(row=i, column=j, columnspan=2)

            elif txt[but_index] == '.' or txt[but_index] == '/':
                bt.grid(row=i, column=j+1)
            else:
                bt.grid(row=i, column=j)

            bt.bind('<Button-1>', cal_command)
            but_index += 1

if __name__ == '__main__':

    win = tk.Tk()
    win.title("简单的计算器")
    show_text = tk.StringVar(value='')
    lab = tk.Label(win, relief=tk.SUNKEN, borderwidth=8, anchor=tk.SE)
    lab.configure(background='white', textvariable=show_text, height=2, width=66)
    lab.grid(row=0, column=0, columnspan=5, sticky=tk.SW)

    layout()
    win.mainloop()







