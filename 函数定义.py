# _*_ coding : utf-8 _*_
# @Time : 2023/5/2 10:43
# @Author : 501036554@qq.com
# @File : 认识函数
# @Project : pythonProject


# 定义一个自定义函数
# def：定义函数的关键字
def my_len(date):
    const = 0
    for i in date:
        const += 1
    print(f"字符串{date}的长度是{const}")
    return const
