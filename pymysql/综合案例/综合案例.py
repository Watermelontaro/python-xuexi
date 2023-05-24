from pymysql import Connection

import data_define
from file_define import TextFileReader, JsonFileReader

text_file_reader = TextFileReader("E:\Axuexi\Python\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:\Axuexi\Python\\2011年2月销售数据JSON.txt")

jan_data: list[data_define.Record] = text_file_reader.read_data()
fed_data: list[data_define.Record] = json_file_reader.read_data()
# 将两个list合并成一个list
all_data: list[data_define.Record] = jan_data + fed_data

# 构建MySQL数据库连接

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="501036",
    autocommit=True,
)
# 获得游标
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 执行SQL语句
for record in all_data:
    # 添加数据
    sql = f"insert into orders values('{record.date}', " \
          f"'{record.order_id}', {record.money}, '{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)

# 关闭数据库连接
conn.close()
