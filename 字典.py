# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 19:08
# @Author : 501036554@qq.com
# @File : 字典
# @Project : python-xuexi
# 字典的定义
dict1 = {"wang": 11, "wu": 2, "li": 3}
# 定义空字典
dict2 = {}
dict3 = dict()
# key值不能重复
dict4 = {"li": 1, "li": 2, "wang": 3}
print(dict4)
# 字典可以嵌套 key不可，value可以
dict5 = {
    "小王": {"语文": 11, "数学": 22, "英语": 33},
    "小周": {"语文": 77, "数学": 88, "英语": 99},
    "小林": {"语文": 44, "数学": 55, "英语": 66}}
print(dict5["小周"]["语文"])
# 新增和修改
dict1["zhao"] = 55
print(dict1)
dict1["zhao"] = 66
print(dict1)
# 删除
a = dict1.pop("zhao")
print("a==", a)
print(dict1)
# 清空
dict1.clear()
print(dict1)
# 循环遍历
for key in dict5:
    print(key)
    print(dict5[key])
# 统计字典的元素数量
print(len(dict5))
