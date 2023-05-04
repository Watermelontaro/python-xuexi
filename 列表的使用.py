# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 8:37
# @Author : 501036554@qq.com
# @File : 列表的使用
# @Project : pythonProject
from 函数定义 import my_len

# 定义列表
list1 = [1, "王炸", "蘑菇头", [2, "黑马", "程序员", "list"], "age", "name", "add", "network"]

# 使用查找元素方法index
print(list1.index("王炸"))
print(list1.index(1))
print(list1.index("add"))
# 如果查不到会报ValueError错误提示
# print(list1.index(2))

# 通过下标修改元素值
list1[0] = "哈哈"
print(list1[0])

# 使用insert插入元素值
list1.insert(0, "我是插入的元素")
print(list1)

# 使用append追加元素
list1.append("我是追加的元素")
print(list1)

# extend:将多个元素追加到列表尾部,两种追加方式
list2 = [1, 2, 3]
# list1.extend(list2)
list1.extend([2, 3, [1, 2]])
print(list1)

# 通过下标删除元素，两种方法
# 通过关键字del
del list1[0]
print(list1)
# 通过pop方法
list1.pop(-1)
print(list1)

# 通过元素删除
list1.remove("add")
print(list1)

# 统计某元素在列表中的个数
print(list1.count(2))

# 统计列表中所有元素的个数
print(len(list1))
print(my_len(list1))

# 清空元素
list1.clear()
print(list1)
