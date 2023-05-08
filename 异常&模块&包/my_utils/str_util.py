# _*_ coding : utf-8 _*_
# @Time : 2023/5/8 10:06
# @Author : 501036554@qq.com
# @File : str_util
# @Project : python-xuexi
def str_reverse(e):
    a = str()
    i = 0
    while i < len(e):
        a += e[-(i + 1)]
        i += 1
    return a


def substr(s, x=0, y=-1):
    s = s[x:y]
    return s
