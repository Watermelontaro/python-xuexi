# _*_ coding : utf-8 _*_
# @Time : 2023/5/3 15:25
# @Author : 501036554@qq.com
# @File : 函数案例黑马ATM
# @Project : pythonProject
import sys


def cxye():
    print(f"当前账户余额为：{money}元")
    zcd()


def ck(e):
    global money
    money += e
    cxye()


def qk(e):
    global money
    a = money
    a -= e
    if money <= 0:
        print("余额不足")
    else:
        money -= e
    cxye()


def zcd():
    print("----------黑马ATM欢迎您----------")
    print(f"尊敬的{name}，欢迎使用黑马ATM")
    print("1.查询余额\t2.存款\n3.取款\t\t0.退出")
    i = int(input("请输入需要的功能的序号："))
    print("已输入%d" % i)
    if i == 0:
        print("退出程序！！！\n")
        sys.exit()
    elif i == 1:
        cxye()
    elif i == 2:
        s = int(input("请输入存款金额："))
        ck(s)
    elif i == 3:
        s = int(input("请输入取款金额："))
        qk(s)
    else:
        print("输入错误，退出程序！！！\n")
        sys.exit()


print("----------黑马ATM欢迎您----------")
money = 5000000
name = input("请输入客户名称：")
zcd()
