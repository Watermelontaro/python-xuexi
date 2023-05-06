# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 15:41
# @Author : 501036554@qq.com
# @File : 异常
# @Project : python-xuexi

# 异常
# try:可能出现异常的代码
try:
    print("1", open("D:\mysql\word.txt", "r", encoding="utf-8"))
# except:出现异常后执行的代码
except:
    print("2", open("C:\mysql\word.txt", "r", encoding="utf-8"))
