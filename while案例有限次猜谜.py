# _*_ coding : utf-8 _*_
# @Time : 2023/4/26 14:21
# @Author : 501036554@qq.com
# @File : FOR
# @Project : pythonProject
# 多层嵌套练习
# 猜大小，共三次机会for循环版
import random

num = random.randint(1, 10)
i = 0
while i < 3:
    if i < 3:
        i += 1
        j = int(input("输入一个整数："))
        if j == num:
            print("恭喜答对")
            break
        elif j > num:
            print("猜大了！")
            continue
        elif j < num:
            print("猜小了")
            continue
else:
    print("次数上限！")
