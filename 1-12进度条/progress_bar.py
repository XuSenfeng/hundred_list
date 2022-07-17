import sys
from time import sleep


class ProgressBar(object):
    def __init__(self, len, bar_char="#"):
        # 总长度
        self.total_len = len
        # 显示的文字
        self.bar_char = bar_char
        # 已经有的长度
        self.cur_len = 0
        # 记录打印用的文字
        self.write_direction = sys.stdout
        if not self.total_len:
            return
        vstr = '-'*45
        self.write_direction.write("\n"+vstr+"进度条演示"+vstr+'\n')

    def show(self, show_len):
        # 计算文件的百分比
        if show_len > self.total_len:
            percent_int = 100
        else:
            percent_int = (show_len*100)//self.total_len
        # 打印进度条
        cur_string = ("%s" % (self.bar_char*percent_int))
        blank = ' '*(100 - percent_int)
        # 打印百分比
        self.write_direction.write("\r"+cur_string+blank+str(percent_int)+'%')
        self.write_direction.flush()

        self.cur_len = show_len
        if percent_int == 100:
            self.write_direction.write("\n")

    def add_bar_len(self, new_line):
        self.cur_len = self.cur_len + new_line
        self.show(self.cur_len)


if __name__ == '__main__':
    progressbar_obj = ProgressBar(len=200)
    for i in range(200):
        sleep(0.1)
        progressbar_obj.add_bar_len(1)


