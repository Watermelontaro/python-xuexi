# _*_ coding : utf-8 _*_
# @Time : 2023/5/8 8:45
# @Author : 501036554@qq.com
# @File : 自定义模块的使用
# @Project : python-xuexi


# 导入模块
from 自定义模块 import *
# import 自定义模块
from 自定义模块1 import te

# 同时调用te函数 后调用的会生效
try:
    te(5, 5)
    # 自定义模块.teb(2, 1)
    # 自定义模块.tec(2, 1)
    teb(2, 1)
    tec(2, 1)
except Exception as e:
    print(e)
