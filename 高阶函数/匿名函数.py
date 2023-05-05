# _*_ coding : utf-8 _*_
# @Time : 2023/5/5 15:54
# @Author : 501036554@qq.com
# @File : 匿名函数
# @Project : python-xuexi

def func(e):
    s = e(5, 8)
    print(s)


# lambda 定义匿名函数的关键字
func(lambda x, y: x * y)
