# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 18:01
# @Author : 501036554@qq.com
# @File : 集合的方法
# @Project : python-xuexi
pot = {6, 8, 5, 1, 2}
log = {1, 2, 3, 4}
# 取出pot中有，log中没有的元素 有返回值
se = pot.difference(log)
print(se)
# 删除掉pot中有，log中没有的元素 无返回值
pot.difference_update(log)
print(se)
print(pot)
# 两个集合合成一个集合
se = pot.union(log)
print(pot)
print(log)
print(se)
# 统计集合的元素数量
print(len(pot))
# 集合的遍历
for i in log:
    print(i)
