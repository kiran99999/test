from pyspark import SparkConf,SparkContext
from pyspark.sql import Row,SQLContext
conf = SparkConf().setAppName('sample csv')
sc = SparkContext.getOrCreate(conf = conf)
sqlctxt = SQLContext(sc)
data = sc.textFile('file:///Users/kiranreddy/Downloads/scala.txt')
data.take(2)
data = data.map(lambda x: x.split("\n"))
data = data.map(lambda x: [x[0],int(x[2])])
print data.take(5)
data = data.reduceByKey(lambda x,y:x+y)
print data.take(5)
data = data.toDF()
df = data.selectExpr("_1 as name", "_2 as cost")
print df.show()
print df.filter(df.name == 'kiran').show()
df.registerTempTable("df")
print type(df)
sqlctxt.sql("select * from df where cost > 150").show()
data = df.toPandas()
print data
import pyspark.sql.functions as f
from 
data = sc.textFile("file:///Users/kiranreddy/Desktop/data.csv")
data.collect()
data = data.map(lambda x: x.split(",")).map(lambda x: (x[0],x[1],x[2])).toDF(['client_name','datetime','ss_time'])
data = data.filter(data.client_name != 'client_name')
data = data.withColumn('timedate',f.split(data.datetime," "))
data = data.withColumn('Date',data.timedate[0].cast())
data = data.withColumn('Time',data.timedate[1])
data = data.drop('timedate','datetime')
data.show()
func =  udf (lambda x: datetime.strptime(x, '%Y%M%d'), DateType())

df = df1.withColumn('new_col', date_format(func(col('old_col')), 'MM-dd-yyy'))

df.show()
