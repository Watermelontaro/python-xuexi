# _*_ coding : utf-8 _*_
# @Time : 2023/5/8 10:06
# @Author : 501036554@qq.com
# @File : str_util
# @Project : python-xuexi
def str_reverse(e):
    """
    将传入的字符串反转返回
    :param e: 传入字符串
    :return: 返回反转后的字符串
    """
    a = str()
    i = 0
    while i < len(e):
        a += e[-(i + 1)]
        i += 1
    return a


def substr(s, x=0, y=-1):
    """
    传入字符串，并对指定的下标进行切片
    :param s: 字符串
    :param x: 切片开始的下标
    :param y: 切片结束的下标
    :return: 返回切片
    """
    s = s[x:y]
    return s
