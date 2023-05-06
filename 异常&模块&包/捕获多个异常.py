# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 16:44
# @Author : 501036554@qq.com
# @File : 捕获多个异常
# @Project : python-xuexi
# 捕获多个异常

try:
    print(name)
    # 1 / 0

except (NameError, ZeroDivisionError) as e:
    print(f"出现异常，异常说明:{e}")
