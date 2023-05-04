# _*_ coding : utf-8 _*_
# @Time : 2023/5/3 10:03
# @Author : 501036554@qq.com
# @File : 函数的返回值
# @Project : pythonProject

def fh(a, b):
    """
    函数说明：
    fh函数可以接受两个参数，计算并返回相加结果
    :param a:两数相加的其中一个
    :param b:两数相加的其中一个
    :return:返回两数相加的结果
    """
    r = a + b
    return r


def fh1():
    return None


fh(2, 10)
print(fh(1, 2))
print(fh1())
print(type(fh1()))
