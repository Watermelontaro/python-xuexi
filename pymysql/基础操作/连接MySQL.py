from pymysql import Connection

# 创建连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='501036'
)
# 创建游标
cursor = conn.cursor()
# 选择数据库
conn.select_db('school')
# 执行SQL，并返回收影响行数
# effect_row = cursor.execute('create table student(id int, name varchar(20))')
# 执行SQL,查询数据
cursor.execute('select * from student')
# 打印数据
# print(cursor.fetchall())
# 遍历数据
for row in cursor.fetchall():
    print(row)
# 打印数据库版本号
print(conn.get_server_info())

# 关闭连接
conn.close()
