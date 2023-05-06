# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 16:33
# @Author : 501036554@qq.com
# @File : 捕获指定异常
# @Project : python-xuexi
n = [1, 2, 3]
try:
    # print(name)
    # 1 / 0
    # 只能捕获指定异常
    print(n[5])
except NameError as e:
    print("出异常了！变量名为定义异常=>", e)
except ZeroDivisionError as e:
    print("出异常了！除0异常=>", e)
