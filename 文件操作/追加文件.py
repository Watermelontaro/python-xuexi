# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 11:24
# @Author : 501036554@qq.com
# @File : 追加文件
# @Project : python-xuexi
# 文件追加使用方式同文件写入一样
with open("C:\mysql\\text.txt", "a", encoding="utf-8") as i:
    i.write("\nhello world!")
