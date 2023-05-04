# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 11:33
# @Author : 501036554@qq.com
# @File : 字符串
# @Project : pythonProject

# 字符串
name = "    jiningzhiyejishuxueyuan and jiningshi    "
# name[0] = "H"
print(name)
print(name.index("j"))
a = name.replace("j", "J")
print(a)
b = name.split("j")
print(b)
print(name)
print(name.strip())
print(name.strip("ji"))
print(name.count("n"))
print(len(name))
