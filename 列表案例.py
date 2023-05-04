# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 9:57
# @Author : 501036554@qq.com
# @File : 列表案例
# @Project : pythonProject
age = [21, 25, 21, 23, 22, 20]
print(age)
# 追加元素
age.append(31)
print(age)
age1 = [29, 33, 30]
age.extend(age1)
print(age)
print(age[0])
print(age[-1])
print(age.index(31))
# 循环遍历
# while
print(age)
i = 0
while i < len(age):
    # 输出偶数
    if age[i] % 2 == 0:
        print(age[i])
    i += 1

# for
print(age)
i = 0
for i in age:
    # print(i)
    # 输出偶数
    if i % 2 == 0:
        print(i)
