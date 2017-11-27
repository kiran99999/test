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

# hello


schema = StructType([StructField("client_name", StringType(), True),
                    StructField("time", TimestampType(), True),
                    StructField("client_date", DateType(), True),
                    StructField("client_time", TimestampType(), True),
                    StructField("ss_date", DateType(), True),
                    StructField("ss_time", TimestampType(), True),
                    StructField("SS_value", DoubleType(), True),
                    StructField("work_day", StringType(), True),
                    StructField("weekday", IntegerType(), True),
                    StructField("client_identifier", IntegerType(), True),
                    StructField("datetime", DateType(), True),
                    StructField("date_identifier", IntegerType(), True)
                    ])
data1 = sqlctxt.read.csv("/Users/kiranreddy/Desktop/data.csv",header=True,inferSchema=True)
data1 = data1.drop('file_name','work_day',)
data1.show()
data1.printSchema()

data1.printSchema()
data1.columns



data1 = data1.withColumn('timedate',f.split(data1.datetime," "))
data1 = data1.withColumn('CDate',data1.timedate[0].cast(DateType()))
data1 = data1.withColumn('Ctime',data1.timedate[1].cast(TimestampType()))
data1 = data1.drop('timedate','datetime')

data1.describe().show()

data1.select(format_number('SS_value',2).alias('SS_VALUE')).show()

data1 = data1.withColumn('ss_date',data1.ss_date.cast(DateType()))

data1.printSchema()

print data1.show()

data1.write.csv("/Users/kiranreddy/Desktop/kiran.csv")

data1 = sqlctxt.read.csv("/Users/kiranreddy/Desktop/data.csv",header=True,inferSchema=True)
data1 = data1.drop('file_name','work_day',)
data1.show()
data1.printSchema()

data1 = data1.withColumn('new_Time',data1.Time.cast(TimestampType()))\
             .withColumn('ss_date',data1.ss_date.cast(TimestampType()))\
             .withColumn('ss_time',data1.ss_time.cast(TimestampType()))\
             .withColumn('Client_date',data1.Client_date.cast(DateType()))

data1.select('new_Time').show()

data1 = data1.withColumn('new_Time',from_unixtime(data1.Time,"est"))

from pyspark.sql.functions import 


