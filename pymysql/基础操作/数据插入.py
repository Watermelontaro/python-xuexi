from pymysql import Connection

comm = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='501036',
    autocommit=True  # 自动提交
)
# 选择数据库
comm.select_db('school')
# 创建游标
cursor = comm.cursor()
# 插入一条数据
effect_row = cursor.execute("insert into student values(100022,'王五',18,'男')")
# 提交事务
# comm.commit()
# 打印影响行数
print(effect_row)
# 关闭连接
comm.close()
