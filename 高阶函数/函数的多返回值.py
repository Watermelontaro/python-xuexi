# _*_ coding : utf-8 _*_
# @Time : 2023/5/5 14:47
# @Author : 501036554@qq.com
# @File : 函数的多返回值
# @Project : python-xuexi

# 函数返回值按顺序写，变量也按顺序接收
def func():
    """
    函数的多返回值
    :return: 返回多个值
    """
    return 1, 2


s, d = func()
print(s)
print(d)
