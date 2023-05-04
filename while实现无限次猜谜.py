# _*_ coding : utf-8 _*_
# @Time : 2023/4/26 14:52
# @Author : 501036554@qq.com
# @File : while
# @Project : pythonProject
"""
a = 0
i = 1
while i <= 100:
    a += i
    i += 1
    print(a)
"""
import random

un = 0
box = True
a = random.randint(1, 100)
while box:
    un += 1
    num = int(input("输入猜测的数字："))
    if 0 < num < 100:
        if num == a:
            print("猜中了！")
            box = False
        elif num > a:
            print("猜大了！")
        elif num < a:
            print("猜小了！")
    else:
        print("输入有误，请重新输入！！！")
print(f"本次猜谜游戏中，共猜测{un}次")
