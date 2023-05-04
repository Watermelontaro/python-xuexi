# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 17:18
# @Author : 501036554@qq.com
# @File : 集合
# @Project : python-xuexi

# 集合的定义
set1 = {1, 1, 2, 3, 4, 5, 6}
set2 = set()
print(type(set1))
print(type(set2))
print(set1)
print(len(set1))
for i in set1:
    print(i)
# 在集合中，元素不重复，且无序
# 添加新元素
set2.add("ip")
print(set2)
# 移除元素
set1.remove(1)
print(set1)
# 取出元素
print(set1)
print(set1.pop())

print(set1)
# 清空元素
set1.clear()
print(set1)
