# _*_ coding : utf-8 _*_
# @Time : 2023/5/3 10:29
# @Author : 501036554@qq.com
# @File : 函数嵌套调用
# @Project : pythonProject
def s1():
    print("---2---")


def s2():
    print("---1---")
    s1()
    print("---3---")


s2()
