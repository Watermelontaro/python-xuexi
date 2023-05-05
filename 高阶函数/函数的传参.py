# _*_ coding : utf-8 _*_
# @Time : 2023/5/5 14:50
# @Author : 501036554@qq.com
# @File : 函数的传参
# @Project : python-xuexi

# 函数的多种传参方式
# 位置传参（最常用的）
def func(name, age, gender):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")


func("小王", 18, "男")

# 关键字传参
func(age=20, gender="女", name="小红")


#  缺省参数
def func(name, gender, age=18):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")


func(gender="男", name="小蓝")
func("小兰", "女", 50)


# 不定长参数
# 位置不定长
def func(*args):
    print(f"args的类型是：{type(args)},它的值为：{args}")


func(1, 5, 6, "小王", "hello")


# 关键字不定长
def func(**kwargs):
    print(f"kwargs的类型是：{type(kwargs)},它的值为：{kwargs}")


func(name="小王", age=18, gender="女")
