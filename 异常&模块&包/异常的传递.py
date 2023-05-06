# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 17:16
# @Author : 501036554@qq.com
# @File : 异常的传递
# @Project : python-xuexi
# func3的异常在func1中被捕获
def func3():
    print(name)


def func2():
    func3()


def func1():
    try:
        func2()
    except Exception as e:
        print(e)


func1()
