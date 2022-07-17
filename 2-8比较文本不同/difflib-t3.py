import difflib
import sys


def file_to_line(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        text = fp.read()
    return text.splitlines()

if __name__ == '__main__':

    file1 = input("请输入要比较的第一个文件名： ")
    file2 = input("请输入要比较的第二个文件名： ")
    try:
        str1_line = file_to_line(file1)
        str2_line = file_to_line(file2)
    except Exception as e:
        print("文件读取错误,退出", e)
        sys.exit()

    htmldiff_obj = difflib.HtmlDiff()
    htmlfile = htmldiff_obj.make_file(str1_line, str2_line)
    with open("./diff.html", "w", encoding="utf-8") as fp:
        fp.write(htmlfile)

    print("over")
