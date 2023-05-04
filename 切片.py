# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 16:26
# @Author : 501036554@qq.com
# @File : 字符串案例
# @Project : python-xuexi

# list类型
my = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 对序列进行切片操作：截取指定的
my1 = my[0:6:2]
print(my1)
my2 = my[::3]
print(my2)
my3 = my[-1::-2]
print(my3)
# tuple类型
my = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(my[1:8:4])
print(my[:10:2])
print(my[5::2])
# str类型
my = "qazwsxedcrfvtgbyhnujmikolp"
print(my[1::5])
print(my[::-5])
