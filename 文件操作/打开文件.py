# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 8:40
# @Author : 501036554@qq.com
# @File : 打开文件
# @Project : python-xuexi

# 使用open函数打开文件
f = open("C:\mysql\mysql-5.7.38-winx64\my.ini", "r", encoding="utf-8")
print(type(f))
print(f)
# 读取文件
# read1 = f.read(50)  # 值不写表示读取整个文件
# print(read1)
# 读取文件全部行，并以列表的形式封装
# line = f.readlines()
# print(line)
# 一次读取文件一行，并以列表的形式封装
# line = f.readline()
# print(line)
# for 循环遍历文件每一行
# for lie in f:
#     print(lie)
