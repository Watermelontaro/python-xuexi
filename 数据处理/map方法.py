import os

from pyspark import SparkConf, SparkContext

# 设置Python环境变量
os.environ['PYSPARK_PYTHON'] = 'C:/Users/ZSC_PC/anaconda3/pythonw.exe'
# 创建spark上下文
conf = SparkConf().setMaster("local[*]").setAppName("MyApp")
sc = SparkContext(conf=conf)

# 准被一个RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# 通过map方法对rdd1中的每个元素进行乘以10的操作
rdd2 = rdd1.map(lambda x: x * 10)
# 输出rdd2中的数据
print(rdd2.collect())
# 关闭spark上下文
sc.stop()
