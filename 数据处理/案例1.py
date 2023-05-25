import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = 'C:/Users/ZSC_PC/anaconda3/pythonw.exe'

conf = SparkConf().setMaster("local[*]").setAppName("MyApp")
sc = SparkContext(conf=conf)
# 将hello.txt文件转换为RDD，并将每一行数据切分为单词，将每个单词映射为(word,1)的形式，
# 然后再通过reduceByKey方法对每个单词进行统计，最后输出统计结果
text = sc.textFile("E:\Axuexi\Python\hello.txt").flatMap(lambda x: x.split(" ")). \
    map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
# 输出rdd2中的数据
print(text.collect())
sc.stop()
