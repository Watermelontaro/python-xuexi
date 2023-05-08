# _*_ coding : utf-8 _*_
# @Time : 2023/5/8 10:06
# @Author : 501036554@qq.com
# @File : file_util
# @Project : python-xuexi
def print_file_info(name):
    global f
    try:
        f = open(name, "r", encoding="utf-8")
    except Exception as e:
        print(f"发生异常！异常信息：{e}")
    else:
        print(f.read())
    finally:
        f.close()


def append_to_file(name, data):
    f = open(name, "a", encoding="utf-8")
    f.write(data)
    f.close()
