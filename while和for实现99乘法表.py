# _*_ coding : utf-8 _*_
# @Time : 2023/5/1 9:24
# @Author : 501036554@qq.com
# @File : whileqiantao
# @Project : pythonProject
i = 1
j = 1
while i < 10:
    j = 1
    while j <= i:
        #        print("{i}*{j}={i * j}")
        print("%d*%d=%d" % (j, i, (j * i)), end='\t')
        if i == j:
            print("\n")
        j += 1
    i += 1

for i1 in range(10):
    for j1 in range(1, i1 + 1):
        print(f"{j1}*{i1}={i1 * j1}", end='\t')
        if j1 == i1:
            print("\n")
