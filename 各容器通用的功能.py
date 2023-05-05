# _*_ coding : utf-8 _*_
# @Time : 2023/5/5 10:44
# @Author : 501036554@qq.com
# @File : 各容器通用的方法
# @Project : python-xuexi

# print("tuple1", max(tuple1))
# print("set1：", max(set1))
# print("dict1：", max(dict1))
# print("name：", max(name))
# print("tuple：1", max(tuple1))
name1 = [1, 2, 3]  # 列表
name2 = (1, 2, 3)  # 元组
name3 = {1, 2, 3}  # 集合
name4 = "hello world z"  # 字符串
name5 = {"w1": 18, "w2": 20, "w3": 55, "w4": 60}  # 字典
# 找出最大
print(max(name1))
print(max(name2))
print(max(name3))
print(max(name4))
print(max(name5))
# 找出最小
print(min(name1))
print(min(name2))
print(min(name3))
print(min(name4))
print(min(name5))
# 容器类型可以互相转换。但是不能转换为字典类型，因为缺少value值
# 转为list列表
print(list(name1))
print(list(name2))
print(list(name3))
print(list(name4))
print(list(name5))
# 转为tuple元组
print(tuple(name1))
print(tuple(name2))
print(tuple(name3))
print(tuple(name4))
print(tuple(name5))
# 转为str字符串
print(str(name1))
print(str(name2))
print(str(name3))
print(str(name4))
print(str(name5))
# 转为set集合
print(set(name1))
print(set(name2))
print(set(name3))
print(set(name4))
print(set(name5))
