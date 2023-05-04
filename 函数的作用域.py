# _*_ coding : utf-8 _*_
# @Time : 2023/5/3 10:34
# @Author : 501036554@qq.com
# @File : 函数的作用域
# @Project : pythonProject
def tset_a(a):
    num = a
    print(f"输出num：{num}")


tset_a(100)
# 函数的作用域num只有在tset_a中有定义，从函数tset_a外面无法获取到num的值；因为它未定义
# print(num)

# 局部变量修改不影响全局变量
a = 100


def aa():
    a = 1000
    print(f"aa()中a={a}")


def bb():
    print(f"dd()中a={a}")


aa()
bb()
print(f"a修改前a={a}")
a = 2000
print(f"a修改后a={a}")
# 局部变量修改不影响全局变量，可使用gro
aa = 100


def a():
    global aa
    aa = 1000
    print(f"a()中aa={aa}")


def b():
    print(f"d()中aa={aa}")


b()
a()

print(f"a修改前aa={aa}")
aa = 2000
print(f"a修改后aa={aa}")
