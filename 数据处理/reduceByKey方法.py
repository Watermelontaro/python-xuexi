import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = 'C:/Users/ZSC_PC/anaconda3/pythonw.exe'
conf = SparkConf().setMaster("local[*]").setAppName("MyApp")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([("男", 31), ("女", 73), ("男", 82), ("男", 26), ("女", 35)])
# 通过reduceByKey方法对rdd1中的每个元素进行聚合的操作
rdd2 = rdd1.reduceByKey(lambda x, y: x + y)
# 输出rdd2中的数据
print(rdd2.collect())
sc.stop()
