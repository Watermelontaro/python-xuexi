# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 16:58
# @Author : 501036554@qq.com
# @File : 异常的else和finally
# @Project : python-xuexi
try:
    print(name)
    # print("hello")
except Exception as e:
    print(e)
else:
    print("我是else")
finally:
    print("我是finally")
