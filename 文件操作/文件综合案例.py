# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 11:35
# @Author : 501036554@qq.com
# @File : 文件综合案例
# @Project : python-xuexi
i = open("C:\mysql\\bill.txt", "r", encoding="utf-8")
for j in i:
    m = j.replace("\n", " ")
    m = m.strip()
    print(m)
    a, b = m[-2], m[-1]
    a = a + b
    print(a)
    if a != "测试":
        with open("C:\mysql\\bill.txt.bak", "a", encoding="utf-8") as l:
            l.write(j)
            print("正式：", j)
