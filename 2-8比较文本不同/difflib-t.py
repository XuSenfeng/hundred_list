import difflib

if __name__ == '__main__':

    str1 = """
    text 1:
    a b c d e f g h 
    o o o o o o o o
    1 2 3 4 5 6 7 8
    """
    str2 = """
    text 2:
    a k c d e f g h
    o o o o o o o o
    1 2 3 8 5 6 7 8
    """
    str1_line = str1.splitlines()
    str2_line = str2.splitlines()

    diff_obj = difflib.Differ()
    a = ["123"]
    b = ['321']
    diffs = diff_obj.compare(str1_line, str2_line)

    list_diffs = list(diffs)

    print("\n".join(list_diffs))
    print(list_diffs)