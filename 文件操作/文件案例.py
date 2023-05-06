# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 9:49
# @Author : 501036554@qq.com
# @File : 文件案例
# @Project : python-xuexi

with open("C:\mysql\word.txt", "r", encoding="utf-8") as f:
    lie = f.readlines()
    a = str(lie)
    b = list(a)
    i = "南"
    t = 0
    for j in b:
        if j == i:
            t += 1
    print(f"南出现的次数：{t}")
