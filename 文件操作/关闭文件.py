# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 9:17
# @Author : 501036554@qq.com
# @File : 关闭文件
# @Project : python-xuexi

f = open("C:\mysql\mysql-5.7.38-winx64\my.ini", "r", encoding="utf-8")
f.read()
# 让程序睡眠50000秒，在此期间，文件一直被占用
# time.sleep(50000)
# 程序结束和使用close方法可以使文件关闭
f.close()
# with open语法自动关闭文件
with open("C:\mysql\mysql-5.7.38-winx64\my.ini", "r", encoding="utf-8") as j:
    for ll in j:
        print(ll)

# time.sleep(50000)
