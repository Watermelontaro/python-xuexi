# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 10:32
# @Author : 501036554@qq.com
# @File : 元组
# @Project : pythonProject

# 定义元组字面量
("王炸", 1, 2, "add")
# 定义元组的变量
tuple1 = ("王炸", 1, 2, "add")
# 定义空元组
tuple2 = ()
tuple3 = tuple()
name = ("王炸")
print(name, type(name))
name = ("王炸",)
print(name, type(name))

# 元组嵌套
up = (("zhao", "qian", "sun", "li"), ("zhou", "wu", "zheng", "wang"), "add", "add", 1, 2, 3, "name", "age", "name")
# 取出wang
print(up[1][3])
# 查询某个元素，并返回下标
print(up.index("name"))
# 统计某个元素在元组中的个数
print(up.count("name"))
# 计元组中的所有元素的个数
print(len(up))

# 遍历
# while
index = 0
while index < len(up):
    print(up[index])
    index += 1

# for
for i in up:
    print(i)
