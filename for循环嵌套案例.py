# _*_ coding : utf-8 _*_
# @Time : 2023/5/2 9:37
# @Author : 501036554@qq.com
# @File : 循环嵌套案例
# @Project : pythonProject
import random

w = 10000

for i in range(1, 21):
    if w <= 0:
        print("公司没钱了，下月再说吧")
        break
    j = random.randint(1, 10)
    if j < 5:
        print(f"员工编号：{i},您的绩效为：{j}低于5，不满足发工资的条件，下一位")
        continue
    else:
        w -= 1000
        print(f"向员工编号"
              f"{i}发放工资1000，工资剩余余额：{w}")
