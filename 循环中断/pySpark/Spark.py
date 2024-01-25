from pyspark import SparkConf, SparkContext
# 创建SparkConf类对象
conf = SparkConf().setAppName("MyApp").setMaster("local[4]").set("spark.executor.memory", "4g")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 查看PySpark的运行版本
print(sc.version)
# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()