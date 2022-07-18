import tkinter as tk
import time
import datetime


def get_week_day(date):
    dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日',
    }
    day = date.weekday()
    return dict[day]


def show_time():
    week_day = get_week_day(datetime.datetime.now())
    # 设置日期
    str_data = time.strftime('%Y{}%m{}%d{}  ').format('年', '月', '日') + week_day
    str_time = time.strftime("%H:%M:%S %p")

    date_str.set(str_data)
    time_str.set(str_time)

    clock_label.after(1000, show_time)


if __name__ == '__main__':
    win = tk.Tk()
    win.title = "电子时钟"
    win.geometry('380x160')
    time_str = tk.StringVar()
    date_str = tk.StringVar()

    date_label = tk.Label(win, textvariable=date_str, bg='white', fg='blue',
                          font=("Arial", 20), width=50, height=2)
    clock_label = tk.Label(win, textvariable=time_str, bg='white', fg='blue',
                          font=("Arial", 20), width=50, height=2)
    date_label.pack(anchor='center')
    clock_label.pack(anchor='center')
    show_time()
    win.mainloop()


