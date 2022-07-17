def color_set(str, sel_color):
    color_dic = {
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'FUCHSIA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
        'NORMAL': '\033[0m',
    }
    sel_color = sel_color.upper()
    if sel_color in color_dic.keys():
        return '%s%s%s' % (color_dic[sel_color], str, color_dic["NORMAL"])
    else:
        print("没有找到对应的颜色")
        return '%s%s%s' % (color_dic["NORMAL"], str, color_dic["NORMAL"])

if __name__ == '__main__':
    print(color_set("红色", "red"))
    print(color_set("董浩昕", "green"))
    print(color_set("黄色", "yellow"))

