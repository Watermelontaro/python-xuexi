import os

from pyspark import SparkConf, SparkContext

# 设置Python环境变量
os.environ['PYSPARK_PYTHON'] = 'C:/Users/ZSC_PC/anaconda3/pythonw.exe'
# 创建spark上下文
conf = SparkConf().setMaster("local[*]").setAppName("MyApp")
sc = SparkContext(conf=conf)
# 准被一个RDD
rdd1 = sc.parallelize(["hello world", "hello spark", "hello hadoop"])
# 通过flatMap方法对rdd1中的每个元素进行切分的操作，
rdd2 = rdd1.flatMap(lambda x: x.split(" "))
# 输出rdd2中的数据
print(rdd2.collect())
# 关闭spark上下文
sc.stop()
