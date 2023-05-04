# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 11:16
# @Author : 501036554@qq.com
# @File : 元组案例
# @Project : pythonProject

# 元组实现的案例
people = ("周杰轮", 11, ["football", 'music'])
print(people.index(11))
print(people[0])
# del people[2][0]
people[2].pop(0)
print(people)
people[2].append("coding")
print(people)
