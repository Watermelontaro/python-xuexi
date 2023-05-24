from pyspark import SparkConf, SparkContext

conn = SparkConf().setMaster("local[*]").setAppName("MyApp")
sc = SparkContext(conf=conn)

#  读取数据
rdd1 = sc.parallelize([1, 2, 3, 4, 5])  # list
rdd2 = sc.parallelize((1, 2, 3, 4, 5))  # tuple
rdd3 = sc.parallelize({1, 2, 3, 4, 5})  # set
rdd4 = sc.parallelize('hello')  # str
rdd5 = sc.parallelize({'name': 'zs', 'age': 18})  # dict
#  输出数据 输出数据时候需要collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())
#  读取本地文件
rdd = sc.textFile('E:/Axuexi/Python/hello.txt')
print(rdd.collect())
