# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 8:01
# @Author : 501036554@qq.com
# @File : 列表
# @Project : pythonProject

# 定义列表
name_list = ["程序员", "list", "for", "王炸", [1, 2, "haha", [2, "wang"]]]
# 输出列表
print(name_list)
# 输出元素类型
print(type(name_list))
# 打印出列表的最后一个元素
print(name_list[-1])
# 打印出列表第二个元素
print(name_list[1])
# 取出列表中的列表的第2个元素
print(name_list[4][1])
# 取出列表中多层嵌套的第2个元素
print(name_list[4][3][1])
