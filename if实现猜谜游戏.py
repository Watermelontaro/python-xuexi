# _*_ coding : utf-8 _*_
# @Time : 2023/4/26 10:33
# @Author : 501036554@qq.com
# @File : ifMAX
# @Project : pythonProject
# 多层嵌套练习
# 猜大小，共三次机会，
import random

a = 0
num1 = random.randint(1, 10)
if a <= 3:  # 第一次
    a += 1
    print(f"您共有3次机会；第{a}次")
    b = int(input("输入一个1~10之间的整数:"))
    if b == num1:  # 第一次，猜对了
        print("猜对了!")
    elif b < num1:  # 第一次，猜小了
        print("猜小了，再来一次")
        if a <= 3:  # 第二次
            a += 1
            print(f"您共有3次机会；第{a}次")
            b = int(input("输入一个1~10之间的整数:"))
            if b == num1:  # 第二次，猜对了
                print("猜对了!")
            elif b < num1:  # 第二次，猜小了
                print("猜小了，再来一次")
                if a <= 3:  # 第三次
                    a += 1
                    print(f"您共有3次机会；第{a}次")
                    b = int(input("输入一个1~10之间的整数:"))
                    if b == num1:  # 第三次，猜对了
                        print("猜对了!")
                    elif b < num1:  # 第三次，猜小了
                        print("猜小了")
                        print(f"已使用{a}次，没有机会了")
                    elif b > num1:  # 第三次，猜大了
                        print("猜大了")
                        print(f"已使用{a}次，没有机会了")
            elif b > num1:  # 第二次，猜大了
                print("猜大了，再来一次")
                if a <= 3:  # 第三次
                    a += 1
                    print(f"您共有3次机会；第{a}次")
                    b = int(input("输入一个1~10之间的整数:"))
                    if b == num1:  # 第三次，猜对了
                        print("猜对了!")
                    elif b < num1:  # 第三次，猜小了
                        print("猜小了")
                        print(f"已使用{a}次，没有机会了")
                    elif b > num1:  # 第三次，猜大了
                        print("猜大了")
                        print(f"已使用{a}次，没有机会了")
    elif b > num1:  # 第一次，猜大了
        print("猜大了，再来一次")
        if a <= 3:  # 第二次
            a += 1
            print(f"您共有3次机会；第{a}次")
            b = int(input("输入一个1~10之间的整数:"))
            if b == num1:  # 第二次，猜对了
                print("猜对了!")
            elif b < num1:  # 第二次，猜小了
                print("猜小了，再来一次")
                if a <= 3:  # 第三次
                    a += 1
                    print(f"您共有3次机会；第{a}次")
                    b = int(input("输入一个1~10之间的整数:"))
                    if b == num1:  # 第三次，猜对了
                        print("猜对了!")
                    elif b < num1:  # 第三次，猜小了
                        print("猜小了")
                        print(f"已使用{a}次，没有机会了")
                    elif b > num1:  # 第三次，猜大了
                        print("猜大了")
                        print(f"已使用{a}次，没有机会了")
            elif b > num1:  # 第二次，猜大了
                print("猜大了，再来一次")
                if a <= 3:  # 第三次
                    a += 1
                    print(f"您共有3次机会；第{a}次")
                    b = int(input("输入一个1~10之间的整数:"))
                    if b == num1:  # 第三次，猜对了
                        print("猜对了!")
                    elif b < num1:  # 第三次，猜小了
                        print("猜小了")
                        print(f"已使用{a}次，没有机会了")
                    elif b > num1:  # 第三次，猜大了
                        print("猜大了")
                        print(f"已使用{a}次，没有机会了")
