# _*_ coding : utf-8 _*_
# @Time : 2023/5/1 14:53
# @Author : 501036554@qq.com
# @File : for1
# @Project : pythonProject
i = "app data ace apl var for whale china"
s = 0
for j in i:
    if j == 'a':
        s += 1
        print(j, end='\t')
print("\n字母a出现的次数是%d" % s)
for i in range(2, 14, 3):
    print(i)
