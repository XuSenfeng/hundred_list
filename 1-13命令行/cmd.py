from optparse import OptionParser
import sys


def set_parse(cmd):
    usage_info = "\n 命令调用的方式：python %prog [option] arg\n" \
                 "python %prog [-d|--day] 星期几\t 得出这个日期是否工作" \
                 "python %prog [-e|--eval] 表达式\t 计算出表达式的值" \
                 "python %prog [-q|--quit] \t 直接退出程序"

    parser_obj = OptionParser(usage=usage_info,
                              prog="1-13命令行\cmd,py",
                              version='%prog ver 0.8')
    parser_obj.add_option("-d", "--day", dest="dayname",
                          action="store", help="DAYNAME为星期几")
    parser_obj.add_option("-e", "--eval", dest="expression",
                          action="store", help="EXPRESSION为数学计算表达式")
    parser_obj.add_option("-q", "--quit", dest="verbose",
                          action="store_true", help="直接退出程序")
    (options, args) = parser_obj.parse_args(cmd)
    return options, args


def test_day(week_day):
    if week_day == '星期六' or week_day == "星期日":
        print("今天不用上班")
    else:
        print("滚去工作")


def fun_eval(exp):
    try:
        value = eval(exp)
        print(exp, "的值是", str(value))
    except Exception as e:
        print("表达式错误")


if __name__ == '__main__':
    while True:

        options, args = set_parse(input("cmd>").split())


        if options.verbose:
            print("退出程序")
            sys.exit()
        if len(args)>1:
            print('本程序的位置参数是： ', args)

        if options.dayname:
            test_day(options.dayname)
        if options.expression:
            fun_eval(options.expression)

