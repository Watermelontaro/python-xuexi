# _*_ coding : utf-8 _*_
# @Time : 2023/5/5 15:32
# @Author : 501036554@qq.com
# @File : 函数作为参数传递
# @Project : python-xuexi

# 函数作为参数传递
def func(com):
    a = com(12, 5)
    print(a)


def compute(x, y):
    return x * y


func(compute)
