# 导入spark
from pyspark import SparkConf, SparkContext

# 创建spark上下文
# SparkConf()：创建spark配置对象； setMaster("local[*]"）：设置本地运行模式； setAppName("My App")：设置应用(本任务)名称
conf = SparkConf().setMaster("local[*]").setAppName("MyApp")
# SparkContext(conf=conf)：创建spark上下文对象 SparkContext():入口对象
sc = SparkContext(conf=conf)
# 输出版本号
print(sc.version)

# 停止spark上下文
sc.stop()
