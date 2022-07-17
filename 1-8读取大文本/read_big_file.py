def test():
    print("您好现在程序开始执行")

    first_rec = yield 1

    print("第一次收到的值->", first_rec)
    second_rec = yield 2

    print("第一次收到的值->", second_rec)
    third_rec = yield 3

    print("第一次收到的值->", third_rec)
    yield 666
    print("没有返回值结束")

if __name__ == '__main__':
    test = test()
    value1 = next(test)
    print(value1)
    value2 = test.send("第一次发送")
    print(value2)
    value3 = test.send("第二次发送")
    print(value3)
    value4 = test.send("第一次发送")
    print(value4)

