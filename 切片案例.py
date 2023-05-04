# _*_ coding : utf-8 _*_
# @Time : 2023/5/4 16:54
# @Author : 501036554@qq.com
# @File : 切片案例
# @Project : python-xuexi
# 取出黑马程序员
hm = "万过薪月 员序程马黑来 nohtyp学"
# 方法一
print(hm[::-1][9:14])
# 方法二
print(hm[9:4:-1])
# 方法三
print(hm.split(" ")[1].replace("来", " ").strip()[::-1])
