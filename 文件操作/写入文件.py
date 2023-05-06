# _*_ coding : utf-8 _*_
# @Time : 2023/5/6 11:12
# @Author : 501036554@qq.com
# @File : 写入文件
# @Project : python-xuexi

# 使用open的w模式写入
with open("C:\mysql\\text.txt", "w", encoding="utf-8") as i:
    # write会把内容写入内存中积攒起来
    i.write("hello world!")
    # flush将内存中积攒的内容写入文件中去；close方法包含了flush的功能； with open自带有close；所以使用with open不需要手动保存
