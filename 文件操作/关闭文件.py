# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 9:17
# @Author : 501036554@qq.com
# @File : 关闭文件
# @Project : python-xuexi

f = open("C:\mysql\mysql-5.7.38-winx64\my.ini", "r", encoding="utf-8")
f.read()
# 让程序暂停50000秒，在此期间，文件一直被占用
# time.sleep(50000)
# 程序结束和使用close方法可以使文件关闭
f.close()
