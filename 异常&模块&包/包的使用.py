# _*_ coding : utf-8 _*_
# @Time : 2023/5/8 9:25
# @Author : 501036554@qq.com
# @File : 包的使用
# @Project : python-xuexi

# 导入包的几种方法
# import mybao
# import mybao.my_py1
# import mybao.my_py2
import mybao.my_py3
# from mybao import my_py1
from mybao import *
from mybao import my_py1
from mybao import my_py2
# from mybao import my_py3
# from mybao.my_py1 import bao
# from mybao.my_py2 import bao
from mybao.my_py3 import bao

mybao.my_py1.bao()
my_py3.bao()
my_py1.bao()
my_py2.bao()
bao()
