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



Client name	File Name	Time	Client Date	Client Time	SS_DATE	SS Time (EST)	SS_TIME_VALUE	week_day	weekday	Client_Identifier	DATETIME	Date_Identifier
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Aug  1 10:14 Alger_Orders_20160801100959.csv.20160801101415281	10:14	8/1/2016	10:09:59	2016-01-08	10:14:15	0.426563	Mon	1	1	2016-08-01 10:14	1
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Aug  1 12:28 Alger_Orders_20160801122629.csv.20160801122824071	12:28	8/1/2016	12:26:29	2016-01-08	12:28:24	0.519722	Mon	1	1	2016-08-01 12:28	1
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1707 Aug  1 04:33 SSC_BAM_FXREQ_20160801_093027.csv.pgp.ndm05.20160801043356900	4:33	8/1/2016	9:30:27	2016-01-08	4:33:56	0.190231	Mon	1	3	2016-08-01 04:33	1
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1932 Aug  1 05:33 SSC_BAM_FXREQ_20160801_103030.csv.pgp.ndm05.20160801053302243	5:33	8/1/2016	10:30:30	2016-01-08	5:33:02	0.231273	Mon	1	3	2016-08-01 05:33	1
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Aug  1 09:33 SSC_BAM_FXREQ_20160801_143039.csv.pgp.ndm05.20160801093342569	9:33	8/1/2016	14:30:39	2016-01-08	9:33:42	0.398403	Mon	1	3	2016-08-01 09:33	1
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1419 Aug  1 11:32 SSC_BAM_FXREQ_20160801_163044.csv.pgp.ndm05.20160801113251055	11:32	8/1/2016	16:30:44	2016-01-08	11:32:51	0.481146	Mon	1	3	2016-08-01 11:32	1
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug  1 12:34 SSC_BAM_FXREQ_20160801_173046.csv.pgp.ndm05.20160801123457804	12:34	8/1/2016	17:30:46	2016-01-08	12:34:57	0.524271	Mon	1	3	2016-08-01 12:34	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:37 BCRTOFX.txt.20160801063759045	6:37			2016-01-08	6:37:59	0.276377	Mon	1	4	2016-08-01 06:37	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:37 BCRTOFX.txt.20160801063759257	6:37			2016-01-08	6:37:59	0.276377	Mon	1	4	2016-08-01 06:37	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:37 BCRTOFX.txt.20160801063759459	6:37			2016-01-08	6:37:59	0.276377	Mon	1	4	2016-08-01 06:37	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:37 BCRTOFX.txt.20160801063759656	6:37			2016-01-08	6:37:59	0.276377	Mon	1	4	2016-08-01 06:37	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:37 BCRTOFX.txt.20160801063759861	6:37			2016-01-08	6:37:59	0.276377	Mon	1	4	2016-08-01 06:37	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:38 BCRTOFX.txt.20160801063800066	6:38			2016-01-08	6:38:00	0.276389	Mon	1	4	2016-08-01 06:38	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:38 BCRTOFX.txt.20160801063800580	6:38			2016-01-08	6:38:00	0.276389	Mon	1	4	2016-08-01 06:38	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:38 BCRTOFX.txt.20160801063800886	6:38			2016-01-08	6:38:00	0.276389	Mon	1	4	2016-08-01 06:38	1
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  1 06:38 BCRTOFX.txt.20160801063801074	6:38			2016-01-08	6:38:01	0.2764	Mon	1	4	2016-08-01 06:38	1
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3589 Aug  1 14:36 BRA_BRA_Ver_20160801.csv.20160801143613048	14:36	8/1/2016		2016-01-08	14:36:13	0.608484	Mon	1	5	2016-08-01 14:36	1
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       218 Aug  1 05:26 scbcnhtrades1.in.201608011714.20160801052601066	5:26	8/1/2016	17:14:00	2016-01-08	5:26:01	0.2264	Mon	1	7	2016-08-01 05:26	1
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  1 05:26 scbcnhtrades2.in.201608011714.20160801052601297	5:26	8/1/2016	17:14:00	2016-01-08	5:26:01	0.2264	Mon	1	7	2016-08-01 05:26	1
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1011 Aug  1 10:08 SPOT_FET_Instructions_StateStreet_20160801-155859.csv.20160801100814882	10:08	8/1/2016	15:58:59	2016-01-08	10:08:14	0.422384	Mon	1	7	2016-08-01 10:08	1
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  1 17:18 08012016_GAM_GAM_STAR_GS.20160801.csv.20160801171825912	17:18	8/1/2016		2016-01-08	17:18:25	0.721123	Mon	1	9	2016-08-01 17:18	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug  1 10:34 trade10.dat.20160801103416549	10:34			2016-01-08	10:34:16	0.440463	Mon	1	10	2016-08-01 10:34	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Aug  1 12:34 trade10.dat.20160801123426767	12:34			2016-01-08	12:34:26	0.523912	Mon	1	10	2016-08-01 12:34	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Aug  1 14:34 trade10.dat.20160801143412537	14:34			2016-01-08	14:34:12	0.607083	Mon	1	10	2016-08-01 14:34	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     22564 Aug  1 16:24 trade10.dat.20160801162418895	16:24			2016-01-08	16:24:18	0.683542	Mon	1	10	2016-08-01 16:24	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  1 17:04 trade10.dat.20160801170424582	17:04			2016-01-08	17:04:24	0.711389	Mon	1	10	2016-08-01 17:04	1
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  1 18:04 trade10.dat.20160801180430595	18:04			2016-01-08	18:04:30	0.753125	Mon	1	10	2016-08-01 18:04	1
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    318325 Aug  1 09:00 passporttrans.20160801.csv.20160801090008215	9:00	8/1/2016		2016-01-08	9:00:08	0.375093	Mon	1	15	2016-08-01 09:00	1
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1645 Aug  1 08:32 HighlandCapitalManagementRecon201608010730.csv.20160801083206695	8:32	8/1/2016	7:30:00	2016-01-08	8:32:06	0.355625	Mon	1	16	2016-08-01 08:32	1
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       188 Aug  1 13:40 Highland_Orders_20160801csv.20160801134008651	13:40	8/1/2016		2016-01-08	13:40:08	0.569537	Mon	1	16	2016-08-01 13:40	1
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       479 Aug  1 03:03 HSBC-LKR.in.01082016-1.20160801030351186	3:03	1/8/2016		2016-01-08	3:03:51	0.127674	Mon	1	17	2016-08-01 03:03	1
John Hancock Investments	HAN_TRANS_HANVER_20160722.csv.20160801155015611	15:50	7/22/2016		2016-01-08	15:50:15	0.659896	Mon	1	18	2016-08-01 15:50	1
John Hancock Investments	HAN_TRANS_HANVER_20160801.csv.20160801155216142	15:52	8/1/2016		2016-01-08	15:52:16	0.661296	Mon	1	18	2016-08-01 15:52	1
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       222 Aug  1 06:37 NOS_SFX_20160801.csv.20160801063758661	6:37	8/1/2016		2016-01-08	6:37:58	0.276366	Mon	1	21	2016-08-01 06:37	1
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       178 Aug  1 11:28 NOS_SFX_20160801_TRY.csv.20160801112820574	11:28	8/1/2016		2016-01-08	11:28:20	0.478009	Mon	1	21	2016-08-01 11:28	1
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       210 Aug  1 08:20 PGI_Orders_20160801071744.csv.20160801082005257	8:20	8/1/2016	7:17:44	2016-01-08	8:20:05	0.34728	Mon	1	24	2016-08-01 08:20	1
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       207 Aug  1 16:32 PGI_Orders_20160801153059.csv.20160801163219870	16:32	8/1/2016	15:30:59	2016-01-08	16:32:19	0.689109	Mon	1	24	2016-08-01 16:32	1
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Aug  1 03:17 FT_fx_20160801_091606.csv.20160801031752080	3:17	8/1/2016	9:16:06	2016-01-08	3:17:52	0.137407	Mon	1	26	2016-08-01 03:17	1
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug  1 03:51 INV_fx_20160801_094922.csv.20160801035154617	3:51	8/1/2016	9:49:22	2016-01-08	3:51:54	0.161042	Mon	1	26	2016-08-01 03:51	1
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug  1 05:11 INV_fx_20160801_110830.csv.20160801051159691	5:11	8/1/2016	11:08:30	2016-01-08	5:11:59	0.216655	Mon	1	26	2016-08-01 05:11	1
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       230 Aug  1 05:18 FT_fx_20160801_111527.csv.20160801051800400	5:18	8/1/2016	11:15:27	2016-01-08	5:18:00	0.220833	Mon	1	26	2016-08-01 05:18	1
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug  1 05:40 FT_fx_20160801_113730.csv.20160801054002776	5:40	8/1/2016	11:37:30	2016-01-08	5:40:02	0.236134	Mon	1	26	2016-08-01 05:40	1
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        59 Aug  1 04:21 citicnhtrades.in.201608011607.20160801042156232	4:21	8/1/2016	16:07:00	2016-01-08	4:21:56	0.181898	Mon	1	28	2016-08-01 04:21	1
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  1 05:28 citicnhtrades.in.201608011715.20160801052801610	5:28	8/1/2016	17:15:00	2016-01-08	5:28:01	0.227789	Mon	1	28	2016-08-01 05:28	1
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       288 Aug  1 05:28 hsbccnhtrades.in.201608011715.20160801052801785	5:28	8/1/2016	17:15:00	2016-01-08	5:28:01	0.227789	Mon	1	29	2016-08-01 05:28	1
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23920 Aug  1 10:40 RSWGD1-17_SSGM_Confirmed_File__20160801.csv.20160801104017738	10:40	8/1/2016		2016-01-08	10:40:17	0.444641	Mon	1	30	2016-08-01 10:40	1
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     10860 Aug  1 09:32 TIAACREFREPAT.csv.20160801093211307	9:32			2016-01-08	9:32:11	0.39735	Mon	1	32	2016-08-01 09:32	1
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     12310 Aug  1 13:32 TIAACREFREPAT.csv.20160801133207797	13:32			2016-01-08	13:32:07	0.56397	Mon	1	32	2016-08-01 13:32	1
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       471 Aug  1 21:32 tokyofundtrades.in.201608020902.20160801213243557	21:32	8/2/2016	9:02:00	2016-01-08	21:32:43	0.89772	Mon	1	33	2016-08-01 21:32	1
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       688 Aug  1 23:14 tokyofundtrades.in.201608021101.20160801231421207	23:14	8/2/2016	11:01:00	2016-01-08	23:14:21	0.968299	Mon	1	33	2016-08-01 23:14	1
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       191 Aug  2 15:21 Alger_Orders_20160802151941.csv.20160802152119615	15:21	8/2/2016	15:19:41	2016-02-08	15:21:19	0.639803	Tue	2	1	2016-08-02 15:21	2
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1528 Aug  2 04:33 SSC_BAM_FXREQ_20160802_093029.csv.pgp.ndm05.20160802043305929	4:33	8/2/2016	9:30:29	2016-02-08	4:33:05	0.189641	Tue	2	3	2016-08-02 04:33	2
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug  2 06:33 SSC_BAM_FXREQ_20160802_113035.csv.pgp.ndm05.20160802063305677	6:33	8/2/2016	11:30:35	2016-02-08	6:33:05	0.272975	Tue	2	3	2016-08-02 06:33	2
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Aug  2 10:33 SSC_BAM_FXREQ_20160802_153049.csv.pgp.ndm05.20160802103329855	10:33	8/2/2016	15:30:49	2016-02-08	10:33:29	0.439919	Tue	2	3	2016-08-02 10:33	2
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1436 Aug  2 11:33 SSC_BAM_FXREQ_20160802_163054.csv.pgp.ndm05.20160802113334490	11:33	8/2/2016	16:30:54	2016-02-08	11:33:34	0.481644	Tue	2	3	2016-08-02 11:33	2
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1540 Aug  2 12:33 SSC_BAM_FXREQ_20160802_173058.csv.pgp.ndm05.20160802123339624	12:33	8/2/2016	17:30:58	2016-02-08	12:33:39	0.523368	Tue	2	3	2016-08-02 12:33	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063806268	6:38			2016-02-08	6:38:06	0.276458	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063806610	6:38			2016-02-08	6:38:06	0.276458	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063806802	6:38			2016-02-08	6:38:06	0.276458	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063807109	6:38			2016-02-08	6:38:07	0.27647	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063807386	6:38			2016-02-08	6:38:07	0.27647	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063807635	6:38			2016-02-08	6:38:07	0.27647	Tue	2	4	2016-08-02 06:38	2
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  2 06:38 BCRTOFX.txt.20160802063807799	6:38			2016-02-08	6:38:07	0.27647	Tue	2	4	2016-08-02 06:38	2
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4198 Aug  2 14:41 BRA_BRA_Ver_20160802.csv.20160802144117762	14:41	8/2/2016		2016-02-08	14:41:17	0.612002	Tue	2	5	2016-08-02 14:41	2
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug  2 14:35 CDPSfx_BRLorder.20160802.143306.csv.20160802143517354	14:35	8/2/2016	14:33:06	2016-02-08	14:35:17	0.607836	Tue	2	6	2016-08-02 14:35	2
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       437 Aug  2 10:16 SPOT_FET_Instructions_StateStreet_20160802-160634.csv.20160802101656310	10:16	8/2/2016	16:06:34	2016-02-08	10:16:56	0.428426	Tue	2	7	2016-08-02 10:16	2
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       254 Aug  2 17:19 08022016_GAM_GAM_STAR_GS.20160802.csv.20160802171928366	17:19	8/2/2016		2016-02-08	17:19:28	0.721852	Tue	2	9	2016-08-02 17:19	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  2 10:32 trade10.dat.20160802103259520	10:32			2016-02-08	10:32:59	0.439572	Tue	2	10	2016-08-02 10:32	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  2 12:33 trade10.dat.20160802123309349	12:33			2016-02-08	12:33:09	0.523021	Tue	2	10	2016-08-02 12:33	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5204 Aug  2 14:33 trade10.dat.20160802143316651	14:33			2016-02-08	14:33:16	0.606435	Tue	2	10	2016-08-02 14:33	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9544 Aug  2 16:23 trade10.dat.20160802162322657	16:23			2016-02-08	16:23:22	0.682894	Tue	2	10	2016-08-02 16:23	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  2 17:03 trade10.dat.20160802170325473	17:03			2016-02-08	17:03:25	0.710706	Tue	2	10	2016-08-02 17:03	2
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  2 18:03 trade10.dat.20160802180333810	18:03			2016-02-08	18:03:33	0.752465	Tue	2	10	2016-08-02 18:03	2
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       179 Aug  2 06:21 UKFCMCurrencyTemplate020816.csv.20160802062104946	6:21			2016-02-08	6:21:04	0.26463	Tue	2	11	2016-08-02 06:21	2
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    289478 Aug  2 08:54 passporttrans.20160802.csv.20160802085450110	8:54	8/2/2016		2016-02-08	8:54:50	0.371412	Tue	2	15	2016-08-02 08:54	2
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug  2 08:31 HighlandCapitalManagementRecon201608020730.csv.20160802083116022	8:31	8/2/2016	7:30:00	2016-02-08	8:31:16	0.355046	Tue	2	16	2016-08-02 08:31	2
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       481 Aug  2 03:40 HSBC-LKR.in.02082016-1.20160802034032912	3:40	2/8/2016		2016-02-08	3:40:32	0.153148	Tue	2	17	2016-08-02 03:40	2
John Hancock Investments	HAN_TRANS_HANVER_20160802.csv.20160802154120436	15:41	8/2/2016		2016-02-08	15:41:20	0.653704	Tue	2	18	2016-08-02 15:41	2
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr      9927 Aug  2 06:39 NOS_SFX_20160802.csv.20160802063908048	6:39	8/2/2016		2016-02-08	6:39:08	0.277176	Tue	2	21	2016-08-02 06:39	2
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr      9927 Aug  2 07:27 NOS_SFX_20160802.csv.20160802072711711	7:27	8/2/2016		2016-02-08	7:27:11	0.310544	Tue	2	21	2016-08-02 07:27	2
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr      9927 Aug  2 07:29 NOS_SFX_20160802_THB.csv.20160802072911963	7:29	8/2/2016		2016-02-08	7:29:11	0.311933	Tue	2	21	2016-08-02 07:29	2
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       181 Aug  2 07:39 NOS_SFX_20160802_THB2.csv.20160802073912566	7:39	8/2/2016		2016-02-08	7:39:12	0.318889	Tue	2	21	2016-08-02 07:39	2
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       202 Aug  2 12:05 PGI_Orders_20160802110316.csv.20160802120506691	12:05	8/2/2016	11:03:16	2016-02-08	12:05:06	0.503542	Tue	2	24	2016-08-02 12:05	2
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug  2 03:12 FT_fx_20160802_091002.csv.20160802031231204	3:12	8/2/2016	9:10:02	2016-02-08	3:12:31	0.133692	Tue	2	26	2016-08-02 03:12	2
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug  2 04:28 FT_fx_20160802_102547.csv.20160802042835345	4:28	8/2/2016	10:25:47	2016-02-08	4:28:35	0.186516	Tue	2	26	2016-08-02 04:28	2
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Aug  2 04:38 INV_fx_20160802_103538.csv.20160802043836583	4:38	8/2/2016	10:35:38	2016-02-08	4:38:36	0.193472	Tue	2	26	2016-08-02 04:38	2
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug  2 05:04 INV_fx_20160802_110344.csv.20160802050437611	5:04	8/2/2016	11:03:44	2016-02-08	5:04:37	0.211539	Tue	2	26	2016-08-02 05:04	2
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22867 Aug  2 10:49 RSWGD1-17_SSGM_Confirmed_File__20160802.csv.20160802104900946	10:49	8/2/2016		2016-02-08	10:49:00	0.450694	Tue	2	30	2016-08-02 10:49	2
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7342 Aug  2 09:30 TIAACREFREPAT.csv.20160802093053098	9:30			2016-02-08	9:30:53	0.396447	Tue	2	32	2016-08-02 09:30	2
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       769 Aug  2 21:47 tokyofundtrades.in.201608030923.20160802214716131	21:47	8/3/2016	9:23:00	2016-02-08	21:47:16	0.907824	Tue	2	33	2016-08-02 21:47	2
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       618 Aug  2 23:39 tokyofundtrades.in.201608031044.20160802233923725	23:39	8/3/2016	10:44:00	2016-02-08	23:39:23	0.985683	Tue	2	33	2016-08-02 23:39	2
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       356 Aug  2 10:24 TrinityStreetFX_080216.csv.20160802102458830	10:24			2016-02-08	10:24:58	0.434005	Tue	2	34	2016-08-02 10:24	2
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       256 Aug  3 16:21 Alger_Orders_20160803161803.csv.20160803162157372	16:21	8/3/2016	16:18:03	2016-03-08	16:21:57	0.68191	Wed	3	1	2016-08-03 16:21	3
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug  3 06:14 SSC_BAM_FXREQ_20160803_103017.csv.pgp.ndm05.20160803061445405	6:14	8/3/2016	10:30:17	2016-03-08	6:14:45	0.260243	Wed	3	3	2016-08-03 06:14	3
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1456 Aug  3 11:32 SSC_BAM_FXREQ_20160803_163043.csv.pgp.ndm05.20160803113239146	11:32	8/3/2016	16:30:43	2016-03-08	11:32:39	0.481007	Wed	3	3	2016-08-03 11:32	3
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1430 Aug  3 12:34 SSC_BAM_FXREQ_20160803_173046.csv.pgp.ndm05.20160803123414519	12:34	8/3/2016	17:30:46	2016-03-08	12:34:14	0.523773	Wed	3	3	2016-08-03 12:34	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063846370	6:38			2016-03-08	6:38:46	0.276921	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063846656	6:38			2016-03-08	6:38:46	0.276921	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063846837	6:38			2016-03-08	6:38:46	0.276921	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063847045	6:38			2016-03-08	6:38:47	0.276933	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063847233	6:38			2016-03-08	6:38:47	0.276933	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063847435	6:38			2016-03-08	6:38:47	0.276933	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063847640	6:38			2016-03-08	6:38:47	0.276933	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063847832	6:38			2016-03-08	6:38:47	0.276933	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063848050	6:38			2016-03-08	6:38:48	0.276944	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063848232	6:38			2016-03-08	6:38:48	0.276944	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063848433	6:38			2016-03-08	6:38:48	0.276944	Wed	3	4	2016-08-03 06:38	3
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  3 06:38 BCRTOFX.txt.20160803063848629	6:38			2016-03-08	6:38:48	0.276944	Wed	3	4	2016-08-03 06:38	3
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3302 Aug  3 14:39 BRA_BRA_Ver_20160803.csv.20160803143952196	14:39	8/3/2016		2016-03-08	14:39:52	0.611019	Wed	3	5	2016-08-03 14:39	3
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       337 Aug  3 16:33 CDPSfx_IDRorder.20160803.163500.csv.20160803163359268	16:33	8/3/2016	16:35:00	2016-03-08	16:33:59	0.690266	Wed	3	6	2016-08-03 16:33	3
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug  3 16:33 CDPSfx_THBorder.20160803.163500.csv.20160803163359473	16:33	8/3/2016	16:35:00	2016-03-08	16:33:59	0.690266	Wed	3	6	2016-08-03 16:33	3
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       335 Aug  3 20:34 CDPSfx_TWDorder.20160803.203500.csv.20160803203422723	20:34	8/3/2016	20:35:00	2016-03-08	20:34:22	0.857199	Wed	3	6	2016-08-03 20:34	3
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       648 Aug  3 05:43 scbcnhtrades1.in.201608031734.20160803054343089	5:43	8/3/2016	17:34:00	2016-03-08	5:43:43	0.238692	Wed	3	7	2016-08-03 05:43	3
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  3 05:43 scbcnhtrades2.in.201608031734.20160803054343420	5:43	8/3/2016	17:34:00	2016-03-08	5:43:43	0.238692	Wed	3	7	2016-08-03 05:43	3
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       865 Aug  3 09:29 SPOT_FET_Instructions_StateStreet_20160803-152029.csv.20160803092930266	9:29	8/3/2016	15:20:29	2016-03-08	9:29:30	0.395486	Wed	3	7	2016-08-03 09:29	3
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  3 16:52 08032016_GAM_GAM_STAR_GS.20160803.csv.20160803165200951	16:52	8/3/2016		2016-03-08	16:52:00	0.702778	Wed	3	9	2016-08-03 16:52	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  3 10:33 trade10.dat.20160803103334904	10:33			2016-03-08	10:33:34	0.439977	Wed	3	10	2016-08-03 10:33	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  3 12:33 trade10.dat.20160803123344027	12:33			2016-03-08	12:33:44	0.523426	Wed	3	10	2016-08-03 12:33	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      7374 Aug  3 14:33 trade10.dat.20160803143351675	14:33			2016-03-08	14:33:51	0.60684	Wed	3	10	2016-08-03 14:33	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     32112 Aug  3 16:23 trade10.dat.20160803162357805	16:23			2016-03-08	16:23:57	0.683299	Wed	3	10	2016-08-03 16:23	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  3 17:04 trade10.dat.20160803170402631	17:04			2016-03-08	17:04:02	0.711134	Wed	3	10	2016-08-03 17:04	3
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  3 18:04 trade10.dat.20160803180411905	18:04			2016-03-08	18:04:11	0.752905	Wed	3	10	2016-08-03 18:04	3
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    278514 Aug  3 08:59 passporttrans.20160803.csv.20160803085955889	8:59	8/3/2016		2016-03-08	8:59:55	0.374942	Wed	3	15	2016-08-03 08:59	3
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1660 Aug  3 08:31 HighlandCapitalManagementRecon201608030730.csv.20160803083154940	8:31	8/3/2016	7:30:00	2016-03-08	8:31:54	0.355486	Wed	3	16	2016-08-03 08:31	3
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       481 Aug  3 03:01 HSBC-LKR.in.03082016-1.20160803030132988	3:01	3/8/2016		2016-03-08	3:01:32	0.126065	Wed	3	17	2016-08-03 03:01	3
John Hancock Investments	HAN_TRANS_HANVER_20160803.csv.20160803153955231	15:39	8/3/2016		2016-03-08	15:39:55	0.65272	Wed	3	18	2016-08-03 15:39	3
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Aug  3 05:51 NOS_SFX_20160803.csv.20160803055144247	5:51	8/3/2016		2016-03-08	5:51:44	0.244259	Wed	3	21	2016-08-03 05:51	3
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       146 Aug  3 10:35 PresimaOrders.csv.20160803103535699	10:35			2016-03-08	10:35:35	0.441377	Wed	3	25	2016-08-03 10:35	3
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug  3 03:03 FT_fx_20160803_090120.csv.20160803030333516	3:03	8/3/2016	9:01:20	2016-03-08	3:03:33	0.127465	Wed	3	26	2016-08-03 03:03	3
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug  3 03:33 INV_fx_20160803_093043.csv.20160803033336138	3:33	8/3/2016	9:30:43	2016-03-08	3:33:36	0.148333	Wed	3	26	2016-08-03 03:33	3
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug  3 04:25 FT_fx_20160803_102438.csv.20160803042538835	4:25	8/3/2016	10:24:38	2016-03-08	4:25:38	0.184468	Wed	3	26	2016-08-03 04:25	3
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Aug  3 05:31 INV_fx_20160803_112954.csv.20160803053142446	5:31	8/3/2016	11:29:54	2016-03-08	5:31:42	0.230347	Wed	3	26	2016-08-03 05:31	3
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  3 05:23 citicnhtrades.in.201608031717.20160803052341581	5:23	8/3/2016	17:17:00	2016-03-08	5:23:41	0.22478	Wed	3	28	2016-08-03 05:23	3
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       398 Aug  3 05:23 hsbccnhtrades.in.201608031717.20160803052341871	5:23	8/3/2016	17:17:00	2016-03-08	5:23:41	0.22478	Wed	3	29	2016-08-03 05:23	3
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23008 Aug  3 10:11 RSWGD1-17_SSGM_Confirmed_File__20160803.csv.20160803101133201	10:11	8/3/2016		2016-03-08	10:11:33	0.424688	Wed	3	30	2016-08-03 10:11	3
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3563 Aug  3 09:01 tcwta20160803.csv.20160803090157053	9:01	8/3/2016		2016-03-08	9:01:57	0.376354	Wed	3	31	2016-08-03 09:01	3
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6133 Aug  3 09:31 TIAACREFREPAT.csv.20160803093130669	9:31			2016-03-08	9:31:30	0.396875	Wed	3	32	2016-08-03 09:31	3
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       348 Aug  3 21:55 tokyofundtrades.in.201608040924.20160803215557028	21:55	8/4/2016	9:24:00	2016-03-08	21:55:57	0.913854	Wed	3	33	2016-08-03 21:55	3
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1524 Aug  4 04:32 SSC_BAM_FXREQ_20160804_093011.csv.pgp.ndm05.20160804043253832	4:32	8/4/2016	9:30:11	2016-04-08	4:32:53	0.189502	Thu	4	3	2016-08-04 04:32	4
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1464 Aug  4 05:33 SSC_BAM_FXREQ_20160804_103025.csv.pgp.ndm05.20160804053328622	5:33	8/4/2016	10:30:25	2016-04-08	5:33:28	0.231574	Thu	4	3	2016-08-04 05:33	4
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1458 Aug  4 12:34 SSC_BAM_FXREQ_20160804_173119.csv.pgp.ndm05.20160804123417145	12:34	8/4/2016	17:31:19	2016-04-08	12:34:17	0.523808	Thu	4	3	2016-08-04 12:34	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063849062	6:38			2016-04-08	6:38:49	0.276956	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063849295	6:38			2016-04-08	6:38:49	0.276956	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063849483	6:38			2016-04-08	6:38:49	0.276956	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063849695	6:38			2016-04-08	6:38:49	0.276956	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063849888	6:38			2016-04-08	6:38:49	0.276956	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063850100	6:38			2016-04-08	6:38:50	0.276968	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063850302	6:38			2016-04-08	6:38:50	0.276968	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063850481	6:38			2016-04-08	6:38:50	0.276968	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063850693	6:38			2016-04-08	6:38:50	0.276968	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063850900	6:38			2016-04-08	6:38:50	0.276968	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063851089	6:38			2016-04-08	6:38:51	0.276979	Thu	4	4	2016-08-04 06:38	4
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  4 06:38 BCRTOFX.txt.20160804063851299	6:38			2016-04-08	6:38:51	0.276979	Thu	4	4	2016-08-04 06:38	4
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3038 Aug  4 14:40 BRA_BRA_Ver_20160804.csv.20160804144056911	14:40	8/4/2016		2016-04-08	14:40:56	0.611759	Thu	4	5	2016-08-04 14:40	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 08:34 CDPSfx_BRLorder.20160804.083500.csv.20160804083426960	8:34	8/4/2016	8:35:00	2016-04-08	8:34:26	0.357245	Thu	4	6	2016-08-04 08:34	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 09:34 CDPSfx_BRLorder.20160804.093500.csv.20160804093434353	9:34	8/4/2016	9:35:00	2016-04-08	9:34:34	0.399005	Thu	4	6	2016-08-04 09:34	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 10:34 CDPSfx_BRLorder.20160804.103500.csv.20160804103438984	10:34	8/4/2016	10:35:00	2016-04-08	10:34:38	0.440718	Thu	4	6	2016-08-04 10:34	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 11:34 CDPSfx_BRLorder.20160804.113500.csv.20160804113443234	11:34	8/4/2016	11:35:00	2016-04-08	11:34:43	0.482442	Thu	4	6	2016-08-04 11:34	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug  4 21:32 CDPSfx_PHPorder.20160804.213500.csv.20160804213255330	21:32	8/4/2016	21:35:00	2016-04-08	21:32:55	0.897859	Thu	4	6	2016-08-04 21:32	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 22:35 CDPSfx_MYRorder.20160804.223500.csv.20160804223500239	22:35	8/4/2016	22:35:00	2016-04-08	22:35:00	0.940972	Thu	4	6	2016-08-04 22:35	4
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug  4 22:35 CDPSfx_PHPorder.20160804.223500.csv.20160804223500521	22:35	8/4/2016	22:35:00	2016-04-08	22:35:00	0.940972	Thu	4	6	2016-08-04 22:35	4
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Aug  4 05:14 scbcnhtrades1.in.201608041702.20160804051426474	5:14	8/4/2016	17:02:00	2016-04-08	5:14:26	0.218356	Thu	4	7	2016-08-04 05:14	4
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  4 05:14 scbcnhtrades2.in.201608041702.20160804051426767	5:14	8/4/2016	17:02:00	2016-04-08	5:14:26	0.218356	Thu	4	7	2016-08-04 05:14	4
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1018 Aug  4 09:16 SPOT_FET_Instructions_StateStreet_20160804-144922.csv.20160804091629980	9:16	8/4/2016	14:49:22	2016-04-08	9:16:29	0.386447	Thu	4	7	2016-08-04 09:16	4
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  4 17:07 08042016_GAM_GAM_STAR_GS.20160804.csv.20160804170706587	17:07	8/4/2016		2016-04-08	17:07:06	0.713264	Thu	4	9	2016-08-04 17:07	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Aug  4 10:34 trade10.dat.20160804103439457	10:34			2016-04-08	10:34:39	0.440729	Thu	4	10	2016-08-04 10:34	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug  4 12:34 trade10.dat.20160804123447503	12:34			2016-04-08	12:34:47	0.524155	Thu	4	10	2016-08-04 12:34	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Aug  4 14:34 trade10.dat.20160804143455742	14:34			2016-04-08	14:34:55	0.607581	Thu	4	10	2016-08-04 14:34	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Aug  4 16:23 trade10.dat.20160804162302584	16:23			2016-04-08	16:23:02	0.682662	Thu	4	10	2016-08-04 16:23	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  4 17:03 trade10.dat.20160804170305729	17:03			2016-04-08	17:03:05	0.710475	Thu	4	10	2016-08-04 17:03	4
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  4 18:03 trade10.dat.20160804180312353	18:03			2016-04-08	18:03:12	0.752222	Thu	4	10	2016-08-04 18:03	4
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    261764 Aug  4 08:58 passporttrans.20160804.csv.20160804085828059	8:58	8/4/2016		2016-04-08	8:58:28	0.373935	Thu	4	15	2016-08-04 08:58	4
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1847 Aug  4 08:32 HighlandCapitalManagementRecon201608040730.csv.20160804083226513	8:32	8/4/2016	7:30:00	2016-04-08	8:32:26	0.355856	Thu	4	16	2016-08-04 08:32	4
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       757 Aug  4 03:00 HSBC-LKR.in.04082016-1.20160804030012238	3:00	4/8/2016		2016-04-08	3:00:12	0.125139	Thu	4	17	2016-08-04 03:00	4
John Hancock Investments	HAN_TRANS_HANVER_20160802.csv.20160804154700598	15:47	8/2/2016		2016-04-08	15:47:00	0.657639	Thu	4	18	2016-08-04 15:47	4
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       206 Aug  4 12:16 PGI_Orders_20160804111356.csv.20160804121645948	12:16	8/4/2016	11:13:56	2016-04-08	12:16:45	0.511632	Thu	4	24	2016-08-04 12:16	4
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       203 Aug  4 12:42 PGI_Orders_20160804114151.csv.20160804124248484	12:42	8/4/2016	11:41:51	2016-04-08	12:42:48	0.529722	Thu	4	24	2016-08-04 12:42	4
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Aug  4 03:08 FT_fx_20160804_090544.csv.20160804030812995	3:08	8/4/2016	9:05:44	2016-04-08	3:08:12	0.130694	Thu	4	26	2016-08-04 03:08	4
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug  4 03:46 INV_fx_20160804_094433.csv.20160804034617232	3:46	8/4/2016	9:44:33	2016-04-08	3:46:17	0.157141	Thu	4	26	2016-08-04 03:46	4
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Aug  4 04:32 FT_fx_20160804_102814.csv.20160804043223468	4:32	8/4/2016	10:28:14	2016-04-08	4:32:23	0.189155	Thu	4	26	2016-08-04 04:32	4
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       295 Aug  4 05:28 INV_fx_20160804_112514.csv.20160804052828092	5:28	8/4/2016	11:25:14	2016-04-08	5:28:28	0.228102	Thu	4	26	2016-08-04 05:28	4
SchaFer Cullen	-rw-r--r--   1 ftpgmrin ftpgmr       385 Aug  4 09:54 SchaferCullenOrders.csv.20160804095435328	9:54			2016-04-08	9:54:35	0.412905	Thu	4	27	2016-08-04 09:54	4
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  4 05:20 citicnhtrades.in.201608041712.20160804052027186	5:20	8/4/2016	17:12:00	2016-04-08	5:20:27	0.222535	Thu	4	28	2016-08-04 05:20	4
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        58 Aug  4 05:20 hsbccnhtrades.in.201608041712.20160804052027578	5:20	8/4/2016	17:12:00	2016-04-08	5:20:27	0.222535	Thu	4	29	2016-08-04 05:20	4
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24125 Aug  4 10:22 RSWGD1-17_SSGM_Confirmed_File__20160804.csv.20160804102237397	10:22	8/4/2016		2016-04-08	10:22:37	0.432373	Thu	4	30	2016-08-04 10:22	4
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5479 Aug  4 09:30 TIAACREFREPAT.csv.20160804093033167	9:30			2016-04-08	9:30:33	0.396215	Thu	4	32	2016-08-04 09:30	4
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       611 Aug  4 05:08 tokyofundtrades.in.201608041704.20160804050826041	5:08	8/4/2016	17:04:00	2016-04-08	5:08:26	0.21419	Thu	4	33	2016-08-04 05:08	4
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       398 Aug  4 22:30 tokyofundtrades.in.201608051022.20160804223059516	22:30	8/5/2016	10:22:00	2016-04-08	22:30:59	0.938183	Thu	4	33	2016-08-04 22:30	4
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1502 Aug  5 04:33 SSC_BAM_FXREQ_20160805_093015.csv.pgp.ndm05.20160805043346220	4:33	8/5/2016	9:30:15	2016-05-08	4:33:46	0.190116	Fri	5	3	2016-08-05 04:33	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1531 Aug  5 05:47 SSC_BAM_FXREQ_20160805_103011.csv.pgp.ndm05.20160805054750268	5:47	8/5/2016	10:30:11	2016-05-08	5:47:50	0.241551	Fri	5	3	2016-08-05 05:47	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug  5 06:34 SSC_BAM_FXREQ_20160805_113025.csv.pgp.ndm05.20160805063409095	6:34	8/5/2016	11:30:25	2016-05-08	6:34:09	0.273715	Fri	5	3	2016-08-05 06:34	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1422 Aug  5 08:34 SSC_BAM_FXREQ_20160805_133038.csv.pgp.ndm05.20160805083417691	8:34	8/5/2016	13:30:38	2016-05-08	8:34:17	0.357141	Fri	5	3	2016-08-05 08:34	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1455 Aug  5 09:33 SSC_BAM_FXREQ_20160805_143042.csv.pgp.ndm05.20160805093323510	9:33	8/5/2016	14:30:42	2016-05-08	9:33:23	0.398183	Fri	5	3	2016-08-05 09:33	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1486 Aug  5 10:34 SSC_BAM_FXREQ_20160805_153046.csv.pgp.ndm05.20160805103457962	10:34	8/5/2016	15:30:46	2016-05-08	10:34:57	0.440938	Fri	5	3	2016-08-05 10:34	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1523 Aug  5 11:33 SSC_BAM_FXREQ_20160805_163051.csv.pgp.ndm05.20160805113301775	11:33	8/5/2016	16:30:51	2016-05-08	11:33:01	0.481262	Fri	5	3	2016-08-05 11:33	5
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1601 Aug  5 12:33 SSC_BAM_FXREQ_20160805_173053.csv.pgp.ndm05.20160805123336249	12:33	8/5/2016	17:30:53	2016-05-08	12:33:36	0.523333	Fri	5	3	2016-08-05 12:33	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063909538	6:39			2016-05-08	6:39:09	0.277188	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063909728	6:39			2016-05-08	6:39:09	0.277188	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063909930	6:39			2016-05-08	6:39:09	0.277188	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063910126	6:39			2016-05-08	6:39:10	0.277199	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063910335	6:39			2016-05-08	6:39:10	0.277199	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063910524	6:39			2016-05-08	6:39:10	0.277199	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063910737	6:39			2016-05-08	6:39:10	0.277199	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063910926	6:39			2016-05-08	6:39:10	0.277199	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063911135	6:39			2016-05-08	6:39:11	0.277211	Fri	5	4	2016-08-05 06:39	5
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  5 06:39 BCRTOFX.txt.20160805063911322	6:39			2016-05-08	6:39:11	0.277211	Fri	5	4	2016-08-05 06:39	5
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3678 Aug  5 14:39 BRA_BRA_Ver_20160805.csv.20160805143944693	14:39	8/5/2016		2016-05-08	14:39:44	0.610926	Fri	5	5	2016-08-05 14:39	5
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1163 Aug  5 09:09 SPOT_FET_Instructions_StateStreet_20160805-145224.csv.20160805090920296	9:09	8/5/2016	14:52:24	2016-05-08	9:09:20	0.381481	Fri	5	7	2016-08-05 09:09	5
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  5 16:41 08052016_GAM_GAM_STAR_GS.20160805.csv.20160805164152002	16:41	8/5/2016		2016-05-08	16:41:52	0.695741	Fri	5	9	2016-08-05 16:41	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  5 10:33 trade10.dat.20160805103327412	10:33			2016-05-08	10:33:27	0.439896	Fri	5	10	2016-08-05 10:33	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug  5 12:33 trade10.dat.20160805123335879	12:33			2016-05-08	12:33:35	0.523322	Fri	5	10	2016-08-05 12:33	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Aug  5 14:33 trade10.dat.20160805143344113	14:33			2016-05-08	14:33:44	0.606759	Fri	5	10	2016-08-05 14:33	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     29074 Aug  5 16:23 trade10.dat.20160805162350699	16:23			2016-05-08	16:23:50	0.683218	Fri	5	10	2016-08-05 16:23	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  5 17:03 trade10.dat.20160805170353831	17:03			2016-05-08	17:03:53	0.71103	Fri	5	10	2016-08-05 17:03	5
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  5 18:03 trade10.dat.20160805180332407	18:03			2016-05-08	18:03:32	0.752454	Fri	5	10	2016-08-05 18:03	5
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    889704 Aug  5 09:15 passporttrans.20160805.csv.20160805091520817	9:15	8/5/2016		2016-05-08	9:15:20	0.385648	Fri	5	15	2016-08-05 09:15	5
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug  5 08:31 HighlandCapitalManagementRecon201608050730.csv.20160805083117261	8:31	8/5/2016	7:30:00	2016-05-08	8:31:17	0.355058	Fri	5	16	2016-08-05 08:31	5
John Hancock Investments	HAN_TRANS_HANVER_20160805.csv.20160805153948800	15:39	8/5/2016		2016-05-08	15:39:48	0.652639	Fri	5	18	2016-08-05 15:39	5
PGI	-rw-r--r--   1 ftpgmrin ftpgmr      1065 Aug  5 15:17 PGI_Orders_20160805141616.csv.20160805151747571	15:17	8/5/2016	14:16:16	2016-05-08	15:17:47	0.63735	Fri	5	24	2016-08-05 15:17	5
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Aug  5 03:13 FT_fx_20160805_091153.csv.20160805031311167	3:13	8/5/2016	9:11:53	2016-05-08	3:13:11	0.134155	Fri	5	26	2016-08-05 03:13	5
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       366 Aug  5 03:41 INV_fx_20160805_093900.csv.20160805034113665	3:41	8/5/2016	9:39:00	2016-05-08	3:41:13	0.153623	Fri	5	26	2016-08-05 03:41	5
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug  5 04:23 FT_fx_20160805_102144.csv.20160805042315776	4:23	8/5/2016	10:21:44	2016-05-08	4:23:15	0.182813	Fri	5	26	2016-08-05 04:23	5
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug  5 04:53 INV_fx_20160805_105009.csv.20160805045317116	4:53	8/5/2016	10:50:09	2016-05-08	4:53:17	0.203669	Fri	5	26	2016-08-05 04:53	5
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug  5 06:13 INV_fx_20160805_121059.csv.20160805061338268	6:13	8/5/2016	12:10:59	2016-05-08	6:13:38	0.259468	Fri	5	26	2016-08-05 06:13	5
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  5 05:25 citicnhtrades.in.201608051714.20160805052519124	5:25	8/5/2016	17:14:00	2016-05-08	5:25:19	0.225914	Fri	5	28	2016-08-05 05:25	5
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        57 Aug  5 05:25 hsbccnhtrades.in.201608051714.20160805052519380	5:25	8/5/2016	17:14:00	2016-05-08	5:25:19	0.225914	Fri	5	29	2016-08-05 05:25	5
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24407 Aug  5 10:29 RSWGD1-17_SSGM_Confirmed_File__20160805.csv.20160805102926790	10:29	8/5/2016		2016-05-08	10:29:26	0.437106	Fri	5	30	2016-08-05 10:29	5
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5883 Aug  5 09:31 TIAACREFREPAT.csv.20160805093122844	9:31			2016-05-08	9:31:22	0.396782	Fri	5	32	2016-08-05 09:31	5
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug  7 20:33 CDPSfx_TWDorder.20160807.203000.csv.20160807203346009	20:33	8/7/2016	20:30:00	2016-07-08	20:33:46	0.856782	Sun	7	6	2016-08-07 20:33	#N/A
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       351 Aug  7 21:41 tokyofundtrades.in.201608080931.20160807214151017	21:41	8/8/2016	9:31:00	2016-07-08	21:41:51	0.904063	Sun	7	33	2016-08-07 21:41	#N/A
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1445 Aug  8 04:33 SSC_BAM_FXREQ_20160808_093003.csv.pgp.ndm05.20160808043311519	4:33	8/8/2016	9:30:03	2016-08-08	4:33:11	0.189711	Mon	1	3	2016-08-08 04:33	6
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Aug  8 05:33 SSC_BAM_FXREQ_20160808_103006.csv.pgp.ndm05.20160808053344517	5:33	8/8/2016	10:30:06	2016-08-08	5:33:44	0.231759	Mon	1	3	2016-08-08 05:33	6
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1421 Aug  8 10:33 SSC_BAM_FXREQ_20160808_153021.csv.pgp.ndm05.20160808103314276	10:33	8/8/2016	15:30:21	2016-08-08	10:33:14	0.439745	Mon	1	3	2016-08-08 10:33	6
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1423 Aug  8 12:32 SSC_BAM_FXREQ_20160808_173026.csv.pgp.ndm05.20160808123254052	12:32	8/8/2016	17:30:26	2016-08-08	12:32:54	0.522847	Mon	1	3	2016-08-08 12:32	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063755706	6:37			2016-08-08	6:37:55	0.276331	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063755908	6:37			2016-08-08	6:37:55	0.276331	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063756166	6:37			2016-08-08	6:37:56	0.276343	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063756322	6:37			2016-08-08	6:37:56	0.276343	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063756521	6:37			2016-08-08	6:37:56	0.276343	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063756710	6:37			2016-08-08	6:37:56	0.276343	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063756907	6:37			2016-08-08	6:37:56	0.276343	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063757144	6:37			2016-08-08	6:37:57	0.276354	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063757311	6:37			2016-08-08	6:37:57	0.276354	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063757515	6:37			2016-08-08	6:37:57	0.276354	Mon	1	4	2016-08-08 06:37	6
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  8 06:37 BCRTOFX.txt.20160808063757708	6:37			2016-08-08	6:37:57	0.276354	Mon	1	4	2016-08-08 06:37	6
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4016 Aug  8 14:40 BRA_BRA_Ver_20160808.csv.20160808144009585	14:40	8/8/2016		2016-08-08	14:40:09	0.611215	Mon	1	5	2016-08-08 14:40	6
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug  8 08:34 CDPSfx_BRLorder.20160808.083500.csv.20160808083405427	8:34	8/8/2016	8:35:00	2016-08-08	8:34:05	0.357002	Mon	1	6	2016-08-08 08:34	6
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug  8 09:34 CDPSfx_BRLorder.20160808.093500.csv.20160808093410926	9:34	8/8/2016	9:35:00	2016-08-08	9:34:10	0.398727	Mon	1	6	2016-08-08 09:34	6
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug  8 10:33 CDPSfx_BRLorder.20160808.103500.csv.20160808103345185	10:33	8/8/2016	10:35:00	2016-08-08	10:33:45	0.440104	Mon	1	6	2016-08-08 10:33	6
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug  8 11:33 CDPSfx_BRLorder.20160808.113500.csv.20160808113348860	11:33	8/8/2016	11:35:00	2016-08-08	11:33:48	0.481806	Mon	1	6	2016-08-08 11:33	6
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       431 Aug  8 09:34 SPOT_FET_Instructions_StateStreet_20160808-152305.csv.20160808093410692	9:34	8/8/2016	15:23:05	2016-08-08	9:34:10	0.398727	Mon	1	7	2016-08-08 09:34	6
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  8 16:38 08082016_GAM_GAM_STAR_GS.20160808.csv.20160808163814872	16:38	8/8/2016		2016-08-08	16:38:14	0.693218	Mon	1	9	2016-08-08 16:38	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  8 10:33 trade10.dat.20160808103344767	10:33			2016-08-08	10:33:44	0.440093	Mon	1	10	2016-08-08 10:33	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9110 Aug  8 12:33 trade10.dat.20160808123354484	12:33			2016-08-08	12:33:54	0.523542	Mon	1	10	2016-08-08 12:33	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Aug  8 14:34 trade10.dat.20160808143408895	14:34			2016-08-08	14:34:08	0.607037	Mon	1	10	2016-08-08 14:34	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Aug  8 16:24 trade10.dat.20160808162413759	16:24			2016-08-08	16:24:13	0.683484	Mon	1	10	2016-08-08 16:24	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  8 17:04 trade10.dat.20160808170416714	17:04			2016-08-08	17:04:16	0.711296	Mon	1	10	2016-08-08 17:04	6
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  8 18:04 trade10.dat.20160808180421948	18:04			2016-08-08	18:04:21	0.753021	Mon	1	10	2016-08-08 18:04	6
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    295591 Aug  8 09:04 passporttrans.20160808.csv.20160808090407534	9:04	8/8/2016		2016-08-08	9:04:07	0.377859	Mon	1	15	2016-08-08 09:04	6
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      6515 Aug  8 08:32 HighlandCapitalManagementRecon201608080730.csv.20160808083204888	8:32	8/8/2016	7:30:00	2016-08-08	8:32:04	0.355602	Mon	1	16	2016-08-08 08:32	6
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       480 Aug  8 03:23 HSBC-LKR.in.08082016-1.20160808032337970	3:23	8/8/2016		2016-08-08	3:23:37	0.1414	Mon	1	17	2016-08-08 03:23	6
John Hancock Investments	HAN_TRANS_HANVER_20160808.csv.20160808153811857	15:38	8/8/2016		2016-08-08	15:38:11	0.651516	Mon	1	18	2016-08-08 15:38	6
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Aug  8 03:23 FT_fx_20160808_091806.csv.20160808032337814	3:23	8/8/2016	9:18:06	2016-08-08	3:23:37	0.1414	Mon	1	26	2016-08-08 03:23	6
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug  8 03:39 INV_fx_20160808_093816.csv.20160808033939047	3:39	8/8/2016	9:38:16	2016-08-08	3:39:39	0.152535	Mon	1	26	2016-08-08 03:39	6
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug  8 04:49 FT_fx_20160808_104425.csv.20160808044942098	4:49	8/8/2016	10:44:25	2016-08-08	4:49:42	0.201181	Mon	1	26	2016-08-08 04:49	6
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  8 05:21 citicnhtrades.in.201608081714.20160808052143713	5:21	8/8/2016	17:14:00	2016-08-08	5:21:43	0.223414	Mon	1	28	2016-08-08 05:21	6
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        59 Aug  8 05:21 hsbccnhtrades.in.201608081714.20160808052144005	5:21	8/8/2016	17:14:00	2016-08-08	5:21:44	0.223426	Mon	1	29	2016-08-08 05:21	6
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24263 Aug  8 10:53 RSWGD1-17_SSGM_Confirmed_File__20160808.csv.20160808105346106	10:53	8/8/2016		2016-08-08	10:53:46	0.454005	Mon	1	30	2016-08-08 10:53	6
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3609 Aug  8 09:38 tcwta20160808.csv.20160808.093706.20160808093811332	9:38	8/8/2016		2016-08-08	9:38:11	0.401516	Mon	1	31	2016-08-08 09:38	6
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4970 Aug  8 09:32 TIAACREFREPAT.csv.20160808093209742	9:32			2016-08-08	9:32:09	0.397326	Mon	1	32	2016-08-08 09:32	6
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       695 Aug  8 13:32 TIAACREFREPAT.csv.20160808133204560	13:32			2016-08-08	13:32:04	0.563935	Mon	1	32	2016-08-08 13:32	6
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       171 Aug  8 02:29 tokyofundtrades.in.201608081422.20160808022935648	2:29	8/8/2016	14:22:00	2016-08-08	2:29:35	0.103877	Mon	1	33	2016-08-08 02:29	6
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       292 Aug  8 21:46 tokyofundtrades.in.201608090938.20160808214634976	21:46	8/9/2016	9:38:00	2016-08-08	21:46:34	0.907338	Mon	1	33	2016-08-08 21:46	6
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug  9 05:28 SSC_BAM_FXREQ_20160809_093004.csv.pgp.20160809052833202	5:28	8/9/2016	9:30:04	2016-09-08	5:28:33	0.22816	Tue	2	3	2016-08-09 05:28	7
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug  9 05:31 SSC_BAM_FXREQ_20160809_093004.csv.pgp.ndm05.20160809053134123	5:31	8/9/2016	9:30:04	2016-09-08	5:31:34	0.230255	Tue	2	3	2016-08-09 05:31	7
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1445 Aug  9 05:33 SSC_BAM_FXREQ_20160809_103007.csv.pgp.ndm05.20160809053304423	5:33	8/9/2016	10:30:07	2016-09-08	5:33:04	0.231296	Tue	2	3	2016-08-09 05:33	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063847871	6:38			2016-09-08	6:38:47	0.276933	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063848154	6:38			2016-09-08	6:38:48	0.276944	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063848342	6:38			2016-09-08	6:38:48	0.276944	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063848564	6:38			2016-09-08	6:38:48	0.276944	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063848761	6:38			2016-09-08	6:38:48	0.276944	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063848943	6:38			2016-09-08	6:38:48	0.276944	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063849155	6:38			2016-09-08	6:38:49	0.276956	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063849411	6:38			2016-09-08	6:38:49	0.276956	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063849588	6:38			2016-09-08	6:38:49	0.276956	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063849765	6:38			2016-09-08	6:38:49	0.276956	Tue	2	4	2016-08-09 06:38	7
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug  9 06:38 BCRTOFX.txt.20160809063849979	6:38			2016-09-08	6:38:49	0.276956	Tue	2	4	2016-08-09 06:38	7
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2989 Aug  9 14:38 BRA_BRA_Ver_20160809.csv.20160809143854866	14:38	8/9/2016		2016-09-08	14:38:54	0.610347	Tue	2	5	2016-08-09 14:38	7
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug  9 20:32 CDPSfx_TWDorder.20160809.203000.csv.20160809203248588	20:32	8/9/2016	20:30:00	2016-09-08	20:32:48	0.856111	Tue	2	6	2016-08-09 20:32	7
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       580 Aug  9 10:56 SPOT_FET_Instructions_StateStreet_20160809-164223.csv.20160809105639799	10:56	8/9/2016	16:42:23	2016-09-08	10:56:39	0.456007	Tue	2	7	2016-08-09 10:56	7
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  9 17:09 08092016_GAM_GAM_STAR_GS.20160809.csv.20160809170903843	17:09	8/9/2016		2016-09-08	17:09:03	0.714618	Tue	2	9	2016-08-09 17:09	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  9 10:34 trade10.dat.20160809103438672	10:34			2016-09-08	10:34:38	0.440718	Tue	2	10	2016-08-09 10:34	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Aug  9 12:34 trade10.dat.20160809123446255	12:34			2016-09-08	12:34:46	0.524144	Tue	2	10	2016-08-09 12:34	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  9 14:32 trade10.dat.20160809143253776	14:32			2016-09-08	14:32:53	0.606169	Tue	2	10	2016-08-09 14:32	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     20394 Aug  9 16:24 trade10.dat.20160809162459682	16:24			2016-09-08	16:24:59	0.684016	Tue	2	10	2016-08-09 16:24	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Aug  9 17:03 trade10.dat.20160809170302822	17:03			2016-09-08	17:03:02	0.71044	Tue	2	10	2016-08-09 17:03	7
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug  9 18:03 trade10.dat.20160809180308320	18:03			2016-09-08	18:03:08	0.752176	Tue	2	10	2016-08-09 18:03	7
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       255 Aug  9 04:58 UKFCMCurrencyTemplate090816.csv.20160809045830831	4:58			2016-09-08	4:58:30	0.207292	Tue	2	11	2016-08-09 04:58	7
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    248177 Aug  9 09:04 passporttrans.20160809.csv.20160809090430664	9:04	8/9/2016		2016-09-08	9:04:30	0.378125	Tue	2	15	2016-08-09 09:04	7
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1666 Aug  9 08:30 HighlandCapitalManagementRecon201608090730.csv.20160809083025745	8:30	8/9/2016	7:30:00	2016-09-08	8:30:25	0.354456	Tue	2	16	2016-08-09 08:30	7
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       186 Aug  9 11:26 Highland_Orders_20160809csv.20160809112642124	11:26	8/9/2016		2016-09-08	11:26:42	0.476875	Tue	2	16	2016-08-09 11:26	7
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       933 Aug  9 03:46 HSBC-LKR.in.09082016-1.20160809034627370	3:46	9/8/2016		2016-09-08	3:46:27	0.157257	Tue	2	17	2016-08-09 03:46	7
John Hancock Investments	HAN_TRANS_HANVER_20160809.csv.20160809155858038	15:58	8/9/2016		2016-09-08	15:58:58	0.665949	Tue	2	18	2016-08-09 15:58	7
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       276 Aug  9 12:50 PGI_Orders_20160809114925.csv.20160809125047484	12:50	8/9/2016	11:49:25	2016-09-08	12:50:47	0.535266	Tue	2	24	2016-08-09 12:50	7
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug  9 03:36 FT_fx_20160809_092721.csv.20160809033626753	3:36	8/9/2016	9:27:21	2016-09-08	3:36:26	0.150301	Tue	2	26	2016-08-09 03:36	7
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug  9 04:42 FT_fx_20160809_103910.csv.20160809044229802	4:42	8/9/2016	10:39:10	2016-09-08	4:42:29	0.196169	Tue	2	26	2016-08-09 04:42	7
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug  9 04:56 INV_fx_20160809_105425.csv.20160809045630415	4:56	8/9/2016	10:54:25	2016-09-08	4:56:30	0.205903	Tue	2	26	2016-08-09 04:56	7
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       115 Aug  9 04:30 citicnhtrades.in.201608091619.20160809043028973	4:30	8/9/2016	16:19:00	2016-09-08	4:30:28	0.187824	Tue	2	28	2016-08-09 04:30	7
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug  9 05:28 citicnhtrades.in.201608091719.20160809052833635	5:28	8/9/2016	17:19:00	2016-09-08	5:28:33	0.22816	Tue	2	28	2016-08-09 05:28	7
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       172 Aug  9 05:28 hsbccnhtrades.in.201608091719.20160809052833835	5:28	8/9/2016	17:19:00	2016-09-08	5:28:33	0.22816	Tue	2	29	2016-08-09 05:28	7
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23407 Aug  9 10:30 RSWGD1-17_SSGM_Confirmed_File__20160809.csv.20160809103038108	10:30	8/9/2016		2016-09-08	10:30:38	0.43794	Tue	2	30	2016-08-09 10:30	7
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3609 Aug  9 09:30 tcwta20160809.csv.20160809.092921.20160809093033158	9:30	8/9/2016		2016-09-08	9:30:33	0.396215	Tue	2	31	2016-08-09 09:30	7
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1061 Aug  9 09:30 TIAACREFREPAT.csv.20160809093033731	9:30			2016-09-08	9:30:33	0.396215	Tue	2	32	2016-08-09 09:30	7
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       614 Aug  9 13:30 TIAACREFREPAT.csv.20160809133050230	13:30			2016-09-08	13:30:50	0.563079	Tue	2	32	2016-08-09 13:30	7
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       460 Aug  9 21:06 tokyofundtrades.in.201608100852.20160809210651414	21:06	8/10/2016	8:52:00	2016-09-08	21:06:51	0.879757	Tue	2	33	2016-08-09 21:06	7
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       286 Aug  9 23:21 tokyofundtrades.in.201608101036.20160809232100752	23:21	8/10/2016	10:36:00	2016-09-08	23:21:00	0.972917	Tue	2	33	2016-08-09 23:21	7
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        63 Aug 10 09:17 Alger_Orders_20160810091522.csv.20160810091709481	9:17	8/10/2016	9:15:22	2016-10-08	9:17:09	0.38691	Wed	3	1	2016-08-10 09:17	8
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       130 Aug 10 14:31 Alger_Orders_20160810142920.csv.20160810143134177	14:31	8/10/2016	14:29:20	2016-10-08	14:31:34	0.605255	Wed	3	1	2016-08-10 14:31	8
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 10 05:42 SSC_BAM_FXREQ_20160810_103016.csv.pgp.ndm05.20160810054221211	5:42	8/10/2016	10:30:16	2016-10-08	5:42:21	0.237743	Wed	3	3	2016-08-10 05:42	8
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug 10 06:33 SSC_BAM_FXREQ_20160810_113018.csv.pgp.ndm05.20160810063353396	6:33	8/10/2016	11:30:18	2016-10-08	6:33:53	0.27353	Wed	3	3	2016-08-10 06:33	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063853962	6:38			2016-10-08	6:38:53	0.277002	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063854216	6:38			2016-10-08	6:38:54	0.277014	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063854361	6:38			2016-10-08	6:38:54	0.277014	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063854551	6:38			2016-10-08	6:38:54	0.277014	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063854862	6:38			2016-10-08	6:38:54	0.277014	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063855236	6:38			2016-10-08	6:38:55	0.277025	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063855580	6:38			2016-10-08	6:38:55	0.277025	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063855828	6:38			2016-10-08	6:38:55	0.277025	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063855998	6:38			2016-10-08	6:38:55	0.277025	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063856232	6:38			2016-10-08	6:38:56	0.277037	Wed	3	4	2016-08-10 06:38	8
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 10 06:38 BCRTOFX.txt.20160810063856612	6:38			2016-10-08	6:38:56	0.277037	Wed	3	4	2016-08-10 06:38	8
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2780 Aug 10 14:53 BRA_BRA_Ver_20160810.csv.20160810145335871	14:53	8/10/2016		2016-10-08	14:53:35	0.620544	Wed	3	5	2016-08-10 14:53	8
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        54 Aug 10 05:17 scbcnhtrades1.in.201608101656.20160810051719043	5:17	8/10/2016	16:56:00	2016-10-08	5:17:19	0.220359	Wed	3	7	2016-08-10 05:17	8
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 10 05:17 scbcnhtrades2.in.201608101656.20160810051719220	5:17	8/10/2016	16:56:00	2016-10-08	5:17:19	0.220359	Wed	3	7	2016-08-10 05:17	8
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1311 Aug 10 09:51 SPOT_FET_Instructions_StateStreet_20160810-144926.csv.20160810095112999	9:51	8/10/2016	14:49:26	2016-10-08	9:51:12	0.410556	Wed	3	7	2016-08-10 09:51	8
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 10 16:27 08102016_GAM_GAM_STAR_GS.20160810.csv.20160810162743070	16:27	8/10/2016		2016-10-08	16:27:43	0.685914	Wed	3	9	2016-08-10 16:27	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 10 10:33 trade10.dat.20160810103317123	10:33			2016-10-08	10:33:17	0.43978	Wed	3	10	2016-08-10 10:33	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Aug 10 12:33 trade10.dat.20160810123325498	12:33			2016-10-08	12:33:25	0.523206	Wed	3	10	2016-08-10 12:33	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Aug 10 14:35 trade10.dat.20160810143535189	14:35			2016-10-08	14:35:35	0.608044	Wed	3	10	2016-08-10 14:35	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     30810 Aug 10 16:23 trade10.dat.20160810162342508	16:23			2016-10-08	16:23:42	0.683125	Wed	3	10	2016-08-10 16:23	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 10 17:03 trade10.dat.20160810170345456	17:03			2016-10-08	17:03:45	0.710938	Wed	3	10	2016-08-10 17:03	8
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 10 18:03 trade10.dat.20160810180351925	18:03			2016-10-08	18:03:51	0.752674	Wed	3	10	2016-08-10 18:03	8
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       254 Aug 10 05:37 UKFCMCurrencyTemplate100816.csv.20160810053720665	5:37			2016-10-08	5:37:20	0.234259	Wed	3	11	2016-08-10 05:37	8
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    263161 Aug 10 08:59 passporttrans.20160810.csv.20160810085906725	8:59	8/10/2016		2016-10-08	8:59:06	0.374375	Wed	3	15	2016-08-10 08:59	8
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      6702 Aug 10 08:31 HighlandCapitalManagementRecon201608100730.csv.20160810083134049	8:31	8/10/2016	7:30:00	2016-10-08	8:31:34	0.355255	Wed	3	16	2016-08-10 08:31	8
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       476 Aug 10 02:59 HSBC-LKR.in.10082016-1.20160810025910031	2:59	10/8/2016		2016-10-08	2:59:10	0.124421	Wed	3	17	2016-08-10 02:59	8
John Hancock Investments	HAN_TRANS_HANVER_20160810.csv.20160810153739530	15:37	8/10/2016		2016-10-08	15:37:39	0.651146	Wed	3	18	2016-08-10 15:37	8
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       146 Aug 10 10:27 PresimaOrders.csv.20160810102715995	10:27			2016-10-08	10:27:15	0.43559	Wed	3	25	2016-08-10 10:27	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Aug 10 02:49 FT_fx_20160810_084507.csv.20160810024909501	2:49	8/10/2016	8:45:07	2016-10-08	2:49:09	0.117465	Wed	3	26	2016-08-10 02:49	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Aug 10 03:19 FT_fx_20160810_091638.csv.20160810031911226	3:19	8/10/2016	9:16:38	2016-10-08	3:19:11	0.138322	Wed	3	26	2016-08-10 03:19	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 10 04:15 INV_fx_20160810_101245.csv.20160810041514256	4:15	8/10/2016	10:12:45	2016-10-08	4:15:14	0.177245	Wed	3	26	2016-08-10 04:15	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 10 04:17 FT_fx_20160810_101356.csv.20160810041714746	4:17	8/10/2016	10:13:56	2016-10-08	4:17:14	0.178634	Wed	3	26	2016-08-10 04:17	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Aug 10 04:37 INV_fx_20160810_103407.csv.20160810043715563	4:37	8/10/2016	10:34:07	2016-10-08	4:37:15	0.192535	Wed	3	26	2016-08-10 04:37	8
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug 10 05:13 FT_fx_20160810_110917.csv.20160810051318462	5:13	8/10/2016	11:09:17	2016-10-08	5:13:18	0.217569	Wed	3	26	2016-08-10 05:13	8
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 10 05:21 citicnhtrades.in.201608101714.20160810052119598	5:21	8/10/2016	17:14:00	2016-10-08	5:21:19	0.223137	Wed	3	28	2016-08-10 05:21	8
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       174 Aug 10 05:21 hsbccnhtrades.in.201608101714.20160810052119910	5:21	8/10/2016	17:14:00	2016-10-08	5:21:19	0.223137	Wed	3	29	2016-08-10 05:21	8
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24198 Aug 10 10:23 RSWGD1-17_SSGM_Confirmed_File__20160810.csv.20160810102315601	10:23	8/10/2016		2016-10-08	10:23:15	0.432813	Wed	3	30	2016-08-10 10:23	8
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7445 Aug 10 09:31 TIAACREFREPAT.csv.20160810093111408	9:31			2016-10-08	9:31:11	0.396655	Wed	3	32	2016-08-10 09:31	8
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1304 Aug 10 10:31 TIAACREFREPAT.csv.20160810103116818	10:31			2016-10-08	10:31:16	0.43838	Wed	3	32	2016-08-10 10:31	8
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       403 Aug 10 23:13 tokyofundtrades.in.201608111058.20160810231341674	23:13	8/11/2016	10:58:00	2016-10-08	23:13:41	0.967836	Wed	3	33	2016-08-10 23:13	8
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       245 Aug 10 05:47 TrinityStreetFX_100816.csv.20160810054721671	5:47			2016-10-08	5:47:21	0.241215	Wed	3	34	2016-08-10 05:47	8
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        63 Aug 11 09:06 Alger_Orders_20160811090448.csv.20160811090610758	9:06	8/11/2016	9:04:48	2016-11-08	9:06:10	0.379282	Thu	4	1	2016-08-11 09:06	9
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Aug 11 16:08 Alger_Orders_20160811160516.csv.20160811160816927	16:08	8/11/2016	16:05:16	2016-11-08	16:08:16	0.672407	Thu	4	1	2016-08-11 16:08	9
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug 11 05:34 SSC_BAM_FXREQ_20160811_103015.csv.pgp.ndm05.20160811053401633	5:34	8/11/2016	10:30:15	2016-11-08	5:34:01	0.231956	Thu	4	3	2016-08-11 05:34	9
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 11 11:33 SSC_BAM_FXREQ_20160811_163029.csv.pgp.ndm05.20160811113356483	11:33	8/11/2016	16:30:29	2016-11-08	11:33:56	0.481898	Thu	4	3	2016-08-11 11:33	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063856275	6:38			2016-11-08	6:38:56	0.277037	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063856672	6:38			2016-11-08	6:38:56	0.277037	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063856860	6:38			2016-11-08	6:38:56	0.277037	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063857060	6:38			2016-11-08	6:38:57	0.277049	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063857246	6:38			2016-11-08	6:38:57	0.277049	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063857461	6:38			2016-11-08	6:38:57	0.277049	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063857654	6:38			2016-11-08	6:38:57	0.277049	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063857861	6:38			2016-11-08	6:38:57	0.277049	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063858043	6:38			2016-11-08	6:38:58	0.27706	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063858279	6:38			2016-11-08	6:38:58	0.27706	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 06:38 BCRTOFX.txt.20160811063858467	6:38			2016-11-08	6:38:58	0.27706	Thu	4	4	2016-08-11 06:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1827 Aug 11 10:48 BCRTOFX.txt.20160811104818829	10:48			2016-11-08	10:48:18	0.450208	Thu	4	4	2016-08-11 10:48	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1827 Aug 11 10:48 BCRTOFX.txt.20160811104819240	10:48			2016-11-08	10:48:19	0.45022	Thu	4	4	2016-08-11 10:48	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:20 BCRTOFX_1.txt.20160811112020282	11:20			2016-11-08	11:20:20	0.472454	Thu	4	4	2016-08-11 11:20	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:20 BCRTOFX.txt.20160811112020584	11:20			2016-11-08	11:20:20	0.472454	Thu	4	4	2016-08-11 11:20	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:24 BCRTOFX_2.txt.20160811112421860	11:24			2016-11-08	11:24:21	0.475243	Thu	4	4	2016-08-11 11:24	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:24 BCRTOFX.txt.20160811112422087	11:24			2016-11-08	11:24:22	0.475255	Thu	4	4	2016-08-11 11:24	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:30 BCRTOFX_3.txt.20160811113022663	11:30			2016-11-08	11:30:22	0.479421	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:30 BCRTOFX.txt.20160811113022892	11:30			2016-11-08	11:30:22	0.479421	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:30 BCRTOFX_4.txt.20160811113023097	11:30			2016-11-08	11:30:23	0.479433	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:30 BCRTOFX.txt.20160811113023302	11:30			2016-11-08	11:30:23	0.479433	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1499 Aug 11 11:30 BCRTOFX_5.txt.20160811113023500	11:30			2016-11-08	11:30:23	0.479433	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1499 Aug 11 11:30 BCRTOFX_6.txt.20160811113023734	11:30			2016-11-08	11:30:23	0.479433	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1499 Aug 11 11:30 BCRTOFX.txt.20160811113023887	11:30			2016-11-08	11:30:23	0.479433	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX_7.txt.20160811113024100	11:30			2016-11-08	11:30:24	0.479444	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX_8.txt.20160811113024317	11:30			2016-11-08	11:30:24	0.479444	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1499 Aug 11 11:30 BCRTOFX.txt.20160811113024517	11:30			2016-11-08	11:30:24	0.479444	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX_9.txt.20160811113024715	11:30			2016-11-08	11:30:24	0.479444	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX_10.txt.20160811113024893	11:30			2016-11-08	11:30:24	0.479444	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX_11.txt.20160811113025114	11:30			2016-11-08	11:30:25	0.479456	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX.txt.20160811113025320	11:30			2016-11-08	11:30:25	0.479456	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX.txt.20160811113025505	11:30			2016-11-08	11:30:25	0.479456	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX.txt.20160811113025716	11:30			2016-11-08	11:30:25	0.479456	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX.txt.20160811113025916	11:30			2016-11-08	11:30:25	0.479456	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1497 Aug 11 11:30 BCRTOFX.txt.20160811113026120	11:30			2016-11-08	11:30:26	0.479468	Thu	4	4	2016-08-11 11:30	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:38 BCRTOFX_05.txt.20160811113826898	11:38			2016-11-08	11:38:26	0.485023	Thu	4	4	2016-08-11 11:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:38 BCRTOFX.txt.20160811113827174	11:38			2016-11-08	11:38:27	0.485035	Thu	4	4	2016-08-11 11:38	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:40 BCRTOFX_06.txt.20160811114027443	11:40			2016-11-08	11:40:27	0.486424	Thu	4	4	2016-08-11 11:40	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:40 BCRTOFX.txt.20160811114027658	11:40			2016-11-08	11:40:27	0.486424	Thu	4	4	2016-08-11 11:40	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:48 BCRTOFX_07.txt.20160811114828056	11:48			2016-11-08	11:48:28	0.491991	Thu	4	4	2016-08-11 11:48	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:48 BCRTOFX.txt.20160811114828356	11:48			2016-11-08	11:48:28	0.491991	Thu	4	4	2016-08-11 11:48	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:52 BCRTOFX_08.txt.20160811115228695	11:52			2016-11-08	11:52:28	0.494769	Thu	4	4	2016-08-11 11:52	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:52 BCRTOFX.txt.20160811115228900	11:52			2016-11-08	11:52:28	0.494769	Thu	4	4	2016-08-11 11:52	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:52 BCRTOFX_09.txt.20160811115229110	11:52			2016-11-08	11:52:29	0.49478	Thu	4	4	2016-08-11 11:52	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:52 BCRTOFX.txt.20160811115229384	11:52			2016-11-08	11:52:29	0.49478	Thu	4	4	2016-08-11 11:52	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:56 BCRTOFX_010.txt.20160811115629637	11:56			2016-11-08	11:56:29	0.497558	Thu	4	4	2016-08-11 11:56	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:56 BCRTOFX.txt.20160811115630015	11:56			2016-11-08	11:56:30	0.497569	Thu	4	4	2016-08-11 11:56	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:56 BCRTOFX_011.txt.20160811115630358	11:56			2016-11-08	11:56:30	0.497569	Thu	4	4	2016-08-11 11:56	9
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 11 11:56 BCRTOFX.txt.20160811115630518	11:56			2016-11-08	11:56:30	0.497569	Thu	4	4	2016-08-11 11:56	9
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      1962 Aug 11 14:44 BRA_BRA_Ver_20160811.csv.20160811144441854	14:44	8/11/2016		2016-11-08	14:44:41	0.614363	Thu	4	5	2016-08-11 14:44	9
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 11 15:38 CDPSfxv2_TWDorder.20160811.203000.csv.20160811153814955	15:38	8/11/2016	20:30:00	2016-11-08	15:38:14	0.651551	Thu	4	6	2016-08-11 15:38	9
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1014 Aug 11 08:44 SPOT_FET_Instructions_StateStreet_20160811-143528.csv.20160811084408480	8:44	8/11/2016	14:35:28	2016-11-08	8:44:08	0.363981	Thu	4	7	2016-08-11 08:44	9
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 11 16:30 08112016_GAM_GAM_STAR_GS.20160811.csv.20160811163019130	16:30	8/11/2016		2016-11-08	16:30:19	0.68772	Thu	4	9	2016-08-11 16:30	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug 11 10:34 trade10.dat.20160811103417533	10:34			2016-11-08	10:34:17	0.440475	Thu	4	10	2016-08-11 10:34	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Aug 11 12:34 trade10.dat.20160811123433246	12:34			2016-11-08	12:34:33	0.523993	Thu	4	10	2016-08-11 12:34	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Aug 11 14:34 trade10.dat.20160811143440980	14:34			2016-11-08	14:34:40	0.607407	Thu	4	10	2016-08-11 14:34	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     51642 Aug 11 16:24 trade10.dat.20160811162418250	16:24			2016-11-08	16:24:18	0.683542	Thu	4	10	2016-08-11 16:24	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 11 17:04 trade10.dat.20160811170421343	17:04			2016-11-08	17:04:21	0.711354	Thu	4	10	2016-08-11 17:04	9
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 11 18:04 trade10.dat.20160811180430036	18:04			2016-11-08	18:04:30	0.753125	Thu	4	10	2016-08-11 18:04	9
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       930 Aug 11 06:47 UKFCMCurrencyTemplate110816.csv.20160811064758997	6:47			2016-11-08	6:47:58	0.28331	Thu	4	11	2016-08-11 06:47	9
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    257014 Aug 11 09:00 passporttrans.20160811.csv.20160811090009766	9:00	8/11/2016		2016-11-08	9:00:09	0.375104	Thu	4	15	2016-08-11 09:00	9
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1666 Aug 11 08:32 HighlandCapitalManagementRecon201608110730.csv.20160811083207436	8:32	8/11/2016	7:30:00	2016-11-08	8:32:07	0.355637	Thu	4	16	2016-08-11 08:32	9
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       568 Aug 11 03:19 HSBC-LKR.in.11082016-1.20160811031951626	3:19	11/8/2016		2016-11-08	3:19:51	0.138785	Thu	4	17	2016-08-11 03:19	9
John Hancock Investments	HAN_TRANS_HANVER_20160811.csv.20160811153614504	15:36	8/11/2016		2016-11-08	15:36:14	0.650162	Thu	4	18	2016-08-11 15:36	9
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       589 Aug 11 13:32 PGI_Orders_20160811123108.csv.20160811133237129	13:32	8/11/2016	12:31:08	2016-11-08	13:32:37	0.564317	Thu	4	24	2016-08-11 13:32	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 11 03:09 FT_fx_20160811_090726.csv.20160811030950831	3:09	8/11/2016	9:07:26	2016-11-08	3:09:50	0.131829	Thu	4	26	2016-08-11 03:09	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 11 03:59 FT_fx_20160811_095642.csv.20160811035955496	3:59	8/11/2016	9:56:42	2016-11-08	3:59:55	0.166609	Thu	4	26	2016-08-11 03:59	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 11 04:03 INV_fx_20160811_100206.csv.20160811040355948	4:03	8/11/2016	10:02:06	2016-11-08	4:03:55	0.169387	Thu	4	26	2016-08-11 04:03	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 11 04:15 FT_fx_20160811_101246.csv.20160811041556503	4:15	8/11/2016	10:12:46	2016-11-08	4:15:56	0.177731	Thu	4	26	2016-08-11 04:15	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 11 04:51 FT_fx_20160811_104817.csv.20160811045158429	4:51	8/11/2016	10:48:17	2016-11-08	4:51:58	0.202755	Thu	4	26	2016-08-11 04:51	9
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 11 05:12 INV_fx_20160811_111001.csv.20160811051200396	5:12	8/11/2016	11:10:01	2016-11-08	5:12:00	0.216667	Thu	4	26	2016-08-11 05:12	9
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23549 Aug 11 10:24 RSWGD1-17_SSGM_Confirmed_File__20160811.csv.20160811102416434	10:24	8/11/2016		2016-11-08	10:24:16	0.433519	Thu	4	30	2016-08-11 10:24	9
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4140 Aug 11 09:32 TIAACREFREPAT.csv.20160811093212686	9:32			2016-11-08	9:32:12	0.397361	Thu	4	32	2016-08-11 09:32	9
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       800 Aug 11 10:32 TIAACREFREPAT.csv.20160811103216887	10:32			2016-11-08	10:32:16	0.439074	Thu	4	32	2016-08-11 10:32	9
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       636 Aug 11 21:36 tokyofundtrades.in.201608120928.20160811213643191	21:36	8/12/2016	9:28:00	2016-11-08	21:36:43	0.900498	Thu	4	33	2016-08-11 21:36	9
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       197 Aug 12 09:45 Alger_Orders_20160812094257.csv.20160812094516468	9:45	8/12/2016	9:42:57	2016-12-08	9:45:16	0.406435	Fri	5	1	2016-08-12 09:45	10
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1447 Aug 12 04:32 SSC_BAM_FXREQ_20160812_093013.csv.pgp.ndm05.20160812043237748	4:32	8/12/2016	9:30:13	2016-12-08	4:32:37	0.189317	Fri	5	3	2016-08-12 04:32	10
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug 12 11:34 SSC_BAM_FXREQ_20160812_163051.csv.pgp.ndm05.20160812113423840	11:34	8/12/2016	16:30:51	2016-12-08	11:34:23	0.482211	Fri	5	3	2016-08-12 11:34	10
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1422 Aug 12 12:33 SSC_BAM_FXREQ_20160812_173055.csv.pgp.ndm05.20160812123358432	12:33	8/12/2016	17:30:55	2016-12-08	12:33:58	0.523588	Fri	5	3	2016-08-12 12:33	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063832330	6:38			2016-12-08	6:38:32	0.276759	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063832675	6:38			2016-12-08	6:38:32	0.276759	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063832872	6:38			2016-12-08	6:38:32	0.276759	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063833087	6:38			2016-12-08	6:38:33	0.276771	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063833321	6:38			2016-12-08	6:38:33	0.276771	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063833545	6:38			2016-12-08	6:38:33	0.276771	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063833750	6:38			2016-12-08	6:38:33	0.276771	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063833927	6:38			2016-12-08	6:38:33	0.276771	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063834135	6:38			2016-12-08	6:38:34	0.276782	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063834376	6:38			2016-12-08	6:38:34	0.276782	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063834589	6:38			2016-12-08	6:38:34	0.276782	Fri	5	4	2016-08-12 06:38	10
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 12 06:38 BCRTOFX.txt.20160812063834747	6:38			2016-12-08	6:38:34	0.276782	Fri	5	4	2016-08-12 06:38	10
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      8222 Aug 12 12:31 BRA_BRA_Ver_20160811.csv.20160812123127712	12:31	8/11/2016		2016-12-08	12:31:27	0.52184	Fri	5	5	2016-08-12 12:31	10
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2251 Aug 12 14:29 BRA_BRA_Ver_20160812.csv.20160812142904750	14:29	8/12/2016		2016-12-08	14:29:04	0.603519	Fri	5	5	2016-08-12 14:29	10
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2441 Aug 12 14:35 BRA_BRA_Ver_20160812.csv.20160812143506436	14:35	8/12/2016		2016-12-08	14:35:06	0.607708	Fri	5	5	2016-08-12 14:35	10
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      8217 Aug 12 17:19 BRA_BRA_Ver_20160811.csv.20160812171916656	17:19	8/11/2016		2016-12-08	17:19:16	0.721713	Fri	5	5	2016-08-12 17:19	10
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug 12 20:33 CDPSfxv2_TWDorder.20160812.203000.csv.20160812203333639	20:33	8/12/2016	20:30:00	2016-12-08	20:33:33	0.856632	Fri	5	6	2016-08-12 20:33	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 12 10:33 trade10.dat.20160812103319679	10:33			2016-12-08	10:33:19	0.439803	Fri	5	10	2016-08-12 10:33	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 12 12:32 trade10.dat.20160812123258129	12:32			2016-12-08	12:32:58	0.522894	Fri	5	10	2016-08-12 12:32	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 12 14:33 trade10.dat.20160812143305540	14:33			2016-12-08	14:33:05	0.606308	Fri	5	10	2016-08-12 14:33	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     17790 Aug 12 16:23 trade10.dat.20160812162312082	16:23			2016-12-08	16:23:12	0.682778	Fri	5	10	2016-08-12 16:23	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 12 17:03 trade10.dat.20160812170314431	17:03			2016-12-08	17:03:14	0.710579	Fri	5	10	2016-08-12 17:03	10
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 12 18:03 trade10.dat.20160812180323277	18:03			2016-12-08	18:03:23	0.75235	Fri	5	10	2016-08-12 18:03	10
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       179 Aug 12 05:36 UKFCMCurrencyTemplate120816.csv.20160812053642776	5:36			2016-12-08	5:36:42	0.233819	Fri	5	11	2016-08-12 05:36	10
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    257711 Aug 12 09:01 passporttrans.20160812.csv.20160812090111820	9:01	8/12/2016		2016-12-08	9:01:11	0.375822	Fri	5	15	2016-08-12 09:01	10
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 12 08:31 HighlandCapitalManagementRecon201608120730.csv.20160812083109864	8:31	8/12/2016	7:30:00	2016-12-08	8:31:09	0.354965	Fri	5	16	2016-08-12 08:31	10
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       376 Aug 12 14:07 Highland_Orders_20160812csv.20160812140703100	14:07	8/12/2016		2016-12-08	14:07:03	0.588229	Fri	5	16	2016-08-12 14:07	10
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       742 Aug 12 02:04 HSBC-LKR.in.12082016-1.20160812020457338	2:04	12/8/2016		2016-12-08	2:04:57	0.086771	Fri	5	17	2016-08-12 02:04	10
John Hancock Investments	HAN_TRANS_HANVER_20160812.csv.20160812153509447	15:35	8/12/2016		2016-12-08	15:35:09	0.64941	Fri	5	18	2016-08-12 15:35	10
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       607 Aug 12 12:21 PGI_Orders_20160812111915.csv.20160812122126596	12:21	8/12/2016	11:19:15	2016-12-08	12:21:26	0.514884	Fri	5	24	2016-08-12 12:21	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 12 03:13 FT_fx_20160812_090957.csv.20160812031301350	3:13	8/12/2016	9:09:57	2016-12-08	3:13:01	0.134039	Fri	5	26	2016-08-12 03:13	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 12 03:37 INV_fx_20160812_093345.csv.20160812033703393	3:37	8/12/2016	9:33:45	2016-12-08	3:37:03	0.150729	Fri	5	26	2016-08-12 03:37	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 12 04:26 INV_fx_20160812_102358.csv.20160812042636931	4:26	8/12/2016	10:23:58	2016-12-08	4:26:36	0.185139	Fri	5	26	2016-08-12 04:26	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Aug 12 04:28 FT_fx_20160812_102433.csv.20160812042837304	4:28	8/12/2016	10:24:33	2016-12-08	4:28:37	0.186539	Fri	5	26	2016-08-12 04:28	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 12 05:06 FT_fx_20160812_110310.csv.20160812050640284	5:06	8/12/2016	11:03:10	2016-12-08	5:06:40	0.212963	Fri	5	26	2016-08-12 05:06	10
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 12 05:12 INV_fx_20160812_111106.csv.20160812051240843	5:12	8/12/2016	11:11:06	2016-12-08	5:12:40	0.21713	Fri	5	26	2016-08-12 05:12	10
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 12 05:26 citicnhtrades.in.201608121713.20160812052641754	5:26	8/12/2016	17:13:00	2016-12-08	5:26:41	0.226863	Fri	5	28	2016-08-12 05:26	10
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        58 Aug 12 05:26 hsbccnhtrades.in.201608121713.20160812052642179	5:26	8/12/2016	17:13:00	2016-12-08	5:26:42	0.226875	Fri	5	29	2016-08-12 05:26	10
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24283 Aug 12 10:59 RSWGD1-17_SSGM_Confirmed_File__20160812.csv.20160812105921696	10:59	8/12/2016		2016-12-08	10:59:21	0.457882	Fri	5	30	2016-08-12 10:59	10
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4912 Aug 12 09:31 TIAACREFREPAT.csv.20160812093114727	9:31			2016-12-08	9:31:14	0.39669	Fri	5	32	2016-08-12 09:31	10
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       306 Aug 12 15:31 TIAACREFREPAT.csv.20160812153108746	15:31			2016-12-08	15:31:08	0.64662	Fri	5	32	2016-08-12 15:31	10
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       351 Aug 14 21:36 tokyofundtrades.in.201608150929.20160814213651773	21:36	8/15/2016	9:29:00	2016-14-08	21:36:51	0.90059	Sun	7	33	2016-14-8 21:36:51	#N/A
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       349 Aug 14 23:08 tokyofundtrades.in.201608151103.20160814230855874	23:08	8/15/2016	11:03:00	2016-14-08	23:08:55	0.964525	Sun	7	33	2016-14-8 23:08:55	#N/A
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Aug 15 06:08 SSC_BAM_FXREQ_20160815_103014.csv.pgp.20160815060849097	6:08	8/15/2016	10:30:14	2016-15-08	6:08:49	0.256123	Mon	1	3	2016-15-8 6:08:49	11
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 15 07:08 SSC_BAM_FXREQ_20160815_113017.csv.pgp.20160815070853874	7:08	8/15/2016	11:30:17	2016-15-08	7:08:53	0.297836	Mon	1	3	2016-15-8 7:08:53	11
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Aug 15 09:14 SSC_BAM_FXREQ_20160815_103014.csv.pgp.ndm05.20160815091430210	9:14	8/15/2016	10:30:14	2016-15-08	9:14:30	0.385069	Mon	1	3	2016-15-8 9:14:30	11
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 15 09:14 SSC_BAM_FXREQ_20160815_113017.csv.pgp.ndm05.20160815091430476	9:14	8/15/2016	11:30:17	2016-15-08	9:14:30	0.385069	Mon	1	3	2016-15-8 9:14:30	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063750820	6:37			2016-15-08	6:37:50	0.276273	Mon	1	4	2016-15-8 6:37:50	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063751207	6:37			2016-15-08	6:37:51	0.276285	Mon	1	4	2016-15-8 6:37:51	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063751421	6:37			2016-15-08	6:37:51	0.276285	Mon	1	4	2016-15-8 6:37:51	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063751630	6:37			2016-15-08	6:37:51	0.276285	Mon	1	4	2016-15-8 6:37:51	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063751857	6:37			2016-15-08	6:37:51	0.276285	Mon	1	4	2016-15-8 6:37:51	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063752027	6:37			2016-15-08	6:37:52	0.276296	Mon	1	4	2016-15-8 6:37:52	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063752253	6:37			2016-15-08	6:37:52	0.276296	Mon	1	4	2016-15-8 6:37:52	11
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 15 06:37 BCRTOFX.txt.20160815063752460	6:37			2016-15-08	6:37:52	0.276296	Mon	1	4	2016-15-8 6:37:52	11
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      1470 Aug 15 14:39 BRA_BRA_Ver_20160815.csv.20160815143921712	14:39	8/15/2016		2016-15-08	14:39:21	0.61066	Mon	1	5	2016-15-8 14:39:21	11
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 15 21:33 CDPSfxv_TWDorder.20160815.213000.csv.20160815213312473	21:33	8/15/2016	21:30:00	2016-15-08	21:33:12	0.898056	Mon	1	6	2016-15-8 21:33:12	11
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1434 Aug 15 06:16 SPOT_FET_Instructions_StateStreet_20160815-120701.csv.20160815061649734	6:16	8/15/2016	12:07:01	2016-15-08	6:16:49	0.261678	Mon	1	7	2016-15-8 6:16:49	11
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 16:49 08152016_GAM_GAM_STAR_GS.20160815.csv.20160815164926593	16:49	8/15/2016		2016-15-08	16:49:26	0.700995	Mon	1	9	2016-15-8 16:49:26	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 10:33 trade10.dat.20160815103305665	10:33			2016-15-08	10:33:05	0.439641	Mon	1	10	2016-15-8 10:33:05	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 12:33 trade10.dat.20160815123314616	12:33			2016-15-08	12:33:14	0.523079	Mon	1	10	2016-15-8 12:33:14	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 14:33 trade10.dat.20160815143320871	14:33			2016-15-08	14:33:20	0.606481	Mon	1	10	2016-15-8 14:33:20	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     19526 Aug 15 16:23 trade10.dat.20160815162325238	16:23			2016-15-08	16:23:25	0.682928	Mon	1	10	2016-15-8 16:23:25	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 17:03 trade10.dat.20160815170328103	17:03			2016-15-08	17:03:28	0.710741	Mon	1	10	2016-15-8 17:03:28	11
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 18:03 trade10.dat.20160815180302315	18:03			2016-15-08	18:03:02	0.752106	Mon	1	10	2016-15-8 18:03:02	11
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr      1764 Aug 15 05:07 UKFCMCurrencyTemplate150816.csv.20160815050713243	5:07			2016-15-08	5:07:13	0.213345	Mon	1	11	2016-15-8 5:07:13	11
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       178 Aug 15 06:44 UKFCMCurrencyTemplate150816a.csv.20160815064452899	6:44			2016-15-08	6:44:52	0.281157	Mon	1	11	2016-15-8 6:44:52	11
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       177 Aug 15 07:44 UKFCMCurrencyTemplate150816b.csv.20160815074455906	7:44			2016-15-08	7:44:55	0.322859	Mon	1	11	2016-15-8 7:44:55	11
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 15 08:54 passporttrans.20160815.csv.20160815085458738	8:54	8/15/2016		2016-15-08	8:54:58	0.371505	Mon	1	15	2016-15-8 8:54:58	11
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 15 08:30 HighlandCapitalManagementRecon201608150730.csv.20160815083057774	8:30	8/15/2016	7:30:00	2016-15-08	8:30:57	0.354826	Mon	1	16	2016-15-8 8:30:57	11
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       209 Aug 15 02:55 HSBC-LKR.in.15082016-1.20160815025506908	2:55	8/15/2016		2016-15-08	2:55:06	0.121597	Mon	1	17	2016-15-8 2:55:06	11
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       664 Aug 15 03:05 HSBC-LKR.in.15082016-1.20160815030507732	3:05	8/15/2016		2016-15-08	3:05:07	0.128553	Mon	1	17	2016-15-8 3:05:07	11
John Hancock Investments	HAN_TRANS_HANVER_20160815.csv.20160815154323486	15:43	8/15/2016		2016-15-08	15:43:23	0.655127	Mon	1	18	2016-15-8 15:43:23	11
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       116 Aug 15 04:25 citicnhtrades.in.201608151607.20160815042511396	4:25	8/15/2016	16:07:00	2016-15-08	4:25:11	0.184155	Mon	1	28	2016-15-8 4:25:11	11
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 15 05:26 citicnhtrades.in.201608151716.20160815052644594	5:26	8/15/2016	17:16:00	2016-15-08	5:26:44	0.226898	Mon	1	28	2016-15-8 5:26:44	11
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       112 Aug 15 05:26 hsbccnhtrades.in.201608151716.20160815052644869	5:26	8/15/2016	17:16:00	2016-15-08	5:26:44	0.226898	Mon	1	29	2016-15-8 5:26:44	11
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3612 Aug 15 09:47 tcwta20160815.csv.20160815.094451.20160815094702699	9:47	8/15/2016		2016-15-08	9:47:02	0.407662	Mon	1	31	2016-15-8 9:47:02	11
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     21696 Aug 15 09:31 TIAACREFREPAT.csv.20160815093101907	9:31			2016-15-08	9:31:01	0.396539	Mon	1	32	2016-15-8 9:31:01	11
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       411 Aug 15 10:31 TIAACREFREPAT.csv.20160815103105007	10:31			2016-15-08	10:31:05	0.438252	Mon	1	32	2016-15-8 10:31:05	11
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       377 Aug 15 22:55 tokyofundtrades.in.201608161049.20160815225517864	22:55	8/16/2016	10:49:00	2016-15-08	22:55:17	0.955058	Mon	1	33	2016-15-8 22:55:17	11
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       398 Aug 15 23:17 tokyofundtrades.in.201608161113.20160815231719083	23:17	8/16/2016	11:13:00	2016-15-08	23:17:19	0.970359	Mon	1	33	2016-15-8 23:17:19	11
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       296 Aug 15 10:39 TrinityStreetFX_081516.csv.20160815103906420	10:39			2016-15-08	10:39:06	0.443819	Mon	1	34	2016-15-8 10:39:06	11
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 16 04:33 SSC_BAM_FXREQ_20160816_093027.csv.pgp.ndm05.20160816043302655	4:33	8/16/2016	9:30:27	2016-16-08	4:33:02	0.189606	Tue	2	3	2016-16-8 4:33:02	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug 16 06:33 SSC_BAM_FXREQ_20160816_113034.csv.pgp.ndm05.20160816063309245	6:33	8/16/2016	11:30:34	2016-16-08	6:33:09	0.273021	Tue	2	3	2016-16-8 6:33:09	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1519 Aug 16 11:13 SSC_BAM_FXREQ_20160816_153046.csv.pgp.20160816111327317	11:13	8/16/2016	15:30:46	2016-16-08	11:13:27	0.467674	Tue	2	3	2016-16-8 11:13:27	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1542 Aug 16 12:03 SSC_BAM_FXREQ_20160816_163049.csv.pgp.20160816120331377	12:03	8/16/2016	16:30:49	2016-16-08	12:03:31	0.502442	Tue	2	3	2016-16-8 12:03:31	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1519 Aug 16 12:23 SSC_BAM_FXREQ_20160816_153046.csv.pgp.ndm05.20160816122332859	12:23	8/16/2016	15:30:46	2016-16-08	12:23:32	0.516343	Tue	2	3	2016-16-8 12:23:32	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1542 Aug 16 12:23 SSC_BAM_FXREQ_20160816_163049.csv.pgp.ndm05.20160816122333203	12:23	8/16/2016	16:30:49	2016-16-08	12:23:33	0.516354	Tue	2	3	2016-16-8 12:23:33	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1510 Aug 16 12:38 SSC_BAM_FXREQ_20160816_173056.csv.pgp.ndm05.20160816123804462	12:38	8/16/2016	17:30:56	2016-16-08	12:38:04	0.526435	Tue	2	3	2016-16-8 12:38:04	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063809799	6:38			2016-16-08	6:38:09	0.276493	Tue	2	4	2016-16-8 6:38:09	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063809960	6:38			2016-16-08	6:38:09	0.276493	Tue	2	4	2016-16-8 6:38:09	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063810146	6:38			2016-16-08	6:38:10	0.276505	Tue	2	4	2016-16-8 6:38:10	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063810366	6:38			2016-16-08	6:38:10	0.276505	Tue	2	4	2016-16-8 6:38:10	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063810558	6:38			2016-16-08	6:38:10	0.276505	Tue	2	4	2016-16-8 6:38:10	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063810755	6:38			2016-16-08	6:38:10	0.276505	Tue	2	4	2016-16-8 6:38:10	12
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 16 06:38 BCRTOFX.txt.20160816063810935	6:38			2016-16-08	6:38:10	0.276505	Tue	2	4	2016-16-8 6:38:10	12
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2932 Aug 16 14:43 BRA_BRA_Ver_20160816.csv.20160816144340632	14:43	8/16/2016		2016-16-08	14:43:40	0.613657	Tue	2	5	2016-16-8 14:43:40	12
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 16 20:34 CDPSfx_TWDorder.20160816.203000.csv.20160816203402520	20:34	8/16/2016	20:30:00	2016-16-08	20:34:02	0.856968	Tue	2	6	2016-16-8 20:34:02	12
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1459 Aug 16 10:09 SPOT_FET_Instructions_StateStreet_20160816-153711.csv.20160816100923610	10:09	8/16/2016	15:37:11	2016-16-08	10:09:23	0.423183	Tue	2	7	2016-16-8 10:09:23	12
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 16 16:21 08162016_GAM_GAM_STAR_GS.20160816.csv.20160816162145618	16:21	8/16/2016		2016-16-08	16:21:45	0.681771	Tue	2	9	2016-16-8 16:21:45	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 16 10:33 trade10.dat.20160816103325342	10:33			2016-16-08	10:33:25	0.439873	Tue	2	10	2016-16-8 10:33:25	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 16 12:33 trade10.dat.20160816123333832	12:33			2016-16-08	12:33:33	0.523299	Tue	2	10	2016-16-8 12:33:33	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 16 14:33 trade10.dat.20160816143339983	14:33			2016-16-08	14:33:39	0.606701	Tue	2	10	2016-16-8 14:33:39	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Aug 16 16:23 trade10.dat.20160816162345989	16:23			2016-16-08	16:23:45	0.68316	Tue	2	10	2016-16-8 16:23:45	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Aug 16 17:03 trade10.dat.20160816170349232	17:03			2016-16-08	17:03:49	0.710984	Tue	2	10	2016-16-8 17:03:49	12
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 16 18:03 trade10.dat.20160816180353315	18:03			2016-16-08	18:03:53	0.752697	Tue	2	10	2016-16-8 18:03:53	12
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    422640 Aug 16 09:13 passporttrans.20160816.csv.20160816091349024	9:13	8/16/2016		2016-16-08	9:13:49	0.384595	Tue	2	15	2016-16-8 9:13:49	12
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 16 08:31 HighlandCapitalManagementRecon201608160730.csv.20160816083145947	8:31	8/16/2016	7:30:00	2016-16-08	8:31:45	0.355382	Tue	2	16	2016-16-8 8:31:45	12
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       393 Aug 16 03:43 HSBC-LKR.in.16082016-1.20160816034330640	3:43	8/16/2016		2016-16-08	3:43:30	0.155208	Tue	2	17	2016-16-8 3:43:30	12
John Hancock Investments	HAN_TRANS_HANVER_20160816.csv.20160816152942487	15:29	8/16/2016		2016-16-08	15:29:42	0.645625	Tue	2	18	2016-16-8 15:29:42	12
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       290 Aug 16 11:09 PGI_Orders_20160816100734.csv.20160816110926752	11:09	8/16/2016	10:07:34	2016-16-08	11:09:26	0.464884	Tue	2	24	2016-16-8 11:09:26	12
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 16 03:03 FT_fx_20160816_090218.csv.20160816030328204	3:03	8/16/2016	9:02:18	2016-16-08	3:03:28	0.127407	Tue	2	26	2016-16-8 3:03:28	12
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 16 04:41 INV_fx_20160816_103921.csv.20160816044133242	4:41	8/16/2016	10:39:21	2016-16-08	4:41:33	0.195521	Tue	2	26	2016-16-8 4:41:33	12
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       296 Aug 16 05:27 FT_fx_20160816_112622.csv.20160816052736626	5:27	8/16/2016	11:26:22	2016-16-08	5:27:36	0.2275	Tue	2	26	2016-16-8 5:27:36	12
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 16 05:27 citicnhtrades.in.201608161714.20160816052736187	5:27	8/16/2016	17:14:00	2016-16-08	5:27:36	0.2275	Tue	2	28	2016-16-8 5:27:36	12
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        57 Aug 16 05:27 hsbccnhtrades.in.201608161714.20160816052736428	5:27	8/16/2016	17:14:00	2016-16-08	5:27:36	0.2275	Tue	2	29	2016-16-8 5:27:36	12
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24828 Aug 16 11:17 RSWGD1-17_SSGM_Confirmed_File__20160816.csv.20160816111727693	11:17	8/16/2016		2016-16-08	11:17:27	0.470451	Tue	2	30	2016-16-8 11:17:27	12
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       174 Aug 16 09:55 tcwgt20160816.csv.20160816.095354.20160816095522091	9:55	8/16/2016		2016-16-08	9:55:22	0.413449	Tue	2	31	2016-16-8 9:55:22	12
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6926 Aug 16 09:31 TIAACREFREPAT.csv.20160816093150695	9:31			2016-16-08	9:31:50	0.397106	Tue	2	32	2016-16-8 9:31:50	12
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1411 Aug 16 10:31 TIAACREFREPAT.csv.20160816103124363	10:31			2016-16-08	10:31:24	0.438472	Tue	2	32	2016-16-8 10:31:24	12
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       419 Aug 16 13:31 TIAACREFREPAT.csv.20160816133136953	13:31			2016-16-08	13:31:36	0.563611	Tue	2	32	2016-16-8 13:31:36	12
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       641 Aug 16 15:31 TIAACREFREPAT.csv.20160816153143292	15:31			2016-16-08	15:31:43	0.647025	Tue	2	32	2016-16-8 15:31:43	12
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       644 Aug 16 21:30 tokyofundtrades.in.201608170918.20160816213005565	21:30	8/17/2016	9:18:00	2016-16-08	21:30:05	0.895891	Tue	2	33	2016-16-8 21:30:05	12
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug 17 05:35 SSC_BAM_FXREQ_20160817_103011.csv.pgp.ndm05.20160817053501022	5:35	8/17/2016	10:30:11	2016-17-08	5:35:01	0.23265	Wed	3	3	2016-17-8 5:35:01	13
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1440 Aug 17 06:33 SSC_BAM_FXREQ_20160817_113014.csv.pgp.ndm05.20160817063333529	6:33	8/17/2016	11:30:14	2016-17-08	6:33:33	0.273299	Wed	3	3	2016-17-8 6:33:33	13
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1431 Aug 17 12:32 SSC_BAM_FXREQ_20160817_173027.csv.pgp.ndm05.20160817123258317	12:32	8/17/2016	17:30:27	2016-17-08	12:32:58	0.522894	Wed	3	3	2016-17-8 12:32:58	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063804091	6:38			2016-17-08	6:38:04	0.276435	Wed	3	4	2016-17-8 6:38:04	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063804259	6:38			2016-17-08	6:38:04	0.276435	Wed	3	4	2016-17-8 6:38:04	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063804467	6:38			2016-17-08	6:38:04	0.276435	Wed	3	4	2016-17-8 6:38:04	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063804662	6:38			2016-17-08	6:38:04	0.276435	Wed	3	4	2016-17-8 6:38:04	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063804857	6:38			2016-17-08	6:38:04	0.276435	Wed	3	4	2016-17-8 6:38:04	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063805051	6:38			2016-17-08	6:38:05	0.276447	Wed	3	4	2016-17-8 6:38:05	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063805273	6:38			2016-17-08	6:38:05	0.276447	Wed	3	4	2016-17-8 6:38:05	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063805469	6:38			2016-17-08	6:38:05	0.276447	Wed	3	4	2016-17-8 6:38:05	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063805688	6:38			2016-17-08	6:38:05	0.276447	Wed	3	4	2016-17-8 6:38:05	13
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 17 06:38 BCRTOFX.txt.20160817063805923	6:38			2016-17-08	6:38:05	0.276447	Wed	3	4	2016-17-8 6:38:05	13
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2474 Aug 17 14:38 BRA_BRA_Ver_20160817.csv.20160817143805181	14:38	8/17/2016		2016-17-08	14:38:05	0.60978	Wed	3	5	2016-17-8 14:38:05	13
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Aug 17 20:34 CDPSfx_TWDorder.20160817.203500.csv.20160817203426382	20:34	8/17/2016	20:35:00	2016-17-08	20:34:26	0.857245	Wed	3	6	2016-17-8 20:34:26	13
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Aug 17 05:11 scbcnhtrades1.in.201608171657.20160817051158987	5:11	8/17/2016	16:57:00	2016-17-08	5:11:58	0.216644	Wed	3	7	2016-17-8 5:11:58	13
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 17 05:11 scbcnhtrades2.in.201608171657.20160817051159395	5:11	8/17/2016	16:57:00	2016-17-08	5:11:59	0.216655	Wed	3	7	2016-17-8 5:11:59	13
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1587 Aug 17 09:23 SPOT_FET_Instructions_StateStreet_20160817-151740.csv.20160817092345263	9:23	8/17/2016	15:17:40	2016-17-08	9:23:45	0.391493	Wed	3	7	2016-17-8 9:23:45	13
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       513 Aug 17 06:32 CRUX_20160817.csv.20160817063203129	6:32	8/17/2016		2016-17-08	6:32:03	0.272257	Wed	3	8	2016-17-8 6:32:03	13
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       121 Aug 17 17:00 08172016_GAM_GAM_STAR_GS.20160817.csv.20160817170012501	17:00	8/17/2016		2016-17-08	17:00:12	0.708472	Wed	3	9	2016-17-8 17:00:12	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 17 10:33 trade10.dat.20160817103351675	10:33			2016-17-08	10:33:51	0.440174	Wed	3	10	2016-17-8 10:33:51	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      8242 Aug 17 12:33 trade10.dat.20160817123358700	12:33			2016-17-08	12:33:58	0.523588	Wed	3	10	2016-17-8 12:33:58	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug 17 14:34 trade10.dat.20160817143404648	14:34			2016-17-08	14:34:04	0.606991	Wed	3	10	2016-17-8 14:34:04	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9978 Aug 17 16:24 trade10.dat.20160817162409754	16:24			2016-17-08	16:24:09	0.683438	Wed	3	10	2016-17-8 16:24:09	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 17 17:04 trade10.dat.20160817170413805	17:04			2016-17-08	17:04:13	0.711262	Wed	3	10	2016-17-8 17:04:13	13
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 17 18:04 trade10.dat.20160817180418163	18:04			2016-17-08	18:04:18	0.752986	Wed	3	10	2016-17-8 18:04:18	13
Glendon	-rw-r--r--   1 ftpgmrin ftpgmr       166 Aug 17 10:07 GlendonOrders.csv.20160817100748471	10:07			2016-17-08	10:07:48	0.422083	Wed	3	14	2016-17-8 10:07:48	13
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    264857 Aug 17 09:04 passporttrans.20160817.csv.20160817090412602	9:04	8/17/2016		2016-17-08	9:04:12	0.377917	Wed	3	15	2016-17-8 9:04:12	13
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1666 Aug 17 08:32 HighlandCapitalManagementRecon201608170730.csv.20160817083210692	8:32	8/17/2016	7:30:00	2016-17-08	8:32:10	0.355671	Wed	3	16	2016-17-8 8:32:10	13
John Hancock Investments	HAN_TRANS_HANVER_20160817.csv.20160817153807444	15:38	8/17/2016		2016-17-08	15:38:07	0.65147	Wed	3	18	2016-17-8 15:38:07	13
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 17 03:13 FT_fx_20160817_091220.csv.20160817031351458	3:13	8/17/2016	9:12:20	2016-17-08	3:13:51	0.134618	Wed	3	26	2016-17-8 3:13:51	13
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 17 03:49 INV_fx_20160817_094719.csv.20160817034953702	3:49	8/17/2016	9:47:19	2016-17-08	3:49:53	0.159641	Wed	3	26	2016-17-8 3:49:53	13
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 17 04:15 INV_fx_20160817_101255.csv.20160817041554919	4:15	8/17/2016	10:12:55	2016-17-08	4:15:54	0.177708	Wed	3	26	2016-17-8 4:15:54	13
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 17 04:43 FT_fx_20160817_104139.csv.20160817044356495	4:43	8/17/2016	10:41:39	2016-17-08	4:43:56	0.197176	Wed	3	26	2016-17-8 4:43:56	13
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 17 05:05 FT_fx_20160817_110425.csv.20160817050558604	5:05	8/17/2016	11:04:25	2016-17-08	5:05:58	0.212477	Wed	3	26	2016-17-8 5:05:58	13
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 17 05:26 citicnhtrades.in.201608171720.20160817052600004	5:26	8/17/2016	17:20:00	2016-17-08	5:26:00	0.226389	Wed	3	28	2016-17-8 5:26:00	13
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       175 Aug 17 05:26 hsbccnhtrades.in.201608171720.20160817052600441	5:26	8/17/2016	17:20:00	2016-17-08	5:26:00	0.226389	Wed	3	29	2016-17-8 5:26:00	13
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     31305 Aug 17 10:27 RSWGD1-17_SSGM_Confirmed_File__20160817.csv.20160817102750681	10:27	8/17/2016		2016-17-08	10:27:50	0.435995	Wed	3	30	2016-17-8 10:27:50	13
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4091 Aug 17 09:31 TIAACREFREPAT.csv.20160817093145757	9:31			2016-17-08	9:31:45	0.397049	Wed	3	32	2016-17-8 9:31:45	13
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       316 Aug 17 10:31 TIAACREFREPAT.csv.20160817103151137	10:31			2016-17-08	10:31:51	0.438785	Wed	3	32	2016-17-8 10:31:51	13
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       700 Aug 17 21:34 tokyofundtrades.in.201608180931.20160817213429294	21:34	8/18/2016	9:31:00	2016-17-08	21:34:29	0.898947	Wed	3	33	2016-17-8 21:34:29	13
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       230 Aug 17 10:15 TrinityStreetFX_081716.csv.20160817101548993	10:15			2016-17-08	10:15:48	0.427639	Wed	3	34	2016-17-8 10:15:48	13
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Aug 18 09:12 Alger_Orders_20160818090940.csv.20160818091238081	9:12	8/18/2016	9:09:40	2016-18-08	9:12:38	0.383773	Thu	4	1	2016-18-8 9:12:38	14
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1738 Aug 18 04:33 SSC_BAM_FXREQ_20160818_093001.csv.pgp.ndm05.20160818043318750	4:33	8/18/2016	9:30:01	2016-18-08	4:33:18	0.189792	Thu	4	3	2016-18-8 4:33:18	14
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug 18 09:19 SSC_BAM_FXREQ_20160817_103011.csv.pgp.ndm05.20160818091938986	9:19	8/17/2016	10:30:11	2016-18-08	9:19:38	0.388634	Thu	4	3	2016-18-8 9:19:38	14
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 18 11:33 SSC_BAM_FXREQ_20160818_163018.csv.pgp.ndm05.20160818113347991	11:33	8/18/2016	16:30:18	2016-18-08	11:33:47	0.481794	Thu	4	3	2016-18-8 11:33:47	14
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1462 Aug 18 12:34 SSC_BAM_FXREQ_20160818_173020.csv.pgp.ndm05.20160818123421261	12:34	8/18/2016	17:30:20	2016-18-08	12:34:21	0.523854	Thu	4	3	2016-18-8 12:34:21	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063827872	6:38			2016-18-08	6:38:27	0.276701	Thu	4	4	2016-18-8 6:38:27	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063828285	6:38			2016-18-08	6:38:28	0.276713	Thu	4	4	2016-18-8 6:38:28	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063828476	6:38			2016-18-08	6:38:28	0.276713	Thu	4	4	2016-18-8 6:38:28	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063828674	6:38			2016-18-08	6:38:28	0.276713	Thu	4	4	2016-18-8 6:38:28	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063828892	6:38			2016-18-08	6:38:28	0.276713	Thu	4	4	2016-18-8 6:38:28	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063829106	6:38			2016-18-08	6:38:29	0.276725	Thu	4	4	2016-18-8 6:38:29	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063829347	6:38			2016-18-08	6:38:29	0.276725	Thu	4	4	2016-18-8 6:38:29	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063829732	6:38			2016-18-08	6:38:29	0.276725	Thu	4	4	2016-18-8 6:38:29	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063830104	6:38			2016-18-08	6:38:30	0.276736	Thu	4	4	2016-18-8 6:38:30	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063830283	6:38			2016-18-08	6:38:30	0.276736	Thu	4	4	2016-18-8 6:38:30	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063830479	6:38			2016-18-08	6:38:30	0.276736	Thu	4	4	2016-18-8 6:38:30	14
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 18 06:38 BCRTOFX.txt.20160818063830667	6:38			2016-18-08	6:38:30	0.276736	Thu	4	4	2016-18-8 6:38:30	14
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2855 Aug 18 14:40 BRA_BRA_Ver_20160818.csv.20160818144029941	14:40	8/18/2016		2016-18-08	14:40:29	0.611447	Thu	4	5	2016-18-8 14:40:29	14
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       335 Aug 18 12:34 CDPSfx_KRWorder.20160818.123500.csv.20160818123421792	12:34	8/18/2016	12:35:00	2016-18-08	12:34:21	0.523854	Thu	4	6	2016-18-8 12:34:21	14
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Aug 18 06:12 scbcnhtrades1.in.201608181800.20160818061226642	6:12	8/18/2016	18:00:00	2016-18-08	6:12:26	0.258634	Thu	4	7	2016-18-8 6:12:26	14
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 18 06:12 scbcnhtrades2.in.201608181800.20160818061226941	6:12	8/18/2016	18:00:00	2016-18-08	6:12:26	0.258634	Thu	4	7	2016-18-8 6:12:26	14
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1005 Aug 18 10:04 SPOT_FET_Instructions_StateStreet_20160818-155807.csv.20160818100442288	10:04	8/18/2016	15:58:07	2016-18-08	10:04:42	0.419931	Thu	4	7	2016-18-8 10:04:42	14
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 18 17:04 08182016_GAM_GAM_STAR_GS.20160818.csv.20160818170437214	17:04	8/18/2016		2016-18-08	17:04:37	0.711539	Thu	4	9	2016-18-8 17:04:37	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 18 10:34 trade10.dat.20160818103444834	10:34			2016-18-08	10:34:44	0.440787	Thu	4	10	2016-18-8 10:34:44	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Aug 18 12:34 trade10.dat.20160818123421591	12:34			2016-18-08	12:34:21	0.523854	Thu	4	10	2016-18-8 12:34:21	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 18 14:34 trade10.dat.20160818143429304	14:34			2016-18-08	14:34:29	0.60728	Thu	4	10	2016-18-8 14:34:29	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     41660 Aug 18 16:24 trade10.dat.20160818162434661	16:24			2016-18-08	16:24:34	0.683727	Thu	4	10	2016-18-8 16:24:34	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 18 17:04 trade10.dat.20160818170436978	17:04			2016-18-08	17:04:36	0.711528	Thu	4	10	2016-18-8 17:04:36	14
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 18 18:04 trade10.dat.20160818180440611	18:04			2016-18-08	18:04:40	0.753241	Thu	4	10	2016-18-8 18:04:40	14
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    241909 Aug 18 09:00 passporttrans.20160818.csv.20160818090036741	9:00	8/18/2016		2016-18-08	9:00:36	0.375417	Thu	4	15	2016-18-8 9:00:36	14
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1837 Aug 18 08:30 HighlandCapitalManagementRecon201608180730.csv.20160818083035579	8:30	8/18/2016	7:30:00	2016-18-08	8:30:35	0.354572	Thu	4	16	2016-18-8 8:30:35	14
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       253 Aug 18 14:24 Highland_Orders_20160818csv.20160818142428094	14:24	8/18/2016		2016-18-08	14:24:28	0.600324	Thu	4	16	2016-18-8 14:24:28	14
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       209 Aug 18 02:48 HSBC-LKR.in.18082016-1.20160818024811956	2:48	8/18/2016		2016-18-08	2:48:11	0.116794	Thu	4	17	2016-18-8 2:48:11	14
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       938 Aug 18 23:47 HSBC-LKR.in.19082016-1.20160818234701454	23:47	8/18/2016		2016-18-08	23:47:01	0.990984	Thu	4	17	2016-18-8 23:47:01	14
John Hancock Investments	HAN_TRANS_HANVER_20160818.csv.20160818152631900	15:26	8/18/2016		2016-18-08	15:26:31	0.643414	Thu	4	18	2016-18-8 15:26:31	14
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 18 03:08 FT_fx_20160818_090652.csv.20160818030813109	3:08	8/18/2016	9:06:52	2016-18-08	3:08:13	0.130706	Thu	4	26	2016-18-8 3:08:13	14
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 18 04:40 INV_fx_20160818_103731.csv.20160818044019376	4:40	8/18/2016	10:37:31	2016-18-08	4:40:19	0.194664	Thu	4	26	2016-18-8 4:40:19	14
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 18 04:46 FT_fx_20160818_104431.csv.20160818044619835	4:46	8/18/2016	10:44:31	2016-18-08	4:46:19	0.198831	Thu	4	26	2016-18-8 4:46:19	14
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 18 04:20 citicnhtrades.in.201608181609.20160818042017602	4:20	8/18/2016	16:09:00	2016-18-08	4:20:17	0.180752	Thu	4	28	2016-18-8 4:20:17	14
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 18 05:24 citicnhtrades.in.201608181717.20160818052422167	5:24	8/18/2016	17:17:00	2016-18-08	5:24:22	0.225255	Thu	4	28	2016-18-8 5:24:22	14
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       519 Aug 18 05:26 hsbccnhtrades.in.201608181717.20160818052622564	5:26	8/18/2016	17:17:00	2016-18-08	5:26:22	0.226644	Thu	4	29	2016-18-8 5:26:22	14
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     21740 Aug 18 10:08 RSWGD1-17_SSGM_Confirmed_File__20160818.csv.20160818100842809	10:08	8/18/2016		2016-18-08	10:08:42	0.422708	Thu	4	30	2016-18-8 10:08:42	14
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6920 Aug 18 09:30 TIAACREFREPAT.csv.20160818093040151	9:30			2016-18-08	9:30:40	0.396296	Thu	4	32	2016-18-8 9:30:40	14
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 18 21:30 tokyofundtrades.in.201608190922.20160818213053090	21:30	8/19/2016	9:22:00	2016-18-08	21:30:53	0.896447	Thu	4	33	2016-18-8 21:30:53	14
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2169 Aug 19 05:00 SSC_BAM_FXREQ_20160819_093001.csv.pgp.20160819050045852	5:00	8/19/2016	9:30:01	2016-19-08	5:00:45	0.208854	Fri	5	3	2016-19-8 5:00:45	15
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2169 Aug 19 05:14 SSC_BAM_FXREQ_20160819_093001.csv.pgp.ndm05.20160819051417508	5:14	8/19/2016	9:30:01	2016-19-08	5:14:17	0.218252	Fri	5	3	2016-19-8 5:14:17	15
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1545 Aug 19 05:33 SSC_BAM_FXREQ_20160819_103007.csv.pgp.ndm05.20160819053318852	5:33	8/19/2016	10:30:07	2016-19-08	5:33:18	0.231458	Fri	5	3	2016-19-8 5:33:18	15
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1457 Aug 19 10:32 SSC_BAM_FXREQ_20160819_153018.csv.pgp.ndm05.20160819103239233	10:32	8/19/2016	15:30:18	2016-19-08	10:32:39	0.43934	Fri	5	3	2016-19-8 10:32:39	15
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Aug 19 11:34 SSC_BAM_FXREQ_20160819_163021.csv.pgp.ndm05.20160819113412808	11:34	8/19/2016	16:30:21	2016-19-08	11:34:12	0.482083	Fri	5	3	2016-19-8 11:34:12	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063822322	6:38			2016-19-08	6:38:22	0.276644	Fri	5	4	2016-19-8 6:38:22	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063822573	6:38			2016-19-08	6:38:22	0.276644	Fri	5	4	2016-19-8 6:38:22	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063822765	6:38			2016-19-08	6:38:22	0.276644	Fri	5	4	2016-19-8 6:38:22	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063822987	6:38			2016-19-08	6:38:22	0.276644	Fri	5	4	2016-19-8 6:38:22	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063823170	6:38			2016-19-08	6:38:23	0.276655	Fri	5	4	2016-19-8 6:38:23	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063823368	6:38			2016-19-08	6:38:23	0.276655	Fri	5	4	2016-19-8 6:38:23	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063823576	6:38			2016-19-08	6:38:23	0.276655	Fri	5	4	2016-19-8 6:38:23	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063823772	6:38			2016-19-08	6:38:23	0.276655	Fri	5	4	2016-19-8 6:38:23	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063823974	6:38			2016-19-08	6:38:23	0.276655	Fri	5	4	2016-19-8 6:38:23	15
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 19 06:38 BCRTOFX.txt.20160819063824161	6:38			2016-19-08	6:38:24	0.276667	Fri	5	4	2016-19-8 6:38:24	15
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2692 Aug 19 14:37 BRA_BRA_Ver_20160819.csv.20160819143723990	14:37	8/19/2016		2016-19-08	14:37:23	0.609294	Fri	5	5	2016-19-8 14:37:23	15
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Aug 19 06:12 scbcnhtrades1.in.201608191806.20160819061250978	6:12	8/19/2016	18:06:00	2016-19-08	6:12:50	0.258912	Fri	5	7	2016-19-8 6:12:50	15
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 19 06:12 scbcnhtrades2.in.201608191806.20160819061251351	6:12	8/19/2016	18:06:00	2016-19-08	6:12:51	0.258924	Fri	5	7	2016-19-8 6:12:51	15
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       866 Aug 19 09:27 SPOT_FET_Instructions_StateStreet_20160819-151816.csv.20160819092704424	9:27	8/19/2016	15:18:16	2016-19-08	9:27:04	0.393796	Fri	5	7	2016-19-8 9:27:04	15
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 19 16:39 08192016_GAM_GAM_STAR_GS.20160819.csv.20160819163901092	16:39	8/19/2016		2016-19-08	16:39:01	0.693762	Fri	5	9	2016-19-8 16:39:01	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 19 10:35 trade10.dat.20160819103509566	10:35			2016-19-08	10:35:09	0.441076	Fri	5	10	2016-19-8 10:35:09	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     12148 Aug 19 12:35 trade10.dat.20160819123517458	12:35			2016-19-08	12:35:17	0.524502	Fri	5	10	2016-19-8 12:35:17	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6940 Aug 19 14:33 trade10.dat.20160819143323415	14:33			2016-19-08	14:33:23	0.606516	Fri	5	10	2016-19-8 14:33:23	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     22998 Aug 19 16:23 trade10.dat.20160819162329527	16:23			2016-19-08	16:23:29	0.682975	Fri	5	10	2016-19-8 16:23:29	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 19 17:05 trade10.dat.20160819170503044	17:05			2016-19-08	17:05:03	0.71184	Fri	5	10	2016-19-8 17:05:03	15
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 19 18:03 trade10.dat.20160819180306587	18:03			2016-19-08	18:03:06	0.752153	Fri	5	10	2016-19-8 18:03:06	15
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       331 Aug 19 10:11 UKFCMCurrencyTemplate190816.csv.20160819101108014	10:11			2016-19-08	10:11:08	0.424398	Fri	5	11	2016-19-8 10:11:08	15
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    230938 Aug 19 08:59 passporttrans.20160819.csv.20160819085901370	8:59	8/19/2016		2016-19-08	8:59:01	0.374317	Fri	5	15	2016-19-8 8:59:01	15
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1845 Aug 19 08:31 HighlandCapitalManagementRecon201608190730.csv.20160819083100270	8:31	8/19/2016	7:30:00	2016-19-08	8:31:00	0.354861	Fri	5	16	2016-19-8 8:31:00	15
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       253 Aug 19 11:59 Highland_Orders_20160819csv.20160819115913792	11:59	8/19/2016		2016-19-08	11:59:13	0.499456	Fri	5	16	2016-19-8 11:59:13	15
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       484 Aug 19 03:29 HSBC-LKR.in.19082016-2.20160819032910652	3:29	8/19/2016		2016-19-08	3:29:10	0.145255	Fri	5	17	2016-19-8 3:29:10	15
John Hancock Investments	HAN_TRANS_HANVER_20160819.csv.20160819152526500	15:25	8/19/2016		2016-19-08	15:25:26	0.642662	Fri	5	18	2016-19-8 15:25:26	15
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       203 Aug 19 12:27 PGI_Orders_20160819112457.csv.20160819122716437	12:27	8/19/2016	11:24:57	2016-19-08	12:27:16	0.518935	Fri	5	24	2016-19-8 12:27:16	15
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       989 Aug 19 15:03 PGI_Orders_20160819140139.csv.20160819150325054	15:03	8/19/2016	14:01:39	2016-19-08	15:03:25	0.627373	Fri	5	24	2016-19-8 15:03:25	15
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       296 Aug 19 03:05 FT_fx_20160819_090314.csv.20160819030509088	3:05	8/19/2016	9:03:14	2016-19-08	3:05:09	0.128576	Fri	5	26	2016-19-8 3:05:09	15
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 19 03:43 INV_fx_20160819_094147.csv.20160819034311603	3:43	8/19/2016	9:41:47	2016-19-08	3:43:11	0.154988	Fri	5	26	2016-19-8 3:43:11	15
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       296 Aug 19 04:34 FT_fx_20160819_103305.csv.20160819043444855	4:34	8/19/2016	10:33:05	2016-19-08	4:34:44	0.190787	Fri	5	26	2016-19-8 4:34:44	15
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 19 05:28 citicnhtrades.in.201608191718.20160819052848208	5:28	8/19/2016	17:18:00	2016-19-08	5:28:48	0.228333	Fri	5	28	2016-19-8 5:28:48	15
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        63 Aug 19 05:28 hsbccnhtrades.in.201608191718.20160819052848530	5:28	8/19/2016	17:18:00	2016-19-08	5:28:48	0.228333	Fri	5	29	2016-19-8 5:28:48	15
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22155 Aug 19 09:57 RSWGD1-17_SSGM_Confirmed_File__20160819.csv.20160819095706253	9:57	8/19/2016		2016-19-08	9:57:06	0.414653	Fri	5	30	2016-19-8 9:57:06	15
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5654 Aug 19 09:31 TIAACREFREPAT.csv.20160819093104821	9:31			2016-19-08	9:31:04	0.396574	Fri	5	32	2016-19-8 9:31:04	15
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       530 Aug 21 22:02 tokyofundtrades.in.201608220950.20160821220256160	22:02	8/22/2016	9:50:00	2016-21-08	22:02:56	0.918704	Sun	7	33	2016-21-8 22:02:56	#N/A
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1440 Aug 22 05:14 SSC_BAM_FXREQ_20160822_093022.csv.pgp.ndm05.20160822051448741	5:14	8/22/2016	9:30:22	2016-22-08	5:14:48	0.218611	Mon	1	3	2016-22-8 5:14:48	16
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1450 Aug 22 05:32 SSC_BAM_FXREQ_20160822_103025.csv.pgp.ndm05.20160822053249519	5:32	8/22/2016	10:30:25	2016-22-08	5:32:49	0.231123	Mon	1	3	2016-22-8 5:32:49	16
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1409 Aug 22 10:31 SSC_BAM_FXREQ_20160822_153038.csv.pgp.ndm05.20160822103138264	10:31	8/22/2016	15:30:38	2016-22-08	10:31:38	0.438634	Mon	1	3	2016-22-8 10:31:38	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063723245	6:37			2016-22-08	6:37:23	0.275961	Mon	1	4	2016-22-8 6:37:23	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063723559	6:37			2016-22-08	6:37:23	0.275961	Mon	1	4	2016-22-8 6:37:23	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063723771	6:37			2016-22-08	6:37:23	0.275961	Mon	1	4	2016-22-8 6:37:23	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063723948	6:37			2016-22-08	6:37:23	0.275961	Mon	1	4	2016-22-8 6:37:23	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063724154	6:37			2016-22-08	6:37:24	0.275972	Mon	1	4	2016-22-8 6:37:24	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063724354	6:37			2016-22-08	6:37:24	0.275972	Mon	1	4	2016-22-8 6:37:24	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063724563	6:37			2016-22-08	6:37:24	0.275972	Mon	1	4	2016-22-8 6:37:24	16
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 22 06:37 BCRTOFX.txt.20160822063724779	6:37			2016-22-08	6:37:24	0.275972	Mon	1	4	2016-22-8 6:37:24	16
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4023 Aug 22 14:45 BRA_BRA_Ver_20160822.csv.20160822144526252	14:45	8/22/2016		2016-22-08	14:45:26	0.614884	Mon	1	5	2016-22-8 14:45:26	16
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 22 21:33 CDPSfxv_TWDorder.20160822.213000.csv.20160822213349018	21:33	8/22/2016	21:30:00	2016-22-08	21:33:49	0.898484	Mon	1	6	2016-22-8 21:33:49	16
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       732 Aug 22 09:33 SPOT_FET_Instructions_StateStreet_20160822-152049.csv.20160822093304916	9:33	8/22/2016	15:20:49	2016-22-08	9:33:04	0.397963	Mon	1	7	2016-22-8 9:33:04	16
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       178 Aug 22 06:43 CRUX_20160822.csv.20160822064325160	6:43	8/22/2016		2016-22-08	6:43:25	0.28015	Mon	1	8	2016-22-8 6:43:25	16
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 22 17:15 08222016_GAM_GAM_STAR_GS.20160822.csv.20160822171535911	17:15	8/22/2016		2016-22-08	17:15:35	0.719155	Mon	1	9	2016-22-8 17:15:35	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 22 10:33 trade10.dat.20160822103308785	10:33			2016-22-08	10:33:08	0.439676	Mon	1	10	2016-22-8 10:33:08	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Aug 22 12:33 trade10.dat.20160822123317059	12:33			2016-22-08	12:33:17	0.523113	Mon	1	10	2016-22-8 12:33:17	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Aug 22 14:33 trade10.dat.20160822143325435	14:33			2016-22-08	14:33:25	0.606539	Mon	1	10	2016-22-8 14:33:25	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     16488 Aug 22 16:23 trade10.dat.20160822162331277	16:23			2016-22-08	16:23:31	0.682998	Mon	1	10	2016-22-8 16:23:31	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 22 17:03 trade10.dat.20160822170334238	17:03			2016-22-08	17:03:34	0.71081	Mon	1	10	2016-22-8 17:03:34	16
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 22 18:03 trade10.dat.20160822180338871	18:03			2016-22-08	18:03:38	0.752523	Mon	1	10	2016-22-8 18:03:38	16
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    225993 Aug 22 08:59 passporttrans.20160822.csv.20160822085901662	8:59	8/22/2016		2016-22-08	8:59:01	0.374317	Mon	1	15	2016-22-8 8:59:01	16
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1666 Aug 22 08:31 HighlandCapitalManagementRecon201608220730.csv.20160822083100515	8:31	8/22/2016	7:30:00	2016-22-08	8:31:00	0.354861	Mon	1	16	2016-22-8 8:31:00	16
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       563 Aug 22 02:53 HSBC-LKR.in.22082016-1.20160822025309204	2:53	8/22/2016		2016-22-08	2:53:09	0.120243	Mon	1	17	2016-22-8 2:53:09	16
John Hancock Investments	HAN_TRANS_HANVER_20160822.csv.20160822153728537	15:37	8/22/2016		2016-22-08	15:37:28	0.651019	Mon	1	18	2016-22-8 15:37:28	16
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Aug 22 03:23 FT_fx_20160822_091822.csv.20160822032311166	3:23	8/22/2016	9:18:22	2016-22-08	3:23:11	0.1411	Mon	1	26	2016-22-8 3:23:11	16
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Aug 22 03:39 INV_fx_20160822_093642.csv.20160822033912342	3:39	8/22/2016	9:36:42	2016-22-08	3:39:12	0.152222	Mon	1	26	2016-22-8 3:39:12	16
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 22 04:29 INV_fx_20160822_102607.csv.20160822042915501	4:29	8/22/2016	10:26:07	2016-22-08	4:29:15	0.186979	Mon	1	26	2016-22-8 4:29:15	16
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Aug 22 04:59 FT_fx_20160822_105623.csv.20160822045916856	4:59	8/22/2016	10:56:23	2016-22-08	4:59:16	0.207824	Mon	1	26	2016-22-8 4:59:16	16
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 22 05:51 FT_fx_20160822_114224.csv.20160822055120825	5:51	8/22/2016	11:42:24	2016-22-08	5:51:20	0.243981	Mon	1	26	2016-22-8 5:51:20	16
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 22 05:35 citicnhtrades.in.201608221720.20160822053519865	5:35	8/22/2016	17:20:00	2016-22-08	5:35:19	0.232859	Mon	1	28	2016-22-8 5:35:19	16
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       652 Aug 22 05:35 hsbccnhtrades.in.201608221720.20160822053520171	5:35	8/22/2016	17:20:00	2016-22-08	5:35:20	0.23287	Mon	1	29	2016-22-8 5:35:20	16
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22832 Aug 22 10:53 RSWGD1-17_SSGM_Confirmed_File__20160822.csv.20160822105309970	10:53	8/22/2016		2016-22-08	10:53:09	0.453576	Mon	1	30	2016-22-8 10:53:09	16
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4195 Aug 22 09:39 tcwta20160822.csv.20160822093905290	9:39	8/22/2016		2016-22-08	9:39:05	0.402141	Mon	1	31	2016-22-8 9:39:05	16
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4191 Aug 22 09:31 TIAACREFREPAT.csv.20160822093104034	9:31			2016-22-08	9:31:04	0.396574	Mon	1	32	2016-22-8 9:31:04	16
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1248 Aug 22 13:31 TIAACREFREPAT.csv.20160822133121422	13:31			2016-22-08	13:31:21	0.563438	Mon	1	32	2016-22-8 13:31:21	16
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       574 Aug 22 21:35 tokyofundtrades.in.201608230924.20160822213549610	21:35	8/23/2016	9:24:00	2016-22-08	21:35:49	0.899873	Mon	1	33	2016-22-8 21:35:49	16
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       464 Aug 22 21:45 tokyofundtrades.in.201608230916.20160822214550228	21:45	8/23/2016	9:16:00	2016-22-08	21:45:50	0.906829	Mon	1	33	2016-22-8 21:45:50	16
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 22 04:37 TrinityStreetFX_082216.csv.20160822043716050	4:37			2016-22-08	4:37:16	0.192546	Mon	1	34	2016-22-8 4:37:16	16
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Aug 23 08:21 Alger_Orders_20160823081957.csv.20160823082154770	8:21	8/23/2016	8:19:57	2016-23-08	8:21:54	0.348542	Tue	2	1	2016-23-8 8:21:54	17
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1457 Aug 23 04:32 SSC_BAM_FXREQ_20160823_093020.csv.pgp.ndm05.20160823043208943	4:32	8/23/2016	9:30:20	2016-23-08	4:32:08	0.188981	Tue	2	3	2016-23-8 4:32:08	17
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1442 Aug 23 06:32 SSC_BAM_FXREQ_20160823_113025.csv.pgp.ndm05.20160823063216999	6:32	8/23/2016	11:30:25	2016-23-08	6:32:16	0.272407	Tue	2	3	2016-23-8 6:32:16	17
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1416 Aug 23 07:32 SSC_BAM_FXREQ_20160823_123028.csv.pgp.ndm05.20160823073222087	7:32	8/23/2016	12:30:28	2016-23-08	7:32:22	0.314144	Tue	2	3	2016-23-8 7:32:22	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063847948	6:38			2016-23-08	6:38:47	0.276933	Tue	2	4	2016-23-8 6:38:47	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063848118	6:38			2016-23-08	6:38:48	0.276944	Tue	2	4	2016-23-8 6:38:48	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063848314	6:38			2016-23-08	6:38:48	0.276944	Tue	2	4	2016-23-8 6:38:48	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063848515	6:38			2016-23-08	6:38:48	0.276944	Tue	2	4	2016-23-8 6:38:48	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063848749	6:38			2016-23-08	6:38:48	0.276944	Tue	2	4	2016-23-8 6:38:48	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063848913	6:38			2016-23-08	6:38:48	0.276944	Tue	2	4	2016-23-8 6:38:48	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063849126	6:38			2016-23-08	6:38:49	0.276956	Tue	2	4	2016-23-8 6:38:49	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063849331	6:38			2016-23-08	6:38:49	0.276956	Tue	2	4	2016-23-8 6:38:49	17
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 23 06:38 BCRTOFX.txt.20160823063849512	6:38			2016-23-08	6:38:49	0.276956	Tue	2	4	2016-23-8 6:38:49	17
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3176 Aug 23 14:43 BRA_BRA_Ver_20160823.csv.20160823144351637	14:43	8/23/2016		2016-23-08	14:43:51	0.613785	Tue	2	5	2016-23-8 14:43:51	17
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       295 Aug 23 09:11 SPOT_FET_Instructions_StateStreet_20160823-150427.csv.20160823091159419	9:11	8/23/2016	15:04:27	2016-23-08	9:11:59	0.383322	Tue	2	7	2016-23-8 9:11:59	17
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       459 Aug 23 11:48 CRUX_20160823.csv.20160823114810361	11:48	8/23/2016		2016-23-08	11:48:10	0.491782	Tue	2	8	2016-23-8 11:48:10	17
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 23 16:49 08232016_GAM_GAM_STAR_GS.20160823.csv.20160823164958841	16:49	8/23/2016		2016-23-08	16:49:58	0.701366	Tue	2	9	2016-23-8 16:49:58	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 23 10:34 trade10.dat.20160823103405714	10:34			2016-23-08	10:34:05	0.440336	Tue	2	10	2016-23-8 10:34:05	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5638 Aug 23 12:33 trade10.dat.20160823123344132	12:33			2016-23-08	12:33:44	0.523426	Tue	2	10	2016-23-8 12:33:44	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Aug 23 14:33 trade10.dat.20160823143351009	14:33			2016-23-08	14:33:51	0.60684	Tue	2	10	2016-23-8 14:33:51	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      7374 Aug 23 16:23 trade10.dat.20160823162356872	16:23			2016-23-08	16:23:56	0.683287	Tue	2	10	2016-23-8 16:23:56	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 23 17:03 trade10.dat.20160823170359977	17:03			2016-23-08	17:03:59	0.7111	Tue	2	10	2016-23-8 17:03:59	17
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 23 18:04 trade10.dat.20160823180403655	18:04			2016-23-08	18:04:03	0.752813	Tue	2	10	2016-23-8 18:04:03	17
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       178 Aug 23 05:27 UKFCMCurrencyTemplate230816.csv.20160823052742422	5:27			2016-23-08	5:27:42	0.227569	Tue	2	11	2016-23-8 5:27:42	17
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    218548 Aug 23 08:59 passporttrans.20160823.csv.20160823085958262	8:59	8/23/2016		2016-23-08	8:59:58	0.374977	Tue	2	15	2016-23-8 8:59:58	17
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 23 08:31 HighlandCapitalManagementRecon201608230730.csv.20160823083156101	8:31	8/23/2016	7:30:00	2016-23-08	8:31:56	0.355509	Tue	2	16	2016-23-8 8:31:56	17
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       669 Aug 23 03:57 HSBC-LKR.in.23082016-1.20160823035736732	3:57	8/23/2016		2016-23-08	3:57:36	0.165	Tue	2	17	2016-23-8 3:57:36	17
John Hancock Investments	HAN_TRANS_HANVER_20160823.csv.20160823153754050	15:37	8/23/2016		2016-23-08	15:37:54	0.651319	Tue	2	18	2016-23-8 15:37:54	17
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug 23 03:27 FT_fx_20160823_092419.csv.20160823032735145	3:27	8/23/2016	9:24:19	2016-23-08	3:27:35	0.144155	Tue	2	26	2016-23-8 3:27:35	17
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 23 03:33 INV_fx_20160823_093140.csv.20160823033335795	3:33	8/23/2016	9:31:40	2016-23-08	3:33:35	0.148322	Tue	2	26	2016-23-8 3:33:35	17
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Aug 23 05:03 FT_fx_20160823_105919.csv.20160823050340798	5:03	8/23/2016	10:59:19	2016-23-08	5:03:40	0.21088	Tue	2	26	2016-23-8 5:03:40	17
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 23 05:23 citicnhtrades.in.201608231713.20160823052341694	5:23	8/23/2016	17:13:00	2016-23-08	5:23:41	0.22478	Tue	2	28	2016-23-8 5:23:41	17
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       348 Aug 23 05:23 hsbccnhtrades.in.201608231713.20160823052342068	5:23	8/23/2016	17:13:00	2016-23-08	5:23:42	0.224792	Tue	2	29	2016-23-8 5:23:42	17
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     21320 Aug 23 11:00 RSWGD1-17_SSGM_Confirmed_File__20160823.csv.20160823110007425	11:00	8/23/2016		2016-23-08	11:00:07	0.458414	Tue	2	30	2016-23-8 11:00:07	17
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3568 Aug 23 09:50 tcwta20160823.csv.20160823095002601	9:50	8/23/2016		2016-23-08	9:50:02	0.409745	Tue	2	31	2016-23-8 9:50:02	17
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2108 Aug 23 09:32 TIAACREFREPAT.csv.20160823093200987	9:32			2016-23-08	9:32:00	0.397222	Tue	2	32	2016-23-8 9:32:00	17
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       330 Aug 23 12:07 TIAACREFREPAT.csv.20160823120742714	12:07			2016-23-08	12:07:42	0.505347	Tue	2	32	2016-23-8 12:07:42	17
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       174 Aug 23 21:26 tokyofundtrades.in.201608240917.20160823212614897	21:26	8/24/2016	9:17:00	2016-23-08	21:26:14	0.893218	Tue	2	33	2016-23-8 21:26:14	17
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       284 Aug 23 23:34 tokyofundtrades.in.201608241017.20160823233423264	23:34	8/24/2016	10:17:00	2016-23-08	23:34:23	0.982211	Tue	2	33	2016-23-8 23:34:23	17
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Aug 24 10:56 Alger_Orders_20160824105342.csv.20160824105630285	10:56	8/24/2016	10:53:42	2016-24-08	10:56:30	0.455903	Wed	3	1	2016-24-8 10:56:30	18
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       130 Aug 24 14:38 Alger_Orders_20160824143725.csv.20160824143843831	14:38	8/24/2016	14:37:25	2016-24-08	14:38:43	0.61022	Wed	3	1	2016-24-8 14:38:43	18
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1434 Aug 24 04:33 SSC_BAM_FXREQ_20160824_093017.csv.pgp.ndm05.20160824043334656	4:33	8/24/2016	9:30:17	2016-24-08	4:33:34	0.189977	Wed	3	3	2016-24-8 4:33:34	18
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1401 Aug 24 05:31 SSC_BAM_FXREQ_20160824_103020.csv.pgp.ndm05.20160824053138942	5:31	8/24/2016	10:30:20	2016-24-08	5:31:38	0.230301	Wed	3	3	2016-24-8 5:31:38	18
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Aug 24 10:31 SSC_BAM_FXREQ_20160824_153034.csv.pgp.ndm05.20160824103158623	10:31	8/24/2016	15:30:34	2016-24-08	10:31:58	0.438866	Wed	3	3	2016-24-8 10:31:58	18
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1431 Aug 24 11:32 SSC_BAM_FXREQ_20160824_163036.csv.pgp.ndm05.20160824113203091	11:32	8/24/2016	16:30:36	2016-24-08	11:32:03	0.48059	Wed	3	3	2016-24-8 11:32:03	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063812506	6:38			2016-24-08	6:38:12	0.276528	Wed	3	4	2016-24-8 6:38:12	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063812865	6:38			2016-24-08	6:38:12	0.276528	Wed	3	4	2016-24-8 6:38:12	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063813056	6:38			2016-24-08	6:38:13	0.276539	Wed	3	4	2016-24-8 6:38:13	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063813254	6:38			2016-24-08	6:38:13	0.276539	Wed	3	4	2016-24-8 6:38:13	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063813463	6:38			2016-24-08	6:38:13	0.276539	Wed	3	4	2016-24-8 6:38:13	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063813672	6:38			2016-24-08	6:38:13	0.276539	Wed	3	4	2016-24-8 6:38:13	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063813857	6:38			2016-24-08	6:38:13	0.276539	Wed	3	4	2016-24-8 6:38:13	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063814115	6:38			2016-24-08	6:38:14	0.276551	Wed	3	4	2016-24-8 6:38:14	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063814267	6:38			2016-24-08	6:38:14	0.276551	Wed	3	4	2016-24-8 6:38:14	18
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 24 06:38 BCRTOFX.txt.20160824063814507	6:38			2016-24-08	6:38:14	0.276551	Wed	3	4	2016-24-8 6:38:14	18
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      1968 Aug 24 14:42 BRA_BRA_Ver_20160824.csv.20160824144244141	14:42	8/24/2016		2016-24-08	14:42:44	0.613009	Wed	3	5	2016-24-8 14:42:44	18
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       331 Aug 24 10:02 CDPSfx_BRLorder.20160824.100026.csv.20160824100225827	10:02	8/24/2016	10:00:26	2016-24-08	10:02:25	0.418345	Wed	3	6	2016-24-8 10:02:25	18
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       720 Aug 24 09:26 SPOT_FET_Instructions_StateStreet_20160824-151508.csv.20160824092623078	9:26	8/24/2016	15:15:08	2016-24-08	9:26:23	0.393322	Wed	3	7	2016-24-8 9:26:23	18
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 24 17:20 08242016_GAM_GAM_STAR_GS.20160824.csv.20160824172022512	17:20	8/24/2016		2016-24-08	17:20:22	0.722477	Wed	3	9	2016-24-8 17:20:22	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 24 10:34 trade10.dat.20160824103429084	10:34			2016-24-08	10:34:29	0.440613	Wed	3	10	2016-24-8 10:34:29	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Aug 24 12:34 trade10.dat.20160824123436903	12:34			2016-24-08	12:34:36	0.524028	Wed	3	10	2016-24-8 12:34:36	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 24 14:34 trade10.dat.20160824143442900	14:34			2016-24-08	14:34:42	0.607431	Wed	3	10	2016-24-8 14:34:42	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     88098 Aug 24 16:24 trade10.dat.20160824162448455	16:24			2016-24-08	16:24:48	0.683889	Wed	3	10	2016-24-8 16:24:48	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 24 17:04 trade10.dat.20160824170421229	17:04			2016-24-08	17:04:21	0.711354	Wed	3	10	2016-24-8 17:04:21	18
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 24 18:04 trade10.dat.20160824180426099	18:04			2016-24-08	18:04:26	0.753079	Wed	3	10	2016-24-8 18:04:26	18
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       178 Aug 24 06:30 UKFCMCurrencyTemplate240816.csv.20160824063011904	6:30			2016-24-08	6:30:11	0.270961	Wed	3	11	2016-24-8 6:30:11	18
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr      1572 Aug 24 08:58 UKFCMCurrencyTemplate240816a.csv.20160824085820316	8:58			2016-24-08	8:58:20	0.373843	Wed	3	11	2016-24-8 8:58:20	18
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    229487 Aug 24 09:04 passporttrans.20160824.csv.20160824090420695	9:04	8/24/2016		2016-24-08	9:04:20	0.378009	Wed	3	15	2016-24-8 9:04:20	18
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 24 08:32 HighlandCapitalManagementRecon201608240730.csv.20160824083219382	8:32	8/24/2016	7:30:00	2016-24-08	8:32:19	0.355775	Wed	3	16	2016-24-8 8:32:19	18
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       391 Aug 24 02:46 HSBC-LKR.in.24082016-1.20160824024629584	2:46	8/24/2016		2016-24-08	2:46:29	0.115613	Wed	3	17	2016-24-8 2:46:29	18
John Hancock Investments	HAN_TRANS_HANVER_20160824.csv.20160824153846223	15:38	8/24/2016		2016-24-08	15:38:46	0.651921	Wed	3	18	2016-24-8 15:38:46	18
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 24 03:24 FT_fx_20160824_091954.csv.20160824032431361	3:24	8/24/2016	9:19:54	2016-24-08	3:24:31	0.142025	Wed	3	26	2016-24-8 3:24:31	18
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 24 03:30 INV_fx_20160824_092854.csv.20160824033031819	3:30	8/24/2016	9:28:54	2016-24-08	3:30:31	0.146192	Wed	3	26	2016-24-8 3:30:31	18
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 24 05:02 FT_fx_20160824_105706.csv.20160824050206246	5:02	8/24/2016	10:57:06	2016-24-08	5:02:06	0.209792	Wed	3	26	2016-24-8 5:02:06	18
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 24 05:52 FT_fx_20160824_114647.csv.20160824055210302	5:52	8/24/2016	11:46:47	2016-24-08	5:52:10	0.24456	Wed	3	26	2016-24-8 5:52:10	18
SchaFer Cullen	-rw-r--r--   1 ftpgmrin ftpgmr       388 Aug 24 09:44 SchaferCullenOrders.csv.20160824094425116	9:44			2016-24-08	9:44:25	0.405845	Wed	3	27	2016-24-8 9:44:25	18
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 24 05:22 citicnhtrades.in.201608241713.20160824052208084	5:22	8/24/2016	17:13:00	2016-24-08	5:22:08	0.223704	Wed	3	28	2016-24-8 5:22:08	18
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        59 Aug 24 05:22 hsbccnhtrades.in.201608241713.20160824052208476	5:22	8/24/2016	17:13:00	2016-24-08	5:22:08	0.223704	Wed	3	29	2016-24-8 5:22:08	18
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22361 Aug 24 11:46 RSWGD1-17_SSGM_Confirmed_File__20160824.csv.20160824114633803	11:46	8/24/2016		2016-24-08	11:46:33	0.49066	Wed	3	30	2016-24-8 11:46:33	18
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3631 Aug 24 09:42 tcwta20160824.csv.20160824.094106.20160824094224640	9:42	8/24/2016		2016-24-08	9:42:24	0.404444	Wed	3	31	2016-24-8 9:42:24	18
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4070 Aug 24 09:32 TIAACREFREPAT.csv.20160824093223567	9:32			2016-24-08	9:32:23	0.397488	Wed	3	32	2016-24-8 9:32:23	18
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       258 Aug 25 08:47 Alger_Orders_20160825084428.csv.20160825084708397	8:47	8/25/2016	8:44:28	2016-25-08	8:47:08	0.366065	Thu	4	1	2016-25-8 8:47:08	19
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       194 Aug 25 10:18 Alger_Orders_20160825101659.csv.20160825101845334	10:18	8/25/2016	10:16:59	2016-25-08	10:18:45	0.429688	Thu	4	1	2016-25-8 10:18:45	19
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Aug 25 13:14 Alger_Orders_20160825131243.csv.20160825131455271	13:14	8/25/2016	13:12:43	2016-25-08	13:14:55	0.552025	Thu	4	1	2016-25-8 13:14:55	19
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1475 Aug 25 04:32 SSC_BAM_FXREQ_20160825_093016.csv.pgp.ndm05.20160825043222924	4:32	8/25/2016	9:30:16	2016-25-08	4:32:22	0.189144	Thu	4	3	2016-25-8 4:32:22	19
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1465 Aug 25 07:32 SSC_BAM_FXREQ_20160825_123024.csv.pgp.ndm05.20160825073234929	7:32	8/25/2016	12:30:24	2016-25-08	7:32:34	0.314282	Thu	4	3	2016-25-8 7:32:34	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063800543	6:38			2016-25-08	6:38:00	0.276389	Thu	4	4	2016-25-8 6:38:00	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063800966	6:38			2016-25-08	6:38:00	0.276389	Thu	4	4	2016-25-8 6:38:00	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063801355	6:38			2016-25-08	6:38:01	0.2764	Thu	4	4	2016-25-8 6:38:01	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063801559	6:38			2016-25-08	6:38:01	0.2764	Thu	4	4	2016-25-8 6:38:01	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063801741	6:38			2016-25-08	6:38:01	0.2764	Thu	4	4	2016-25-8 6:38:01	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063801959	6:38			2016-25-08	6:38:01	0.2764	Thu	4	4	2016-25-8 6:38:01	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063802148	6:38			2016-25-08	6:38:02	0.276412	Thu	4	4	2016-25-8 6:38:02	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063802328	6:38			2016-25-08	6:38:02	0.276412	Thu	4	4	2016-25-8 6:38:02	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063802540	6:38			2016-25-08	6:38:02	0.276412	Thu	4	4	2016-25-8 6:38:02	19
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 25 06:38 BCRTOFX.txt.20160825063802744	6:38			2016-25-08	6:38:02	0.276412	Thu	4	4	2016-25-8 6:38:02	19
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2789 Aug 25 14:43 BRA_BRA_Ver_20160825.csv.20160825144300044	14:43	8/25/2016		2016-25-08	14:43:00	0.613194	Thu	4	5	2016-25-8 14:43:00	19
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       331 Aug 25 09:46 CDPSfx_BRLorder.20160825.094608.csv.20160825094642851	9:46	8/25/2016	9:46:08	2016-25-08	9:46:42	0.407431	Thu	4	6	2016-25-8 9:46:42	19
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 25 17:01 08252016_GAM_GAM_STAR_GS.20160825.csv.20160825170107933	17:01	8/25/2016		2016-25-08	17:01:07	0.709109	Thu	4	9	2016-25-8 17:01:07	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 25 10:32 trade10.dat.20160825103246574	10:32			2016-25-08	10:32:46	0.439421	Thu	4	10	2016-25-8 10:32:46	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Aug 25 12:34 trade10.dat.20160825123452883	12:34			2016-25-08	12:34:52	0.524213	Thu	4	10	2016-25-8 12:34:52	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Aug 25 14:34 trade10.dat.20160825143459616	14:34			2016-25-08	14:34:59	0.607627	Thu	4	10	2016-25-8 14:34:59	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9978 Aug 25 16:25 trade10.dat.20160825162505462	16:25			2016-25-08	16:25:05	0.684086	Thu	4	10	2016-25-8 16:25:05	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 25 17:03 trade10.dat.20160825170308395	17:03			2016-25-08	17:03:08	0.710509	Thu	4	10	2016-25-8 17:03:08	19
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 25 18:03 trade10.dat.20160825180312210	18:03			2016-25-08	18:03:12	0.752222	Thu	4	10	2016-25-8 18:03:12	19
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    231155 Aug 25 09:05 passporttrans.20160825.csv.20160825090509672	9:05	8/25/2016		2016-25-08	9:05:09	0.378576	Thu	4	15	2016-25-8 9:05:09	19
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 25 08:33 HighlandCapitalManagementRecon201608250730.csv.20160825083307538	8:33	8/25/2016	7:30:00	2016-25-08	8:33:07	0.356331	Thu	4	16	2016-25-8 8:33:07	19
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       579 Aug 25 03:24 HSBC-LKR.in.25082016-1.20160825032449608	3:24	8/25/2016		2016-25-08	3:24:49	0.142234	Thu	4	17	2016-25-8 3:24:49	19
John Hancock Investments	HAN_TRANS_HANVER_20160825.csv.20160825153702739	15:37	8/25/2016		2016-25-08	15:37:02	0.650718	Thu	4	18	2016-25-8 15:37:02	19
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Aug 25 02:52 FT_fx_20160825_085103.csv.20160825025247695	2:52	8/25/2016	8:51:03	2016-25-08	2:52:47	0.119988	Thu	4	26	2016-25-8 2:52:47	19
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 25 03:18 INV_fx_20160825_091624.csv.20160825031848576	3:18	8/25/2016	9:16:24	2016-25-08	3:18:48	0.138056	Thu	4	26	2016-25-8 3:18:48	19
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug 25 04:28 FT_fx_20160825_102743.csv.20160825042852474	4:28	8/25/2016	10:27:43	2016-25-08	4:28:52	0.186713	Thu	4	26	2016-25-8 4:28:52	19
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 25 05:20 INV_fx_20160825_111603.csv.20160825052055687	5:20	8/25/2016	11:16:03	2016-25-08	5:20:55	0.222859	Thu	4	26	2016-25-8 5:20:55	19
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       119 Aug 25 04:16 citicnhtrades.in.201608251607.20160825041651504	4:16	8/25/2016	16:07:00	2016-25-08	4:16:51	0.178368	Thu	4	28	2016-25-8 4:16:51	19
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 25 05:34 citicnhtrades.in.201608251715.20160825053456447	5:34	8/25/2016	17:15:00	2016-25-08	5:34:56	0.232593	Thu	4	28	2016-25-8 5:34:56	19
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        64 Aug 25 05:34 hsbccnhtrades.in.201608251715.20160825053456837	5:34	8/25/2016	17:15:00	2016-25-08	5:34:56	0.232593	Thu	4	29	2016-25-8 5:34:56	19
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23213 Aug 25 10:18 RSWGD1-17_SSGM_Confirmed_File__20160825.csv.20160825101845060	10:18	8/25/2016		2016-25-08	10:18:45	0.429688	Thu	4	30	2016-25-8 10:18:45	19
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     13822 Aug 25 09:30 TIAACREFREPAT.csv.20160825093041541	9:30			2016-25-08	9:30:41	0.396308	Thu	4	32	2016-25-8 9:30:41	19
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       230 Aug 25 21:47 tokyofundtrades.in.201608260931.20160825214723268	21:47	8/26/2016	9:31:00	2016-25-08	21:47:23	0.907905	Thu	4	33	2016-25-8 21:47:23	19
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Aug 26 08:55 Alger_Orders_20160826085226.csv.20160826085527581	8:55	8/26/2016	8:52:26	2016-26-08	8:55:27	0.37184	Fri	5	1	2016-26-8 8:55:27	20
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Aug 26 11:31 Alger_Orders_20160826112841.csv.20160826113138816	11:31	8/26/2016	11:28:41	2016-26-08	11:31:38	0.480301	Fri	5	1	2016-26-8 11:31:38	20
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        66 Aug 26 15:21 Alger_Orders_20160826152035.csv.20160826152121981	15:21	8/26/2016	15:20:35	2016-26-08	15:21:21	0.639826	Fri	5	1	2016-26-8 15:21:21	20
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Aug 26 04:31 SSC_BAM_FXREQ_20160826_093009.csv.pgp.ndm05.20160826043111752	4:31	8/26/2016	9:30:09	2016-26-08	4:31:11	0.188322	Fri	5	3	2016-26-8 4:31:11	20
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Aug 26 05:31 SSC_BAM_FXREQ_20160826_103011.csv.pgp.ndm05.20160826053115657	5:31	8/26/2016	10:30:11	2016-26-08	5:31:15	0.230035	Fri	5	3	2016-26-8 5:31:15	20
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Aug 26 12:32 SSC_BAM_FXREQ_20160826_173029.csv.pgp.ndm05.20160826123212501	12:32	8/26/2016	17:30:29	2016-26-08	12:32:12	0.522361	Fri	5	3	2016-26-8 12:32:12	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064120359	6:41			2016-26-08	6:41:20	0.278704	Fri	5	4	2016-26-8 6:41:20	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064120614	6:41			2016-26-08	6:41:20	0.278704	Fri	5	4	2016-26-8 6:41:20	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064120803	6:41			2016-26-08	6:41:20	0.278704	Fri	5	4	2016-26-8 6:41:20	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064121003	6:41			2016-26-08	6:41:21	0.278715	Fri	5	4	2016-26-8 6:41:21	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064121224	6:41			2016-26-08	6:41:21	0.278715	Fri	5	4	2016-26-8 6:41:21	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064121477	6:41			2016-26-08	6:41:21	0.278715	Fri	5	4	2016-26-8 6:41:21	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064121596	6:41			2016-26-08	6:41:21	0.278715	Fri	5	4	2016-26-8 6:41:21	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064121796	6:41			2016-26-08	6:41:21	0.278715	Fri	5	4	2016-26-8 6:41:21	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064122030	6:41			2016-26-08	6:41:22	0.278727	Fri	5	4	2016-26-8 6:41:22	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064122231	6:41			2016-26-08	6:41:22	0.278727	Fri	5	4	2016-26-8 6:41:22	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064122406	6:41			2016-26-08	6:41:22	0.278727	Fri	5	4	2016-26-8 6:41:22	20
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 26 06:41 BCRTOFX.txt.20160826064122633	6:41			2016-26-08	6:41:22	0.278727	Fri	5	4	2016-26-8 6:41:22	20
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2332 Aug 26 14:43 BRA_BRA_Ver_20160826.csv.20160826144320361	14:43	8/26/2016		2016-26-08	14:43:20	0.613426	Fri	5	5	2016-26-8 14:43:20	20
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1006 Aug 26 01:13 SPOT_FET_Instructions_StateStreet_20160825-144533.csv.20160826011302587	1:13	8/25/2016	14:45:33	2016-26-08	1:13:02	0.050718	Fri	5	7	2016-26-8 1:13:02	20
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1012 Aug 26 09:31 SPOT_FET_Instructions_StateStreet_20160826-152245.csv.20160826093130789	9:31	8/26/2016	15:22:45	2016-26-08	9:31:30	0.396875	Fri	5	7	2016-26-8 9:31:30	20
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 26 16:29 08262016_GAM_GAM_STAR_GS.20160826.csv.20160826162925770	16:29	8/26/2016		2016-26-08	16:29:25	0.687095	Fri	5	9	2016-26-8 16:29:25	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 26 10:33 trade10.dat.20160826103335294	10:33			2016-26-08	10:33:35	0.439988	Fri	5	10	2016-26-8 10:33:35	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 26 12:33 trade10.dat.20160826123342879	12:33			2016-26-08	12:33:42	0.523403	Fri	5	10	2016-26-8 12:33:42	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Aug 26 14:33 trade10.dat.20160826143319677	14:33			2016-26-08	14:33:19	0.60647	Fri	5	10	2016-26-8 14:33:19	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     24734 Aug 26 16:23 trade10.dat.20160826162325061	16:23			2016-26-08	16:23:25	0.682928	Fri	5	10	2016-26-8 16:23:25	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 26 17:03 trade10.dat.20160826170328698	17:03			2016-26-08	17:03:28	0.710741	Fri	5	10	2016-26-8 17:03:28	20
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 26 18:03 trade10.dat.20160826180332144	18:03			2016-26-08	18:03:32	0.752454	Fri	5	10	2016-26-8 18:03:32	20
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       251 Aug 26 06:17 UKFCMCurrencyTemplate260816.csv.20160826061719465	6:17			2016-26-08	6:17:19	0.262025	Fri	5	11	2016-26-8 6:17:19	20
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    249605 Aug 26 08:59 passporttrans.20160826.csv.20160826085928073	8:59	8/26/2016		2016-26-08	8:59:28	0.37463	Fri	5	15	2016-26-8 8:59:28	20
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 26 08:31 HighlandCapitalManagementRecon201608260730.csv.20160826083126485	8:31	8/26/2016	7:30:00	2016-26-08	8:31:26	0.355162	Fri	5	16	2016-26-8 8:31:26	20
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       394 Aug 26 03:33 HSBC-LKR.in.26082016-1.20160826033308892	3:33	8/26/2016		2016-26-08	3:33:08	0.148009	Fri	5	17	2016-26-8 3:33:08	20
John Hancock Investments	HAN_TRANS_HANVER_20160826.csv.20160826153722565	15:37	8/26/2016		2016-26-08	15:37:22	0.650949	Fri	5	18	2016-26-8 15:37:22	20
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       179 Aug 26 12:37 NOS_SFX_20160826.csv.20160826123743743	12:37	8/26/2016		2016-26-08	12:37:43	0.526192	Fri	5	21	2016-26-8 12:37:43	20
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       748 Aug 26 11:49 PGI_Orders_20160826104805.csv.20160826114939750	11:49	8/26/2016	10:48:05	2016-26-08	11:49:39	0.492813	Fri	5	24	2016-26-8 11:49:39	20
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       369 Aug 26 02:57 FT_fx_20160826_085602.csv.20160826025706714	2:57	8/26/2016	8:56:02	2016-26-08	2:57:06	0.122986	Fri	5	26	2016-26-8 2:57:06	20
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 26 03:25 INV_fx_20160826_092411.csv.20160826032508409	3:25	8/26/2016	9:24:11	2016-26-08	3:25:08	0.142454	Fri	5	26	2016-26-8 3:25:08	20
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Aug 26 04:23 FT_fx_20160826_102102.csv.20160826042311374	4:23	8/26/2016	10:21:02	2016-26-08	4:23:11	0.182766	Fri	5	26	2016-26-8 4:23:11	20
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Aug 26 04:41 INV_fx_20160826_103854.csv.20160826044112476	4:41	8/26/2016	10:38:54	2016-26-08	4:41:12	0.195278	Fri	5	26	2016-26-8 4:41:12	20
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 26 05:25 citicnhtrades.in.201608261716.20160826052514964	5:25	8/26/2016	17:16:00	2016-26-08	5:25:14	0.225856	Fri	5	28	2016-26-8 5:25:14	20
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        60 Aug 26 05:25 hsbccnhtrades.in.201608261716.20160826052515282	5:25	8/26/2016	17:16:00	2016-26-08	5:25:15	0.225868	Fri	5	29	2016-26-8 5:25:15	20
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     21893 Aug 26 10:05 RSWGD1-17_SSGM_Confirmed_File__20160826.csv.20160826100533319	10:05	8/26/2016		2016-26-08	10:05:33	0.420521	Fri	5	30	2016-26-8 10:05:33	20
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     18966 Aug 26 09:31 TIAACREFREPAT.csv.20160826093131079	9:31			2016-26-08	9:31:31	0.396887	Fri	5	32	2016-26-8 9:31:31	20
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       331 Aug 26 10:31 TIAACREFREPAT.csv.20160826103134603	10:31			2016-26-08	10:31:34	0.438588	Fri	5	32	2016-26-8 10:31:34	20
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       693 Aug 28 22:10 tokyofundtrades.in.201608290955.20160828221040395	22:10	8/29/2016	9:55:00	2016-28-08	22:10:40	0.924074	Sun	7	33	2016-28-8 22:10:40	#N/A
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063804284	6:38			2016-29-08	6:38:04	0.276435	Mon	1	4	2016-29-8 6:38:04	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063804645	6:38			2016-29-08	6:38:04	0.276435	Mon	1	4	2016-29-8 6:38:04	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063804845	6:38			2016-29-08	6:38:04	0.276435	Mon	1	4	2016-29-8 6:38:04	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063805035	6:38			2016-29-08	6:38:05	0.276447	Mon	1	4	2016-29-8 6:38:05	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063805234	6:38			2016-29-08	6:38:05	0.276447	Mon	1	4	2016-29-8 6:38:05	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063805423	6:38			2016-29-08	6:38:05	0.276447	Mon	1	4	2016-29-8 6:38:05	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063805631	6:38			2016-29-08	6:38:05	0.276447	Mon	1	4	2016-29-8 6:38:05	21
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 29 06:38 BCRTOFX.txt.20160829063805828	6:38			2016-29-08	6:38:05	0.276447	Mon	1	4	2016-29-8 6:38:05	21
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2562 Aug 29 14:39 BRA_BRA_Ver_20160829.csv.20160829143903123	14:39	8/29/2016		2016-29-08	14:39:03	0.610451	Mon	1	5	2016-29-8 14:39:03	21
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug 29 11:34 CDPSfx_BRLorder.20160829.113500.csv.20160829113452559	11:34	8/29/2016	11:35:00	2016-29-08	11:34:52	0.482546	Mon	1	6	2016-29-8 11:34:52	21
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       336 Aug 29 16:33 CDPSfx_IDRorder.20160829.163000.csv.20160829163307987	16:33	8/29/2016	16:30:00	2016-29-08	16:33:07	0.689664	Mon	1	6	2016-29-8 16:33:07	21
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Aug 29 16:33 CDPSfx_MYRorder.20160829.163500.csv.20160829163308200	16:33	8/29/2016	16:35:00	2016-29-08	16:33:08	0.689676	Mon	1	6	2016-29-8 16:33:08	21
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Aug 29 05:08 scbcnhtrades1.in.201608291656.20160829050859238	5:08	8/29/2016	16:56:00	2016-29-08	5:08:59	0.214572	Mon	1	7	2016-29-8 5:08:59	21
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 29 05:08 scbcnhtrades2.in.201608291656.20160829050859480	5:08	8/29/2016	16:56:00	2016-29-08	5:08:59	0.214572	Mon	1	7	2016-29-8 5:08:59	21
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1003 Aug 29 11:00 SPOT_FET_Instructions_StateStreet_20160829-164855.csv.20160829110049145	11:00	8/29/2016	16:48:55	2016-29-08	11:00:49	0.4589	Mon	1	7	2016-29-8 11:00:49	21
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 29 16:51 08292016_GAM_GAM_STAR_GS.20160829.csv.20160829165109027	16:51	8/29/2016		2016-29-08	16:51:09	0.702188	Mon	1	9	2016-29-8 16:51:09	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 29 10:32 trade10.dat.20160829103247560	10:32			2016-29-08	10:32:47	0.439433	Mon	1	10	2016-29-8 10:32:47	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 29 12:34 trade10.dat.20160829123456003	12:34			2016-29-08	12:34:56	0.524259	Mon	1	10	2016-29-8 12:34:56	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 29 14:33 trade10.dat.20160829143302494	14:33			2016-29-08	14:33:02	0.606273	Mon	1	10	2016-29-8 14:33:02	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     11714 Aug 29 16:25 trade10.dat.20160829162507041	16:25			2016-29-08	16:25:07	0.684109	Mon	1	10	2016-29-8 16:25:07	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 29 17:03 trade10.dat.20160829170309621	17:03			2016-29-08	17:03:09	0.710521	Mon	1	10	2016-29-8 17:03:09	21
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 29 18:03 trade10.dat.20160829180313352	18:03			2016-29-08	18:03:13	0.752234	Mon	1	10	2016-29-8 18:03:13	21
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       181 Aug 29 04:44 UKFCMCurrencyTemplate290816.csv.20160829044457317	4:44			2016-29-08	4:44:57	0.197882	Mon	1	11	2016-29-8 4:44:57	21
Glendon	-rw-r--r--   1 ftpgmrin ftpgmr       166 Aug 29 10:14 GlendonOrders.csv.20160829101446894	10:14			2016-29-08	10:14:46	0.426921	Mon	1	14	2016-29-8 10:14:46	21
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1648 Aug 29 08:31 HighlandCapitalManagementRecon201608290730.csv.20160829083110472	8:31	8/29/2016	7:30:00	2016-29-08	8:31:10	0.354977	Mon	1	16	2016-29-8 8:31:10	21
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       208 Aug 29 02:08 HSBC-LKR.in.29082016-1.20160829020850206	2:08	8/29/2016		2016-29-08	2:08:50	0.089468	Mon	1	17	2016-29-8 2:08:50	21
John Hancock Investments	HAN_TRANS_HANVER_20160829.csv.20160829153705427	15:37	8/29/2016		2016-29-08	15:37:05	0.650752	Mon	1	18	2016-29-8 15:37:05	21
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       369 Aug 29 02:52 FT_fx_20160829_084948.csv.20160829025252687	2:52	8/29/2016	8:49:48	2016-29-08	2:52:52	0.120046	Mon	1	26	2016-29-8 2:52:52	21
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 29 03:18 INV_fx_20160829_091704.csv.20160829031853635	3:18	8/29/2016	9:17:04	2016-29-08	3:18:53	0.138113	Mon	1	26	2016-29-8 3:18:53	21
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Aug 29 05:04 FT_fx_20160829_110347.csv.20160829050458109	5:04	8/29/2016	11:03:47	2016-29-08	5:04:58	0.211782	Mon	1	26	2016-29-8 5:04:58	21
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Aug 29 05:14 INV_fx_20160829_111330.csv.20160829051459834	5:14	8/29/2016	11:13:30	2016-29-08	5:14:59	0.218738	Mon	1	26	2016-29-8 5:14:59	21
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 29 05:31 citicnhtrades.in.201608291716.20160829053100841	5:31	8/29/2016	17:16:00	2016-29-08	5:31:00	0.229861	Mon	1	28	2016-29-8 5:31:00	21
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        59 Aug 29 05:23 hsbccnhtrades.in.201608291716.20160829052300309	5:23	8/29/2016	17:16:00	2016-29-08	5:23:00	0.224306	Mon	1	29	2016-29-8 5:23:00	21
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22575 Aug 29 11:26 RSWGD1-17_SSGM_Confirmed_20160829.csv.20160829112651997	11:26	8/29/2016		2016-29-08	11:26:51	0.476979	Mon	1	30	2016-29-8 11:26:51	21
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3629 Aug 29 09:24 tcwta20160829.csv.20160829.092413.20160829092443719	9:24	8/29/2016		2016-29-08	9:24:43	0.392164	Mon	1	31	2016-29-8 9:24:43	21
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8775 Aug 29 09:30 TIAACREFREPAT.csv.20160829093044220	9:30			2016-29-08	9:30:44	0.396343	Mon	1	32	2016-29-8 9:30:44	21
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       502 Aug 29 02:26 tokyofundtrades.in.201608291407.20160829022651451	2:26	8/29/2016	14:07:00	2016-29-08	2:26:51	0.101979	Mon	1	33	2016-29-8 2:26:51	21
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Aug 30 08:29 Alger_Orders_20160830082814.csv.20160830082922888	8:29	8/30/2016	8:28:14	2016-30-08	8:29:22	0.353727	Tue	2	1	2016-30-8 8:29:22	22
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1409 Aug 30 12:32 SSC_BAM_FXREQ_20160830_173050.csv.pgp.ndm05.20160830123239647	12:32	8/30/2016	17:30:50	2016-30-08	12:32:39	0.522674	Tue	2	3	2016-30-8 12:32:39	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063816971	6:38			2016-30-08	6:38:16	0.276574	Tue	2	4	2016-30-8 6:38:16	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063817199	6:38			2016-30-08	6:38:17	0.276586	Tue	2	4	2016-30-8 6:38:17	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063817398	6:38			2016-30-08	6:38:17	0.276586	Tue	2	4	2016-30-8 6:38:17	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063817598	6:38			2016-30-08	6:38:17	0.276586	Tue	2	4	2016-30-8 6:38:17	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063817787	6:38			2016-30-08	6:38:17	0.276586	Tue	2	4	2016-30-8 6:38:17	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063817996	6:38			2016-30-08	6:38:17	0.276586	Tue	2	4	2016-30-8 6:38:17	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063818212	6:38			2016-30-08	6:38:18	0.276597	Tue	2	4	2016-30-8 6:38:18	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063818420	6:38			2016-30-08	6:38:18	0.276597	Tue	2	4	2016-30-8 6:38:18	22
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 30 06:38 BCRTOFX.txt.20160830063818630	6:38			2016-30-08	6:38:18	0.276597	Tue	2	4	2016-30-8 6:38:18	22
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3199 Aug 30 14:45 BRA_BRA_Ver_20160830.csv.20160830144517028	14:45	8/30/2016		2016-30-08	14:45:17	0.61478	Tue	2	5	2016-30-8 14:45:17	22
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 30 17:33 CDPSfx_PHPorder.20160830.173500.csv.20160830173326455	17:33	8/30/2016	17:35:00	2016-30-08	17:33:26	0.731551	Tue	2	6	2016-30-8 17:33:26	22
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Aug 30 18:33 CDPSfx_THBorder.20160830.183500.csv.20160830183330758	18:33	8/30/2016	18:35:00	2016-30-08	18:33:30	0.773264	Tue	2	6	2016-30-8 18:33:30	22
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1012 Aug 30 10:11 SPOT_FET_Instructions_StateStreet_20160830-155709.csv.20160830101130836	10:11	8/30/2016	15:57:09	2016-30-08	10:11:30	0.424653	Tue	2	7	2016-30-8 10:11:30	22
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 30 16:23 08302016_GAM_GAM_STAR_GS.20160830.csv.20160830162321427	16:23	8/30/2016		2016-30-08	16:23:21	0.682882	Tue	2	9	2016-30-8 16:23:21	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 30 10:33 trade10.dat.20160830103332644	10:33			2016-30-08	10:33:32	0.439954	Tue	2	10	2016-30-8 10:33:32	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 30 12:33 trade10.dat.20160830123340066	12:33			2016-30-08	12:33:40	0.52338	Tue	2	10	2016-30-8 12:33:40	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 30 14:33 trade10.dat.20160830143346230	14:33			2016-30-08	14:33:46	0.606782	Tue	2	10	2016-30-8 14:33:46	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Aug 30 16:23 trade10.dat.20160830162321837	16:23			2016-30-08	16:23:21	0.682882	Tue	2	10	2016-30-8 16:23:21	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 30 17:03 trade10.dat.20160830170324427	17:03			2016-30-08	17:03:24	0.710694	Tue	2	10	2016-30-8 17:03:24	22
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 30 18:03 trade10.dat.20160830180328043	18:03			2016-30-08	18:03:28	0.752407	Tue	2	10	2016-30-8 18:03:28	22
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       400 Aug 30 06:09 UKFCMCurrencyTemplate300816.csv.20160830060915966	6:09			2016-30-08	6:09:15	0.256424	Tue	2	11	2016-30-8 6:09:15	22
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    424049 Aug 30 09:29 passporttrans.20160830.csv.20160830092927177	9:29	8/30/2016		2016-30-08	9:29:27	0.395451	Tue	2	15	2016-30-8 9:29:27	22
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Aug 30 08:31 HighlandCapitalManagementRecon201608300730.csv.20160830083123506	8:31	8/30/2016	7:30:00	2016-30-08	8:31:23	0.355127	Tue	2	16	2016-30-8 8:31:23	22
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       757 Aug 30 02:35 HSBC-LKR.in.30082016-1.20160830023505647	2:35	8/30/2016		2016-30-08	2:35:05	0.107697	Tue	2	17	2016-30-8 2:35:05	22
John Hancock Investments	HAN_TRANS_HANVER_20160830.csv.20160830153919166	15:39	8/30/2016		2016-30-08	15:39:19	0.652303	Tue	2	18	2016-30-8 15:39:19	22
Northern Trust Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2145 Aug 30 07:39 SNBEM-FX-TradeDate31.08.2016.csv.20160830073921371	7:39	8/31/2016		2016-30-08	7:39:21	0.318993	Tue	2	22	2016-30-8 7:39:21	22
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Aug 30 02:57 FT_fx_20160830_085547.csv.20160830025706821	2:57	8/30/2016	8:55:47	2016-30-08	2:57:06	0.122986	Tue	2	26	2016-30-8 2:57:06	22
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Aug 30 04:17 FT_fx_20160830_101440.csv.20160830041709782	4:17	8/30/2016	10:14:40	2016-30-08	4:17:09	0.178576	Tue	2	26	2016-30-8 4:17:09	22
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       230 Aug 30 05:01 INV_fx_20160830_105953.csv.20160830050111894	5:01	8/30/2016	10:59:53	2016-30-08	5:01:11	0.209155	Tue	2	26	2016-30-8 5:01:11	22
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Aug 30 07:35 INV_fx_20160830_133231.csv.20160830073520887	7:35	8/30/2016	13:32:31	2016-30-08	7:35:20	0.316204	Tue	2	26	2016-30-8 7:35:20	22
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        58 Aug 30 04:19 citicnhtrades.in.201608301606.20160830041910271	4:19	8/30/2016	16:06:00	2016-30-08	4:19:10	0.179977	Tue	2	28	2016-30-8 4:19:10	22
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 30 05:27 citicnhtrades.in.201608301718.20160830052713682	5:27	8/30/2016	17:18:00	2016-30-08	5:27:13	0.227234	Tue	2	28	2016-30-8 5:27:13	22
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       117 Aug 30 05:27 hsbccnhtrades.in.201608301718.20160830052713970	5:27	8/30/2016	17:18:00	2016-30-08	5:27:13	0.227234	Tue	2	29	2016-30-8 5:27:13	22
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22575 Aug 30 00:03 RSWGD1-17_SSGM_Confirmed_File__20160829.csv.20160830000330312	0:03	8/29/2016		2016-30-08	0:03:30	0.002431	Tue	2	30	2016-30-8 0:03:30	22
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     19178 Aug 30 09:57 RSWGD1-17_SSGM_Confirmed_File__20160830.csv.20160830095729294	9:57	8/30/2016		2016-30-08	9:57:29	0.414919	Tue	2	30	2016-30-8 9:57:29	22
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8494 Aug 30 09:31 TIAACREFREPAT.csv.20160830093127684	9:31			2016-30-08	9:31:27	0.39684	Tue	2	32	2016-30-8 9:31:27	22
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       827 Aug 30 10:31 TIAACREFREPAT.csv.20160830103132054	10:31			2016-30-08	10:31:32	0.438565	Tue	2	32	2016-30-8 10:31:32	22
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1420 Aug 31 08:33 SSC_BAM_FXREQ_20160831_133026.csv.pgp.ndm05.20160831083308712	8:33	8/31/2016	13:30:26	2016-31-08	8:33:08	0.356343	Wed	3	3	2016-31-8 8:33:08	23
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1424 Aug 31 09:33 SSC_BAM_FXREQ_20160831_143030.csv.pgp.ndm05.20160831093313913	9:33	8/31/2016	14:30:30	2016-31-08	9:33:13	0.398067	Wed	3	3	2016-31-8 9:33:13	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063831200	6:38			2016-31-08	6:38:31	0.276748	Wed	3	4	2016-31-8 6:38:31	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063831543	6:38			2016-31-08	6:38:31	0.276748	Wed	3	4	2016-31-8 6:38:31	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063831734	6:38			2016-31-08	6:38:31	0.276748	Wed	3	4	2016-31-8 6:38:31	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063831919	6:38			2016-31-08	6:38:31	0.276748	Wed	3	4	2016-31-8 6:38:31	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063832119	6:38			2016-31-08	6:38:32	0.276759	Wed	3	4	2016-31-8 6:38:32	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063832332	6:38			2016-31-08	6:38:32	0.276759	Wed	3	4	2016-31-8 6:38:32	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063832541	6:38			2016-31-08	6:38:32	0.276759	Wed	3	4	2016-31-8 6:38:32	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063832772	6:38			2016-31-08	6:38:32	0.276759	Wed	3	4	2016-31-8 6:38:32	23
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Aug 31 06:38 BCRTOFX.txt.20160831063832921	6:38			2016-31-08	6:38:32	0.276759	Wed	3	4	2016-31-8 6:38:32	23
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3948 Aug 31 14:40 BRA_BRA_Ver_20160831.csv.20160831144002821	14:40	8/31/2016		2016-31-08	14:40:02	0.611134	Wed	3	5	2016-31-8 14:40:02	23
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1003 Aug 31 09:13 SPOT_FET_Instructions_StateStreet_20160831-150622.csv.20160831091341734	9:13	8/31/2016	15:06:22	2016-31-08	9:13:41	0.384502	Wed	3	7	2016-31-8 9:13:41	23
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 31 16:42 08312016_GAM_GAM_STAR_GS.20160831.csv.20160831164208631	16:42	8/31/2016		2016-31-08	16:42:08	0.695926	Wed	3	9	2016-31-8 16:42:08	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 31 10:33 trade10.dat.20160831103347961	10:33			2016-31-08	10:33:47	0.440127	Wed	3	10	2016-31-8 10:33:47	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 31 12:33 trade10.dat.20160831123355835	12:33			2016-31-08	12:33:55	0.523553	Wed	3	10	2016-31-8 12:33:55	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Aug 31 14:34 trade10.dat.20160831143401916	14:34			2016-31-08	14:34:01	0.606956	Wed	3	10	2016-31-8 14:34:01	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Aug 31 17:26 trade10.dat.20160831172611199	17:26			2016-31-08	17:26:11	0.726516	Wed	3	10	2016-31-8 17:26:11	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 31 17:30 trade10.dat.20160831173011785	17:30			2016-31-08	17:30:11	0.729294	Wed	3	10	2016-31-8 17:30:11	23
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Aug 31 18:04 trade10.dat.20160831180414284	18:04			2016-31-08	18:04:14	0.75294	Wed	3	10	2016-31-8 18:04:14	23
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       179 Aug 31 06:46 UKFCMCurrencyTemplate310816.csv.20160831064603409	6:46			2016-31-08	6:46:03	0.281979	Wed	3	11	2016-31-8 6:46:03	23
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr      1563 Aug 31 07:36 UKFCMCurrencyTemplate310816a.csv.20160831073605786	7:36			2016-31-08	7:36:05	0.316725	Wed	3	11	2016-31-8 7:36:05	23
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       177 Aug 31 07:45 UKFCMCurrencyTemplate310816b.csv.20160831074536280	7:45			2016-31-08	7:45:36	0.323333	Wed	3	11	2016-31-8 7:45:36	23
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    248292 Aug 31 09:05 passporttrans.20160831.csv.20160831090541051	9:05	8/31/2016		2016-31-08	9:05:41	0.378947	Wed	3	15	2016-31-8 9:05:41	23
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1818 Aug 31 08:31 HighlandCapitalManagementRecon201608310730.csv.20160831083138424	8:31	8/31/2016	7:30:00	2016-31-08	8:31:38	0.355301	Wed	3	16	2016-31-8 8:31:38	23
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       477 Aug 31 02:45 HSBC-LKR.in.31082016-1.20160831024550032	2:45	8/31/2016		2016-31-08	2:45:50	0.115162	Wed	3	17	2016-31-8 2:45:50	23
John Hancock Investments	HAN_TRANS_HANVER_20160831.csv.20160831153204396	15:32	8/31/2016		2016-31-08	15:32:04	0.647269	Wed	3	18	2016-31-8 15:32:04	23
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       203 Aug 31 14:38 PGI_Orders_20160831133605.csv.20160831143802599	14:38	8/31/2016	13:36:05	2016-31-08	14:38:02	0.609745	Wed	3	24	2016-31-8 14:38:02	23
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Aug 31 02:59 FT_fx_20160831_085728.csv.20160831025950654	2:59	8/31/2016	8:57:28	2016-31-08	2:59:50	0.124884	Wed	3	26	2016-31-8 2:59:50	23
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 31 03:51 INV_fx_20160831_095041.csv.20160831035153821	3:51	8/31/2016	9:50:41	2016-31-08	3:51:53	0.16103	Wed	3	26	2016-31-8 3:51:53	23
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Aug 31 04:39 FT_fx_20160831_103751.csv.20160831043955856	4:39	8/31/2016	10:37:51	2016-31-08	4:39:55	0.194387	Wed	3	26	2016-31-8 4:39:55	23
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Aug 31 05:27 INV_fx_20160831_112516.csv.20160831052758879	5:27	8/31/2016	11:25:16	2016-31-08	5:27:58	0.227755	Wed	3	26	2016-31-8 5:27:58	23
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Aug 31 05:23 citicnhtrades.in.201608311716.20160831052358240	5:23	8/31/2016	17:16:00	2016-31-08	5:23:58	0.224977	Wed	3	28	2016-31-8 5:23:58	23
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       177 Aug 31 05:23 hsbccnhtrades.in.201608311716.20160831052358588	5:23	8/31/2016	17:16:00	2016-31-08	5:23:58	0.224977	Wed	3	29	2016-31-8 5:23:58	23
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23592 Aug 31 10:39 RSWGD1-17_SSGM_Confirmed_File__20160831.csv.20160831103948738	10:39	8/31/2016		2016-31-08	10:39:48	0.444306	Wed	3	30	2016-31-8 10:39:48	23
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4095 Aug 31 09:37 tcwta20160831.csv.20160831.093557.20160831093744504	9:37	8/31/2016		2016-31-08	9:37:44	0.401204	Wed	3	31	2016-31-8 9:37:44	23
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     13033 Aug 31 09:31 TIAACREFREPAT.csv.20160831093143325	9:31			2016-31-08	9:31:43	0.397025	Wed	3	32	2016-31-8 9:31:43	23
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Sep  1 11:28 Alger_Orders_20160901112557.csv.20160901112836694	11:28	9/1/2016	11:25:57	2016-01-09	11:28:36	0.478194	Thu	4	1	2016-09-01 11:28	24
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Sep  1 13:04 Alger_Orders_20160901130058.csv.20160901130443399	13:04	9/1/2016	13:00:58	2016-01-09	13:04:43	0.544942	Thu	4	1	2016-09-01 13:04	24
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1893 Sep  1 12:32 SSC_BAM_FXREQ_20160901_173043.csv.pgp.ndm05.20160901123241344	12:32	9/1/2016	17:30:43	2016-01-09	12:32:41	0.522697	Thu	4	3	2016-09-01 12:32	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063847696	6:38			2016-01-09	6:38:47	0.276933	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063848003	6:38			2016-01-09	6:38:48	0.276944	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063848191	6:38			2016-01-09	6:38:48	0.276944	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063848393	6:38			2016-01-09	6:38:48	0.276944	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063848615	6:38			2016-01-09	6:38:48	0.276944	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063848810	6:38			2016-01-09	6:38:48	0.276944	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063849006	6:38			2016-01-09	6:38:49	0.276956	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063849203	6:38			2016-01-09	6:38:49	0.276956	Thu	4	4	2016-09-01 06:38	24
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  1 06:38 BCRTOFX.txt.20160901063849419	6:38			2016-01-09	6:38:49	0.276956	Thu	4	4	2016-09-01 06:38	24
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4940 Sep  1 14:44 BRA_BRA_Ver_20160901.csv.20160901144418967	14:44	9/1/2016		2016-01-09	14:44:18	0.614097	Thu	4	5	2016-09-01 14:44	24
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1003 Sep  1 10:10 SPOT_FET_Instructions_StateStreet_20160901-160708.csv.20160901101030300	10:10	9/1/2016	16:07:08	2016-01-09	10:10:30	0.423958	Thu	4	7	2016-09-01 10:10	24
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  1 16:40 09012016_GAM_GAM_STAR_GS.20160901.csv.20160901164025434	16:40	9/1/2016		2016-01-09	16:40:25	0.694734	Thu	4	9	2016-09-01 16:40	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  1 10:34 trade10.dat.20160901103431766	10:34			2016-01-09	10:34:31	0.440637	Thu	4	10	2016-09-01 10:34	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep  1 12:32 trade10.dat.20160901123241105	12:32			2016-01-09	12:32:41	0.522697	Thu	4	10	2016-09-01 12:32	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  1 14:32 trade10.dat.20160901143217719	14:32			2016-01-09	14:32:17	0.605752	Thu	4	10	2016-09-01 14:32	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Sep  1 16:24 trade10.dat.20160901162423409	16:24			2016-01-09	16:24:23	0.6836	Thu	4	10	2016-09-01 16:24	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Sep  1 17:04 trade10.dat.20160901170427081	17:04			2016-01-09	17:04:27	0.711424	Thu	4	10	2016-09-01 17:04	24
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  1 18:04 trade10.dat.20160901180431157	18:04			2016-01-09	18:04:31	0.753137	Thu	4	10	2016-09-01 18:04	24
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    316027 Sep  1 09:00 passporttrans.20160901.csv.20160901090024433	9:00	9/1/2016		2016-01-09	9:00:24	0.375278	Thu	4	15	2016-09-01 09:00	24
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1991 Sep  1 08:32 HighlandCapitalManagementRecon201609010730.csv.20160901083223585	8:32	9/1/2016	7:30:00	2016-01-09	8:32:23	0.355822	Thu	4	16	2016-09-01 08:32	24
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr      1581 Sep  1 03:32 HSBC-LKR.in.01092016-1.20160901033207845	3:32	1/9/2016		2016-01-09	3:32:07	0.147303	Thu	4	17	2016-09-01 03:32	24
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr      1581 Sep  1 03:34 HSBC-LKR.in.01092016-1.20160901033408294	3:34	1/9/2016		2016-01-09	3:34:08	0.148704	Thu	4	17	2016-09-01 03:34	24
John Hancock Investments	HAN_TRANS_HANVER_20160901.csv.20160901153821842	15:38	9/1/2016		2016-01-09	15:38:21	0.651632	Thu	4	18	2016-09-01 15:38	24
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       372 Sep  1 03:04 FT_fx_20160901_090225.csv.20160901030406376	3:04	9/1/2016	9:02:25	2016-01-09	3:04:06	0.127847	Thu	4	26	2016-09-01 03:04	24
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep  1 04:28 FT_fx_20160901_102658.csv.20160901042810225	4:28	9/1/2016	10:26:58	2016-01-09	4:28:10	0.186227	Thu	4	26	2016-09-01 04:28	24
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       295 Sep  1 05:04 INV_fx_20160901_110159.csv.20160901050412729	5:04	9/1/2016	11:01:59	2016-01-09	5:04:12	0.21125	Thu	4	26	2016-09-01 05:04	24
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Sep  1 06:46 FT_fx_20160901_120009.csv.20160901064619768	6:46	9/1/2016	12:00:09	2016-01-09	6:46:19	0.282164	Thu	4	26	2016-09-01 06:46	24
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        59 Sep  1 04:30 citicnhtrades.in.201609011623.20160901043010718	4:30	9/1/2016	16:23:00	2016-01-09	4:30:10	0.187616	Thu	4	28	2016-09-01 04:30	24
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  1 05:26 citicnhtrades.in.201609011716.20160901052613789	5:26	9/1/2016	17:16:00	2016-01-09	5:26:13	0.226539	Thu	4	28	2016-09-01 05:26	24
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep  1 05:26 hsbccnhtrades.in.201609011716.20160901052614085	5:26	9/1/2016	17:16:00	2016-01-09	5:26:14	0.226551	Thu	4	29	2016-09-01 05:26	24
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24305 Sep  1 11:04 RSWGD1-17_SSGM_Confirmed_File__20160901.csv.20160901110433962	11:04	9/1/2016		2016-01-09	11:04:33	0.461493	Thu	4	30	2016-09-01 11:04	24
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3589 Sep  1 10:06 tcwta20160901.csv.20160901.100418.20160901100628819	10:06	9/1/2016		2016-01-09	10:06:28	0.421157	Thu	4	31	2016-09-01 10:06	24
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     23932 Sep  1 09:32 TIAACREFREPAT.csv.20160901093226822	9:32			2016-01-09	9:32:26	0.397523	Thu	4	32	2016-09-01 09:32	24
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       195 Sep  2 09:16 Alger_Orders_20160902091334.csv.20160902091648597	9:16	9/2/2016	9:13:34	2016-02-09	9:16:48	0.386667	Fri	5	1	2016-09-02 09:16	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1660 Sep  2 04:32 SSC_BAM_FXREQ_20160902_093007.csv.pgp.ndm05.20160902043230508	4:32	9/2/2016	9:30:07	2016-02-09	4:32:30	0.189236	Fri	5	3	2016-09-02 04:32	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep  2 05:30 SSC_BAM_FXREQ_20160902_103011.csv.pgp.ndm05.20160902053033889	5:30	9/2/2016	10:30:11	2016-02-09	5:30:33	0.229549	Fri	5	3	2016-09-02 05:30	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1478 Sep  2 07:31 SSC_BAM_FXREQ_20160902_123018.csv.pgp.ndm05.20160902073114200	7:31	9/2/2016	12:30:18	2016-02-09	7:31:14	0.313356	Fri	5	3	2016-09-02 07:31	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep  2 09:31 SSC_BAM_FXREQ_20160902_143023.csv.pgp.ndm05.20160902093121638	9:31	9/2/2016	14:30:23	2016-02-09	9:31:21	0.396771	Fri	5	3	2016-09-02 09:31	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1434 Sep  2 11:31 SSC_BAM_FXREQ_20160902_163032.csv.pgp.ndm05.20160902113130922	11:31	9/2/2016	16:30:32	2016-02-09	11:31:30	0.480208	Fri	5	3	2016-09-02 11:31	25
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1408 Sep  2 13:31 SSC_BAM_FXREQ_20160902_183037.csv.pgp.ndm05.20160902133139385	13:31	9/2/2016	18:30:37	2016-02-09	13:31:39	0.563646	Fri	5	3	2016-09-02 13:31	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063840135	6:38			2016-02-09	6:38:40	0.276852	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063840441	6:38			2016-02-09	6:38:40	0.276852	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063840643	6:38			2016-02-09	6:38:40	0.276852	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063840861	6:38			2016-02-09	6:38:40	0.276852	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063841057	6:38			2016-02-09	6:38:41	0.276863	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063841265	6:38			2016-02-09	6:38:41	0.276863	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063841466	6:38			2016-02-09	6:38:41	0.276863	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063841676	6:38			2016-02-09	6:38:41	0.276863	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063841889	6:38			2016-02-09	6:38:41	0.276863	Fri	5	4	2016-09-02 06:38	25
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  2 06:38 BCRTOFX.txt.20160902063842101	6:38			2016-02-09	6:38:42	0.276875	Fri	5	4	2016-09-02 06:38	25
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2222 Sep  2 14:39 BRA_BRA_Ver_20160902.csv.20160902143914077	14:39	9/2/2016		2016-02-09	14:39:14	0.610579	Fri	5	5	2016-09-02 14:39	25
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       326 Sep  2 05:03 scbcnhtrades1.in.201609021648.20160902050301882	5:03	9/2/2016	16:48:00	2016-02-09	5:03:01	0.210428	Fri	5	7	2016-09-02 05:03	25
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  2 05:03 scbcnhtrades2.in.201609021648.20160902050302143	5:03	9/2/2016	16:48:00	2016-02-09	5:03:02	0.21044	Fri	5	7	2016-09-02 05:03	25
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  2 06:20 scbcnhtrades2.in.201609021812.20160902062038840	6:20	9/2/2016	18:12:00	2016-02-09	6:20:38	0.264329	Fri	5	7	2016-09-02 06:20	25
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep  2 06:20 scbcnhtrades1.in.201609021812.20160902062039136	6:20	9/2/2016	18:12:00	2016-02-09	6:20:39	0.26434	Fri	5	7	2016-09-02 06:20	25
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       872 Sep  2 10:08 SPOT_FET_Instructions_StateStreet_20160902-160032.csv.20160902100853321	10:08	9/2/2016	16:00:32	2016-02-09	10:08:53	0.422836	Fri	5	7	2016-09-02 10:08	25
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep  2 11:04 CRUX_20160902.csv.20160902110458543	11:04	9/2/2016		2016-02-09	11:04:58	0.461782	Fri	5	8	2016-09-02 11:04	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Sep  2 10:34 trade10.dat.20160902103455550	10:34			2016-02-09	10:34:55	0.440914	Fri	5	10	2016-09-02 10:34	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  2 12:33 trade10.dat.20160902123305377	12:33			2016-02-09	12:33:05	0.522975	Fri	5	10	2016-09-02 12:33	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  2 14:33 trade10.dat.20160902143313385	14:33			2016-02-09	14:33:13	0.6064	Fri	5	10	2016-09-02 14:33	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Sep  2 16:25 trade10.dat.20160902162517734	16:25			2016-02-09	16:25:17	0.684225	Fri	5	10	2016-09-02 16:25	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep  2 17:03 trade10.dat.20160902170320451	17:03			2016-02-09	17:03:20	0.710648	Fri	5	10	2016-09-02 17:03	25
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  2 18:02 trade10.dat.20160902180255020	18:02			2016-02-09	18:02:55	0.752025	Fri	5	10	2016-09-02 18:02	25
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    248589 Sep  2 09:18 passporttrans.20160902.csv.20160902091849079	9:18	9/2/2016		2016-02-09	9:18:49	0.388067	Fri	5	15	2016-09-02 09:18	25
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr      1399 Sep  2 03:16 HSBC-LKR.in.02092016-1.20160902031656214	3:16	2/9/2016		2016-02-09	3:16:56	0.136759	Fri	5	17	2016-09-02 03:16	25
John Hancock Investments	HAN_TRANS_HANVER_20160902.csv.20160902154516094	15:45	9/2/2016		2016-02-09	15:45:16	0.656435	Fri	5	18	2016-09-02 15:45	25
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep  2 10:34 NOS_SFX_20160902.csv.20160902103457055	10:34	9/2/2016		2016-02-09	10:34:57	0.440938	Fri	5	21	2016-09-02 10:34	25
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       179 Sep  2 12:41 NOS_SFX_20160902_EUR.csv.20160902124106498	12:41	9/2/2016		2016-02-09	12:41:06	0.528542	Fri	5	21	2016-09-02 12:41	25
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       526 Sep  2 13:55 PGI_Orders_20160902125431.csv.20160902135510347	13:55	9/2/2016	12:54:31	2016-02-09	13:55:10	0.579977	Fri	5	24	2016-09-02 13:55	25
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep  2 03:10 FT_fx_20160902_090842.csv.20160902031055542	3:10	9/2/2016	9:08:42	2016-02-09	3:10:55	0.132581	Fri	5	26	2016-09-02 03:10	25
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep  2 03:28 INV_fx_20160902_092727.csv.20160902032857448	3:28	9/2/2016	9:27:27	2016-02-09	3:28:57	0.145104	Fri	5	26	2016-09-02 03:28	25
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep  2 04:57 FT_fx_20160902_105359.csv.20160902045701345	4:57	9/2/2016	10:53:59	2016-02-09	4:57:01	0.206262	Fri	5	26	2016-09-02 04:57	25
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Sep  2 05:57 INV_fx_20160902_115224.csv.20160902055705151	5:57	9/2/2016	11:52:24	2016-02-09	5:57:05	0.247975	Fri	5	26	2016-09-02 05:57	25
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep  2 04:29 citicnhtrades.in.201609021615.20160902042900008	4:29	9/2/2016	16:15:00	2016-02-09	4:29:00	0.186806	Fri	5	28	2016-09-02 04:29	25
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  2 05:33 citicnhtrades.in.201609021723.20160902053304396	5:33	9/2/2016	17:23:00	2016-02-09	5:33:04	0.231296	Fri	5	28	2016-09-02 05:33	25
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep  2 05:33 hsbccnhtrades.in.201609021723.20160902053304237	5:33	9/2/2016	17:23:00	2016-02-09	5:33:04	0.231296	Fri	5	29	2016-09-02 05:33	25
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24604 Sep  2 11:02 RSWGD1-17_SSGM_Confirmed_File__20160902.csv.20160902110258180	11:02	9/2/2016		2016-02-09	11:02:58	0.460394	Fri	5	30	2016-09-02 11:02	25
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3510 Sep  2 09:54 tcwta20160902.csv.20160902095452588	9:54	9/2/2016		2016-02-09	9:54:52	0.413102	Fri	5	31	2016-09-02 09:54	25
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8463 Sep  2 09:30 TIAACREFREPAT.csv.20160902093051118	9:30			2016-02-09	9:30:51	0.396424	Fri	5	32	2016-09-02 09:30	25
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  4 20:43 09042016_GAM_GAM_STAR_GS.20160904.csv.20160904204358249	20:43	9/4/2016		2016-04-09	20:43:58	0.863866	Sun	7	9	2016-09-04 20:43	#N/A
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       394 Sep  4 21:48 tokyofundtrades.in.201609050929.20160904214800807	21:48	9/5/2016	9:29:00	2016-04-09	21:48:00	0.908333	Sun	7	33	2016-09-04 21:48	#N/A
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Sep  5 04:31 SSC_BAM_FXREQ_20160905_093017.csv.pgp.ndm05.20160905043147226	4:31	9/5/2016	9:30:17	2016-05-09	4:31:47	0.188738	Mon	1	3	2016-09-05 04:31	26
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep  5 05:31 SSC_BAM_FXREQ_20160905_103019.csv.pgp.ndm05.20160905053151949	5:31	9/5/2016	10:30:19	2016-05-09	5:31:51	0.230451	Mon	1	3	2016-09-05 05:31	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063755611	6:37			2016-05-09	6:37:55	0.276331	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063755996	6:37			2016-05-09	6:37:55	0.276331	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063756199	6:37			2016-05-09	6:37:56	0.276343	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063756394	6:37			2016-05-09	6:37:56	0.276343	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063756681	6:37			2016-05-09	6:37:56	0.276343	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063756820	6:37			2016-05-09	6:37:56	0.276343	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063757018	6:37			2016-05-09	6:37:57	0.276354	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063757208	6:37			2016-05-09	6:37:57	0.276354	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063757413	6:37			2016-05-09	6:37:57	0.276354	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063757603	6:37			2016-05-09	6:37:57	0.276354	Mon	1	4	2016-09-05 06:37	26
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  5 06:37 BCRTOFX.txt.20160905063757808	6:37			2016-05-09	6:37:57	0.276354	Mon	1	4	2016-09-05 06:37	26
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       337 Sep  5 11:34 CDPSfx_IDRorder.20160905.113500.csv.20160905113412736	11:34	9/5/2016	11:35:00	2016-05-09	11:34:12	0.482083	Mon	1	6	2016-09-05 11:34	26
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Sep  5 11:34 CDPSfx_THBorder.20160905.113500.csv.20160905113412998	11:34	9/5/2016	11:35:00	2016-05-09	11:34:12	0.482083	Mon	1	6	2016-09-05 11:34	26
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       335 Sep  5 20:34 CDPSfx_TWDorder.20160905.203500.csv.20160905203440801	20:34	9/5/2016	20:35:00	2016-05-09	20:34:40	0.857407	Mon	1	6	2016-09-05 20:34	26
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep  5 05:18 scbcnhtrades1.in.201609051709.20160905051820556	5:18	9/5/2016	17:09:00	2016-05-09	5:18:20	0.221065	Mon	1	7	2016-09-05 05:18	26
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  5 05:18 scbcnhtrades2.in.201609051709.20160905051820705	5:18	9/5/2016	17:09:00	2016-05-09	5:18:20	0.221065	Mon	1	7	2016-09-05 05:18	26
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       580 Sep  5 10:20 SPOT_FET_Instructions_StateStreet_20160905-154946.csv.20160905102008128	10:20	9/5/2016	15:49:46	2016-05-09	10:20:08	0.430648	Mon	1	7	2016-09-05 10:20	26
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep  5 05:26 CRUX_20160905.csv.20160905052621111	5:26	9/5/2016		2016-05-09	5:26:21	0.226632	Mon	1	8	2016-09-05 05:26	26
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 16:50 09052016_GAM_GAM_STAR_GS.20160905.csv.20160905165029268	16:50	9/5/2016		2016-05-09	16:50:29	0.701725	Mon	1	9	2016-09-05 16:50	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 10:34 trade10.dat.20160905103409823	10:34			2016-05-09	10:34:09	0.440382	Mon	1	10	2016-09-05 10:34	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 12:34 trade10.dat.20160905123417213	12:34			2016-05-09	12:34:17	0.523808	Mon	1	10	2016-09-05 12:34	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep  5 14:34 trade10.dat.20160905143423969	14:34			2016-05-09	14:34:23	0.607211	Mon	1	10	2016-09-05 14:34	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 16:24 trade10.dat.20160905162427828	16:24			2016-05-09	16:24:27	0.683646	Mon	1	10	2016-09-05 16:24	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 17:04 trade10.dat.20160905170430417	17:04			2016-05-09	17:04:30	0.711458	Mon	1	10	2016-09-05 17:04	26
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  5 18:04 trade10.dat.20160905180434113	18:04			2016-05-09	18:04:34	0.753171	Mon	1	10	2016-09-05 18:04	26
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr     63611 Sep  5 08:54 passporttrans.20160905.csv.20160905085433607	8:54	9/5/2016		2016-05-09	8:54:33	0.371215	Mon	1	15	2016-09-05 08:54	26
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Sep  5 08:32 HighlandCapitalManagementRecon201609050730.csv.20160905083232281	8:32	9/5/2016	7:30:00	2016-05-09	8:32:32	0.355926	Mon	1	16	2016-09-05 08:32	26
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       943 Sep  5 03:04 HSBC-LKR.in.05092016-1.20160905030413189	3:04	5/9/2016		2016-05-09	3:04:13	0.127928	Mon	1	17	2016-09-05 03:04	26
Northern Trust Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2145 Sep  5 05:06 SNBEM-FX-TradeDate05.09.2016.csv.20160905050618889	5:06	9/5/2016		2016-05-09	5:06:18	0.212708	Mon	1	22	2016-09-05 05:06	26
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Sep  5 03:08 FT_fx_20160905_090459.csv.20160905030813536	3:08	9/5/2016	9:04:59	2016-05-09	3:08:13	0.130706	Mon	1	26	2016-09-05 03:08	26
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       297 Sep  5 03:20 INV_fx_20160905_091848.csv.20160905032014123	3:20	9/5/2016	9:18:48	2016-05-09	3:20:14	0.139051	Mon	1	26	2016-09-05 03:20	26
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep  5 05:16 INV_fx_20160905_111412.csv.20160905051620112	5:16	9/5/2016	11:14:12	2016-05-09	5:16:20	0.219676	Mon	1	26	2016-09-05 05:16	26
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       294 Sep  5 05:42 FT_fx_20160905_113949.csv.20160905054222544	5:42	9/5/2016	11:39:49	2016-05-09	5:42:22	0.237755	Mon	1	26	2016-09-05 05:42	26
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  5 05:26 citicnhtrades.in.201609051714.20160905052621393	5:26	9/5/2016	17:14:00	2016-05-09	5:26:21	0.226632	Mon	1	28	2016-09-05 05:26	26
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       289 Sep  5 05:26 hsbccnhtrades.in.201609051714.20160905052621606	5:26	9/5/2016	17:14:00	2016-05-09	5:26:21	0.226632	Mon	1	29	2016-09-05 05:26	26
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     21061 Sep  5 11:04 RSWGD1-17_SSGM_Confirmed_File__20160905.csv.20160905110410969	11:04	9/5/2016		2016-05-09	11:04:10	0.461227	Mon	1	30	2016-09-05 11:04	26
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4281 Sep  5 10:26 tiaacrefOrd_hkd_krw.20160905-102522.20160905102609428	10:26	9/5/2016	10:25:22	2016-05-09	10:26:09	0.434826	Mon	1	32	2016-09-05 10:26	26
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       343 Sep  5 22:26 tokyofundtrades.in.201609061015.20160905222645226	22:26	9/6/2016	10:15:00	2016-05-09	22:26:45	0.935243	Mon	1	33	2016-09-05 22:26	26
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       408 Sep  5 08:44 TrinityStreetFX_090516.csv.20160905084432861	8:44			2016-05-09	8:44:32	0.364259	Mon	1	34	2016-09-05 08:44	26
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1590 Sep  6 04:32 SSC_BAM_FXREQ_20160906_093025.csv.pgp.ndm05.20160906043258333	4:32	9/6/2016	9:30:25	2016-06-09	4:32:58	0.18956	Tue	2	3	2016-09-06 04:32	27
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1460 Sep  6 05:33 SSC_BAM_FXREQ_20160906_103029.csv.pgp.ndm05.20160906053301882	5:33	9/6/2016	10:30:29	2016-06-09	5:33:01	0.231262	Tue	2	3	2016-09-06 05:33	27
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1432 Sep  6 06:33 SSC_BAM_FXREQ_20160906_113033.csv.pgp.ndm05.20160906063306151	6:33	9/6/2016	11:30:33	2016-06-09	6:33:06	0.272986	Tue	2	3	2016-09-06 06:33	27
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1419 Sep  6 07:33 SSC_BAM_FXREQ_20160906_123035.csv.pgp.ndm05.20160906073310140	7:33	9/6/2016	12:30:35	2016-06-09	7:33:10	0.314699	Tue	2	3	2016-09-06 07:33	27
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep  6 11:33 SSC_BAM_FXREQ_20160906_163045.csv.pgp.ndm05.20160906113355118	11:33	9/6/2016	16:30:45	2016-06-09	11:33:55	0.481887	Tue	2	3	2016-09-06 11:33	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063806620	6:38			2016-06-09	6:38:06	0.276458	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063806859	6:38			2016-06-09	6:38:06	0.276458	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063807060	6:38			2016-06-09	6:38:07	0.27647	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063807259	6:38			2016-06-09	6:38:07	0.27647	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063807472	6:38			2016-06-09	6:38:07	0.27647	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063807659	6:38			2016-06-09	6:38:07	0.27647	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063807851	6:38			2016-06-09	6:38:07	0.27647	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063808058	6:38			2016-06-09	6:38:08	0.276481	Tue	2	4	2016-09-06 06:38	27
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  6 06:38 BCRTOFX.txt.20160906063808263	6:38			2016-06-09	6:38:08	0.276481	Tue	2	4	2016-09-06 06:38	27
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4501 Sep  6 14:51 BRA_BRA_Ver_20160906.csv.20160906145105270	14:51	9/6/2016		2016-06-09	14:51:05	0.618808	Tue	2	5	2016-09-06 14:51	27
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       337 Sep  6 20:34 CDPSfx_IDRorder.20160906.203000.csv.20160906203452568	20:34	9/6/2016	20:30:00	2016-06-09	20:34:52	0.857546	Tue	2	6	2016-09-06 20:34	27
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  6 20:34 CDPSfx_TWDorder.20160906.203000.csv.20160906203452969	20:34	9/6/2016	20:30:00	2016-06-09	20:34:52	0.857546	Tue	2	6	2016-09-06 20:34	27
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  6 22:32 CDPSfx_MYRorder.20160906.223500.csv.20160906223258108	22:32	9/6/2016	22:35:00	2016-06-09	22:32:58	0.93956	Tue	2	6	2016-09-06 22:32	27
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       334 Sep  6 22:32 CDPSfx_PHPorder.20160906.223500.csv.20160906223258442	22:32	9/6/2016	22:35:00	2016-06-09	22:32:58	0.93956	Tue	2	6	2016-09-06 22:32	27
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1153 Sep  6 09:36 SPOT_FET_Instructions_StateStreet_20160906-152512.csv.20160906093647267	9:36	9/6/2016	15:25:12	2016-06-09	9:36:47	0.400544	Tue	2	7	2016-09-06 09:36	27
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  6 17:26 09062016_GAM_GAM_STAR_GS.20160906.csv.20160906172642733	17:26	9/6/2016		2016-06-09	17:26:42	0.726875	Tue	2	9	2016-09-06 17:26	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Sep  6 10:34 trade10.dat.20160906103450494	10:34			2016-06-09	10:34:50	0.440856	Tue	2	10	2016-09-06 10:34	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     16922 Sep  6 12:34 trade10.dat.20160906123458291	12:34			2016-06-09	12:34:58	0.524282	Tue	2	10	2016-09-06 12:34	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5638 Sep  6 14:33 trade10.dat.20160906143304166	14:33			2016-06-09	14:33:04	0.606296	Tue	2	10	2016-09-06 14:33	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Sep  6 16:25 trade10.dat.20160906162508734	16:25			2016-06-09	16:25:08	0.68412	Tue	2	10	2016-09-06 16:25	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Sep  6 17:02 trade10.dat.20160906170241295	17:02			2016-06-09	17:02:41	0.710197	Tue	2	10	2016-09-06 17:02	27
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  6 18:02 trade10.dat.20160906180245060	18:02			2016-06-09	18:02:45	0.75191	Tue	2	10	2016-09-06 18:02	27
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       408 Sep  6 05:46 UKFCMCurrencyTemplate060916.csv.20160906054632347	5:46			2016-06-09	5:46:32	0.240648	Tue	2	11	2016-09-06 05:46	27
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       720 Sep  6 09:04 UKFCMCurrencyTemplate060916a.csv.20160906090443923	9:04			2016-06-09	9:04:43	0.378275	Tue	2	11	2016-09-06 09:04	27
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    400901 Sep  6 09:04 passporttrans.20160906.csv.20160906090443529	9:04	9/6/2016		2016-06-09	9:04:43	0.378275	Tue	2	15	2016-09-06 09:04	27
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Sep  6 08:30 HighlandCapitalManagementRecon201609060730.csv.20160906083042044	8:30	9/6/2016	7:30:00	2016-06-09	8:30:42	0.354653	Tue	2	16	2016-09-06 08:30	27
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       206 Sep  6 01:40 HSBC-LKR.in.06092016-1.20160906014051459	1:40	6/9/2016		2016-06-09	1:40:51	0.070035	Tue	2	17	2016-09-06 01:40	27
John Hancock Investments	HAN_TRANS_HANVER_20160802.csv.20160906153106564	15:31	8/2/2016		2016-06-09	15:31:06	0.646597	Tue	2	18	2016-09-06 15:31	27
John Hancock Investments	HAN_TRANS_HANVER_20160906.csv.20160906153306869	15:33	9/6/2016		2016-06-09	15:33:06	0.647986	Tue	2	18	2016-09-06 15:33	27
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep  6 03:12 INV_fx_20160906_091040.csv.20160906031254001	3:12	9/6/2016	9:10:40	2016-06-09	3:12:54	0.133958	Tue	2	26	2016-09-06 03:12	27
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Sep  6 03:20 FT_fx_20160906_091642.csv.20160906032054563	3:20	9/6/2016	9:16:42	2016-06-09	3:20:54	0.139514	Tue	2	26	2016-09-06 03:20	27
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       295 Sep  6 04:50 FT_fx_20160906_104531.csv.20160906045029078	4:50	9/6/2016	10:45:31	2016-06-09	4:50:29	0.201725	Tue	2	26	2016-09-06 04:50	27
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       230 Sep  6 05:00 INV_fx_20160906_105841.csv.20160906050029638	5:00	9/6/2016	10:58:41	2016-06-09	5:00:29	0.208669	Tue	2	26	2016-09-06 05:00	27
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep  6 05:32 INV_fx_20160906_113116.csv.20160906053231594	5:32	9/6/2016	11:31:16	2016-06-09	5:32:31	0.230914	Tue	2	26	2016-09-06 05:32	27
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24205 Sep  6 11:24 RSWGD1-17_SSGM_Confirmed_File__20160906.csv.20160906112454613	11:24	9/6/2016		2016-06-09	11:24:54	0.475625	Tue	2	30	2016-09-06 11:24	27
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3577 Sep  6 09:38 tcwta20160906.csv.20160906093847650	9:38	9/6/2016		2016-06-09	9:38:47	0.401933	Tue	2	31	2016-09-06 09:38	27
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5864 Sep  6 09:32 TIAACREFREPAT.csv.20160906093246450	9:32			2016-06-09	9:32:46	0.397755	Tue	2	32	2016-09-06 09:32	27
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5620 Sep  6 10:30 TIAACREFREPAT.csv.20160906103049646	10:30			2016-06-09	10:30:49	0.438067	Tue	2	32	2016-09-06 10:30	27
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep  7 08:43 Alger_Orders_20160907084026.csv.20160907084326338	8:43	9/7/2016	8:40:26	2016-07-09	8:43:26	0.363495	Wed	3	1	2016-09-07 08:43	28
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1600 Sep  7 04:32 SSC_BAM_FXREQ_20160907_093004.csv.pgp.ndm05.20160907043212912	4:32	9/7/2016	9:30:04	2016-07-09	4:32:12	0.189028	Wed	3	3	2016-09-07 04:32	28
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1470 Sep  7 05:32 SSC_BAM_FXREQ_20160907_103009.csv.pgp.ndm05.20160907053216092	5:32	9/7/2016	10:30:09	2016-07-09	5:32:16	0.230741	Wed	3	3	2016-09-07 05:32	28
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1470 Sep  7 11:32 SSC_BAM_FXREQ_20160907_163025.csv.pgp.ndm05.20160907113238470	11:32	9/7/2016	16:30:25	2016-07-09	11:32:38	0.480995	Wed	3	3	2016-09-07 11:32	28
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Sep  7 12:33 SSC_BAM_FXREQ_20160907_173027.csv.pgp.ndm05.20160907123312619	12:33	9/7/2016	17:30:27	2016-07-09	12:33:12	0.523056	Wed	3	3	2016-09-07 12:33	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063849649	6:38			2016-07-09	6:38:49	0.276956	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063849797	6:38			2016-07-09	6:38:49	0.276956	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063849979	6:38			2016-07-09	6:38:49	0.276956	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063850183	6:38			2016-07-09	6:38:50	0.276968	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063850368	6:38			2016-07-09	6:38:50	0.276968	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063850590	6:38			2016-07-09	6:38:50	0.276968	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063850806	6:38			2016-07-09	6:38:50	0.276968	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063851017	6:38			2016-07-09	6:38:51	0.276979	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063851219	6:38			2016-07-09	6:38:51	0.276979	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063851436	6:38			2016-07-09	6:38:51	0.276979	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063851645	6:38			2016-07-09	6:38:51	0.276979	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063851855	6:38			2016-07-09	6:38:51	0.276979	Wed	3	4	2016-09-07 06:38	28
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  7 06:38 BCRTOFX.txt.20160907063852061	6:38			2016-07-09	6:38:52	0.276991	Wed	3	4	2016-09-07 06:38	28
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3194 Sep  7 14:39 BRA_BRA_Ver_20160907.csv.20160907143920807	14:39	9/7/2016		2016-07-09	14:39:20	0.610648	Wed	3	5	2016-09-07 14:39	28
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Sep  7 20:33 CDPSfx_TWDorder.20160907.203000.csv.20160907203340100	20:33	9/7/2016	20:30:00	2016-07-09	20:33:40	0.856713	Wed	3	6	2016-09-07 20:33	28
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       433 Sep  7 09:35 SPOT_FET_Instructions_StateStreet_20160907-152829.csv.20160907093500787	9:35	9/7/2016	15:28:29	2016-07-09	9:35:00	0.399306	Wed	3	7	2016-09-07 09:35	28
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep  7 05:39 CRUX_20160907.csv.20160907053916852	5:39	9/7/2016		2016-07-09	5:39:16	0.235602	Wed	3	8	2016-09-07 05:39	28
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  7 17:15 09072016_GAM_GAM_STAR_GS.20160907.csv.20160907171529654	17:15	9/7/2016		2016-07-09	17:15:29	0.719086	Wed	3	9	2016-09-07 17:15	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5638 Sep  7 10:33 trade10.dat.20160907103304215	10:33			2016-07-09	10:33:04	0.43963	Wed	3	10	2016-09-07 10:33	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Sep  7 12:33 trade10.dat.20160907123312984	12:33			2016-07-09	12:33:12	0.523056	Wed	3	10	2016-09-07 12:33	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep  7 14:33 trade10.dat.20160907143320203	14:33			2016-07-09	14:33:20	0.606481	Wed	3	10	2016-09-07 14:33	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Sep  7 16:23 trade10.dat.20160907162325336	16:23			2016-07-09	16:23:25	0.682928	Wed	3	10	2016-09-07 16:23	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  7 17:03 trade10.dat.20160907170328663	17:03			2016-07-09	17:03:28	0.710741	Wed	3	10	2016-09-07 17:03	28
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  7 18:03 trade10.dat.20160907180332935	18:03			2016-07-09	18:03:32	0.752454	Wed	3	10	2016-09-07 18:03	28
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    250990 Sep  7 09:15 passporttrans.20160907.csv.20160907091528192	9:15	9/7/2016		2016-07-09	9:15:28	0.385741	Wed	3	15	2016-09-07 09:15	28
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1647 Sep  7 08:33 HighlandCapitalManagementRecon201609070730.csv.20160907083325756	8:33	9/7/2016	7:30:00	2016-07-09	8:33:25	0.356539	Wed	3	16	2016-09-07 08:33	28
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       480 Sep  7 02:39 HSBC-LKR.in.07092016-1.20160907023907868	2:39	7/9/2016		2016-07-09	2:39:07	0.110498	Wed	3	17	2016-09-07 02:39	28
John Hancock Investments	HAN_TRANS_HANVER_20160907.csv.20160907153922769	15:39	9/7/2016		2016-07-09	15:39:22	0.652338	Wed	3	18	2016-09-07 15:39	28
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Sep  7 05:43 NOS_SFX_20160907.csv.20160907054317181	5:43	9/7/2016		2016-07-09	5:43:17	0.238391	Wed	3	21	2016-09-07 05:43	28
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep  7 03:29 FT_fx_20160907_092457.csv.20160907032909848	3:29	9/7/2016	9:24:57	2016-07-09	3:29:09	0.145243	Wed	3	26	2016-09-07 03:29	28
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Sep  7 04:53 FT_fx_20160907_104757.csv.20160907045313681	4:53	9/7/2016	10:47:57	2016-07-09	4:53:13	0.203623	Wed	3	26	2016-09-07 04:53	28
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Sep  7 05:23 INV_fx_20160907_112154.csv.20160907052315681	5:23	9/7/2016	11:21:54	2016-07-09	5:23:15	0.224479	Wed	3	26	2016-09-07 05:23	28
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep  7 05:37 INV_fx_20160907_113536.csv.20160907053716575	5:37	9/7/2016	11:35:36	2016-07-09	5:37:16	0.234213	Wed	3	26	2016-09-07 05:37	28
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       229 Sep  7 06:19 INV_fx_20160907_121740.csv.20160907061918505	6:19	9/7/2016	12:17:40	2016-07-09	6:19:18	0.263403	Wed	3	26	2016-09-07 06:19	28
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27560 Sep  7 11:11 RSWGD1-17_SSGM_Confirmed_File__20160907.csv.20160907111105961	11:11	9/7/2016		2016-07-09	11:11:05	0.46603	Wed	3	30	2016-09-07 11:11	28
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4223 Sep  7 09:39 tcwta120160907.csv.20160907.093831.20160907093901257	9:39	9/7/2016		2016-07-09	9:39:01	0.402095	Wed	3	31	2016-09-07 09:39	28
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3641 Sep  7 09:41 tcwta220160907.csv.20160907.093840.20160907094101578	9:41	9/7/2016		2016-07-09	9:41:01	0.403484	Wed	3	31	2016-09-07 09:41	28
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      9482 Sep  7 09:31 TIAACREFREPAT.csv.20160907093129855	9:31			2016-07-09	9:31:29	0.396863	Wed	3	32	2016-09-07 09:31	28
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4280 Sep  7 13:31 TIAACREFREPAT.csv.20160907133117149	13:31			2016-07-09	13:31:17	0.563391	Wed	3	32	2016-09-07 13:31	28
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep  8 08:53 Alger_Orders_20160908085042.csv.20160908085344609	8:53	9/8/2016	8:50:42	2016-08-09	8:53:44	0.370648	Thu	4	1	2016-09-08 08:53	29
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1581 Sep  8 04:32 SSC_BAM_FXREQ_20160908_093010.csv.pgp.ndm05.20160908043258069	4:32	9/8/2016	9:30:10	2016-08-09	4:32:58	0.18956	Thu	4	3	2016-09-08 04:32	29
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1528 Sep  8 06:31 SSC_BAM_FXREQ_20160908_113015.csv.pgp.ndm05.20160908063105538	6:31	9/8/2016	11:30:15	2016-08-09	6:31:05	0.271586	Thu	4	3	2016-09-08 06:31	29
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Sep  8 07:33 SSC_BAM_FXREQ_20160908_123018.csv.pgp.ndm05.20160908073310506	7:33	9/8/2016	12:30:18	2016-08-09	7:33:10	0.314699	Thu	4	3	2016-09-08 07:33	29
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep  8 08:31 SSC_BAM_FXREQ_20160908_133020.csv.pgp.ndm05.20160908083142593	8:31	9/8/2016	13:30:20	2016-08-09	8:31:42	0.355347	Thu	4	3	2016-09-08 08:31	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063906113	6:39			2016-08-09	6:39:06	0.277153	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063906423	6:39			2016-08-09	6:39:06	0.277153	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063906624	6:39			2016-08-09	6:39:06	0.277153	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063906829	6:39			2016-08-09	6:39:06	0.277153	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063907038	6:39			2016-08-09	6:39:07	0.277164	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063907248	6:39			2016-08-09	6:39:07	0.277164	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063907474	6:39			2016-08-09	6:39:07	0.277164	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063907700	6:39			2016-08-09	6:39:07	0.277164	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063907881	6:39			2016-08-09	6:39:07	0.277164	Thu	4	4	2016-09-08 06:39	29
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  8 06:39 BCRTOFX.txt.20160908063908093	6:39			2016-08-09	6:39:08	0.277176	Thu	4	4	2016-09-08 06:39	29
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2469 Sep  8 14:45 BRA_BRA_Ver_20160908.csv.20160908144539162	14:45	9/8/2016		2016-08-09	14:45:39	0.615035	Thu	4	5	2016-09-08 14:45	29
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  8 08:33 CDPSfx_BRLorder.20160908.083500.csv.20160908083343304	8:33	9/8/2016	8:35:00	2016-08-09	8:33:43	0.356748	Thu	4	6	2016-09-08 08:33	29
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  8 09:33 CDPSfx_BRLorder.20160908.093500.csv.20160908093349415	9:33	9/8/2016	9:35:00	2016-08-09	9:33:49	0.398484	Thu	4	6	2016-09-08 09:33	29
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  8 10:33 CDPSfx_BRLorder.20160908.103500.csv.20160908103354722	10:33	9/8/2016	10:35:00	2016-08-09	10:33:54	0.440208	Thu	4	6	2016-09-08 10:33	29
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep  8 11:33 CDPSfx_BRLorder.20160908.113500.csv.20160908113357198	11:33	9/8/2016	11:35:00	2016-08-09	11:33:57	0.48191	Thu	4	6	2016-09-08 11:33	29
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       437 Sep  8 09:27 SPOT_FET_Instructions_StateStreet_20160908-150142.csv.20160908092748241	9:27	9/8/2016	15:01:42	2016-08-09	9:27:48	0.394306	Thu	4	7	2016-09-08 09:27	29
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep  8 09:27 CRUX_20160908.csv.20160908092748414	9:27	9/8/2016		2016-08-09	9:27:48	0.394306	Thu	4	8	2016-09-08 09:27	29
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  8 16:39 09082016_GAM_GAM_STAR_GS.20160908.csv.20160908163944538	16:39	9/8/2016		2016-08-09	16:39:44	0.694259	Thu	4	9	2016-09-08 16:39	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  8 10:33 trade10.dat.20160908103354303	10:33			2016-08-09	10:33:54	0.440208	Thu	4	10	2016-09-08 10:33	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Sep  8 12:34 trade10.dat.20160908123401520	12:34			2016-08-09	12:34:01	0.523623	Thu	4	10	2016-09-08 12:34	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      7374 Sep  8 14:33 trade10.dat.20160908143338170	14:33			2016-08-09	14:33:38	0.60669	Thu	4	10	2016-09-08 14:33	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     35584 Sep  8 16:23 trade10.dat.20160908162342852	16:23			2016-08-09	16:23:42	0.683125	Thu	4	10	2016-09-08 16:23	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  8 17:03 trade10.dat.20160908170345392	17:03			2016-08-09	17:03:45	0.710938	Thu	4	10	2016-09-08 17:03	29
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  8 18:03 trade10.dat.20160908180349184	18:03			2016-08-09	18:03:49	0.75265	Thu	4	10	2016-09-08 18:03	29
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    254935 Sep  8 09:07 passporttrans.20160908.csv.20160908090746125	9:07	9/8/2016		2016-08-09	9:07:46	0.380394	Thu	4	15	2016-09-08 09:07	29
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Sep  8 08:31 HighlandCapitalManagementRecon201609080730.csv.20160908083143016	8:31	9/8/2016	7:30:00	2016-08-09	8:31:43	0.355359	Thu	4	16	2016-09-08 08:31	29
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       187 Sep  8 14:39 Highland_Orders_20160908csv.20160908143938749	14:39	9/8/2016		2016-08-09	14:39:38	0.610856	Thu	4	16	2016-09-08 14:39	29
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       391 Sep  8 01:49 HSBC-LKR.in.08092016-1.20160908014921086	1:49	8/9/2016		2016-08-09	1:49:21	0.075938	Thu	4	17	2016-09-08 01:49	29
John Hancock Investments	HAN_TRANS_HANVER_20160908.csv.20160908153140756	15:31	9/8/2016		2016-08-09	15:31:40	0.646991	Thu	4	18	2016-09-08 15:31	29
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep  8 09:53 NOS_SFX_20160908.csv.20160908095351113	9:53	9/8/2016		2016-08-09	9:53:51	0.412396	Thu	4	21	2016-09-08 09:53	29
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep  8 03:21 FT_fx_20160908_091303.csv.20160908032124424	3:21	9/8/2016	9:13:03	2016-08-09	3:21:24	0.139861	Thu	4	26	2016-09-08 03:21	29
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep  8 03:27 INV_fx_20160908_092508.csv.20160908032725240	3:27	9/8/2016	9:25:08	2016-08-09	3:27:25	0.144039	Thu	4	26	2016-09-08 03:27	29
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Sep  8 05:07 FT_fx_20160908_110254.csv.20160908050729640	5:07	9/8/2016	11:02:54	2016-08-09	5:07:29	0.21353	Thu	4	26	2016-09-08 05:07	29
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep  8 05:51 INV_fx_20160908_115009.csv.20160908055131839	5:51	9/8/2016	11:50:09	2016-08-09	5:51:31	0.244109	Thu	4	26	2016-09-08 05:51	29
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        61 Sep  8 04:13 citicnhtrades.in.201609081607.20160908041327399	4:13	9/8/2016	16:07:00	2016-08-09	4:13:27	0.176007	Thu	4	28	2016-09-08 04:13	29
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  8 05:23 citicnhtrades.in.201609081714.20160908052330732	5:23	9/8/2016	17:14:00	2016-08-09	5:23:30	0.224653	Thu	4	28	2016-09-08 05:23	29
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       342 Sep  8 05:23 hsbccnhtrades.in.201609081714.20160908052330930	5:23	9/8/2016	17:14:00	2016-08-09	5:23:30	0.224653	Thu	4	29	2016-09-08 05:23	29
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24119 Sep  8 10:23 RSWGD1-17_SSGM_Confirmed_File__20160908.csv.20160908102353671	10:23	9/8/2016		2016-08-09	10:23:53	0.433252	Thu	4	30	2016-09-08 10:23	29
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3572 Sep  8 09:43 tcwta20160908.csv.20160908094350477	9:43	9/8/2016		2016-08-09	9:43:50	0.40544	Thu	4	31	2016-09-08 09:43	29
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5042 Sep  8 09:37 TIAACREFREPAT.csv.20160908093750079	9:37			2016-08-09	9:37:50	0.401273	Thu	4	32	2016-09-08 09:37	29
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1077 Sep  8 13:32 TIAACREFREPAT.csv.20160908133205083	13:32			2016-08-09	13:32:05	0.563947	Thu	4	32	2016-09-08 13:32	29
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Sep  9 14:02 Alger_Orders_20160909135750.csv.20160909140250914	14:02	9/9/2016	13:57:50	2016-09-09	14:02:50	0.585301	Fri	5	1	2016-09-09 14:02	30
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep  9 05:32 SSC_BAM_FXREQ_20160909_103012.csv.pgp.ndm05.20160909053218244	5:32	9/9/2016	10:30:12	2016-09-09	5:32:18	0.230764	Fri	5	3	2016-09-09 05:32	30
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1443 Sep  9 07:32 SSC_BAM_FXREQ_20160909_123017.csv.pgp.ndm05.20160909073226664	7:32	9/9/2016	12:30:17	2016-09-09	7:32:26	0.31419	Fri	5	3	2016-09-09 07:32	30
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1415 Sep  9 08:32 SSC_BAM_FXREQ_20160909_133019.csv.pgp.ndm05.20160909083229300	8:32	9/9/2016	13:30:19	2016-09-09	8:32:29	0.355891	Fri	5	3	2016-09-09 08:32	30
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep  9 12:33 SSC_BAM_FXREQ_20160909_173032.csv.pgp.ndm05.20160909123315628	12:33	9/9/2016	17:30:32	2016-09-09	12:33:15	0.52309	Fri	5	3	2016-09-09 12:33	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063822043	6:38			2016-09-09	6:38:22	0.276644	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063822227	6:38			2016-09-09	6:38:22	0.276644	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063822432	6:38			2016-09-09	6:38:22	0.276644	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063822651	6:38			2016-09-09	6:38:22	0.276644	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063822873	6:38			2016-09-09	6:38:22	0.276644	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063823060	6:38			2016-09-09	6:38:23	0.276655	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063823271	6:38			2016-09-09	6:38:23	0.276655	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063823475	6:38			2016-09-09	6:38:23	0.276655	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063823694	6:38			2016-09-09	6:38:23	0.276655	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063823859	6:38			2016-09-09	6:38:23	0.276655	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063824061	6:38			2016-09-09	6:38:24	0.276667	Fri	5	4	2016-09-09 06:38	30
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep  9 06:38 BCRTOFX.txt.20160909063824275	6:38			2016-09-09	6:38:24	0.276667	Fri	5	4	2016-09-09 06:38	30
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4214 Sep  9 14:38 BRA_BRA_Ver_20160909.csv.20160909143823826	14:38	9/9/2016		2016-09-09	14:38:23	0.609988	Fri	5	5	2016-09-09 14:38	30
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1010 Sep  9 09:02 SPOT_FET_Instructions_StateStreet_20160909-142740.csv.20160909090230517	9:02	9/9/2016	14:27:40	2016-09-09	9:02:30	0.376736	Fri	5	7	2016-09-09 09:02	30
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       201 Sep  9 08:18 CRUX_20160909.csv.20160909081828032	8:18	9/9/2016		2016-09-09	8:18:28	0.346157	Fri	5	8	2016-09-09 08:18	30
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       133 Sep  9 16:44 09092016_GAM_GAM_STAR_GS.20160909.csv.20160909164429199	16:44	9/9/2016		2016-09-09	16:44:29	0.697558	Fri	5	9	2016-09-09 16:44	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Sep  9 10:34 trade10.dat.20160909103439403	10:34			2016-09-09	10:34:39	0.440729	Fri	5	10	2016-09-09 10:34	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  9 12:34 trade10.dat.20160909123446325	12:34			2016-09-09	12:34:46	0.524144	Fri	5	10	2016-09-09 12:34	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Sep  9 14:34 trade10.dat.20160909143453501	14:34			2016-09-09	14:34:53	0.607558	Fri	5	10	2016-09-09 14:34	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     21696 Sep  9 16:24 trade10.dat.20160909162427623	16:24			2016-09-09	16:24:27	0.683646	Fri	5	10	2016-09-09 16:24	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  9 17:02 trade10.dat.20160909170230012	17:02			2016-09-09	17:02:30	0.710069	Fri	5	10	2016-09-09 17:02	30
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep  9 18:04 trade10.dat.20160909180433619	18:04			2016-09-09	18:04:33	0.75316	Fri	5	10	2016-09-09 18:04	30
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    251500 Sep  9 09:00 passporttrans.20160909.csv.20160909090030007	9:00	9/9/2016		2016-09-09	9:00:30	0.375347	Fri	5	15	2016-09-09 09:00	30
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Sep  9 08:32 HighlandCapitalManagementRecon201609090730.csv.20160909083228891	8:32	9/9/2016	7:30:00	2016-09-09	8:32:28	0.35588	Fri	5	16	2016-09-09 08:32	30
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       384 Sep  9 02:58 HSBC-LKR.in.09092016-1.20160909025839987	2:58	9/9/2016		2016-09-09	2:58:39	0.124063	Fri	5	17	2016-09-09 02:58	30
John Hancock Investments	HAN_TRANS_HANVER_20160909.csv.20160909152625516	15:26	9/9/2016		2016-09-09	15:26:25	0.643345	Fri	5	18	2016-09-09 15:26	30
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       592 Sep  9 13:16 PGI_Orders_20160909121352.csv.20160909131649202	13:16	9/9/2016	12:13:52	2016-09-09	13:16:49	0.553345	Fri	5	24	2016-09-09 13:16	30
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Sep  9 03:24 FT_fx_20160909_091939.csv.20160909032411004	3:24	9/9/2016	9:19:39	2016-09-09	3:24:11	0.141794	Fri	5	26	2016-09-09 03:24	30
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Sep  9 03:28 INV_fx_20160909_091342.csv.20160909032811440	3:28	9/9/2016	9:13:42	2016-09-09	3:28:11	0.144572	Fri	5	26	2016-09-09 03:28	30
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep  9 04:44 INV_fx_20160909_104151.csv.20160909044414654	4:44	9/9/2016	10:41:51	2016-09-09	4:44:14	0.197384	Fri	5	26	2016-09-09 04:44	30
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Sep  9 04:44 FT_fx_20160909_104132.csv.20160909044415041	4:44	9/9/2016	10:41:32	2016-09-09	4:44:15	0.197396	Fri	5	26	2016-09-09 04:44	30
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep  9 04:54 INV_fx_20160909_105156.csv.20160909045415481	4:54	9/9/2016	10:51:56	2016-09-09	4:54:15	0.20434	Fri	5	26	2016-09-09 04:54	30
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep  9 05:30 citicnhtrades.in.201609091723.20160909053017703	5:30	9/9/2016	17:23:00	2016-09-09	5:30:17	0.229363	Fri	5	28	2016-09-09 05:30	30
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       124 Sep  9 05:30 hsbccnhtrades.in.201609091723.20160909053017977	5:30	9/9/2016	17:23:00	2016-09-09	5:30:17	0.229363	Fri	5	29	2016-09-09 05:30	30
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23624 Sep  9 10:20 RSWGD1-17_SSGM_Confirmed_File__20160909.csv.20160909102038150	10:20	9/9/2016		2016-09-09	10:20:38	0.430995	Fri	5	30	2016-09-09 10:20	30
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     13000 Sep  9 09:32 TIAACREFREPAT.csv.20160909093235330	9:32			2016-09-09	9:32:35	0.397627	Fri	5	32	2016-09-09 09:32	30
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep 12 08:57 Alger_Orders_20160912085525.csv.20160912085738787	8:57	9/12/2016	8:55:25	2016-12-09	8:57:38	0.373356	Mon	1	1	2016-09-12 08:57	31
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 12 05:31 SSC_BAM_FXREQ_20160912_103014.csv.pgp.ndm05.20160912053125978	5:31	9/12/2016	10:30:14	2016-12-09	5:31:25	0.23015	Mon	1	3	2016-09-12 05:31	31
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1408 Sep 12 07:33 SSC_BAM_FXREQ_20160912_123021.csv.pgp.ndm05.20160912073334730	7:33	9/12/2016	12:30:21	2016-12-09	7:33:34	0.314977	Mon	1	3	2016-09-12 07:33	31
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1444 Sep 12 10:33 SSC_BAM_FXREQ_20160912_153030.csv.pgp.ndm05.20160912103347550	10:33	9/12/2016	15:30:30	2016-12-09	10:33:47	0.440127	Mon	1	3	2016-09-12 10:33	31
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 12 11:31 SSC_BAM_FXREQ_20160912_163034.csv.pgp.ndm05.20160912113151049	11:31	9/12/2016	16:30:34	2016-12-09	11:31:51	0.480451	Mon	1	3	2016-09-12 11:31	31
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 12 12:32 SSC_BAM_FXREQ_20160912_173036.csv.pgp.ndm05.20160912123226938	12:32	9/12/2016	17:30:36	2016-12-09	12:32:26	0.522523	Mon	1	3	2016-09-12 12:32	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:37 BCRTOFX.txt.20160912063759754	6:37			2016-12-09	6:37:59	0.276377	Mon	1	4	2016-09-12 06:37	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063800147	6:38			2016-12-09	6:38:00	0.276389	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063800367	6:38			2016-12-09	6:38:00	0.276389	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063800538	6:38			2016-12-09	6:38:00	0.276389	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063800735	6:38			2016-12-09	6:38:00	0.276389	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063800973	6:38			2016-12-09	6:38:00	0.276389	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063801135	6:38			2016-12-09	6:38:01	0.2764	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063801365	6:38			2016-12-09	6:38:01	0.2764	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063801564	6:38			2016-12-09	6:38:01	0.2764	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063801730	6:38			2016-12-09	6:38:01	0.2764	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063801938	6:38			2016-12-09	6:38:01	0.2764	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063802113	6:38			2016-12-09	6:38:02	0.276412	Mon	1	4	2016-09-12 06:38	31
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 12 06:38 BCRTOFX.txt.20160912063802315	6:38			2016-12-09	6:38:02	0.276412	Mon	1	4	2016-09-12 06:38	31
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4217 Sep 12 14:42 BRA_BRA_Ver_20160912.csv.20160912144206387	14:42	9/12/2016		2016-12-09	14:42:06	0.612569	Mon	1	5	2016-09-12 14:42	31
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       726 Sep 12 10:03 SPOT_FET_Instructions_StateStreet_20160912-153554.csv.20160912100343812	10:03	9/12/2016	15:35:54	2016-12-09	10:03:43	0.419248	Mon	1	7	2016-09-12 10:03	31
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       180 Sep 12 06:58 CRUX_20160912.csv.20160912065802967	6:58	9/12/2016		2016-12-09	6:58:02	0.290301	Mon	1	8	2016-09-12 06:58	31
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       134 Sep 12 16:30 09122016_GAM_GAM_STAR_GS.20160912.csv.20160912163011831	16:30	9/12/2016		2016-12-09	16:30:11	0.687627	Mon	1	9	2016-09-12 16:30	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      8242 Sep 12 10:33 trade10.dat.20160912103347334	10:33			2016-12-09	10:33:47	0.440127	Mon	1	10	2016-09-12 10:33	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Sep 12 12:33 trade10.dat.20160912123357391	12:33			2016-12-09	12:33:57	0.523576	Mon	1	10	2016-09-12 12:33	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep 12 14:34 trade10.dat.20160912143405696	14:34			2016-12-09	14:34:05	0.607002	Mon	1	10	2016-09-12 14:34	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     16054 Sep 12 16:24 trade10.dat.20160912162410842	16:24			2016-12-09	16:24:10	0.683449	Mon	1	10	2016-09-12 16:24	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 12 17:10 trade10.dat.20160912171014604	17:10			2016-12-09	17:10:14	0.71544	Mon	1	10	2016-09-12 17:10	31
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 12 18:03 trade10.dat.20160912180349258	18:03			2016-12-09	18:03:49	0.75265	Mon	1	10	2016-09-12 18:03	31
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep 12 05:01 UKFCMCurrencyTemplate120916.csv.20160912050154385	5:01			2016-12-09	5:01:54	0.209653	Mon	1	11	2016-09-12 05:01	31
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       182 Sep 12 17:46 FT_Orders_20160912.csv.20160912174617959	17:46	9/12/2016		2016-12-09	17:46:17	0.740475	Mon	1	12	2016-09-12 17:46	31
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    310239 Sep 12 09:53 passporttrans.20160912.csv.20160912095343115	9:53	9/12/2016		2016-12-09	9:53:43	0.412303	Mon	1	15	2016-09-12 09:53	31
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1642 Sep 12 08:31 HighlandCapitalManagementRecon201609120730.csv.20160912083137240	8:31	9/12/2016	7:30:00	2016-12-09	8:31:37	0.355289	Mon	1	16	2016-09-12 08:31	31
John Hancock Investments	HAN_TRANS_HANVER_20160912.csv.20160912153808804	15:38	9/12/2016		2016-12-09	15:38:08	0.651481	Mon	1	18	2016-09-12 15:38	31
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       238 Sep 12 11:55 NOS_SFX_20160912.csv.20160912115553055	11:55	9/12/2016		2016-12-09	11:55:53	0.497141	Mon	1	21	2016-09-12 11:55	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 12 02:57 FT_fx_20160912_085500.csv.20160912025747768	2:57	9/12/2016	8:55:00	2016-12-09	2:57:47	0.123461	Mon	1	26	2016-09-12 02:57	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Sep 12 03:01 FT_fx_20160912_085926.csv.20160912030148095	3:01	9/12/2016	8:59:26	2016-12-09	3:01:48	0.12625	Mon	1	26	2016-09-12 03:01	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Sep 12 03:21 INV_fx_20160912_092033.csv.20160912032149262	3:21	9/12/2016	9:20:33	2016-12-09	3:21:49	0.14015	Mon	1	26	2016-09-12 03:21	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Sep 12 03:43 FT_fx_20160912_094219.csv.20160912034350069	3:43	9/12/2016	9:42:19	2016-12-09	3:43:50	0.15544	Mon	1	26	2016-09-12 03:43	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Sep 12 04:35 FT_fx_20160912_103434.csv.20160912043553486	4:35	9/12/2016	10:34:34	2016-12-09	4:35:53	0.191586	Mon	1	26	2016-09-12 04:35	31
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       229 Sep 12 05:47 INV_fx_20160912_114457.csv.20160912054757279	5:47	9/12/2016	11:44:57	2016-12-09	5:47:57	0.241632	Mon	1	26	2016-09-12 05:47	31
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep 12 04:13 citicnhtrades.in.201609121607.20160912041351693	4:13	9/12/2016	16:07:00	2016-12-09	4:13:51	0.176285	Mon	1	28	2016-09-12 04:13	31
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     25105 Sep 12 11:01 RSWGD1-17_SSGM_Confirmed_File__20160912.csv.20160912110148424	11:01	9/12/2016		2016-12-09	11:01:48	0.459583	Mon	1	30	2016-09-12 11:01	31
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4353 Sep 12 09:37 tcwta20160912.csv.20160912093742304	9:37	9/12/2016		2016-12-09	9:37:42	0.401181	Mon	1	31	2016-09-12 09:37	31
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6645 Sep 12 09:31 TIAACREFREPAT.csv.20160912093141440	9:31			2016-12-09	9:31:41	0.397002	Mon	1	32	2016-09-12 09:31	31
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7418 Sep 12 10:31 TIAACREFREPAT.csv.20160912103146899	10:31			2016-12-09	10:31:46	0.438727	Mon	1	32	2016-09-12 10:31	31
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       346 Sep 12 22:28 tokyofundtrades.in.201609131014.20160912222803028	22:28	9/13/2016	10:14:00	2016-12-09	22:28:03	0.936146	Mon	1	33	2016-09-12 22:28	31
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       297 Sep 12 05:45 TrinityStreetFX_091216.csv.20160912054556900	5:45			2016-12-09	5:45:56	0.240231	Mon	1	34	2016-09-12 05:45	31
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep 13 08:50 Alger_Orders_20160913084733.csv.20160913085034828	8:50	9/13/2016	8:47:33	2016-13-09	8:50:34	0.368449	Tue	2	1	2016-13-9 8:50:34	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1797 Sep 13 04:32 SSC_BAM_FXREQ_20160913_093016.csv.pgp.ndm05.20160913043219854	4:32	9/13/2016	9:30:16	2016-13-09	4:32:19	0.189109	Tue	2	3	2016-13-9 4:32:19	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1489 Sep 13 05:32 SSC_BAM_FXREQ_20160913_103019.csv.pgp.ndm05.20160913053223117	5:32	9/13/2016	10:30:19	2016-13-09	5:32:23	0.230822	Tue	2	3	2016-13-9 5:32:23	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 13 09:32 SSC_BAM_FXREQ_20160913_143036.csv.pgp.ndm05.20160913093239720	9:32	9/13/2016	14:30:36	2016-13-09	9:32:39	0.397674	Tue	2	3	2016-13-9 9:32:39	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 13 10:33 SSC_BAM_FXREQ_20160913_153042.csv.pgp.ndm05.20160913103313187	10:33	9/13/2016	15:30:42	2016-13-09	10:33:13	0.439734	Tue	2	3	2016-13-9 10:33:13	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 13 12:33 SSC_BAM_FXREQ_20160913_173050.csv.pgp.ndm05.20160913123321140	12:33	9/13/2016	17:30:50	2016-13-09	12:33:21	0.52316	Tue	2	3	2016-13-9 12:33:21	32
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 13 13:33 SSC_BAM_FXREQ_20160913_183052.csv.pgp.ndm05.20160913133325184	13:33	9/13/2016	18:30:52	2016-13-09	13:33:25	0.564873	Tue	2	3	2016-13-9 13:33:25	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063827635	6:38			2016-13-09	6:38:27	0.276701	Tue	2	4	2016-13-9 6:38:27	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063828040	6:38			2016-13-09	6:38:28	0.276713	Tue	2	4	2016-13-9 6:38:28	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063828281	6:38			2016-13-09	6:38:28	0.276713	Tue	2	4	2016-13-9 6:38:28	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063828478	6:38			2016-13-09	6:38:28	0.276713	Tue	2	4	2016-13-9 6:38:28	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063828671	6:38			2016-13-09	6:38:28	0.276713	Tue	2	4	2016-13-9 6:38:28	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063828865	6:38			2016-13-09	6:38:28	0.276713	Tue	2	4	2016-13-9 6:38:28	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063829111	6:38			2016-13-09	6:38:29	0.276725	Tue	2	4	2016-13-9 6:38:29	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063829255	6:38			2016-13-09	6:38:29	0.276725	Tue	2	4	2016-13-9 6:38:29	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063829505	6:38			2016-13-09	6:38:29	0.276725	Tue	2	4	2016-13-9 6:38:29	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063829704	6:38			2016-13-09	6:38:29	0.276725	Tue	2	4	2016-13-9 6:38:29	32
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 13 06:38 BCRTOFX.txt.20160913063829929	6:38			2016-13-09	6:38:29	0.276725	Tue	2	4	2016-13-9 6:38:29	32
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4923 Sep 13 14:36 BRA_BRA_Ver_20160913.csv.20160913143630012	14:36	9/13/2016		2016-13-09	14:36:30	0.608681	Tue	2	5	2016-13-9 14:36:30	32
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1147 Sep 13 09:24 SPOT_FET_Instructions_StateStreet_20160913-151212.csv.20160913092408082	9:24	9/13/2016	15:12:12	2016-13-09	9:24:08	0.391759	Tue	2	7	2016-13-9 9:24:08	32
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       178 Sep 13 09:06 CRUX_20160913.csv.20160913090606905	9:06	9/13/2016		2016-13-09	9:06:06	0.379236	Tue	2	8	2016-13-9 9:06:06	32
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 13 16:44 09132016_GAM_GAM_STAR_GS.20160913.csv.20160913164437926	16:44	9/13/2016		2016-13-09	16:44:37	0.69765	Tue	2	9	2016-13-9 16:44:37	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5204 Sep 13 10:34 trade10.dat.20160913103413652	10:34			2016-13-09	10:34:13	0.440428	Tue	2	10	2016-13-9 10:34:13	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 13 12:34 trade10.dat.20160913123421655	12:34			2016-13-09	12:34:21	0.523854	Tue	2	10	2016-13-9 12:34:21	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep 13 14:34 trade10.dat.20160913143429388	14:34			2016-13-09	14:34:29	0.60728	Tue	2	10	2016-13-9 14:34:29	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      8242 Sep 13 16:24 trade10.dat.20160913162435860	16:24			2016-13-09	16:24:35	0.683738	Tue	2	10	2016-13-9 16:24:35	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 13 17:04 trade10.dat.20160913170439603	17:04			2016-13-09	17:04:39	0.711563	Tue	2	10	2016-13-9 17:04:39	32
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 13 18:04 trade10.dat.20160913180444289	18:04			2016-13-09	18:04:44	0.753287	Tue	2	10	2016-13-9 18:04:44	32
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       179 Sep 13 06:50 UKFCMCurrencyTemplate130916.csv.20160913065030433	6:50			2016-13-09	6:50:30	0.285069	Tue	2	11	2016-13-9 6:50:30	32
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    256481 Sep 13 09:04 passporttrans.20160913.csv.20160913090436118	9:04	9/13/2016		2016-13-09	9:04:36	0.378194	Tue	2	15	2016-13-9 9:04:36	32
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       566 Sep 13 02:54 HSBC-LKR.in.13092016-1.20160913025413781	2:54	9/13/2016		2016-13-09	2:54:13	0.120984	Tue	2	17	2016-13-9 2:54:13	32
John Hancock Investments	HAN_TRANS_HANVER_20160913.csv.20160913153432513	15:34	9/13/2016		2016-13-09	15:34:32	0.648981	Tue	2	18	2016-13-9 15:34:32	32
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       434 Sep 13 14:24 PGI_Orders_20160913132322.csv.20160913142428143	14:24	9/13/2016	13:23:22	2016-13-09	14:24:28	0.600324	Tue	2	24	2016-13-9 14:24:28	32
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 13 02:54 FT_fx_20160913_085122.csv.20160913025413487	2:54	9/13/2016	8:51:22	2016-13-09	2:54:13	0.120984	Tue	2	26	2016-13-9 2:54:13	32
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep 13 03:18 FT_fx_20160913_091626.csv.20160913031814677	3:18	9/13/2016	9:16:26	2016-13-09	3:18:14	0.137662	Tue	2	26	2016-13-9 3:18:14	32
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 13 03:24 INV_fx_20160913_092133.csv.20160913032415772	3:24	9/13/2016	9:21:33	2016-13-09	3:24:15	0.14184	Tue	2	26	2016-13-9 3:24:15	32
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 13 04:18 FT_fx_20160913_101639.csv.20160913041818467	4:18	9/13/2016	10:16:39	2016-13-09	4:18:18	0.179375	Tue	2	26	2016-13-9 4:18:18	32
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 13 05:12 INV_fx_20160913_110919.csv.20160913051221845	5:12	9/13/2016	11:09:19	2016-13-09	5:12:21	0.21691	Tue	2	26	2016-13-9 5:12:21	32
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       118 Sep 13 04:18 citicnhtrades.in.201609131609.20160913041818212	4:18	9/13/2016	16:09:00	2016-13-09	4:18:18	0.179375	Tue	2	28	2016-13-9 4:18:18	32
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 13 05:28 citicnhtrades.in.201609131719.20160913052822393	5:28	9/13/2016	17:19:00	2016-13-09	5:28:22	0.228032	Tue	2	28	2016-13-9 5:28:22	32
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep 13 05:28 hsbccnhtrades.in.201609131719.20160913052822851	5:28	9/13/2016	17:19:00	2016-13-09	5:28:22	0.228032	Tue	2	29	2016-13-9 5:28:22	32
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24572 Sep 13 10:10 RSWGD1-17_SSGM_Confirmed_File__20160913.csv.20160913101011993	10:10	9/13/2016		2016-13-09	10:10:11	0.423738	Tue	2	30	2016-13-9 10:10:11	32
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6030 Sep 13 09:32 TIAACREFREPAT.csv.20160913093208551	9:32			2016-13-09	9:32:08	0.397315	Tue	2	32	2016-13-9 9:32:08	32
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       198 Sep 14 08:51 Alger_Orders_20160914084840.csv.20160914085106242	8:51	9/14/2016	8:48:40	2016-14-09	8:51:06	0.368819	Wed	3	1	2016-14-9 8:51:06	33
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 14 04:33 SSC_BAM_FXREQ_20160914_093025.csv.pgp.ndm05.20160914043319994	4:33	9/14/2016	9:30:25	2016-14-09	4:33:19	0.189803	Wed	3	3	2016-14-9 4:33:19	33
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1806 Sep 14 10:33 SSC_BAM_FXREQ_20160914_153042.csv.pgp.ndm05.20160914103346504	10:33	9/14/2016	15:30:42	2016-14-09	10:33:46	0.440116	Wed	3	3	2016-14-9 10:33:46	33
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1940 Sep 14 11:32 SSC_BAM_FXREQ_20160914_163051.csv.pgp.ndm05.20160914113220935	11:32	9/14/2016	16:30:51	2016-14-09	11:32:20	0.480787	Wed	3	3	2016-14-9 11:32:20	33
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1535 Sep 14 12:32 SSC_BAM_FXREQ_20160914_173054.csv.pgp.ndm05.20160914123226183	12:32	9/14/2016	17:30:54	2016-14-09	12:32:26	0.522523	Wed	3	3	2016-14-9 12:32:26	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063858444	6:38			2016-14-09	6:38:58	0.27706	Wed	3	4	2016-14-9 6:38:58	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063858737	6:38			2016-14-09	6:38:58	0.27706	Wed	3	4	2016-14-9 6:38:58	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063858941	6:38			2016-14-09	6:38:58	0.27706	Wed	3	4	2016-14-9 6:38:58	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063859131	6:38			2016-14-09	6:38:59	0.277072	Wed	3	4	2016-14-9 6:38:59	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063859329	6:38			2016-14-09	6:38:59	0.277072	Wed	3	4	2016-14-9 6:38:59	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063859555	6:38			2016-14-09	6:38:59	0.277072	Wed	3	4	2016-14-9 6:38:59	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063859724	6:38			2016-14-09	6:38:59	0.277072	Wed	3	4	2016-14-9 6:38:59	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:38 BCRTOFX.txt.20160914063859910	6:38			2016-14-09	6:38:59	0.277072	Wed	3	4	2016-14-9 6:38:59	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:39 BCRTOFX.txt.20160914063900129	6:39			2016-14-09	6:39:00	0.277083	Wed	3	4	2016-14-9 6:39:00	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:39 BCRTOFX.txt.20160914063900328	6:39			2016-14-09	6:39:00	0.277083	Wed	3	4	2016-14-9 6:39:00	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:39 BCRTOFX.txt.20160914063900527	6:39			2016-14-09	6:39:00	0.277083	Wed	3	4	2016-14-9 6:39:00	33
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 14 06:39 BCRTOFX.txt.20160914063900744	6:39			2016-14-09	6:39:00	0.277083	Wed	3	4	2016-14-9 6:39:00	33
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4906 Sep 14 14:35 BRA_BRA_Ver_20160914.csv.20160914143502962	14:35	9/14/2016		2016-14-09	14:35:02	0.607662	Wed	3	5	2016-14-9 14:35:02	33
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep 14 06:14 scbcnhtrades1.in.201609141804.20160914061456964	6:14	9/14/2016	18:04:00	2016-14-09	6:14:56	0.26037	Wed	3	7	2016-14-9 6:14:56	33
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 14 06:14 scbcnhtrades2.in.201609141804.20160914061457364	6:14	9/14/2016	18:04:00	2016-14-09	6:14:57	0.260382	Wed	3	7	2016-14-9 6:14:57	33
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1155 Sep 14 09:49 SPOT_FET_Instructions_StateStreet_20160914-153617.csv.20160914094911280	9:49	9/14/2016	15:36:17	2016-14-09	9:49:11	0.409155	Wed	3	7	2016-14-9 9:49:11	33
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       178 Sep 14 04:50 CRUX_20160913.csv.20160914045051190	4:50	9/13/2016		2016-14-09	4:50:51	0.201979	Wed	3	8	2016-14-9 4:50:51	33
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       179 Sep 14 09:55 CRUX_20160914.csv.20160914095512019	9:55	9/14/2016		2016-14-09	9:55:12	0.413333	Wed	3	8	2016-14-9 9:55:12	33
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 14 16:25 09142016_GAM_GAM_STAR_GS.20160914.csv.20160914162508671	16:25	9/14/2016		2016-14-09	16:25:08	0.68412	Wed	3	9	2016-14-9 16:25:08	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Sep 14 10:34 trade10.dat.20160914103446983	10:34			2016-14-09	10:34:46	0.44081	Wed	3	10	2016-14-9 10:34:46	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep 14 12:34 trade10.dat.20160914123456425	12:34			2016-14-09	12:34:56	0.524259	Wed	3	10	2016-14-9 12:34:56	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 14 14:33 trade10.dat.20160914143302406	14:33			2016-14-09	14:33:02	0.606273	Wed	3	10	2016-14-9 14:33:02	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 14 16:23 trade10.dat.20160914162307858	16:23			2016-14-09	16:23:07	0.68272	Wed	3	10	2016-14-9 16:23:07	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 14 17:03 trade10.dat.20160914170311330	17:03			2016-14-09	17:03:11	0.710544	Wed	3	10	2016-14-9 17:03:11	33
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 14 18:03 trade10.dat.20160914180315625	18:03			2016-14-09	18:03:15	0.752257	Wed	3	10	2016-14-9 18:03:15	33
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       830 Sep 14 05:40 UKFCMCurrencyTemplate140916.csv.20160914054055444	5:40			2016-14-09	5:40:55	0.236748	Wed	3	11	2016-14-9 5:40:55	33
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    289966 Sep 14 09:11 passporttrans.20160914.csv.20160914091107524	9:11	9/14/2016		2016-14-09	9:11:07	0.38272	Wed	3	15	2016-14-9 9:11:07	33
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       211 Sep 14 08:31 HighlandCapitalManagementRecon201609140730.csv.20160914083105518	8:31	9/14/2016	7:30:00	2016-14-09	8:31:05	0.354919	Wed	3	16	2016-14-9 8:31:05	33
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       390 Sep 14 02:50 HSBC-LKR.in.14092016-1.20160914025044373	2:50	9/14/2016		2016-14-09	2:50:44	0.118565	Wed	3	17	2016-14-9 2:50:44	33
John Hancock Investments	HAN_TRANS_HANVER_20160914.csv.20160914154305217	15:43	9/14/2016		2016-14-09	15:43:05	0.654919	Wed	3	18	2016-14-9 15:43:05	33
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       238 Sep 14 04:38 NOS_SFX_20160913.csv.20160914043850599	4:38	9/13/2016		2016-14-09	4:38:50	0.193634	Wed	3	21	2016-14-9 4:38:50	33
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       141 Sep 14 09:25 PresimaOrders.csv.20160914092509376	9:25			2016-14-09	9:25:09	0.392465	Wed	3	25	2016-14-9 9:25:09	33
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       279 Sep 14 10:15 PresimaOrders.csv.20160914101513963	10:15			2016-14-09	10:15:13	0.427234	Wed	3	25	2016-14-9 10:15:13	33
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Sep 14 02:52 FT_fx_20160914_085104.csv.20160914025244890	2:52	9/14/2016	8:51:04	2016-14-09	2:52:44	0.119954	Wed	3	26	2016-14-9 2:52:44	33
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 14 03:18 INV_fx_20160914_091657.csv.20160914031846120	3:18	9/14/2016	9:16:57	2016-14-09	3:18:46	0.138032	Wed	3	26	2016-14-9 3:18:46	33
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 14 04:16 FT_fx_20160914_101502.csv.20160914041648494	4:16	9/14/2016	10:15:02	2016-14-09	4:16:48	0.178333	Wed	3	26	2016-14-9 4:16:48	33
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 14 04:52 INV_fx_20160914_105033.csv.20160914045251695	4:52	9/14/2016	10:50:33	2016-14-09	4:52:51	0.203368	Wed	3	26	2016-14-9 4:52:51	33
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep 14 04:26 citicnhtrades.in.201609141613.20160914042649358	4:26	9/14/2016	16:13:00	2016-14-09	4:26:49	0.185289	Wed	3	28	2016-14-9 4:26:49	33
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 14 05:30 citicnhtrades.in.201609141722.20160914053054376	5:30	9/14/2016	17:22:00	2016-14-09	5:30:54	0.229792	Wed	3	28	2016-14-9 5:30:54	33
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       423 Sep 14 05:30 hsbccnhtrades.in.201609141722.20160914053054755	5:30	9/14/2016	17:22:00	2016-14-09	5:30:54	0.229792	Wed	3	29	2016-14-9 5:30:54	33
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23644 Sep 14 10:25 RSWGD1-17_SSGM_Confirmed_File__20160914.csv.20160914102515235	10:25	9/14/2016		2016-14-09	10:25:15	0.434201	Wed	3	30	2016-14-9 10:25:15	33
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       174 Sep 14 10:13 tcwgt20160914.csv.20160914.101232.20160914101313692	10:13	9/14/2016		2016-14-09	10:13:13	0.425845	Wed	3	31	2016-14-9 10:13:13	33
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7463 Sep 14 10:31 TIAACREFREPAT.csv.20160914103115685	10:31			2016-14-09	10:31:15	0.438368	Wed	3	32	2016-14-9 10:31:15	33
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       559 Sep 14 15:59 TIAACREFREPAT.csv.20160914155905918	15:59			2016-14-09	15:59:05	0.66603	Wed	3	32	2016-14-9 15:59:05	33
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Sep 15 08:55 Alger_Orders_20160915085219.csv.20160915085534084	8:55	9/15/2016	8:52:19	2016-15-09	8:55:34	0.371921	Thu	4	1	2016-15-9 8:55:34	34
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1544 Sep 15 04:32 SSC_BAM_FXREQ_20160915_093007.csv.pgp.ndm05.20160915043217763	4:32	9/15/2016	9:30:07	2016-15-09	4:32:17	0.189086	Thu	4	3	2016-15-9 4:32:17	34
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 15 05:32 SSC_BAM_FXREQ_20160915_103009.csv.pgp.ndm05.20160915053221377	5:32	9/15/2016	10:30:09	2016-15-09	5:32:21	0.230799	Thu	4	3	2016-15-9 5:32:21	34
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1427 Sep 15 12:33 SSC_BAM_FXREQ_20160915_173029.csv.pgp.ndm05.20160915123320845	12:33	9/15/2016	17:30:29	2016-15-09	12:33:20	0.523148	Thu	4	3	2016-15-9 12:33:20	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063855776	6:38			2016-15-09	6:38:55	0.277025	Thu	4	4	2016-15-9 6:38:55	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063856130	6:38			2016-15-09	6:38:56	0.277037	Thu	4	4	2016-15-9 6:38:56	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063856357	6:38			2016-15-09	6:38:56	0.277037	Thu	4	4	2016-15-9 6:38:56	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063856527	6:38			2016-15-09	6:38:56	0.277037	Thu	4	4	2016-15-9 6:38:56	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063856729	6:38			2016-15-09	6:38:56	0.277037	Thu	4	4	2016-15-9 6:38:56	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063856942	6:38			2016-15-09	6:38:56	0.277037	Thu	4	4	2016-15-9 6:38:56	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063857147	6:38			2016-15-09	6:38:57	0.277049	Thu	4	4	2016-15-9 6:38:57	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063857391	6:38			2016-15-09	6:38:57	0.277049	Thu	4	4	2016-15-9 6:38:57	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063857564	6:38			2016-15-09	6:38:57	0.277049	Thu	4	4	2016-15-9 6:38:57	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063857765	6:38			2016-15-09	6:38:57	0.277049	Thu	4	4	2016-15-9 6:38:57	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063857986	6:38			2016-15-09	6:38:57	0.277049	Thu	4	4	2016-15-9 6:38:57	34
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 15 06:38 BCRTOFX.txt.20160915063858197	6:38			2016-15-09	6:38:58	0.27706	Thu	4	4	2016-15-9 6:38:58	34
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3914 Sep 15 14:35 BRA_BRA_Ver_20160915.csv.20160915143528540	14:35	9/15/2016		2016-15-09	14:35:28	0.607963	Thu	4	5	2016-15-9 14:35:28	34
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1017 Sep 15 10:17 SPOT_FET_Instructions_StateStreet_20160915-154927.csv.20160915101740711	10:17	9/15/2016	15:49:27	2016-15-09	10:17:40	0.428935	Thu	4	7	2016-15-9 10:17:40	34
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 15 16:53 09152016_GAM_GAM_STAR_GS.20160915.csv.20160915165335378	16:53	9/15/2016		2016-15-09	16:53:35	0.703877	Thu	4	9	2016-15-9 16:53:35	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5638 Sep 15 10:33 trade10.dat.20160915103342236	10:33			2016-15-09	10:33:42	0.440069	Thu	4	10	2016-15-9 10:33:42	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Sep 15 12:33 trade10.dat.20160915123351177	12:33			2016-15-09	12:33:51	0.523507	Thu	4	10	2016-15-9 12:33:51	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep 15 14:33 trade10.dat.20160915143327977	14:33			2016-15-09	14:33:27	0.606563	Thu	4	10	2016-15-9 14:33:27	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     18224 Sep 15 16:23 trade10.dat.20160915162332967	16:23			2016-15-09	16:23:32	0.683009	Thu	4	10	2016-15-9 16:23:32	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 15 17:03 trade10.dat.20160915170336426	17:03			2016-15-09	17:03:36	0.710833	Thu	4	10	2016-15-9 17:03:36	34
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 15 18:03 trade10.dat.20160915180341543	18:03			2016-15-09	18:03:41	0.752558	Thu	4	10	2016-15-9 18:03:41	34
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       332 Sep 15 05:39 UKFCMCurrencyTemplate150916.csv.20160915053921965	5:39			2016-15-09	5:39:21	0.23566	Thu	4	11	2016-15-9 5:39:21	34
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    281218 Sep 15 08:59 passporttrans.20160915.csv.20160915085934596	8:59	9/15/2016		2016-15-09	8:59:34	0.374699	Thu	4	15	2016-15-9 8:59:34	34
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1655 Sep 15 08:31 HighlandCapitalManagementRecon201609150730.csv.20160915083133100	8:31	9/15/2016	7:30:00	2016-15-09	8:31:33	0.355243	Thu	4	16	2016-15-9 8:31:33	34
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       482 Sep 15 02:07 HSBC-LKR.in.15092016-1.20160915020707779	2:07	9/15/2016		2016-15-09	2:07:07	0.088275	Thu	4	17	2016-15-9 2:07:07	34
John Hancock Investments	HAN_TRANS_HANVER_20160915.csv.20160915153530710	15:35	9/15/2016		2016-15-09	15:35:30	0.649653	Thu	4	18	2016-15-9 15:35:30	34
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Sep 15 02:51 FT_fx_20160915_084953.csv.20160915025111797	2:51	9/15/2016	8:49:53	2016-15-09	2:51:11	0.118877	Thu	4	26	2016-15-9 2:51:11	34
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Sep 15 03:33 INV_fx_20160915_093223.csv.20160915033315260	3:33	9/15/2016	9:32:23	2016-15-09	3:33:15	0.14809	Thu	4	26	2016-15-9 3:33:15	34
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 15 04:25 FT_fx_20160915_102320.csv.20160915042517226	4:25	9/15/2016	10:23:20	2016-15-09	4:25:17	0.184225	Thu	4	26	2016-15-9 4:25:17	34
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Sep 15 04:41 INV_fx_20160915_104024.csv.20160915044118487	4:41	9/15/2016	10:40:24	2016-15-09	4:41:18	0.195347	Thu	4	26	2016-15-9 4:41:18	34
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep 15 05:15 INV_fx_20160915_111256.csv.20160915051520646	5:15	9/15/2016	11:12:56	2016-15-09	5:15:20	0.218981	Thu	4	26	2016-15-9 5:15:20	34
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23796 Sep 15 10:37 RSWGD1-17_SSGM_Confirmed_File__20160915.csv.20160915103743322	10:37	9/15/2016		2016-15-09	10:37:43	0.442859	Thu	4	30	2016-15-9 10:37:43	34
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      3626 Sep 15 09:59 tcwta20160915.csv.20160915.095641.20160915095938937	9:59	9/15/2016		2016-15-09	9:59:38	0.416412	Thu	4	31	2016-15-9 9:59:38	34
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     25570 Sep 15 09:31 TIAACREFREPAT.csv.20160915093137293	9:31			2016-15-09	9:31:37	0.396956	Thu	4	32	2016-15-9 9:31:37	34
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr       792 Sep 15 00:45 tokyofundtrades.in.201609151235.20160915004534471	0:45	9/15/2016	12:35:00	2016-15-09	0:45:34	0.031644	Thu	4	33	2016-15-9 0:45:34	34
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 15 10:23 TrinityStreetFX_091516.csv.20160915102341657	10:23			2016-15-09	10:23:41	0.433113	Thu	4	34	2016-15-9 10:23:41	34
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Sep 16 04:31 SSC_BAM_FXREQ_20160916_093002.csv.pgp.ndm05.20160916043121043	4:31	9/16/2016	9:30:02	2016-16-09	4:31:21	0.188438	Fri	5	3	2016-16-9 4:31:21	35
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 16 07:31 SSC_BAM_FXREQ_20160916_123010.csv.pgp.ndm05.20160916073135871	7:31	9/16/2016	12:30:10	2016-16-09	7:31:35	0.3136	Fri	5	3	2016-16-9 7:31:35	35
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 16 12:32 SSC_BAM_FXREQ_20160916_173025.csv.pgp.ndm05.20160916123227205	12:32	9/16/2016	17:30:25	2016-16-09	12:32:27	0.522535	Fri	5	3	2016-16-9 12:32:27	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063900426	6:39			2016-16-09	6:39:00	0.277083	Fri	5	4	2016-16-9 6:39:00	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063900712	6:39			2016-16-09	6:39:00	0.277083	Fri	5	4	2016-16-9 6:39:00	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063900926	6:39			2016-16-09	6:39:00	0.277083	Fri	5	4	2016-16-9 6:39:00	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063901159	6:39			2016-16-09	6:39:01	0.277095	Fri	5	4	2016-16-9 6:39:01	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063901384	6:39			2016-16-09	6:39:01	0.277095	Fri	5	4	2016-16-9 6:39:01	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063901570	6:39			2016-16-09	6:39:01	0.277095	Fri	5	4	2016-16-9 6:39:01	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063901815	6:39			2016-16-09	6:39:01	0.277095	Fri	5	4	2016-16-9 6:39:01	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063901961	6:39			2016-16-09	6:39:01	0.277095	Fri	5	4	2016-16-9 6:39:01	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063902169	6:39			2016-16-09	6:39:02	0.277106	Fri	5	4	2016-16-9 6:39:02	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063902427	6:39			2016-16-09	6:39:02	0.277106	Fri	5	4	2016-16-9 6:39:02	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063903074	6:39			2016-16-09	6:39:03	0.277118	Fri	5	4	2016-16-9 6:39:03	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063903391	6:39			2016-16-09	6:39:03	0.277118	Fri	5	4	2016-16-9 6:39:03	35
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 16 06:39 BCRTOFX.txt.20160916063903581	6:39			2016-16-09	6:39:03	0.277118	Fri	5	4	2016-16-9 6:39:03	35
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      4048 Sep 16 14:36 BRA_BRA_Ver_20160916.csv.20160916143606599	14:36	9/16/2016		2016-16-09	14:36:06	0.608403	Fri	5	5	2016-16-9 14:36:06	35
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1018 Sep 16 09:12 SPOT_FET_Instructions_StateStreet_20160916-145819.csv.20160916091211176	9:12	9/16/2016	14:58:19	2016-16-09	9:12:11	0.383461	Fri	5	7	2016-16-9 9:12:11	35
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 16 16:30 09162016_GAM_GAM_STAR_GS.20160916.csv.20160916163012085	16:30	9/16/2016		2016-16-09	16:30:12	0.687639	Fri	5	9	2016-16-9 16:30:12	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 16 10:34 trade10.dat.20160916103417698	10:34			2016-16-09	10:34:17	0.440475	Fri	5	10	2016-16-9 10:34:17	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Sep 16 12:34 trade10.dat.20160916123427593	12:34			2016-16-09	12:34:27	0.523924	Fri	5	10	2016-16-9 12:34:27	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Sep 16 14:36 trade10.dat.20160916143606387	14:36			2016-16-09	14:36:06	0.608403	Fri	5	10	2016-16-9 14:36:06	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     14318 Sep 16 16:24 trade10.dat.20160916162411097	16:24			2016-16-09	16:24:11	0.683461	Fri	5	10	2016-16-9 16:24:11	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 16 17:04 trade10.dat.20160916170415071	17:04			2016-16-09	17:04:15	0.711285	Fri	5	10	2016-16-9 17:04:15	35
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 16 18:04 trade10.dat.20160916180422314	18:04			2016-16-09	18:04:22	0.753032	Fri	5	10	2016-16-9 18:04:22	35
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       182 Sep 16 05:11 UKFCMCurrencyTemplate160916.csv.20160916051154545	5:11			2016-16-09	5:11:54	0.216597	Fri	5	11	2016-16-9 5:11:54	35
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       335 Sep 16 07:12 UKFCMCurrencyTemplate160916a.csv.20160916071204655	7:12			2016-16-09	7:12:04	0.300046	Fri	5	11	2016-16-9 7:12:04	35
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       184 Sep 16 18:02 FT_Orders_20160916.csv.20160916180221619	18:02	9/16/2016		2016-16-09	18:02:21	0.751632	Fri	5	12	2016-16-9 18:02:21	35
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    275043 Sep 16 09:20 passporttrans.20160916.csv.20160916092012142	9:20	9/16/2016		2016-16-09	9:20:12	0.389028	Fri	5	15	2016-16-9 9:20:12	35
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1832 Sep 16 08:32 HighlandCapitalManagementRecon201609160730.csv.20160916083208409	8:32	9/16/2016	7:30:00	2016-16-09	8:32:08	0.355648	Fri	5	16	2016-16-9 8:32:08	35
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       188 Sep 16 11:04 Highland_Orders_20160916csv.20160916110420067	11:04	9/16/2016		2016-16-09	11:04:20	0.461343	Fri	5	16	2016-16-9 11:04:20	35
John Hancock Investments	HAN_TRANS_HANVER_20160916.csv.20160916154009114	15:40	9/16/2016		2016-16-09	15:40:09	0.652882	Fri	5	18	2016-16-9 15:40:09	35
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       661 Sep 16 12:42 PGI_Orders_20160916114032.csv.20160916124228298	12:42	9/16/2016	11:40:32	2016-16-09	12:42:28	0.529491	Fri	5	24	2016-16-9 12:42:28	35
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       205 Sep 16 12:50 PGI_Orders_20160916114846.csv.20160916125029097	12:50	9/16/2016	11:48:46	2016-16-09	12:50:29	0.535058	Fri	5	24	2016-16-9 12:50:29	35
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 16 03:01 FT_fx_20160916_090108.csv.20160916030146031	3:01	9/16/2016	9:01:08	2016-16-09	3:01:46	0.126227	Fri	5	26	2016-16-9 3:01:46	35
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep 16 03:15 INV_fx_20160916_091440.csv.20160916031547261	3:15	9/16/2016	9:14:40	2016-16-09	3:15:47	0.135961	Fri	5	26	2016-16-9 3:15:47	35
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 16 04:11 FT_fx_20160916_100907.csv.20160916041149503	4:11	9/16/2016	10:09:07	2016-16-09	4:11:49	0.174873	Fri	5	26	2016-16-9 4:11:49	35
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     25507 Sep 16 10:54 RSWGD1-17_SSGM_Confirmed_File__20160916.csv.20160916105419426	10:54	9/16/2016		2016-16-09	10:54:19	0.454387	Fri	5	30	2016-16-9 10:54:19	35
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4525 Sep 16 10:14 tcwta20160916.csv.20160916.101313.20160916101416719	10:14	9/16/2016		2016-16-09	10:14:16	0.426574	Fri	5	31	2016-16-9 10:14:16	35
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8770 Sep 16 09:32 TIAACREFREPAT.csv.20160916093213564	9:32			2016-16-09	9:32:13	0.397373	Fri	5	32	2016-16-9 9:32:13	35
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       332 Sep 18 20:33 CDPSfx_TWDorder.20160918.203000.csv.20160918203335407	20:33	9/18/2016	20:30:00	2016-18-09	20:33:35	0.856655	Sun	7	6	2016-18-9 20:33:35	#N/A
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Sep 19 10:46 Alger_Orders_20160919104243.csv.20160919104619240	10:46	9/19/2016	10:42:43	2016-19-09	10:46:19	0.448831	Mon	1	1	2016-19-9 10:46:19	36
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 19 04:32 SSC_BAM_FXREQ_20160919_093003.csv.pgp.ndm05.20160919043223965	4:32	9/19/2016	9:30:03	2016-19-09	4:32:23	0.189155	Mon	1	3	2016-19-9 4:32:23	36
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 19 05:32 SSC_BAM_FXREQ_20160919_103007.csv.pgp.ndm05.20160919053227609	5:32	9/19/2016	10:30:07	2016-19-09	5:32:27	0.230868	Mon	1	3	2016-19-9 5:32:27	36
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Sep 19 07:32 SSC_BAM_FXREQ_20160919_123012.csv.pgp.ndm05.20160919073237484	7:32	9/19/2016	12:30:12	2016-19-09	7:32:37	0.314317	Mon	1	3	2016-19-9 7:32:37	36
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Sep 19 11:32 SSC_BAM_FXREQ_20160919_163023.csv.pgp.ndm05.20160919113253002	11:32	9/19/2016	16:30:23	2016-19-09	11:32:53	0.481169	Mon	1	3	2016-19-9 11:32:53	36
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1450 Sep 19 12:33 SSC_BAM_FXREQ_20160919_173025.csv.pgp.ndm05.20160919123326458	12:33	9/19/2016	17:30:25	2016-19-09	12:33:26	0.523218	Mon	1	3	2016-19-9 12:33:26	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063833386	6:38			2016-19-09	6:38:33	0.276771	Mon	1	4	2016-19-9 6:38:33	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063833676	6:38			2016-19-09	6:38:33	0.276771	Mon	1	4	2016-19-9 6:38:33	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063833880	6:38			2016-19-09	6:38:33	0.276771	Mon	1	4	2016-19-9 6:38:33	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063834076	6:38			2016-19-09	6:38:34	0.276782	Mon	1	4	2016-19-9 6:38:34	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063834268	6:38			2016-19-09	6:38:34	0.276782	Mon	1	4	2016-19-9 6:38:34	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063834482	6:38			2016-19-09	6:38:34	0.276782	Mon	1	4	2016-19-9 6:38:34	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063834676	6:38			2016-19-09	6:38:34	0.276782	Mon	1	4	2016-19-9 6:38:34	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063834880	6:38			2016-19-09	6:38:34	0.276782	Mon	1	4	2016-19-9 6:38:34	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063835088	6:38			2016-19-09	6:38:35	0.276794	Mon	1	4	2016-19-9 6:38:35	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063835290	6:38			2016-19-09	6:38:35	0.276794	Mon	1	4	2016-19-9 6:38:35	36
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 19 06:38 BCRTOFX.txt.20160919063835489	6:38			2016-19-09	6:38:35	0.276794	Mon	1	4	2016-19-9 6:38:35	36
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2429 Sep 19 14:58 BRA_BRA_Ver_20160919.csv.20160919145805069	14:58	9/19/2016		2016-19-09	14:58:05	0.623669	Mon	1	5	2016-19-9 14:58:05	36
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep 19 06:18 scbcnhtrades1.in.201609191801.20160919061802287	6:18	9/19/2016	18:01:00	2016-19-09	6:18:02	0.262523	Mon	1	7	2016-19-9 6:18:02	36
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 19 06:18 scbcnhtrades2.in.201609191801.20160919061802529	6:18	9/19/2016	18:01:00	2016-19-09	6:18:02	0.262523	Mon	1	7	2016-19-9 6:18:02	36
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr     11251 Sep 19 09:36 SPOT_FET_Instructions_StateStreet_20160919-140000.csv.20160919093613940	9:36	9/19/2016	14:00:00	2016-19-09	9:36:13	0.40015	Mon	1	7	2016-19-9 9:36:13	36
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       719 Sep 19 09:58 SPOT_FET_Instructions_StateStreet_20160919-154923.csv.20160919095814959	9:58	9/19/2016	15:49:23	2016-19-09	9:58:14	0.41544	Mon	1	7	2016-19-9 9:58:14	36
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       293 Sep 19 12:11 CRUX_20160919.csv.20160919121154813	12:11	9/19/2016		2016-19-09	12:11:54	0.508264	Mon	1	8	2016-19-9 12:11:54	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Sep 19 10:34 trade10.dat.20160919103418726	10:34			2016-19-09	10:34:18	0.440486	Mon	1	10	2016-19-9 10:34:18	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Sep 19 12:33 trade10.dat.20160919123356909	12:33			2016-19-09	12:33:56	0.523565	Mon	1	10	2016-19-9 12:33:56	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Sep 19 14:34 trade10.dat.20160919143404082	14:34			2016-19-09	14:34:04	0.606991	Mon	1	10	2016-19-9 14:34:04	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 19 16:24 trade10.dat.20160919162409626	16:24			2016-19-09	16:24:09	0.683438	Mon	1	10	2016-19-9 16:24:09	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 19 17:04 trade10.dat.20160919170413662	17:04			2016-19-09	17:04:13	0.711262	Mon	1	10	2016-19-9 17:04:13	36
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 19 18:04 trade10.dat.20160919180418669	18:04			2016-19-09	18:04:18	0.752986	Mon	1	10	2016-19-9 18:04:18	36
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       250 Sep 19 17:58 FT_Orders_20160919.csv.20160919175817869	17:58	9/19/2016		2016-19-09	17:58:17	0.748808	Mon	1	12	2016-19-9 17:58:17	36
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    251753 Sep 19 09:00 passporttrans.20160919.csv.20160919090010107	9:00	9/19/2016		2016-19-09	9:00:10	0.375116	Mon	1	15	2016-19-9 9:00:10	36
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1646 Sep 19 08:32 HighlandCapitalManagementRecon201609190730.csv.20160919083209210	8:32	9/19/2016	7:30:00	2016-19-09	8:32:09	0.35566	Mon	1	16	2016-19-9 8:32:09	36
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       481 Sep 19 02:19 HSBC-LKR.in.19092016-1.20160919021947940	2:19	9/19/2016		2016-19-09	2:19:47	0.097072	Mon	1	17	2016-19-9 2:19:47	36
John Hancock Investments	HAN_TRANS_HANVER_20160919.csv.20160919155407547	15:54	9/19/2016		2016-19-09	15:54:07	0.662581	Mon	1	18	2016-19-9 15:54:07	36
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep 19 03:41 INV_fx_20160919_092332.csv.20160919034151592	3:41	9/19/2016	9:23:32	2016-19-09	3:41:51	0.154063	Mon	1	26	2016-19-9 3:41:51	36
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Sep 19 03:43 FT_fx_20160919_092251.csv.20160919034351992	3:43	9/19/2016	9:22:51	2016-19-09	3:43:51	0.155451	Mon	1	26	2016-19-9 3:43:51	36
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Sep 19 04:59 FT_fx_20160919_105554.csv.20160919045954873	4:59	9/19/2016	10:55:54	2016-19-09	4:59:54	0.208264	Mon	1	26	2016-19-9 4:59:54	36
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Sep 19 05:35 INV_fx_20160919_113417.csv.20160919053558146	5:35	9/19/2016	11:34:17	2016-19-09	5:35:58	0.23331	Mon	1	26	2016-19-9 5:35:58	36
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       121 Sep 19 04:13 citicnhtrades.in.201609191607.20160919041352980	4:13	9/19/2016	16:07:00	2016-19-09	4:13:52	0.176296	Mon	1	28	2016-19-9 4:13:52	36
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 19 05:21 citicnhtrades.in.201609191713.20160919052156726	5:21	9/19/2016	17:13:00	2016-19-09	5:21:56	0.223565	Mon	1	28	2016-19-9 5:21:56	36
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       431 Sep 19 05:21 hsbccnhtrades.in.201609191713.20160919052157078	5:21	9/19/2016	17:13:00	2016-19-09	5:21:57	0.223576	Mon	1	29	2016-19-9 5:21:57	36
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23137 Sep 19 11:02 RSWGD1-17_SSGM_Confirmed_File__20160919.csv.20160919110220367	11:02	9/19/2016		2016-19-09	11:02:20	0.459954	Mon	1	30	2016-19-9 11:02:20	36
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4226 Sep 19 09:32 TIAACREFREPAT.csv.20160919093213085	9:32			2016-19-09	9:32:13	0.397373	Mon	1	32	2016-19-9 9:32:13	36
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     11871 Sep 19 10:32 TIAACREFREPAT.csv.20160919103217455	10:32			2016-19-09	10:32:17	0.439086	Mon	1	32	2016-19-9 10:32:17	36
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       338 Sep 19 13:32 TIAACREFREPAT.csv.20160919133200595	13:32			2016-19-09	13:32:00	0.563889	Mon	1	32	2016-19-9 13:32:00	36
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Sep 20 10:10 Alger_Orders_20160920100523.csv.20160920101048253	10:10	9/20/2016	10:05:23	2016-20-09	10:10:48	0.424167	Tue	2	1	2016-20-9 10:10:48	37
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1603 Sep 20 04:31 SSC_BAM_FXREQ_20160920_093004.csv.pgp.ndm05.20160920043123091	4:31	9/20/2016	9:30:04	2016-20-09	4:31:23	0.188461	Tue	2	3	2016-20-9 4:31:23	37
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Sep 20 06:33 SSC_BAM_FXREQ_20160920_113009.csv.pgp.ndm05.20160920063334040	6:33	9/20/2016	11:30:09	2016-20-09	6:33:34	0.27331	Tue	2	3	2016-20-9 6:33:34	37
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 20 11:31 SSC_BAM_FXREQ_20160920_163025.csv.pgp.ndm05.20160920113154697	11:31	9/20/2016	16:30:25	2016-20-09	11:31:54	0.480486	Tue	2	3	2016-20-9 11:31:54	37
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Sep 20 12:32 SSC_BAM_FXREQ_20160920_173027.csv.pgp.ndm05.20160920123229795	12:32	9/20/2016	17:30:27	2016-20-09	12:32:29	0.522558	Tue	2	3	2016-20-9 12:32:29	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063834533	6:38			2016-20-09	6:38:34	0.276782	Tue	2	4	2016-20-9 6:38:34	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063834828	6:38			2016-20-09	6:38:34	0.276782	Tue	2	4	2016-20-9 6:38:34	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063835005	6:38			2016-20-09	6:38:35	0.276794	Tue	2	4	2016-20-9 6:38:35	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063835202	6:38			2016-20-09	6:38:35	0.276794	Tue	2	4	2016-20-9 6:38:35	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063835398	6:38			2016-20-09	6:38:35	0.276794	Tue	2	4	2016-20-9 6:38:35	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063835594	6:38			2016-20-09	6:38:35	0.276794	Tue	2	4	2016-20-9 6:38:35	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063835803	6:38			2016-20-09	6:38:35	0.276794	Tue	2	4	2016-20-9 6:38:35	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063836010	6:38			2016-20-09	6:38:36	0.276806	Tue	2	4	2016-20-9 6:38:36	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063836216	6:38			2016-20-09	6:38:36	0.276806	Tue	2	4	2016-20-9 6:38:36	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063836453	6:38			2016-20-09	6:38:36	0.276806	Tue	2	4	2016-20-9 6:38:36	37
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 20 06:38 BCRTOFX.txt.20160920063836678	6:38			2016-20-09	6:38:36	0.276806	Tue	2	4	2016-20-9 6:38:36	37
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3895 Sep 20 14:38 BRA_BRA_Ver_20160920.csv.20160920143838079	14:38	9/20/2016		2016-20-09	14:38:38	0.610162	Tue	2	5	2016-20-9 14:38:38	37
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep 20 20:32 CDPSfx_TWDorder.20160920.203000.csv.20160920203259630	20:32	9/20/2016	20:30:00	2016-20-09	20:32:59	0.856238	Tue	2	6	2016-20-9 20:32:59	37
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       717 Sep 20 09:48 SPOT_FET_Instructions_StateStreet_20160920-153927.csv.20160920094846267	9:48	9/20/2016	15:39:27	2016-20-09	9:48:46	0.408866	Tue	2	7	2016-20-9 9:48:46	37
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 20 16:40 09202016_GAM_GAM_STAR_GS.20160920.csv.20160920164045734	16:40	9/20/2016		2016-20-09	16:40:45	0.694965	Tue	2	9	2016-20-9 16:40:45	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep 20 10:34 trade10.dat.20160920103450743	10:34			2016-20-09	10:34:50	0.440856	Tue	2	10	2016-20-9 10:34:50	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Sep 20 12:35 trade10.dat.20160920123500306	12:35			2016-20-09	12:35:00	0.524306	Tue	2	10	2016-20-9 12:35:00	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep 20 14:34 trade10.dat.20160920143437378	14:34			2016-20-09	14:34:37	0.607373	Tue	2	10	2016-20-9 14:34:37	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Sep 20 16:22 trade10.dat.20160920162243223	16:22			2016-20-09	16:22:43	0.682442	Tue	2	10	2016-20-9 16:22:43	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 20 17:02 trade10.dat.20160920170246885	17:02			2016-20-09	17:02:46	0.710255	Tue	2	10	2016-20-9 17:02:46	37
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 20 18:02 trade10.dat.20160920180250895	18:02			2016-20-09	18:02:50	0.751968	Tue	2	10	2016-20-9 18:02:50	37
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    280298 Sep 20 08:58 passporttrans.20160920.csv.20160920085842483	8:58	9/20/2016		2016-20-09	8:58:42	0.374097	Tue	2	15	2016-20-9 8:58:42	37
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1646 Sep 20 08:32 HighlandCapitalManagementRecon201609200730.csv.20160920083240390	8:32	9/20/2016	7:30:00	2016-20-09	8:32:40	0.356019	Tue	2	16	2016-20-9 8:32:40	37
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       252 Sep 20 11:10 Highland_Orders_20160920csv.20160920111052606	11:10	9/20/2016		2016-20-09	11:10:52	0.46588	Tue	2	16	2016-20-9 11:10:52	37
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       390 Sep 20 01:28 HSBC-LKR.in.20092016-1.20160920012841015	1:28	9/20/2016		2016-20-09	1:28:41	0.061586	Tue	2	17	2016-20-9 1:28:41	37
John Hancock Investments	HAN_TRANS_HANVER_20160920.csv.20160920153440199	15:34	9/20/2016		2016-20-09	15:34:40	0.649074	Tue	2	18	2016-20-9 15:34:40	37
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       146 Sep 20 11:04 PresimaOrders.csv.20160920110451849	11:04			2016-20-09	11:04:51	0.461701	Tue	2	25	2016-20-9 11:04:51	37
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Sep 20 03:16 INV_fx_20160920_091455.csv.20160920031617584	3:16	9/20/2016	9:14:55	2016-20-09	3:16:17	0.136308	Tue	2	26	2016-20-9 3:16:17	37
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 20 03:40 FT_fx_20160920_093141.csv.20160920034020055	3:40	9/20/2016	9:31:41	2016-20-09	3:40:20	0.153009	Tue	2	26	2016-20-9 3:40:20	37
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 20 05:00 FT_fx_20160920_105538.csv.20160920050024327	5:00	9/20/2016	10:55:38	2016-20-09	5:00:24	0.208611	Tue	2	26	2016-20-9 5:00:24	37
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep 20 05:56 INV_fx_20160920_115426.csv.20160920055627278	5:56	9/20/2016	11:54:26	2016-20-09	5:56:27	0.247535	Tue	2	26	2016-20-9 5:56:27	37
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       123 Sep 20 04:18 citicnhtrades.in.201609201609.20160920041821846	4:18	9/20/2016	16:09:00	2016-20-09	4:18:21	0.17941	Tue	2	28	2016-20-9 4:18:21	37
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     26802 Sep 20 10:28 RSWGD1-17_SSGM_Confirmed_File__20160920.csv.20160920102849431	10:28	9/20/2016		2016-20-09	10:28:49	0.436678	Tue	2	30	2016-20-9 10:28:49	37
TCW	-rw-r--r--   1 ftpgmrin ftpgmr      4430 Sep 20 09:40 tcwta20160920.csv.20160920094045732	9:40	9/20/2016		2016-20-09	9:40:45	0.403299	Tue	2	31	2016-20-9 9:40:45	37
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6119 Sep 20 09:32 TIAACREFREPAT.csv.20160920093245024	9:32			2016-20-09	9:32:45	0.397743	Tue	2	32	2016-20-9 9:32:45	37
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5026 Sep 20 10:32 TIAACREFREPAT.csv.20160920103250138	10:32			2016-20-09	10:32:50	0.439468	Tue	2	32	2016-20-9 10:32:50	37
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       469 Sep 20 13:30 TIAACREFREPAT.csv.20160920133033665	13:30			2016-20-09	13:30:33	0.562882	Tue	2	32	2016-20-9 13:30:33	37
Tokyo Funds	-rw-r--r--   1 ftpgmrin ftpgmr      1566 Sep 20 21:43 tokyofundtrades.in.201609210910.20160920214303067	21:43	9/21/2016	9:10:00	2016-20-09	21:43:03	0.904896	Tue	2	33	2016-20-9 21:43:03	37
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       192 Sep 21 09:39 Alger_Orders_20160921093717.csv.20160921093918036	9:39	9/21/2016	9:37:17	2016-21-09	9:39:18	0.402292	Wed	3	1	2016-21-9 9:39:18	38
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Sep 21 11:05 Alger_Orders_20160921110153.csv.20160921110522954	11:05	9/21/2016	11:01:53	2016-21-09	11:05:22	0.46206	Wed	3	1	2016-21-9 11:05:22	38
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1473 Sep 21 04:32 SSC_BAM_FXREQ_20160921_093004.csv.pgp.ndm05.20160921043227811	4:32	9/21/2016	9:30:04	2016-21-09	4:32:27	0.189201	Wed	3	3	2016-21-9 4:32:27	38
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 21 06:32 SSC_BAM_FXREQ_20160921_113010.csv.pgp.ndm05.20160921063234563	6:32	9/21/2016	11:30:10	2016-21-09	6:32:34	0.272616	Wed	3	3	2016-21-9 6:32:34	38
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1408 Sep 21 11:32 SSC_BAM_FXREQ_20160921_163022.csv.pgp.ndm05.20160921113255474	11:32	9/21/2016	16:30:22	2016-21-09	11:32:55	0.481192	Wed	3	3	2016-21-9 11:32:55	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063905031	6:39			2016-21-09	6:39:05	0.277141	Wed	3	4	2016-21-9 6:39:05	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063905348	6:39			2016-21-09	6:39:05	0.277141	Wed	3	4	2016-21-9 6:39:05	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063905558	6:39			2016-21-09	6:39:05	0.277141	Wed	3	4	2016-21-9 6:39:05	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063905746	6:39			2016-21-09	6:39:05	0.277141	Wed	3	4	2016-21-9 6:39:05	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063905952	6:39			2016-21-09	6:39:05	0.277141	Wed	3	4	2016-21-9 6:39:05	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063906169	6:39			2016-21-09	6:39:06	0.277153	Wed	3	4	2016-21-9 6:39:06	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063906376	6:39			2016-21-09	6:39:06	0.277153	Wed	3	4	2016-21-9 6:39:06	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063906573	6:39			2016-21-09	6:39:06	0.277153	Wed	3	4	2016-21-9 6:39:06	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063906789	6:39			2016-21-09	6:39:06	0.277153	Wed	3	4	2016-21-9 6:39:06	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063906989	6:39			2016-21-09	6:39:06	0.277153	Wed	3	4	2016-21-9 6:39:06	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063907189	6:39			2016-21-09	6:39:07	0.277164	Wed	3	4	2016-21-9 6:39:07	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063907397	6:39			2016-21-09	6:39:07	0.277164	Wed	3	4	2016-21-9 6:39:07	38
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 21 06:39 BCRTOFX.txt.20160921063907618	6:39			2016-21-09	6:39:07	0.277164	Wed	3	4	2016-21-9 6:39:07	38
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3244 Sep 21 14:41 BRA_BRA_Ver_20160921.csv.20160921144137808	14:41	9/21/2016		2016-21-09	14:41:37	0.612234	Wed	3	5	2016-21-9 14:41:37	38
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       492 Sep 21 05:27 scbcnhtrades1.in.201609211716.20160921052701289	5:27	9/21/2016	17:16:00	2016-21-09	5:27:01	0.227095	Wed	3	7	2016-21-9 5:27:01	38
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 21 05:27 scbcnhtrades2.in.201609211716.20160921052701576	5:27	9/21/2016	17:16:00	2016-21-09	5:27:01	0.227095	Wed	3	7	2016-21-9 5:27:01	38
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       580 Sep 21 09:25 SPOT_FET_Instructions_StateStreet_20160921-151247.csv.20160921092516458	9:25	9/21/2016	15:12:47	2016-21-09	9:25:16	0.392546	Wed	3	7	2016-21-9 9:25:16	38
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       121 Sep 21 16:51 09212016_GAM_GAM_STAR_GS.20160921.csv.20160921165114912	16:51	9/21/2016		2016-21-09	16:51:14	0.702245	Wed	3	9	2016-21-9 16:51:14	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Sep 21 10:33 trade10.dat.20160921103321139	10:33			2016-21-09	10:33:21	0.439826	Wed	3	10	2016-21-9 10:33:21	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Sep 21 12:33 trade10.dat.20160921123330478	12:33			2016-21-09	12:33:30	0.523264	Wed	3	10	2016-21-9 12:33:30	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Sep 21 14:33 trade10.dat.20160921143336929	14:33			2016-21-09	14:33:36	0.606667	Wed	3	10	2016-21-9 14:33:36	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Sep 21 16:23 trade10.dat.20160921162312558	16:23			2016-21-09	16:23:12	0.682778	Wed	3	10	2016-21-9 16:23:12	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 21 17:03 trade10.dat.20160921170315841	17:03			2016-21-09	17:03:15	0.71059	Wed	3	10	2016-21-9 17:03:15	38
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 21 18:03 trade10.dat.20160921180320622	18:03			2016-21-09	18:03:20	0.752315	Wed	3	10	2016-21-9 18:03:20	38
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       945 Sep 21 05:29 UKFCMCurrencyTemplate210916.csv.20160921052901870	5:29			2016-21-09	5:29:01	0.228484	Wed	3	11	2016-21-9 5:29:01	38
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    262369 Sep 21 09:15 passporttrans.20160921.csv.20160921091514519	9:15	9/21/2016		2016-21-09	9:15:14	0.385579	Wed	3	15	2016-21-9 9:15:14	38
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1656 Sep 21 08:31 HighlandCapitalManagementRecon201609210730.csv.20160921083111641	8:31	9/21/2016	7:30:00	2016-21-09	8:31:11	0.354988	Wed	3	16	2016-21-9 8:31:11	38
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       189 Sep 21 10:37 Highland_Orders_20160921csv.20160921103722039	10:37	9/21/2016		2016-21-09	10:37:22	0.442616	Wed	3	16	2016-21-9 10:37:22	38
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       390 Sep 21 01:37 HSBC-LKR.in.21092016-1.20160921013715765	1:37	9/21/2016		2016-21-09	1:37:15	0.067535	Wed	3	17	2016-21-9 1:37:15	38
John Hancock Investments	HAN_TRANS_HANVER_20160921.csv.20160921154339834	15:43	9/21/2016		2016-21-09	15:43:39	0.655313	Wed	3	18	2016-21-9 15:43:39	38
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 21 03:41 FT_fx_20160921_093721.csv.20160921034124205	3:41	9/21/2016	9:37:21	2016-21-09	3:41:24	0.15375	Wed	3	26	2016-21-9 3:41:24	38
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       428 Sep 21 05:04 INV_fx_20160921_110256.csv.20160921050459108	5:04	9/21/2016	11:02:56	2016-21-09	5:04:59	0.211794	Wed	3	26	2016-21-9 5:04:59	38
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Sep 21 05:15 FT_fx_20160921_111049.csv.20160921051500750	5:15	9/21/2016	11:10:49	2016-21-09	5:15:00	0.21875	Wed	3	26	2016-21-9 5:15:00	38
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep 21 06:13 INV_fx_20160921_121130.csv.20160921061303688	6:13	9/21/2016	12:11:30	2016-21-09	6:13:03	0.259063	Wed	3	26	2016-21-9 6:13:03	38
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep 21 07:49 INV_fx_20160921_134705.csv.20160921074910465	7:49	9/21/2016	13:47:05	2016-21-09	7:49:10	0.32581	Wed	3	26	2016-21-9 7:49:10	38
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        61 Sep 21 04:16 citicnhtrades.in.201609211609.20160921041655820	4:16	9/21/2016	16:09:00	2016-21-09	4:16:55	0.178414	Wed	3	28	2016-21-9 4:16:55	38
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 21 05:43 citicnhtrades.in.201609211728.20160921054302457	5:43	9/21/2016	17:28:00	2016-21-09	5:43:02	0.238218	Wed	3	28	2016-21-9 5:43:02	38
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       119 Sep 21 05:43 hsbccnhtrades.in.201609211728.20160921054302723	5:43	9/21/2016	17:28:00	2016-21-09	5:43:02	0.238218	Wed	3	29	2016-21-9 5:43:02	38
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23273 Sep 21 10:35 RSWGD1-17_SSGM_Confirmed_File__20160921.csv.20160921103521794	10:35	9/21/2016		2016-21-09	10:35:21	0.441215	Wed	3	30	2016-21-9 10:35:21	38
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7474 Sep 21 09:31 TIAACREFREPAT.csv.20160921093116977	9:31			2016-21-09	9:31:16	0.396713	Wed	3	32	2016-21-9 9:31:16	38
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       460 Sep 21 04:20 TrinityStreetFX_092116.csv.20160921042056387	4:20			2016-21-09	4:20:56	0.181204	Wed	3	34	2016-21-9 4:20:56	38
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Sep 22 09:25 Alger_Orders_20160922092222.csv.20160922092541300	9:25	9/22/2016	9:22:22	2016-22-09	9:25:41	0.392836	Thu	4	1	2016-22-9 9:25:41	39
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Sep 22 10:39 Alger_Orders_20160922103646.csv.20160922103948173	10:39	9/22/2016	10:36:46	2016-22-09	10:39:48	0.444306	Thu	4	1	2016-22-9 10:39:48	39
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Sep 22 11:43 Alger_Orders_20160922113903.csv.20160922114352272	11:43	9/22/2016	11:39:03	2016-22-09	11:43:52	0.488796	Thu	4	1	2016-22-9 11:43:52	39
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 22 05:31 SSC_BAM_FXREQ_20160922_103003.csv.pgp.ndm05.20160922053125283	5:31	9/22/2016	10:30:03	2016-22-09	5:31:25	0.23015	Thu	4	3	2016-22-9 5:31:25	39
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1415 Sep 22 10:31 SSC_BAM_FXREQ_20160922_153018.csv.pgp.ndm05.20160922103147073	10:31	9/22/2016	15:30:18	2016-22-09	10:31:47	0.438738	Thu	4	3	2016-22-9 10:31:47	39
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1417 Sep 22 12:32 SSC_BAM_FXREQ_20160922_173024.csv.pgp.ndm05.20160922123226493	12:32	9/22/2016	17:30:24	2016-22-09	12:32:26	0.522523	Thu	4	3	2016-22-9 12:32:26	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063830949	6:38			2016-22-09	6:38:30	0.276736	Thu	4	4	2016-22-9 6:38:30	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063831185	6:38			2016-22-09	6:38:31	0.276748	Thu	4	4	2016-22-9 6:38:31	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063831379	6:38			2016-22-09	6:38:31	0.276748	Thu	4	4	2016-22-9 6:38:31	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063831604	6:38			2016-22-09	6:38:31	0.276748	Thu	4	4	2016-22-9 6:38:31	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063831791	6:38			2016-22-09	6:38:31	0.276748	Thu	4	4	2016-22-9 6:38:31	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063831998	6:38			2016-22-09	6:38:31	0.276748	Thu	4	4	2016-22-9 6:38:31	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063832217	6:38			2016-22-09	6:38:32	0.276759	Thu	4	4	2016-22-9 6:38:32	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063832405	6:38			2016-22-09	6:38:32	0.276759	Thu	4	4	2016-22-9 6:38:32	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063832619	6:38			2016-22-09	6:38:32	0.276759	Thu	4	4	2016-22-9 6:38:32	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063832818	6:38			2016-22-09	6:38:32	0.276759	Thu	4	4	2016-22-9 6:38:32	39
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 22 06:38 BCRTOFX.txt.20160922063833016	6:38			2016-22-09	6:38:33	0.276771	Thu	4	4	2016-22-9 6:38:33	39
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      3850 Sep 22 14:38 BRA_BRA_Ver_20160922.csv.20160922143804544	14:38	9/22/2016		2016-22-09	14:38:04	0.609769	Thu	4	5	2016-22-9 14:38:04	39
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep 22 11:33 CDPSfx_BRLorder.20160922.113500.csv.20160922113351563	11:33	9/22/2016	11:35:00	2016-22-09	11:33:51	0.48184	Thu	4	6	2016-22-9 11:33:51	39
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1288 Sep 22 09:07 SPOT_FET_Instructions_StateStreet_20160922-145915.csv.20160922090740011	9:07	9/22/2016	14:59:15	2016-22-09	9:07:40	0.380324	Thu	4	7	2016-22-9 9:07:40	39
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 22 16:36 09222016_GAM_GAM_STAR_GS.20160922.csv.20160922163610807	16:36	9/22/2016		2016-22-09	16:36:10	0.691782	Thu	4	9	2016-22-9 16:36:10	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 22 10:33 trade10.dat.20160922103347486	10:33			2016-22-09	10:33:47	0.440127	Thu	4	10	2016-22-9 10:33:47	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 22 12:33 trade10.dat.20160922123357434	12:33			2016-22-09	12:33:57	0.523576	Thu	4	10	2016-22-9 12:33:57	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Sep 22 14:34 trade10.dat.20160922143403960	14:34			2016-22-09	14:34:03	0.606979	Thu	4	10	2016-22-9 14:34:03	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3034 Sep 22 16:24 trade10.dat.20160922162409378	16:24			2016-22-09	16:24:09	0.683438	Thu	4	10	2016-22-9 16:24:09	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 22 17:06 trade10.dat.20160922170612822	17:06			2016-22-09	17:06:12	0.712639	Thu	4	10	2016-22-9 17:06:12	39
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 22 18:04 trade10.dat.20160922180416824	18:04			2016-22-09	18:04:16	0.752963	Thu	4	10	2016-22-9 18:04:16	39
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       334 Sep 22 07:53 UKFCMCurrencyTemplate220916.csv.20160922075335677	7:53			2016-22-09	7:53:35	0.328877	Thu	4	11	2016-22-9 7:53:35	39
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       258 Sep 22 10:41 UKFCMCurrencyTemplate220916a.csv.20160922104148518	10:41			2016-22-09	10:41:48	0.445694	Thu	4	11	2016-22-9 10:41:48	39
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    256692 Sep 22 08:59 passporttrans.20160922.csv.20160922085939104	8:59	9/22/2016		2016-22-09	8:59:39	0.374757	Thu	4	15	2016-22-9 8:59:39	39
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1651 Sep 22 08:31 HighlandCapitalManagementRecon201609220730.csv.20160922083137465	8:31	9/22/2016	7:30:00	2016-22-09	8:31:37	0.355289	Thu	4	16	2016-22-9 8:31:37	39
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr      1678 Sep 22 03:23 HSBC-LKR.in.22092016-1.20160922032348888	3:23	9/22/2016		2016-22-09	3:23:48	0.141528	Thu	4	17	2016-22-9 3:23:48	39
John Hancock Investments	HAN_TRANS_HANVER_20160922.csv.20160922153606666	15:36	9/22/2016		2016-22-09	15:36:06	0.650069	Thu	4	18	2016-22-9 15:36:06	39
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       467 Sep 22 09:45 PresimaOrders.csv.20160922094543283	9:45			2016-22-09	9:45:43	0.406748	Thu	4	25	2016-22-9 9:45:43	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 22 03:13 INV_fx_20160922_091053.csv.20160922031347273	3:13	9/22/2016	9:10:53	2016-22-09	3:13:47	0.134572	Thu	4	26	2016-22-9 3:13:47	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Sep 22 03:37 FT_fx_20160922_093452.csv.20160922033749531	3:37	9/22/2016	9:34:52	2016-22-09	3:37:49	0.151262	Thu	4	26	2016-22-9 3:37:49	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep 22 04:53 FT_fx_20160922_104542.csv.20160922045352307	4:53	9/22/2016	10:45:42	2016-22-09	4:53:52	0.204074	Thu	4	26	2016-22-9 4:53:52	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Sep 22 05:09 FT_fx_20160922_110404.csv.20160922050953630	5:09	9/22/2016	11:04:04	2016-22-09	5:09:53	0.215197	Thu	4	26	2016-22-9 5:09:53	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 22 05:19 INV_fx_20160922_111700.csv.20160922051954068	5:19	9/22/2016	11:17:00	2016-22-09	5:19:54	0.222153	Thu	4	26	2016-22-9 5:19:54	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Sep 22 05:43 FT_fx_20160922_111559.csv.20160922054355775	5:43	9/22/2016	11:15:59	2016-22-09	5:43:55	0.238831	Thu	4	26	2016-22-9 5:43:55	39
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Sep 22 05:53 INV_fx_20160922_115144.csv.20160922055356356	5:53	9/22/2016	11:51:44	2016-22-09	5:53:56	0.245787	Thu	4	26	2016-22-9 5:53:56	39
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        59 Sep 22 04:15 citicnhtrades.in.201609221609.20160922041550852	4:15	9/22/2016	16:09:00	2016-22-09	4:15:50	0.177662	Thu	4	28	2016-22-9 4:15:50	39
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 22 05:27 citicnhtrades.in.201609221718.20160922052754571	5:27	9/22/2016	17:18:00	2016-22-09	5:27:54	0.227708	Thu	4	28	2016-22-9 5:27:54	39
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       176 Sep 22 05:27 hsbccnhtrades.in.201609221718.20160922052754930	5:27	9/22/2016	17:18:00	2016-22-09	5:27:54	0.227708	Thu	4	29	2016-22-9 5:27:54	39
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     22762 Sep 22 11:11 RSWGD1-17_SSGM_Confirmed_File__20160922.csv.20160922111149462	11:11	9/22/2016		2016-22-09	11:11:49	0.466539	Thu	4	30	2016-22-9 11:11:49	39
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      7072 Sep 22 09:31 TIAACREFREPAT.csv.20160922093142190	9:31			2016-22-09	9:31:42	0.397014	Thu	4	32	2016-22-9 9:31:42	39
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Sep 23 05:32 SSC_BAM_FXREQ_20160923_103009.csv.pgp.ndm05.20160923053230029	5:32	9/23/2016	10:30:09	2016-23-09	5:32:30	0.230903	Fri	5	3	2016-23-9 5:32:30	40
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1523 Sep 23 07:32 SSC_BAM_FXREQ_20160923_123014.csv.pgp.ndm05.20160923073241293	7:32	9/23/2016	12:30:14	2016-23-09	7:32:41	0.314363	Fri	5	3	2016-23-9 7:32:41	40
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 23 08:32 SSC_BAM_FXREQ_20160923_133016.csv.pgp.ndm05.20160923083243926	8:32	9/23/2016	13:30:16	2016-23-09	8:32:43	0.356053	Fri	5	3	2016-23-9 8:32:43	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063906599	6:39			2016-23-09	6:39:06	0.277153	Fri	5	4	2016-23-9 6:39:06	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063906892	6:39			2016-23-09	6:39:06	0.277153	Fri	5	4	2016-23-9 6:39:06	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063907087	6:39			2016-23-09	6:39:07	0.277164	Fri	5	4	2016-23-9 6:39:07	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063907289	6:39			2016-23-09	6:39:07	0.277164	Fri	5	4	2016-23-9 6:39:07	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063907489	6:39			2016-23-09	6:39:07	0.277164	Fri	5	4	2016-23-9 6:39:07	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063907697	6:39			2016-23-09	6:39:07	0.277164	Fri	5	4	2016-23-9 6:39:07	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063907911	6:39			2016-23-09	6:39:07	0.277164	Fri	5	4	2016-23-9 6:39:07	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063908102	6:39			2016-23-09	6:39:08	0.277176	Fri	5	4	2016-23-9 6:39:08	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063908341	6:39			2016-23-09	6:39:08	0.277176	Fri	5	4	2016-23-9 6:39:08	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063908527	6:39			2016-23-09	6:39:08	0.277176	Fri	5	4	2016-23-9 6:39:08	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063908771	6:39			2016-23-09	6:39:08	0.277176	Fri	5	4	2016-23-9 6:39:08	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063908998	6:39			2016-23-09	6:39:08	0.277176	Fri	5	4	2016-23-9 6:39:08	40
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 23 06:39 BCRTOFX.txt.20160923063909181	6:39			2016-23-09	6:39:09	0.277188	Fri	5	4	2016-23-9 6:39:09	40
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      2685 Sep 23 14:44 BRA_BRA_Ver_20160923.csv.20160923144439172	14:44	9/23/2016		2016-23-09	14:44:39	0.61434	Fri	5	5	2016-23-9 14:44:39	40
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Sep 23 05:18 scbcnhtrades1.in.201609231708.20160923051828528	5:18	9/23/2016	17:08:00	2016-23-09	5:18:28	0.221157	Fri	5	7	2016-23-9 5:18:28	40
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 23 05:18 scbcnhtrades2.in.201609231708.20160923051828852	5:18	9/23/2016	17:08:00	2016-23-09	5:18:28	0.221157	Fri	5	7	2016-23-9 5:18:28	40
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1429 Sep 23 09:28 SPOT_FET_Instructions_StateStreet_20160923-151642.csv.20160923092818476	9:28	9/23/2016	15:16:42	2016-23-09	9:28:18	0.394653	Fri	5	7	2016-23-9 9:28:18	40
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       200 Sep 23 05:00 CRUX_20160923.csv.20160923050026606	5:00	9/23/2016		2016-23-09	5:00:26	0.208634	Fri	5	8	2016-23-9 5:00:26	40
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 23 16:52 09232016_GAM_GAM_STAR_GS.20160923.csv.20160923165246796	16:52	9/23/2016		2016-23-09	16:52:46	0.70331	Fri	5	9	2016-23-9 16:52:46	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Sep 23 10:34 trade10.dat.20160923103423683	10:34			2016-23-09	10:34:23	0.440544	Fri	5	10	2016-23-9 10:34:23	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 23 12:34 trade10.dat.20160923123431962	12:34			2016-23-09	12:34:31	0.52397	Fri	5	10	2016-23-9 12:34:31	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     10846 Sep 23 14:34 trade10.dat.20160923143438319	14:34			2016-23-09	14:34:38	0.607384	Fri	5	10	2016-23-9 14:34:38	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Sep 23 16:24 trade10.dat.20160923162444789	16:24			2016-23-09	16:24:44	0.683843	Fri	5	10	2016-23-9 16:24:44	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 23 17:02 trade10.dat.20160923170247791	17:02			2016-23-09	17:02:47	0.710266	Fri	5	10	2016-23-9 17:02:47	40
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Sep 23 18:04 trade10.dat.20160923180452439	18:04			2016-23-09	18:04:52	0.75338	Fri	5	10	2016-23-9 18:04:52	40
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep 23 04:34 UKFCMCurrencyTemplate230916.csv.20160923043425069	4:34			2016-23-09	4:34:25	0.190567	Fri	5	11	2016-23-9 4:34:25	40
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    302238 Sep 23 09:04 passporttrans.20160923.csv.20160923090415109	9:04	9/23/2016		2016-23-09	9:04:15	0.377951	Fri	5	15	2016-23-9 9:04:15	40
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1657 Sep 23 08:32 HighlandCapitalManagementRecon201609230730.csv.20160923083213572	8:32	9/23/2016	7:30:00	2016-23-09	8:32:13	0.355706	Fri	5	16	2016-23-9 8:32:13	40
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr      1297 Sep 23 03:42 HSBC-LKR.in.23092016-1.20160923034222357	3:42	9/23/2016		2016-23-09	3:42:22	0.154421	Fri	5	17	2016-23-9 3:42:22	40
John Hancock Investments	HAN_TRANS_HANVER_20160923.csv.20160923154042366	15:40	9/23/2016		2016-23-09	15:40:42	0.653264	Fri	5	18	2016-23-9 15:40:42	40
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep 23 05:48 NOS_SFX_20160923.csv.20160923054831035	5:48	9/23/2016		2016-23-09	5:48:31	0.242025	Fri	5	21	2016-23-9 5:48:31	40
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       896 Sep 23 15:34 PGI_Orders_20160923143233.csv.20160923153441832	15:34	9/23/2016	14:32:33	2016-23-09	15:34:41	0.649086	Fri	5	24	2016-23-9 15:34:41	40
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 23 03:14 INV_fx_20160923_091151.csv.20160923031419353	3:14	9/23/2016	9:11:51	2016-23-09	3:14:19	0.134942	Fri	5	26	2016-23-9 3:14:19	40
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Sep 23 03:26 FT_fx_20160923_092333.csv.20160923032621095	3:26	9/23/2016	9:23:33	2016-23-09	3:26:21	0.143299	Fri	5	26	2016-23-9 3:26:21	40
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Sep 23 04:58 FT_fx_20160923_105526.csv.20160923045826169	4:58	9/23/2016	10:55:26	2016-23-09	4:58:26	0.207245	Fri	5	26	2016-23-9 4:58:26	40
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Sep 23 05:06 INV_fx_20160923_110439.csv.20160923050628005	5:06	9/23/2016	11:04:39	2016-23-09	5:06:28	0.212824	Fri	5	26	2016-23-9 5:06:28	40
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Sep 23 05:36 FT_fx_20160923_113249.csv.20160923053630530	5:36	9/23/2016	11:32:49	2016-23-09	5:36:30	0.233681	Fri	5	26	2016-23-9 5:36:30	40
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       114 Sep 23 04:16 citicnhtrades.in.201609231605.20160923041623547	4:16	9/23/2016	16:05:00	2016-23-09	4:16:23	0.178044	Fri	5	28	2016-23-9 4:16:23	40
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 23 05:24 citicnhtrades.in.201609231714.20160923052429278	5:24	9/23/2016	17:14:00	2016-23-09	5:24:29	0.225336	Fri	5	28	2016-23-9 5:24:29	40
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       225 Sep 23 05:24 hsbccnhtrades.in.201609231714.20160923052429550	5:24	9/23/2016	17:14:00	2016-23-09	5:24:29	0.225336	Fri	5	29	2016-23-9 5:24:29	40
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     24995 Sep 23 10:52 RSWGD1-17_SSGM_Confirmed_File__20160923.csv.20160923105224739	10:52	9/23/2016		2016-23-09	10:52:24	0.453056	Fri	5	30	2016-23-9 10:52:24	40
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     14972 Sep 23 09:32 TIAACREFREPAT.csv.20160923093219100	9:32			2016-23-09	9:32:19	0.397442	Fri	5	32	2016-23-9 9:32:19	40
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1523 Sep 26 04:31 SSC_BAM_FXREQ_20160926_093001.csv.pgp.ndm05.20160926043130066	4:31	9/26/2016	9:30:01	2016-26-09	4:31:30	0.188542	Mon	1	3	2016-26-9 4:31:30	41
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Sep 26 05:33 SSC_BAM_FXREQ_20160926_103005.csv.pgp.ndm05.20160926053334769	5:33	9/26/2016	10:30:05	2016-26-09	5:33:34	0.231644	Mon	1	3	2016-26-9 5:33:34	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063810436	6:38			2016-26-09	6:38:10	0.276505	Mon	1	4	2016-26-9 6:38:10	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063810767	6:38			2016-26-09	6:38:10	0.276505	Mon	1	4	2016-26-9 6:38:10	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063810966	6:38			2016-26-09	6:38:10	0.276505	Mon	1	4	2016-26-9 6:38:10	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063811174	6:38			2016-26-09	6:38:11	0.276516	Mon	1	4	2016-26-9 6:38:11	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063811365	6:38			2016-26-09	6:38:11	0.276516	Mon	1	4	2016-26-9 6:38:11	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063811567	6:38			2016-26-09	6:38:11	0.276516	Mon	1	4	2016-26-9 6:38:11	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063811783	6:38			2016-26-09	6:38:11	0.276516	Mon	1	4	2016-26-9 6:38:11	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063811976	6:38			2016-26-09	6:38:11	0.276516	Mon	1	4	2016-26-9 6:38:11	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063812191	6:38			2016-26-09	6:38:12	0.276528	Mon	1	4	2016-26-9 6:38:12	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063812403	6:38			2016-26-09	6:38:12	0.276528	Mon	1	4	2016-26-9 6:38:12	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063812622	6:38			2016-26-09	6:38:12	0.276528	Mon	1	4	2016-26-9 6:38:12	41
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Sep 26 06:38 BCRTOFX.txt.20160926063812844	6:38			2016-26-09	6:38:12	0.276528	Mon	1	4	2016-26-9 6:38:12	41
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       331 Sep 26 08:59 CDPSfx_BRLorder.20160926.085803.csv.20160926085948369	8:59	9/26/2016	8:58:03	2016-26-09	8:59:48	0.374861	Mon	1	6	2016-26-9 8:59:48	41
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Sep 26 10:05 CDPSfx_BRLorder.20160926.100503.csv.20160926100553015	10:05	9/26/2016	10:05:03	2016-26-09	10:05:53	0.420752	Mon	1	6	2016-26-9 10:05:53	41
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       114 Sep 26 05:33 scbcnhtrades1.in.201609261726.20160926053335011	5:33	9/26/2016	17:26:00	2016-26-09	5:33:35	0.231655	Mon	1	7	2016-26-9 5:33:35	41
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 26 05:33 scbcnhtrades2.in.201609261726.20160926053335211	5:33	9/26/2016	17:26:00	2016-26-09	5:33:35	0.231655	Mon	1	7	2016-26-9 5:33:35	41
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1000 Sep 26 09:21 SPOT_FET_Instructions_StateStreet_20160926-151150.csv.20160926092149885	9:21	9/26/2016	15:11:50	2016-26-09	9:21:49	0.39015	Mon	1	7	2016-26-9 9:21:49	41
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Sep 26 10:33 trade10.dat.20160926103356900	10:33			2016-26-09	10:33:56	0.440231	Mon	1	10	2016-26-9 10:33:56	41
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       181 Sep 26 05:23 UKFCMCurrencyTemplate260916.csv.20160926052333244	5:23			2016-26-09	5:23:33	0.224688	Mon	1	11	2016-26-9 5:23:33	41
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       176 Sep 26 06:57 UKFCMCurrencyTemplate260916a.csv.20160926065743401	6:57			2016-26-09	6:57:43	0.290081	Mon	1	11	2016-26-9 6:57:43	41
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    475868 Sep 26 09:03 passporttrans.20160926.csv.20160926090348896	9:03	9/26/2016		2016-26-09	9:03:48	0.377639	Mon	1	15	2016-26-9 9:03:48	41
HSBC LKR	-rw-r--r--   1 ftpgmrin ftpgmr       389 Sep 26 03:05 HSBC-LKR.in.26092016-1.20160926030525906	3:05	9/26/2016		2016-26-09	3:05:25	0.128762	Mon	1	17	2016-26-9 3:05:25	41
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Sep 26 03:27 INV_fx_20160926_092528.csv.20160926032727441	3:27	9/26/2016	9:25:28	2016-26-09	3:27:27	0.144063	Mon	1	26	2016-26-9 3:27:27	41
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Sep 26 03:35 FT_fx_20160926_093222.csv.20160926033527922	3:35	9/26/2016	9:32:22	2016-26-09	3:35:27	0.149618	Mon	1	26	2016-26-9 3:35:27	41
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Sep 26 04:37 INV_fx_20160926_103513.csv.20160926043730546	4:37	9/26/2016	10:35:13	2016-26-09	4:37:30	0.192708	Mon	1	26	2016-26-9 4:37:30	41
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Sep 26 05:07 FT_fx_20160926_110455.csv.20160926050732755	5:07	9/26/2016	11:04:55	2016-26-09	5:07:32	0.213565	Mon	1	26	2016-26-9 5:07:32	41
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Sep 26 05:31 FT_fx_20160926_112902.csv.20160926053133897	5:31	9/26/2016	11:29:02	2016-26-09	5:31:33	0.230243	Mon	1	26	2016-26-9 5:31:33	41
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        57 Sep 26 04:15 citicnhtrades.in.201609261608.20160926041528890	4:15	9/26/2016	16:08:00	2016-26-09	4:15:28	0.177407	Mon	1	28	2016-26-9 4:15:28	41
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Sep 26 05:31 citicnhtrades.in.201609261718.20160926053134219	5:31	9/26/2016	17:18:00	2016-26-09	5:31:34	0.230255	Mon	1	28	2016-26-9 5:31:34	41
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       567 Sep 26 05:31 hsbccnhtrades.in.201609261718.20160926053134424	5:31	9/26/2016	17:18:00	2016-26-09	5:31:34	0.230255	Mon	1	29	2016-26-9 5:31:34	41
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     23741 Sep 26 10:19 RSWGD1-17_SSGM_Confirmed_File__20160926.csv.20160926101955485	10:19	9/26/2016		2016-26-09	10:19:55	0.430498	Mon	1	30	2016-26-9 10:19:55	41
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8354 Sep 26 09:31 TIAACREFREPAT.csv.20160926093150893	9:31			2016-26-09	9:31:50	0.397106	Mon	1	32	2016-26-9 9:31:50	41
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Feb  1 14:23 Alger_Orders_20170201142053.csv.20170201142353594	14:23	2/1/2017	14:20:53	2017-01-02	14:23:53	0.599919	Wed	3	1	2017-02-01 14:23	42
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3306 Feb  1 12:01 alps_Orders_02012017100000.csv.20170201120140417	12:01	1/2/2017	10:00:00	2017-01-02	12:01:40	0.501157	Wed	3	2	2017-02-01 12:01	42
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb  1 04:34 SSC_BAM_FXREQ_20170201_093017.csv.pgp.ndm05.20170201043402108	4:34	2/1/2017	9:30:17	2017-01-02	4:34:02	0.190301	Wed	3	3	2017-02-01 04:34	42
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Feb  1 05:32 SSC_BAM_FXREQ_20170201_103019.csv.pgp.ndm05.20170201053206737	5:32	2/1/2017	10:30:19	2017-01-02	5:32:06	0.230625	Wed	3	3	2017-02-01 05:32	42
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1454 Feb  1 12:32 SSC_BAM_FXREQ_20170201_173039.csv.pgp.ndm05.20170201123245389	12:32	2/1/2017	17:30:39	2017-01-02	12:32:45	0.522743	Wed	3	3	2017-02-01 12:32	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064008827	6:40			2017-01-02	6:40:08	0.27787	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064009128	6:40			2017-01-02	6:40:09	0.277882	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064009331	6:40			2017-01-02	6:40:09	0.277882	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064009518	6:40			2017-01-02	6:40:09	0.277882	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064009717	6:40			2017-01-02	6:40:09	0.277882	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064009916	6:40			2017-01-02	6:40:09	0.277882	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064010129	6:40			2017-01-02	6:40:10	0.277894	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064010316	6:40			2017-01-02	6:40:10	0.277894	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064010509	6:40			2017-01-02	6:40:10	0.277894	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064010719	6:40			2017-01-02	6:40:10	0.277894	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064010928	6:40			2017-01-02	6:40:10	0.277894	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064011327	6:40			2017-01-02	6:40:11	0.277905	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064011119	6:40			2017-01-02	6:40:11	0.277905	Wed	3	4	2017-02-01 06:40	42
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  1 06:40 BCRTOFX.txt.20170201064011521	6:40			2017-01-02	6:40:11	0.277905	Wed	3	4	2017-02-01 06:40	42
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7605 Feb  1 14:35 BRA_BRA_Ver_20170201.csv.20170201143556248	14:35	2/1/2017		2017-01-02	14:35:56	0.608287	Wed	3	5	2017-02-01 14:35	42
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       354 Feb  1 16:34 CDPSfx_MYRorder.20170201.163500.csv.20170201163406798	16:34	2/1/2017	16:35:00	2017-01-02	16:34:06	0.690347	Wed	3	6	2017-02-01 16:34	42
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1733 Feb  1 10:55 SPOT_FET_Instructions_StateStreet_20170201-164029.csv.20170201105557224	10:55	2/1/2017	16:40:29	2017-01-02	10:55:57	0.455521	Wed	3	7	2017-02-01 10:55	42
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       384 Feb  1 16:24 02012017_GAM_GAM_STAR_GS.20170201.csv.20170201162404995	16:24	2/1/2017		2017-01-02	16:24:04	0.68338	Wed	3	9	2017-02-01 16:24	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     53378 Feb  1 10:35 trade10.dat.20170201103555703	10:35			2017-01-02	10:35:55	0.441609	Wed	3	10	2017-02-01 10:35	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Feb  1 12:33 trade10.dat.20170201123345875	12:33			2017-01-02	12:33:45	0.523438	Wed	3	10	2017-02-01 12:33	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb  1 14:33 trade10.dat.20170201143355342	14:33			2017-01-02	14:33:55	0.606887	Wed	3	10	2017-02-01 14:33	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9544 Feb  1 16:24 trade10.dat.20170201162405283	16:24			2017-01-02	16:24:05	0.683391	Wed	3	10	2017-02-01 16:24	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  1 17:04 trade10.dat.20170201170409683	17:04			2017-01-02	17:04:09	0.711215	Wed	3	10	2017-02-01 17:04	42
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  1 18:04 trade10.dat.20170201180413691	18:04			2017-01-02	18:04:13	0.752928	Wed	3	10	2017-02-01 18:04	42
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    376920 Feb  1 09:25 passporttrans.20170201.csv.20170201092551669	9:25	2/1/2017		2017-01-02	9:25:51	0.392951	Wed	3	15	2017-02-01 09:25	42
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1856 Feb  1 08:31 HighlandCapitalManagementRecon201702010730.csv.20170201083147370	8:31	2/1/2017	7:30:00	2017-01-02	8:31:47	0.355405	Wed	3	16	2017-02-01 08:31	42
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       481 Feb  1 02:27 HSBC-LKR.in.01022017-1.20170201022724816	 02:2	1/2/2017		2017-01-02	2:27:24	0.102361	Wed	3	17	2017-02-01 02:27	42
John Hancock Investments	HAN_TRANS_HANVER_20170201.csv.20170201153600938	15:36	2/1/2017		2017-01-02	15:36:00	0.65	Wed	3	18	2017-02-01 15:36	42
John Hancock Investments	HAN_TRANS_HANVER_20170201.csv.20170201153600938	15:36	2/1/2017		2017-01-02	15:36:00	0.65	Wed	3	18	2017-02-01 15:36	42
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  1 12:05 PAXStateStreetFX_Orders_020117.txt.20170201120541489	12:05	2/1/2017		2017-01-02	12:05:41	0.503947	Wed	3	23	2017-02-01 12:05	42
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  1 14:55 PAXStateStreetFX_Orders_020117.txt.20170201145557488	14:55	2/1/2017		2017-01-02	14:55:57	0.622188	Wed	3	23	2017-02-01 14:55	42
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  1 16:04 PAXStateStreetFX_Orders_020117.txt.20170201160402949	16:04	2/1/2017		2017-01-02	16:04:02	0.669468	Wed	3	23	2017-02-01 16:04	42
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  1 16:12 PAXStateStreetFX_Orders_020117.txt.20170201161203885	16:12	2/1/2017		2017-01-02	16:12:03	0.675035	Wed	3	23	2017-02-01 16:12	42
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       202 Feb  1 16:24 PGI_Orders_20170201152208.csv.20170201162405504	16:24	2/1/2017	15:22:08	2017-01-02	16:24:05	0.683391	Wed	3	24	2017-02-01 16:24	42
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       208 Feb  1 10:39 PresimaOrders.csv.20170201103956221	10:39			2017-01-02	10:39:56	0.444398	Wed	3	25	2017-02-01 10:39	42
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb  1 02:45 FT_fx_20170201_084219.csv.20170201024525516	2:45	2/1/2017	8:42:19	2017-01-02	2:45:25	0.114873	Wed	3	26	2017-02-01 02:45	42
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb  1 03:37 INV_fx_20170201_093344.csv.20170201033729097	3:37	2/1/2017	9:33:44	2017-01-02	3:37:29	0.15103	Wed	3	26	2017-02-01 03:37	42
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb  1 04:31 FT_fx_20170201_102140.csv.20170201043131775	4:31	2/1/2017	10:21:40	2017-01-02	4:31:31	0.188553	Wed	3	26	2017-02-01 04:31	42
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb  1 04:53 FT_fx_20170201_105152.csv.20170201045332916	4:53	2/1/2017	10:51:52	2017-01-02	4:53:32	0.203843	Wed	3	26	2017-02-01 04:53	42
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  1 05:25 INV_fx_20170201_112407.csv.20170201052536298	5:25	2/1/2017	11:24:07	2017-01-02	5:25:36	0.226111	Wed	3	26	2017-02-01 05:25	42
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28684 Feb  1 11:39 RSWGD1-17_SSGM_Confirmed_File__20170201.csv.20170201113938068	11:39	2/1/2017		2017-01-02	11:39:38	0.485856	Wed	3	30	2017-02-01 11:39	42
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      9059 Feb  1 09:31 TIAACREFREPAT.csv.20170201093152165	9:31			2017-01-02	9:31:52	0.39713	Wed	3	32	2017-02-01 09:31	42
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       414 Feb  1 21:26 tokyofundtrades.in.201702021005.20170201212628273	 21:2	2/2/2017	10:05:00	2017-01-02	21:26:28	0.89338	Wed	3	33	2017-02-01 21:26	42
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       131 Feb  2 09:30 Alger_Orders_20170202092605.csv.20170202093041629	9:30	2/2/2017	9:26:05	2017-02-02	9:30:41	0.396308	Thu	4	1	2017-02-02 09:30	43
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1458 Feb  2 04:32 SSC_BAM_FXREQ_20170202_093028.csv.pgp.ndm05.20170202043251834	4:32	2/2/2017	9:30:28	2017-02-02	4:32:51	0.189479	Thu	4	3	2017-02-02 04:32	43
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1458 Feb  2 11:33 SSC_BAM_FXREQ_20170202_163125.csv.pgp.ndm05.20170202113351739	11:33	2/2/2017	16:31:25	2017-02-02	11:33:51	0.48184	Thu	4	3	2017-02-02 11:33	43
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1400 Feb  2 12:33 SSC_BAM_FXREQ_20170202_173138.csv.pgp.ndm05.20170202123356437	12:33	2/2/2017	17:31:38	2017-02-02	12:33:56	0.523565	Thu	4	3	2017-02-02 12:33	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:39 BCRTOFX.txt.20170202063959406	6:39			2017-02-02	6:39:59	0.277766	Thu	4	4	2017-02-02 06:39	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:39 BCRTOFX.txt.20170202063959761	6:39			2017-02-02	6:39:59	0.277766	Thu	4	4	2017-02-02 06:39	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:39 BCRTOFX.txt.20170202063959954	6:39			2017-02-02	6:39:59	0.277766	Thu	4	4	2017-02-02 06:39	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064000775	6:40			2017-02-02	6:40:00	0.277778	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064000179	6:40			2017-02-02	6:40:00	0.277778	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064000375	6:40			2017-02-02	6:40:00	0.277778	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064000566	6:40			2017-02-02	6:40:00	0.277778	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064000958	6:40			2017-02-02	6:40:00	0.277778	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064001190	6:40			2017-02-02	6:40:01	0.277789	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064001371	6:40			2017-02-02	6:40:01	0.277789	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064001555	6:40			2017-02-02	6:40:01	0.277789	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064001759	6:40			2017-02-02	6:40:01	0.277789	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064001967	6:40			2017-02-02	6:40:01	0.277789	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064002165	6:40			2017-02-02	6:40:02	0.277801	Thu	4	4	2017-02-02 06:40	43
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  2 06:40 BCRTOFX.txt.20170202064002360	6:40			2017-02-02	6:40:02	0.277801	Thu	4	4	2017-02-02 06:40	43
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      8402 Feb  2 14:36 BRA_BRA_Ver_20170202.csv.20170202143634312	14:36	2/2/2017		2017-02-02	14:36:34	0.608727	Thu	4	5	2017-02-02 14:36	43
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1866 Feb  2 10:34 SPOT_FET_Instructions_StateStreet_20170202-162310.csv.20170202103446671	10:34	2/2/2017	16:23:10	2017-02-02	10:34:46	0.44081	Thu	4	7	2017-02-02 10:34	43
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       404 Feb  2 16:44 02022017_GAM_GAM_STAR_GS.20170202.csv.20170202164443492	16:44	2/2/2017		2017-02-02	16:44:43	0.69772	Thu	4	9	2017-02-02 16:44	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      9110 Feb  2 10:34 trade10.dat.20170202103447485	10:34			2017-02-02	10:34:47	0.440822	Thu	4	10	2017-02-02 10:34	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Feb  2 12:34 trade10.dat.20170202123426807	12:34			2017-02-02	12:34:26	0.523912	Thu	4	10	2017-02-02 12:34	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Feb  2 14:34 trade10.dat.20170202143433876	14:34			2017-02-02	14:34:33	0.607326	Thu	4	10	2017-02-02 14:34	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     16488 Feb  2 16:24 trade10.dat.20170202162440860	16:24			2017-02-02	16:24:40	0.683796	Thu	4	10	2017-02-02 16:24	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  2 17:04 trade10.dat.20170202170445047	17:04			2017-02-02	17:04:45	0.711632	Thu	4	10	2017-02-02 17:04	43
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  2 18:03 trade10.dat.20170202180328616	18:03			2017-02-02	18:03:28	0.752407	Thu	4	10	2017-02-02 18:03	43
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       187 Feb  2 17:30 FT_Orders_20170202.csv.20170202173056161	17:30	2/2/2017		2017-02-02	17:30:56	0.729815	Thu	4	12	2017-02-02 17:30	43
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    369647 Feb  2 09:24 passporttrans.20170202.csv.20170202092441264	9:24	2/2/2017		2017-02-02	9:24:41	0.392141	Thu	4	15	2017-02-02 09:24	43
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2406 Feb  2 08:32 HighlandCapitalManagementRecon201702020730.csv.20170202083238330	8:32	2/2/2017	7:30:00	2017-02-02	8:32:38	0.355995	Thu	4	16	2017-02-02 08:32	43
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       479 Feb  2 01:28 HSBC-LKR.in.02022017-1.20170202012812198	 01:2	2/2/2017		2017-02-02	1:28:12	0.06125	Thu	4	17	2017-02-02 01:28	43
John Hancock Investments	HAN_TRANS_HANVER_20170202.csv.20170202153436622	15:34	2/2/2017		2017-02-02	15:34:36	0.649028	Thu	4	18	2017-02-02 15:34	43
John Hancock Investments	HAN_TRANS_HANVER_20170202.csv.20170202153436622	15:34	2/2/2017		2017-02-02	15:34:36	0.649028	Thu	4	18	2017-02-02 15:34	43
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Feb  2 07:02 NOS_SFX_20170202.csv.20170202070233681	7:02	2/2/2017		2017-02-02	7:02:33	0.293438	Thu	4	21	2017-02-02 07:02	43
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  2 15:32 PAXStateStreetFX_Orders_020217.txt.20170202153236272	15:32	2/2/2017		2017-02-02	15:32:36	0.647639	Thu	4	23	2017-02-02 15:32	43
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  2 15:36 PAXStateStreetFX_Orders_020217.txt.20170202153637242	15:36	2/2/2017		2017-02-02	15:36:37	0.650428	Thu	4	23	2017-02-02 15:36	43
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  2 15:44 PAXStateStreetFX_Orders_020217.txt.20170202154437861	15:44	2/2/2017		2017-02-02	15:44:37	0.655984	Thu	4	23	2017-02-02 15:44	43
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  2 03:34 INV_fx_20170202_093223.csv.20170202033419218	3:34	2/2/2017	9:32:23	2017-02-02	3:34:19	0.148831	Thu	4	26	2017-02-02 03:34	43
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Feb  2 04:44 FT_fx_20170202_084635.csv.20170202044422632	4:44	2/2/2017	8:46:35	2017-02-02	4:44:22	0.197477	Thu	4	26	2017-02-02 04:44	43
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       229 Feb  2 04:56 FT_fx_20170202_105453.csv.20170202045623274	4:56	2/2/2017	10:54:53	2017-02-02	4:56:23	0.205822	Thu	4	26	2017-02-02 04:56	43
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Feb  2 05:40 FT_fx_20170202_113924.csv.20170202054025799	5:40	2/2/2017	11:39:24	2017-02-02	5:40:25	0.2364	Thu	4	26	2017-02-02 05:40	43
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     29490 Feb  2 10:54 RSWGD1-17_SSGM_Confirmed_File__20170202.csv.20170202105448830	10:54	2/2/2017		2017-02-02	10:54:48	0.454722	Thu	4	30	2017-02-02 10:54	43
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5846 Feb  2 09:30 TIAACREFREPAT.csv.20170202093042351	9:30			2017-02-02	9:30:42	0.396319	Thu	4	32	2017-02-02 09:30	43
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      1057 Feb  2 21:27 tokyofundtrades.in.201702030946.20170202212722614	 21:2	2/3/2017	9:46:00	2017-02-02	21:27:22	0.894005	Thu	4	33	2017-02-02 21:27	43
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       286 Feb  2 22:25 tokyofundtrades.in.201702031116.20170202222525501	 22:2	2/3/2017	11:16:00	2017-02-02	22:25:25	0.934317	Thu	4	33	2017-02-02 22:25	43
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       394 Feb  3 10:15 Alger_Orders_20170203101252.csv.20170203101547489	10:15	2/3/2017	10:12:52	2017-03-02	10:15:47	0.427627	Fri	5	1	2017-02-03 10:15	44
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        63 Feb  3 13:38 Alger_Orders_20170203133343.csv.20170203133811863	13:38	2/3/2017	13:33:43	2017-03-02	13:38:11	0.568183	Fri	5	1	2017-02-03 13:38	44
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      7474 Feb  3 12:06 alps_Orders_02032017100000.csv.20170203120606564	12:06	3/2/2017	10:00:00	2017-03-02	12:06:06	0.504236	Fri	5	2	2017-02-03 12:06	44
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      8406 Feb  3 14:04 alps_Orders_02032017110000.csv.20170203140413361	14:04	3/2/2017	11:00:00	2017-03-02	14:04:13	0.586262	Fri	5	2	2017-02-03 14:04	44
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      2473 Feb  3 18:00 alps_Orders_02032017120000.csv.20170203180001444	18:00	3/2/2017	12:00:00	2017-03-02	18:00:01	0.750012	Fri	5	2	2017-02-03 18:00	44
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1591 Feb  3 04:31 SSC_BAM_FXREQ_20170203_093026.csv.pgp.ndm05.20170203043148949	4:31	2/3/2017	9:30:26	2017-03-02	4:31:48	0.18875	Fri	5	3	2017-02-03 04:31	44
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb  3 11:32 SSC_BAM_FXREQ_20170203_163048.csv.pgp.ndm05.20170203113234168	11:32	2/3/2017	16:30:48	2017-03-02	11:32:34	0.480949	Fri	5	3	2017-02-03 11:32	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064024520	6:40			2017-03-02	6:40:24	0.278056	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064024818	6:40			2017-03-02	6:40:24	0.278056	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064025015	6:40			2017-03-02	6:40:25	0.278067	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064025205	6:40			2017-03-02	6:40:25	0.278067	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064025396	6:40			2017-03-02	6:40:25	0.278067	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064025590	6:40			2017-03-02	6:40:25	0.278067	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064025785	6:40			2017-03-02	6:40:25	0.278067	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026035	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026197	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026374	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026572	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026775	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064026981	6:40			2017-03-02	6:40:26	0.278079	Fri	5	4	2017-02-03 06:40	44
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  3 06:40 BCRTOFX.txt.20170203064027184	6:40			2017-03-02	6:40:27	0.27809	Fri	5	4	2017-02-03 06:40	44
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7415 Feb  3 14:46 BRA_BRA_Ver_20170203.csv.20170203144617661	14:46	2/3/2017		2017-03-02	14:46:17	0.615475	Fri	5	5	2017-02-03 14:46	44
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Feb  3 09:23 CDPSfx_TWDorder.20170203.092257.csv.20170203092339442	9:23	2/3/2017	9:22:57	2017-03-02	9:23:39	0.391424	Fri	5	6	2017-02-03 09:23	44
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       357 Feb  3 16:34 CDPSfx_THBorder.20170203.163500.csv.20170203163423899	16:34	2/3/2017	16:35:00	2017-03-02	16:34:23	0.690544	Fri	5	6	2017-02-03 16:34	44
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       360 Feb  3 16:34 CDPSfx_IDRorder.20170203.163500.csv.20170203163423470	16:34	2/3/2017	16:35:00	2017-03-02	16:34:23	0.690544	Fri	5	6	2017-02-03 16:34	44
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       113 Feb  3 04:11 scbcnhtrades1.in.201702031706.20170203041147099	4:11	2/3/2017	17:06:00	2017-03-02	4:11:47	0.17485	Fri	5	7	2017-02-03 04:11	44
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  3 04:11 scbcnhtrades2.in.201702031706.20170203041147325	4:11	2/3/2017	17:06:00	2017-03-02	4:11:47	0.17485	Fri	5	7	2017-02-03 04:11	44
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       868 Feb  3 10:15 SPOT_FET_Instructions_StateStreet_20170203-153813.csv.20170203101547735	10:15	2/3/2017	15:38:13	2017-03-02	10:15:47	0.427627	Fri	5	7	2017-02-03 10:15	44
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       403 Feb  3 16:42 02032017_GAM_GAM_STAR_GS.20170203.csv.20170203164224670	16:42	2/3/2017		2017-03-02	16:42:24	0.696111	Fri	5	9	2017-02-03 16:42	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  3 10:33 trade10.dat.20170203103349582	10:33			2017-03-02	10:33:49	0.44015	Fri	5	10	2017-02-03 10:33	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     15186 Feb  3 12:34 trade10.dat.20170203123408620	12:34			2017-03-02	12:34:08	0.523704	Fri	5	10	2017-02-03 12:34	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Feb  3 14:34 trade10.dat.20170203143416616	14:34			2017-03-02	14:34:16	0.60713	Fri	5	10	2017-02-03 14:34	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Feb  3 16:24 trade10.dat.20170203162422725	16:24			2017-03-02	16:24:22	0.683588	Fri	5	10	2017-02-03 16:24	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  3 17:04 trade10.dat.20170203170426466	17:04			2017-03-02	17:04:26	0.711412	Fri	5	10	2017-02-03 17:04	44
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  3 18:04 trade10.dat.20170203180402536	18:04			2017-03-02	18:04:02	0.752801	Fri	5	10	2017-02-03 18:04	44
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    323970 Feb  3 09:09 passporttrans.20170203.csv.20170203090938821	9:09	2/3/2017		2017-03-02	9:09:38	0.38169	Fri	5	15	2017-02-03 09:09	44
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2242 Feb  3 08:31 HighlandCapitalManagementRecon201702030730.csv.20170203083136737	8:31	2/3/2017	7:30:00	2017-03-02	8:31:36	0.355278	Fri	5	16	2017-02-03 08:31	44
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       295 Feb  3 00:39 HSBC-LKR.in.03022017-1.20170203003933056	 00:3	3/2/2017		2017-03-02	0:39:33	0.027465	Fri	5	17	2017-02-03 00:39	44
John Hancock Investments	HAN_TRANS_HANVER_20170203.csv.20170203155020160	15:50	2/3/2017		2017-03-02	15:50:20	0.659954	Fri	5	18	2017-02-03 15:50	44
John Hancock Investments	HAN_TRANS_HANVER_20170203.csv.20170203155020160	15:50	2/3/2017		2017-03-02	15:50:20	0.659954	Fri	5	18	2017-02-03 15:50	44
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  3 10:31 PAXStateStreetFX_Orders_020317.txt.20170203103148873	10:31	2/3/2017		2017-03-02	10:31:48	0.43875	Fri	5	23	2017-02-03 10:31	44
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  3 14:24 PAXStateStreetFX_Orders_020317.txt.20170203142415247	14:24	2/3/2017		2017-03-02	14:24:15	0.600174	Fri	5	23	2017-02-03 14:24	44
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  3 16:48 PAXStateStreetFX_Orders_020317.txt.20170203164825412	16:48	2/3/2017		2017-03-02	16:48:25	0.700289	Fri	5	23	2017-02-03 16:48	44
PGI	-rw-r--r--   1 ftpgmrin ftpgmr      1187 Feb  3 14:44 PGI_Orders_20170203134241.csv.20170203144417319	14:44	2/3/2017	13:42:41	2017-03-02	14:44:17	0.614086	Fri	5	24	2017-02-03 14:44	44
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb  3 02:51 FT_fx_20170203_084847.csv.20170203025142671	2:51	2/3/2017	8:48:47	2017-03-02	2:51:42	0.119236	Fri	5	26	2017-02-03 02:51	44
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  3 03:39 INV_fx_20170203_093807.csv.20170203033945731	3:39	2/3/2017	9:38:07	2017-03-02	3:39:45	0.152604	Fri	5	26	2017-02-03 03:39	44
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb  3 04:29 FT_fx_20170203_102611.csv.20170203042948629	4:29	2/3/2017	10:26:11	2017-03-02	4:29:48	0.187361	Fri	5	26	2017-02-03 04:29	44
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  3 06:27 INV_fx_20170203_122602.csv.20170203062753770	6:27	2/3/2017	12:26:02	2017-03-02	6:27:53	0.269363	Fri	5	26	2017-02-03 06:27	44
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  3 04:27 citicnhtrades.in.201702031722.20170203042748059	4:27	2/3/2017	17:22:00	2017-03-02	4:27:48	0.185972	Fri	5	28	2017-02-03 04:27	44
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       251 Feb  3 04:27 hsbccnhtrades.in.201702031722.20170203042748398	4:27	2/3/2017	17:22:00	2017-03-02	4:27:48	0.185972	Fri	5	29	2017-02-03 04:27	44
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     25447 Feb  3 10:51 RSWGD1-17_SSGM_Confirmed_File__20170203.csv.20170203105150586	10:51	2/3/2017		2017-03-02	10:51:50	0.452662	Fri	5	30	2017-02-03 10:51	44
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3463 Feb  3 09:31 TIAACREFREPAT.csv.20170203093140226	9:31			2017-03-02	9:31:40	0.396991	Fri	5	32	2017-02-03 09:31	44
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       721 Feb  3 05:23 tokyofundtrades.in.201702031743.20170203052352000	 05:2	2/3/2017	17:43:00	2017-03-02	5:23:52	0.224907	Fri	5	33	2017-02-03 05:23	44
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       410 Feb  5 21:25 tokyofundtrades.in.201702060959.20170205212544845	 21:2	2/6/2017	9:59:00	2017-05-02	21:25:44	0.89287	Sun	7	33	2017-02-05 21:25	#N/A
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb  6 09:18 Alger_Orders_20170206091439.csv.20170206091823211	9:18	2/6/2017	9:14:39	2017-06-02	9:18:23	0.387766	Mon	1	1	2017-02-06 09:18	45
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      2636 Feb  6 11:04 alps_Orders_02062017100000.csv.20170206110402553	11:04	6/2/2017	10:00:00	2017-06-02	11:04:02	0.461134	Mon	1	2	2017-02-06 11:04	45
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1866 Feb  6 17:08 alps_Orders_02062017024000.csv.20170206170828607	17:08	6/2/2017	2:40:00	2017-06-02	17:08:28	0.714213	Mon	1	2	2017-02-06 17:08	45
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Feb  6 08:33 SSC_BAM_FXREQ_20170206_133027.csv.pgp.ndm05.20170206083319851	8:33	2/6/2017	13:30:27	2017-06-02	8:33:19	0.35647	Mon	1	3	2017-02-06 08:33	45
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb  6 10:31 SSC_BAM_FXREQ_20170206_153032.csv.pgp.ndm05.20170206103129203	10:31	2/6/2017	15:30:32	2017-06-02	10:31:29	0.43853	Mon	1	3	2017-02-06 10:31	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064541757	6:45			2017-06-02	6:45:41	0.281725	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064542050	6:45			2017-06-02	6:45:42	0.281736	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064542314	6:45			2017-06-02	6:45:42	0.281736	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064542664	6:45			2017-06-02	6:45:42	0.281736	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064542913	6:45			2017-06-02	6:45:42	0.281736	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064543297	6:45			2017-06-02	6:45:43	0.281748	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064543572	6:45			2017-06-02	6:45:43	0.281748	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064543890	6:45			2017-06-02	6:45:43	0.281748	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064544135	6:45			2017-06-02	6:45:44	0.281759	Mon	1	4	2017-02-06 06:45	45
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  6 06:45 BCRTOFX.txt.20170206064544541	6:45			2017-06-02	6:45:44	0.281759	Mon	1	4	2017-02-06 06:45	45
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7918 Feb  6 14:38 BRA_BRA_Ver_20170206.csv.20170206143817900	14:38	2/6/2017		2017-06-02	14:38:17	0.609919	Mon	1	5	2017-02-06 14:38	45
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Feb  6 16:34 CDPSfx_PHPorder.20170206.163500.csv.20170206163424963	16:34	2/6/2017	16:35:00	2017-06-02	16:34:24	0.690556	Mon	1	6	2017-02-06 16:34	45
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       357 Feb  6 16:34 CDPSfx_PHPorder.20170206.163000.csv.20170206163424719	16:34	2/6/2017	16:30:00	2017-06-02	16:34:24	0.690556	Mon	1	6	2017-02-06 16:34	45
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       168 Feb  6 04:16 scbcnhtrades1.in.201702061707.20170206041604281	4:16	2/6/2017	17:07:00	2017-06-02	4:16:04	0.177824	Mon	1	7	2017-02-06 04:16	45
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  6 04:16 scbcnhtrades2.in.201702061707.20170206041604721	4:16	2/6/2017	17:07:00	2017-06-02	4:16:04	0.177824	Mon	1	7	2017-02-06 04:16	45
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1741 Feb  6 09:49 SPOT_FET_Instructions_StateStreet_20170206-154124.csv.20170206094956548	9:49	2/6/2017	15:41:24	2017-06-02	9:49:56	0.409676	Mon	1	7	2017-02-06 09:49	45
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       280 Feb  6 06:52 CRUX_20170206.csv.20170206065215045	6:52	2/6/2017		2017-06-02	6:52:15	0.286285	Mon	1	8	2017-02-06 06:52	45
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       280 Feb  6 13:00 CRUX_20170206.csv.20170206130011323	13:00	2/6/2017		2017-06-02	13:00:11	0.541794	Mon	1	8	2017-02-06 13:00	45
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       139 Feb  6 16:58 02062017_GAM_GAM_STAR_GS.20170206.csv.20170206165826520	16:58	2/6/2017		2017-06-02	16:58:26	0.707245	Mon	1	9	2017-02-06 16:58	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Feb  6 10:34 trade10.dat.20170206103400026	10:34			2017-06-02	10:34:00	0.440278	Mon	1	10	2017-02-06 10:34	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Feb  6 12:34 trade10.dat.20170206123408611	12:34			2017-06-02	12:34:08	0.523704	Mon	1	10	2017-02-06 12:34	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  6 14:34 trade10.dat.20170206143417408	14:34			2017-06-02	14:34:17	0.607141	Mon	1	10	2017-02-06 14:34	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Feb  6 16:24 trade10.dat.20170206162424235	16:24			2017-06-02	16:24:24	0.683611	Mon	1	10	2017-02-06 16:24	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  6 17:04 trade10.dat.20170206170428006	17:04			2017-06-02	17:04:28	0.711435	Mon	1	10	2017-02-06 17:04	45
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  6 18:04 trade10.dat.20170206180433995	18:04			2017-06-02	18:04:33	0.75316	Mon	1	10	2017-02-06 18:04	45
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    374277 Feb  6 09:00 passporttrans.20170206.csv.20170206090020780	9:00	2/6/2017		2017-06-02	9:00:20	0.375231	Mon	1	15	2017-02-06 09:00	45
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1654 Feb  6 08:32 HighlandCapitalManagementRecon201702060730.csv.20170206083219566	8:32	2/6/2017	7:30:00	2017-06-02	8:32:19	0.355775	Mon	1	16	2017-02-06 08:32	45
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       302 Feb  6 00:11 HSBC-LKR.in.06022017-1.20170206001152067	 00:1	6/2/2017		2017-06-02	0:11:52	0.008241	Mon	1	17	2017-02-06 00:11	45
John Hancock Investments	HAN_TRANS_HANVER_20170206.csv.20170206153621007	15:36	2/6/2017		2017-06-02	15:36:21	0.650243	Mon	1	18	2017-02-06 15:36	45
John Hancock Investments	HAN_TRANS_HANVER_20170206.csv.20170206153621007	15:36	2/6/2017		2017-06-02	15:36:21	0.650243	Mon	1	18	2017-02-06 15:36	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Feb  6 03:00 FT_fx_20170206_085833.csv.20170206030000475	3:00	2/6/2017	8:58:33	2017-06-02	3:00:00	0.125	Mon	1	26	2017-02-06 03:00	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       363 Feb  6 03:36 INV_fx_20170206_093501.csv.20170206033603112	3:36	2/6/2017	9:35:01	2017-06-02	3:36:03	0.150035	Mon	1	26	2017-02-06 03:36	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb  6 04:42 FT_fx_20170206_104032.csv.20170206044206744	4:42	2/6/2017	10:40:32	2017-06-02	4:42:06	0.195903	Mon	1	26	2017-02-06 04:42	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb  6 05:04 INV_fx_20170206_110144.csv.20170206050407658	5:04	2/6/2017	11:01:44	2017-06-02	5:04:07	0.211192	Mon	1	26	2017-02-06 05:04	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       227 Feb  6 05:10 INV_fx_20170206_110646.csv.20170206051009093	5:10	2/6/2017	11:06:46	2017-06-02	5:10:09	0.215382	Mon	1	26	2017-02-06 05:10	45
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb  6 05:10 FT_fx_20170206_110741.csv.20170206051009371	5:10	2/6/2017	11:07:41	2017-06-02	5:10:09	0.215382	Mon	1	26	2017-02-06 05:10	45
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        56 Feb  6 03:20 citicnhtrades.in.201702061607.20170206032001612	3:20	2/6/2017	16:07:00	2017-06-02	3:20:01	0.1389	Mon	1	28	2017-02-06 03:20	45
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  6 04:24 citicnhtrades.in.201702061717.20170206042405638	4:24	2/6/2017	17:17:00	2017-06-02	4:24:05	0.183391	Mon	1	28	2017-02-06 04:24	45
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       126 Feb  6 04:24 hsbccnhtrades.in.201702061717.20170206042405929	4:24	2/6/2017	17:17:00	2017-06-02	4:24:05	0.183391	Mon	1	29	2017-02-06 04:24	45
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27830 Feb  6 10:46 RSWGD1-17_SSGM_Confirmed_File__20170206.csv.20170206104600840	10:46	2/6/2017		2017-06-02	10:46:00	0.448611	Mon	1	30	2017-02-06 10:46	45
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       519 Feb  6 09:33 tcwta20170206.csv.20170206093355228	9:33	2/6/2017		2017-06-02	9:33:55	0.398553	Mon	1	31	2017-02-06 09:33	45
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2697 Feb  6 09:31 TIAACREFREPAT.csv.20170206093154473	9:31			2017-06-02	9:31:54	0.397153	Mon	1	32	2017-02-06 09:31	45
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       491 Feb  6 10:31 TIAACREFREPAT.csv.20170206103159535	10:31			2017-06-02	10:31:59	0.438877	Mon	1	32	2017-02-06 10:31	45
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       458 Feb  6 22:32 tokyofundtrades.in.201702071113.20170206223222156	 22:3	2/7/2017	11:13:00	2017-06-02	22:32:22	0.939144	Mon	1	33	2017-02-06 22:32	45
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1431 Feb  7 04:31 SSC_BAM_FXREQ_20170207_093006.csv.pgp.ndm05.20170207043144025	4:31	2/7/2017	9:30:06	2017-07-02	4:31:44	0.188704	Tue	2	3	2017-02-07 04:31	46
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb  7 10:32 SSC_BAM_FXREQ_20170207_153023.csv.pgp.ndm05.20170207103237305	10:32	2/7/2017	15:30:23	2017-07-02	10:32:37	0.439317	Tue	2	3	2017-02-07 10:32	46
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Feb  7 11:32 SSC_BAM_FXREQ_20170207_163025.csv.pgp.ndm05.20170207113248875	11:32	2/7/2017	16:30:25	2017-07-02	11:32:48	0.481111	Tue	2	3	2017-02-07 11:32	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064649633	6:46			2017-07-02	6:46:49	0.282512	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064649967	6:46			2017-07-02	6:46:49	0.282512	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064650162	6:46			2017-07-02	6:46:50	0.282523	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064650375	6:46			2017-07-02	6:46:50	0.282523	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064650589	6:46			2017-07-02	6:46:50	0.282523	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064650789	6:46			2017-07-02	6:46:50	0.282523	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064650968	6:46			2017-07-02	6:46:50	0.282523	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064651172	6:46			2017-07-02	6:46:51	0.282535	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064651373	6:46			2017-07-02	6:46:51	0.282535	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064651569	6:46			2017-07-02	6:46:51	0.282535	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064651775	6:46			2017-07-02	6:46:51	0.282535	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064651968	6:46			2017-07-02	6:46:51	0.282535	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064652180	6:46			2017-07-02	6:46:52	0.282546	Tue	2	4	2017-02-07 06:46	46
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  7 06:46 BCRTOFX.txt.20170207064652372	6:46			2017-07-02	6:46:52	0.282546	Tue	2	4	2017-02-07 06:46	46
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      6728 Feb  7 14:37 BRA_BRA_Ver_20170207.csv.20170207143705056	14:37	2/7/2017		2017-07-02	14:37:05	0.609086	Tue	2	5	2017-02-07 14:37	46
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Feb  7 16:35 CDPSfx_MYRorder.20170207.163500.csv.20170207163510624	16:35	2/7/2017	16:35:00	2017-07-02	16:35:10	0.691088	Tue	2	6	2017-02-07 16:35	46
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       358 Feb  7 16:35 CDPSfx_TWDorder.20170207.163500.csv.20170207163510871	16:35	2/7/2017	16:35:00	2017-07-02	16:35:10	0.691088	Tue	2	6	2017-02-07 16:35	46
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       113 Feb  7 04:22 scbcnhtrades1.in.201702071713.20170207042242707	4:22	2/7/2017	17:13:00	2017-07-02	4:22:42	0.182431	Tue	2	7	2017-02-07 04:22	46
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  7 04:22 scbcnhtrades2.in.201702071713.20170207042242941	4:22	2/7/2017	17:13:00	2017-07-02	4:22:42	0.182431	Tue	2	7	2017-02-07 04:22	46
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       869 Feb  7 09:56 SPOT_FET_Instructions_StateStreet_20170207-154609.csv.20170207095634608	9:56	2/7/2017	15:46:09	2017-07-02	9:56:34	0.414282	Tue	2	7	2017-02-07 09:56	46
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       135 Feb  7 16:23 02072017_GAM_GAM_STAR_GS.20170207.csv.20170207162309073	16:23	2/7/2017		2017-07-02	16:23:09	0.682743	Tue	2	9	2017-02-07 16:23	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     22564 Feb  7 10:34 trade10.dat.20170207103437774	10:34			2017-07-02	10:34:37	0.440706	Tue	2	10	2017-02-07 10:34	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5638 Feb  7 12:34 trade10.dat.20170207123457386	12:34			2017-07-02	12:34:57	0.524271	Tue	2	10	2017-02-07 12:34	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb  7 14:35 trade10.dat.20170207143504476	14:35			2017-07-02	14:35:04	0.607685	Tue	2	10	2017-02-07 14:35	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     69002 Feb  7 16:25 trade10.dat.20170207162509471	16:25			2017-07-02	16:25:09	0.684132	Tue	2	10	2017-02-07 16:25	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  7 17:05 trade10.dat.20170207170513023	17:05			2017-07-02	17:05:13	0.711956	Tue	2	10	2017-02-07 17:05	46
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  7 18:03 trade10.dat.20170207180319666	18:03			2017-07-02	18:03:19	0.752303	Tue	2	10	2017-02-07 18:03	46
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       598 Feb  7 19:17 FT_Orders_20170207.csv.20170207191725196	19:17	2/7/2017		2017-07-02	19:17:25	0.803762	Tue	2	12	2017-02-07 19:17	46
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    323368 Feb  7 09:28 passporttrans.20170207.csv.20170207092832958	9:28	2/7/2017		2017-07-02	9:28:32	0.394815	Tue	2	15	2017-02-07 09:28	46
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Feb  7 08:32 HighlandCapitalManagementRecon201702070730.csv.20170207083259374	8:32	2/7/2017	7:30:00	2017-07-02	8:32:59	0.356238	Tue	2	16	2017-02-07 08:32	46
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       572 Feb  7 02:18 HSBC-LKR.in.07022017-1.20170207021834491	 02:1	7/2/2017		2017-07-02	2:18:34	0.096227	Tue	2	17	2017-02-07 02:18	46
John Hancock Investments	HAN_TRANS_HANVER_20170207.csv.20170207153506961	15:35	2/7/2017		2017-07-02	15:35:06	0.649375	Tue	2	18	2017-02-07 15:35	46
John Hancock Investments	HAN_TRANS_HANVER_20170207.csv.20170207153506961	15:35	2/7/2017		2017-07-02	15:35:06	0.649375	Tue	2	18	2017-02-07 15:35	46
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       353 Feb  7 05:32 NOS_SFX_20170203-06.csv.20170207053247470	5:32	2/3/2017		2017-07-02	5:32:47	0.2311	Tue	2	21	2017-02-07 05:32	46
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Feb  7 02:58 FT_fx_20170207_085715.csv.20170207025838011	2:58	2/7/2017	8:57:15	2017-07-02	2:58:38	0.124051	Tue	2	26	2017-02-07 02:58	46
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       230 Feb  7 03:30 INV_fx_20170207_092820.csv.20170207033040691	3:30	2/7/2017	9:28:20	2017-07-02	3:30:40	0.146296	Tue	2	26	2017-02-07 03:30	46
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb  7 04:32 INV_fx_20170207_103024.csv.20170207043244292	4:32	2/7/2017	10:30:24	2017-07-02	4:32:44	0.189398	Tue	2	26	2017-02-07 04:32	46
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Feb  7 04:38 FT_fx_20170207_103601.csv.20170207043844726	4:38	2/7/2017	10:36:01	2017-07-02	4:38:44	0.193565	Tue	2	26	2017-02-07 04:38	46
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       180 Feb  7 03:24 citicnhtrades.in.201702071613.20170207032440267	3:24	2/7/2017	16:13:00	2017-07-02	3:24:40	0.14213	Tue	2	28	2017-02-07 03:24	46
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  7 04:22 citicnhtrades.in.201702071717.20170207042243346	4:22	2/7/2017	17:17:00	2017-07-02	4:22:43	0.182442	Tue	2	28	2017-02-07 04:22	46
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       365 Feb  7 04:22 hsbccnhtrades.in.201702071717.20170207042243556	4:22	2/7/2017	17:17:00	2017-07-02	4:22:43	0.182442	Tue	2	29	2017-02-07 04:22	46
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28716 Feb  7 11:06 RSWGD1-17_SSGM_Confirmed_File__20170207.csv.20170207110644508	11:06	2/7/2017		2017-07-02	11:06:44	0.463009	Tue	2	30	2017-02-07 11:06	46
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2837 Feb  7 09:32 TIAACREFREPAT.csv.20170207093233715	9:32			2017-07-02	9:32:33	0.397604	Tue	2	32	2017-02-07 09:32	46
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       167 Feb  7 10:50 TrinityStreetFX_070217.csv.20170207105039106	10:50			2017-07-02	10:50:39	0.45184	Tue	2	34	2017-02-07 10:50	46
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       135 Feb  8 08:41 Alger_Orders_20170208083931.csv.20170208084145168	8:41	2/8/2017	8:39:31	2017-08-02	8:41:45	0.362326	Wed	3	1	2017-02-08 08:41	47
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3285 Feb  8 12:06 alps_Orders_02082017101000.csv.20170208120615554	12:06	8/2/2017	10:10:00	2017-08-02	12:06:15	0.50434	Wed	3	2	2017-02-08 12:06	47
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1107 Feb  8 16:20 alps_Orders_02082017022000.csv.20170208162032414	16:20	8/2/2017	2:20:00	2017-08-02	16:20:32	0.680926	Wed	3	2	2017-02-08 16:20	47
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1466 Feb  8 04:32 SSC_BAM_FXREQ_20170208_093024.csv.pgp.ndm05.20170208043258939	4:32	2/8/2017	9:30:24	2017-08-02	4:32:58	0.18956	Wed	3	3	2017-02-08 04:32	47
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb  8 05:33 SSC_BAM_FXREQ_20170208_103026.csv.pgp.ndm05.20170208053302521	5:33	2/8/2017	10:30:26	2017-08-02	5:33:02	0.231273	Wed	3	3	2017-02-08 05:33	47
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1401 Feb  8 06:33 SSC_BAM_FXREQ_20170208_113029.csv.pgp.ndm05.20170208063306034	6:33	2/8/2017	11:30:29	2017-08-02	6:33:06	0.272986	Wed	3	3	2017-02-08 06:33	47
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1456 Feb  8 10:31 SSC_BAM_FXREQ_20170208_153039.csv.pgp.ndm05.20170208103125281	10:31	2/8/2017	15:30:39	2017-08-02	10:31:25	0.438484	Wed	3	3	2017-02-08 10:31	47
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb  8 12:33 SSC_BAM_FXREQ_20170208_173046.csv.pgp.ndm05.20170208123347602	12:33	2/8/2017	17:30:46	2017-08-02	12:33:47	0.523461	Wed	3	3	2017-02-08 12:33	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064636702	6:46			2017-08-02	6:46:36	0.282361	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064636980	6:46			2017-08-02	6:46:36	0.282361	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064637172	6:46			2017-08-02	6:46:37	0.282373	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064637334	6:46			2017-08-02	6:46:37	0.282373	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064637551	6:46			2017-08-02	6:46:37	0.282373	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064637772	6:46			2017-08-02	6:46:37	0.282373	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064638005	6:46			2017-08-02	6:46:38	0.282384	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064638187	6:46			2017-08-02	6:46:38	0.282384	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064638371	6:46			2017-08-02	6:46:38	0.282384	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064638609	6:46			2017-08-02	6:46:38	0.282384	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064638981	6:46			2017-08-02	6:46:38	0.282384	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064639182	6:46			2017-08-02	6:46:39	0.282396	Wed	3	4	2017-02-08 06:46	47
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  8 06:46 BCRTOFX.txt.20170208064639402	6:46			2017-08-02	6:46:39	0.282396	Wed	3	4	2017-02-08 06:46	47
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7460 Feb  8 14:36 BRA_BRA_Ver_20170208.csv.20170208143626559	14:36	2/8/2017		2017-08-02	14:36:26	0.608634	Wed	3	5	2017-02-08 14:36	47
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       359 Feb  8 10:33 CDPSfx_IDRorder.20170208.103500.csv.20170208103355667	10:33	2/8/2017	10:35:00	2017-08-02	10:33:55	0.44022	Wed	3	6	2017-02-08 10:33	47
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       355 Feb  8 17:34 CDPSfx_TWDorder.20170208.173500.csv.20170208173439781	17:34	2/8/2017	17:35:00	2017-08-02	17:34:39	0.732396	Wed	3	6	2017-02-08 17:34	47
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1143 Feb  8 09:21 SPOT_FET_Instructions_StateStreet_20170208-151310.csv.20170208092149208	9:21	2/8/2017	15:13:10	2017-08-02	9:21:49	0.39015	Wed	3	7	2017-02-08 09:21	47
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       141 Feb  8 16:46 02082017_GAM_GAM_STAR_GS.20170208.csv.20170208164634489	16:46	2/8/2017		2017-08-02	16:46:34	0.699005	Wed	3	9	2017-02-08 16:46	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     10412 Feb  8 10:33 trade10.dat.20170208103355970	10:33			2017-08-02	10:33:55	0.44022	Wed	3	10	2017-02-08 10:33	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      7374 Feb  8 12:34 trade10.dat.20170208123417961	12:34			2017-08-02	12:34:17	0.523808	Wed	3	10	2017-02-08 12:34	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  8 14:34 trade10.dat.20170208143425977	14:34			2017-08-02	14:34:25	0.607234	Wed	3	10	2017-02-08 14:34	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     10846 Feb  8 16:24 trade10.dat.20170208162432869	16:24			2017-08-02	16:24:32	0.683704	Wed	3	10	2017-02-08 16:24	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  8 17:04 trade10.dat.20170208170436056	17:04			2017-08-02	17:04:36	0.711528	Wed	3	10	2017-02-08 17:04	47
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  8 18:04 trade10.dat.20170208180442595	18:04			2017-08-02	18:04:42	0.753264	Wed	3	10	2017-02-08 18:04	47
Franklin Templeton	-rw-r--r--   1 ftpgmrin ftpgmr       567 Feb  8 17:46 FT_Orders_20170208.csv.20170208174641630	17:46	2/8/2017		2017-08-02	17:46:41	0.740752	Wed	3	12	2017-02-08 17:46	47
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    391673 Feb  8 09:15 passporttrans.20170208.csv.20170208091547711	9:15	2/8/2017		2017-08-02	9:15:47	0.385961	Wed	3	15	2017-02-08 09:15	47
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2107 Feb  8 08:31 HighlandCapitalManagementRecon201702080730.csv.20170208083144378	8:31	2/8/2017	7:30:00	2017-08-02	8:31:44	0.35537	Wed	3	16	2017-02-08 08:31	47
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       937 Feb  8 01:47 HSBC-LKR.in.08022017-1.20170208014748761	 01:4	8/2/2017		2017-08-02	1:47:48	0.074861	Wed	3	17	2017-02-08 01:47	47
John Hancock Investments	HAN_TRANS_HANVER_20170208.csv.20170208153429652	15:34	2/8/2017		2017-08-02	15:34:29	0.648947	Wed	3	18	2017-02-08 15:34	47
John Hancock Investments	HAN_TRANS_HANVER_20170208.csv.20170208153429652	15:34	2/8/2017		2017-08-02	15:34:29	0.648947	Wed	3	18	2017-02-08 15:34	47
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Feb  8 09:01 NOS_SFX_20170208.csv.20170208090146468	9:01	2/8/2017		2017-08-02	9:01:46	0.376227	Wed	3	21	2017-02-08 09:01	47
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb  8 12:48 PAXStateStreetFX_Orders_020817.txt.20170208124819022	12:48	2/8/2017		2017-08-02	12:48:19	0.533553	Wed	3	23	2017-02-08 12:48	47
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       203 Feb  8 11:20 PGI_Orders_20170208101643.csv.20170208112006016	11:20	2/8/2017	10:16:43	2017-08-02	11:20:06	0.472292	Wed	3	24	2017-02-08 11:20	47
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Feb  8 02:47 FT_fx_20170208_084429.csv.20170208024722500	2:47	2/8/2017	8:44:29	2017-08-02	2:47:22	0.116227	Wed	3	26	2017-02-08 02:47	47
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb  8 03:27 INV_fx_20170208_092529.csv.20170208032725057	3:27	2/8/2017	9:25:29	2017-08-02	3:27:25	0.144039	Wed	3	26	2017-02-08 03:27	47
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Feb  8 04:21 FT_fx_20170208_101946.csv.20170208042127356	4:21	2/8/2017	10:19:46	2017-08-02	4:21:27	0.181563	Wed	3	26	2017-02-08 04:21	47
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  8 04:47 INV_fx_20170208_104439.csv.20170208044729732	4:47	2/8/2017	10:44:39	2017-08-02	4:47:29	0.199641	Wed	3	26	2017-02-08 04:47	47
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb  8 05:37 INV_fx_20170208_113452.csv.20170208053733272	5:37	2/8/2017	11:34:52	2017-08-02	5:37:33	0.23441	Wed	3	26	2017-02-08 05:37	47
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        57 Feb  8 03:21 citicnhtrades.in.201702081609.20170208032124230	3:21	2/8/2017	16:09:00	2017-08-02	3:21:24	0.139861	Wed	3	28	2017-02-08 03:21	47
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  8 04:29 citicnhtrades.in.201702081715.20170208042928595	4:29	2/8/2017	17:15:00	2017-08-02	4:29:28	0.18713	Wed	3	28	2017-02-08 04:29	47
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       429 Feb  8 04:29 hsbccnhtrades.in.201702081715.20170208042928317	4:29	2/8/2017	17:15:00	2017-08-02	4:29:28	0.18713	Wed	3	29	2017-02-08 04:29	47
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27645 Feb  8 10:19 RSWGD1-17_SSGM_Confirmed_File__20170208.csv.20170208101954590	10:19	2/8/2017		2017-08-02	10:19:54	0.430486	Wed	3	30	2017-02-08 10:19	47
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3130 Feb  8 09:31 TIAACREFREPAT.csv.20170208093150021	9:31			2017-08-02	9:31:50	0.397106	Wed	3	32	2017-02-08 09:31	47
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       318 Feb  8 13:32 TIAACREFREPAT.csv.20170208133222219	13:32			2017-08-02	13:32:22	0.564144	Wed	3	32	2017-02-08 13:32	47
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       477 Feb  8 21:30 tokyofundtrades.in.201702091008.20170208213056507	 21:3	2/9/2017	10:08:00	2017-08-02	21:30:56	0.896481	Wed	3	33	2017-02-08 21:30	47
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       167 Feb  8 03:07 TrinityStreetFX_020817.csv.20170208030723463	3:07			2017-08-02	3:07:23	0.130127	Wed	3	34	2017-02-08 03:07	47
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       135 Feb  9 09:39 Alger_Orders_20170209093714.csv.20170209093911412	9:39	2/9/2017	9:37:14	2017-09-02	9:39:11	0.402211	Thu	4	1	2017-02-09 09:39	48
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Feb  9 04:31 SSC_BAM_FXREQ_20170209_093022.csv.pgp.ndm05.20170209043151983	4:31	2/9/2017	9:30:22	2017-09-02	4:31:51	0.188785	Thu	4	3	2017-02-09 04:31	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063957130	6:39			2017-09-02	6:39:57	0.277743	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063957418	6:39			2017-09-02	6:39:57	0.277743	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063957631	6:39			2017-09-02	6:39:57	0.277743	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063957816	6:39			2017-09-02	6:39:57	0.277743	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063958043	6:39			2017-09-02	6:39:58	0.277755	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063958232	6:39			2017-09-02	6:39:58	0.277755	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063958439	6:39			2017-09-02	6:39:58	0.277755	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063958624	6:39			2017-09-02	6:39:58	0.277755	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063958838	6:39			2017-09-02	6:39:58	0.277755	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063959032	6:39			2017-09-02	6:39:59	0.277766	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063959276	6:39			2017-09-02	6:39:59	0.277766	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063959467	6:39			2017-09-02	6:39:59	0.277766	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063959681	6:39			2017-09-02	6:39:59	0.277766	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:39 BCRTOFX.txt.20170209063959803	6:39			2017-09-02	6:39:59	0.277766	Thu	4	4	2017-02-09 06:39	48
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb  9 06:40 BCRTOFX.txt.20170209064000003	6:40			2017-09-02	6:40:00	0.277778	Thu	4	4	2017-02-09 06:40	48
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      8367 Feb  9 14:35 BRA_BRA_Ver_20170209.csv.20170209143553825	14:35	2/9/2017		2017-09-02	14:35:53	0.608252	Thu	4	5	2017-02-09 14:35	48
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       333 Feb  9 09:07 CDPSfx_TWDorder.20170209.090603.csv.20170209090708071	9:07	2/9/2017	9:06:03	2017-09-02	9:07:08	0.379954	Thu	4	6	2017-02-09 09:07	48
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb  9 16:01 CDPSfx_PENorder.20170209.163500.csv.20170209160158993	16:01	2/9/2017	16:35:00	2017-09-02	16:01:58	0.668032	Thu	4	6	2017-02-09 16:01	48
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb  9 16:34 CDPSfx_BRLorder.20170209.163500.csv.20170209163402322	16:34	2/9/2017	16:35:00	2017-09-02	16:34:02	0.690301	Thu	4	6	2017-02-09 16:34	48
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb  9 16:38 CDPSfx_BRLorder.20170209.163500.csv.20170209163803029	16:38	2/9/2017	16:35:00	2017-09-02	16:38:03	0.69309	Thu	4	6	2017-02-09 16:38	48
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb  9 04:16 scbcnhtrades1.in.201702091710.20170209041650474	4:16	2/9/2017	17:10:00	2017-09-02	4:16:50	0.178356	Thu	4	7	2017-02-09 04:16	48
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Feb  9 04:16 scbcnhtrades2.in.201702091710.20170209041650902	4:16	2/9/2017	17:10:00	2017-09-02	4:16:50	0.178356	Thu	4	7	2017-02-09 04:16	48
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1286 Feb  9 09:09 SPOT_FET_Instructions_StateStreet_20170209-145934.csv.20170209090908420	9:09	2/9/2017	14:59:34	2017-09-02	9:09:08	0.381343	Thu	4	7	2017-02-09 09:09	48
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       417 Feb  9 16:34 02092017_GAM_GAM_STAR_GS.20170209.csv.20170209163401934	16:34	2/9/2017		2017-09-02	16:34:01	0.690289	Thu	4	9	2017-02-09 16:34	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Feb  9 10:35 trade10.dat.20170209103516232	10:35			2017-09-02	10:35:16	0.441157	Thu	4	10	2017-02-09 10:35	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6940 Feb  9 12:35 trade10.dat.20170209123546164	12:35			2017-09-02	12:35:46	0.524838	Thu	4	10	2017-02-09 12:35	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb  9 14:33 trade10.dat.20170209143353351	14:33			2017-09-02	14:33:53	0.606863	Thu	4	10	2017-02-09 14:33	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb  9 16:24 trade10.dat.20170209162401094	16:24			2017-09-02	16:24:01	0.683345	Thu	4	10	2017-02-09 16:24	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  9 17:04 trade10.dat.20170209170404334	17:04			2017-09-02	17:04:04	0.711157	Thu	4	10	2017-02-09 17:04	48
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb  9 18:03 trade10.dat.20170209180339539	18:03			2017-09-02	18:03:39	0.752535	Thu	4	10	2017-02-09 18:03	48
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    355359 Feb  9 09:05 passporttrans.20170209.csv.20170209090506954	9:05	2/9/2017		2017-09-02	9:05:06	0.378542	Thu	4	15	2017-02-09 09:05	48
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1661 Feb  9 08:33 HighlandCapitalManagementRecon201702090730.csv.20170209083305483	8:33	2/9/2017	7:30:00	2017-09-02	8:33:05	0.356308	Thu	4	16	2017-02-09 08:33	48
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       663 Feb  9 01:45 HSBC-LKR.in.09022017-1.20170209014511745	 01:4	9/2/2017		2017-09-02	1:45:11	0.073044	Thu	4	17	2017-02-09 01:45	48
John Hancock Investments	HAN_TRANS_HANVER_20170209.csv.20170209153956759	15:39	2/9/2017		2017-09-02	15:39:56	0.652731	Thu	4	18	2017-02-09 15:39	48
John Hancock Investments	HAN_TRANS_HANVER_20170209.csv.20170209153956759	15:39	2/9/2017		2017-09-02	15:39:56	0.652731	Thu	4	18	2017-02-09 15:39	48
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       210 Feb  9 12:39 PGI_Orders_20170209113805.csv.20170209123946607	12:39	2/9/2017	11:38:05	2017-09-02	12:39:46	0.527616	Thu	4	24	2017-02-09 12:39	48
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb  9 02:54 FT_fx_20170209_085330.csv.20170209025446312	2:54	2/9/2017	8:53:30	2017-09-02	2:54:46	0.121366	Thu	4	26	2017-02-09 02:54	48
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb  9 03:14 INV_fx_20170209_091325.csv.20170209031447120	3:14	2/9/2017	9:13:25	2017-09-02	3:14:47	0.135266	Thu	4	26	2017-02-09 03:14	48
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Feb  9 05:46 FT_fx_20170209_114445.csv.20170209054655389	5:46	2/9/2017	11:44:45	2017-09-02	5:46:55	0.240914	Thu	4	26	2017-02-09 05:46	48
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28776 Feb  9 10:13 RSWGD1-17_SSGM_Confirmed_File__20170209.csv.20170209101314385	10:13	2/9/2017		2017-09-02	10:13:14	0.425856	Thu	4	30	2017-02-09 10:13	48
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       512 Feb  9 10:17 tcwta20170209.csv.20170209101714824	10:17	2/9/2017		2017-09-02	10:17:14	0.428634	Thu	4	31	2017-02-09 10:17	48
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2531 Feb  9 09:31 TIAACREFREPAT.csv.20170209093110237	9:31			2017-09-02	9:31:10	0.396644	Thu	4	32	2017-02-09 09:31	48
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       406 Feb  9 21:19 tokyofundtrades.in.201702100952.20170209211952728	 21:1	2/10/2017	9:52:00	2017-09-02	21:19:52	0.888796	Thu	4	33	2017-02-09 21:19	48
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Feb 10 10:48 Alger_Orders_20170210104606.csv.20170210104816135	10:48	2/10/2017	10:46:06	2017-10-02	10:48:16	0.450185	Fri	5	1	2017-02-10 10:48	49
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       261 Feb 10 12:29 Alger_Orders_20170210122741.csv.20170210122908016	12:29	2/10/2017	12:27:41	2017-10-02	12:29:08	0.520231	Fri	5	1	2017-02-10 12:29	49
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3277 Feb 10 12:17 alps_Orders_02102017102000.csv.20170210121706639	12:17	10/2/2017	10:20:00	2017-10-02	12:17:06	0.511875	Fri	5	2	2017-02-10 12:17	49
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1504 Feb 10 04:32 SSC_BAM_FXREQ_20170210_093026.csv.pgp.ndm05.20170210043250259	4:32	2/10/2017	9:30:26	2017-10-02	4:32:50	0.189468	Fri	5	3	2017-02-10 04:32	49
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1434 Feb 10 10:33 SSC_BAM_FXREQ_20170210_153038.csv.pgp.ndm05.20170210103343402	10:33	2/10/2017	15:30:38	2017-10-02	10:33:43	0.440081	Fri	5	3	2017-02-10 10:33	49
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb 10 12:33 SSC_BAM_FXREQ_20170210_173043.csv.pgp.ndm05.20170210123338652	12:33	2/10/2017	17:30:43	2017-10-02	12:33:38	0.523356	Fri	5	3	2017-02-10 12:33	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064026028	6:40			2017-10-02	6:40:26	0.278079	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064026238	6:40			2017-10-02	6:40:26	0.278079	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064026464	6:40			2017-10-02	6:40:26	0.278079	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064026653	6:40			2017-10-02	6:40:26	0.278079	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064026834	6:40			2017-10-02	6:40:26	0.278079	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064027042	6:40			2017-10-02	6:40:27	0.27809	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064027255	6:40			2017-10-02	6:40:27	0.27809	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064027464	6:40			2017-10-02	6:40:27	0.27809	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064027653	6:40			2017-10-02	6:40:27	0.27809	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064027867	6:40			2017-10-02	6:40:27	0.27809	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064028069	6:40			2017-10-02	6:40:28	0.278102	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064028288	6:40			2017-10-02	6:40:28	0.278102	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064028479	6:40			2017-10-02	6:40:28	0.278102	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064028662	6:40			2017-10-02	6:40:28	0.278102	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064028865	6:40			2017-10-02	6:40:28	0.278102	Fri	5	4	2017-02-10 06:40	49
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 10 06:40 BCRTOFX.txt.20170210064029076	6:40			2017-10-02	6:40:29	0.278113	Fri	5	4	2017-02-10 06:40	49
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7146 Feb 10 14:45 BRA_BRA_Ver_20170210.csv.20170210144517938	14:45	2/10/2017		2017-10-02	14:45:17	0.61478	Fri	5	5	2017-02-10 14:45	49
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb 10 10:46 CDPSfx_PENorder.20170210.104500.csv.20170210104615819	10:46	2/10/2017	10:45:00	2017-10-02	10:46:15	0.448785	Fri	5	6	2017-02-10 10:46	49
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb 10 10:46 CDPSfx_BRLorder.20170210.104500.csv.20170210104615510	10:46	2/10/2017	10:45:00	2017-10-02	10:46:15	0.448785	Fri	5	6	2017-02-10 10:46	49
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       359 Feb 10 12:35 CDPSfx_IDRorder.20170210.123500.csv.20170210123509086	12:35	2/10/2017	12:35:00	2017-10-02	12:35:09	0.52441	Fri	5	6	2017-02-10 12:35	49
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        58 Feb 10 05:04 scbcnhtrades1.in.201702101758.20170210050422016	5:04	2/10/2017	17:58:00	2017-10-02	5:04:22	0.211366	Fri	5	7	2017-02-10 05:04	49
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 10 05:06 scbcnhtrades2.in.201702101758.20170210050622388	5:06	2/10/2017	17:58:00	2017-10-02	5:06:22	0.212755	Fri	5	7	2017-02-10 05:06	49
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1862 Feb 10 11:02 SPOT_FET_Instructions_StateStreet_20170210-152157.csv.20170210110216896	11:02	2/10/2017	15:21:57	2017-10-02	11:02:16	0.459907	Fri	5	7	2017-02-10 11:02	49
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       136 Feb 10 16:19 02102017_GAM_GAM_STAR_GS.20170210.csv.20170210161923209	16:19	2/10/2017		2017-10-02	16:19:23	0.680127	Fri	5	9	2017-02-10 16:19	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Feb 10 10:34 trade10.dat.20170210103413821	10:34			2017-10-02	10:34:13	0.440428	Fri	5	10	2017-02-10 10:34	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     13450 Feb 10 12:35 trade10.dat.20170210123509376	12:35			2017-10-02	12:35:09	0.52441	Fri	5	10	2017-02-10 12:35	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 10 14:35 trade10.dat.20170210143517195	14:35			2017-10-02	14:35:17	0.607836	Fri	5	10	2017-02-10 14:35	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     14752 Feb 10 16:23 trade10.dat.20170210162323641	16:23			2017-10-02	16:23:23	0.682905	Fri	5	10	2017-02-10 16:23	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 10 17:03 trade10.dat.20170210170327528	17:03			2017-10-02	17:03:27	0.710729	Fri	5	10	2017-02-10 17:03	49
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 10 18:03 trade10.dat.20170210180331747	18:03			2017-10-02	18:03:31	0.752442	Fri	5	10	2017-02-10 18:03	49
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       215 Feb 10 00:26 FSS_Orders_20170210.csv.20170210002604619	0:26	2/10/2017		2017-10-02	0:26:04	0.018102	Fri	5	13	2017-02-10 00:26	49
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    384703 Feb 10 09:14 passporttrans.20170210.csv.20170210091407790	9:14	2/10/2017		2017-10-02	9:14:07	0.384803	Fri	5	15	2017-02-10 09:14	49
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Feb 10 08:32 HighlandCapitalManagementRecon201702100730.csv.20170210083235028	8:32	2/10/2017	7:30:00	2017-10-02	8:32:35	0.355961	Fri	5	16	2017-02-10 08:32	49
John Hancock Investments	HAN_TRANS_HANVER_20170210.csv.20170210153519804	15:35	2/10/2017		2017-10-02	15:35:19	0.649525	Fri	5	18	2017-02-10 15:35	49
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 10 11:39 PAXStateStreetFX_Orders_021017.txt.20170210113933533	11:39	2/10/2017		2017-10-02	11:39:33	0.485799	Fri	5	23	2017-02-10 11:39	49
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 10 13:29 PAXStateStreetFX_Orders_021017.txt.20170210132912378	13:29	2/10/2017		2017-10-02	13:29:12	0.561944	Fri	5	23	2017-02-10 13:29	49
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 10 16:31 PAXStateStreetFX_Orders_021017.txt.20170210163124482	16:31	2/10/2017		2017-10-02	16:31:24	0.688472	Fri	5	23	2017-02-10 16:31	49
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       211 Feb 10 10:44 PGI_Orders_20170210094230.csv.20170210104414718	10:44	2/10/2017	9:42:30	2017-10-02	10:44:14	0.447384	Fri	5	24	2017-02-10 10:44	49
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       207 Feb 10 11:23 PGI_Orders_20170210102129.csv.20170210112326261	11:23	2/10/2017	10:21:29	2017-10-02	11:23:26	0.474606	Fri	5	24	2017-02-10 11:23	49
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       283 Feb 10 14:03 PGI_Orders_20170210130136.csv.20170210140313993	14:03	2/10/2017	13:01:36	2017-10-02	14:03:13	0.585567	Fri	5	24	2017-02-10 14:03	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb 10 02:50 FT_fx_20170210_084811.csv.20170210025012907	2:50	2/10/2017	8:48:11	2017-10-02	2:50:12	0.118194	Fri	5	26	2017-02-10 02:50	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Feb 10 03:02 FT_fx_20170210_090010.csv.20170210030214449	3:02	2/10/2017	9:00:10	2017-10-02	3:02:14	0.126551	Fri	5	26	2017-02-10 03:02	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 10 03:20 INV_fx_20170210_091851.csv.20170210032015332	3:20	2/10/2017	9:18:51	2017-10-02	3:20:15	0.139063	Fri	5	26	2017-02-10 03:20	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Feb 10 04:44 FT_fx_20170210_104127.csv.20170210044420886	4:44	2/10/2017	10:41:27	2017-10-02	4:44:20	0.197454	Fri	5	26	2017-02-10 04:44	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Feb 10 04:58 FT_fx_20170210_105516.csv.20170210045821398	4:58	2/10/2017	10:55:16	2017-10-02	4:58:21	0.207188	Fri	5	26	2017-02-10 04:58	49
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       230 Feb 10 05:06 INV_fx_20170210_110506.csv.20170210050623394	5:06	2/10/2017	11:05:06	2017-10-02	5:06:23	0.212766	Fri	5	26	2017-02-10 05:06	49
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       525 Feb 10 03:22 citicnhtrades.in.201702101608.20170210032215813	3:22	2/10/2017	16:08:00	2017-10-02	3:22:15	0.140451	Fri	5	28	2017-02-10 03:22	49
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 10 04:32 citicnhtrades.in.201702101718.20170210043219694	4:32	2/10/2017	17:18:00	2017-10-02	4:32:19	0.189109	Fri	5	28	2017-02-10 04:32	49
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr      1010 Feb 10 04:32 hsbccnhtrades.in.201702101718.20170210043220017	4:32	2/10/2017	17:18:00	2017-10-02	4:32:20	0.18912	Fri	5	29	2017-02-10 04:32	49
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27768 Feb 10 11:41 RSWGD1-17_SSGM_Confirmed_File__20170210.csv.20170210114104119	11:41	2/10/2017		2017-10-02	11:41:04	0.486852	Fri	5	30	2017-02-10 11:41	49
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3618 Feb 10 09:32 TIAACREFREPAT.csv.20170210093209318	9:32			2017-10-02	9:32:09	0.397326	Fri	5	32	2017-02-10 09:32	49
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      1734 Feb 12 21:20 tokyofundtrades.in.201702131001.20170212212046629	 21:2	2/13/2017	10:01:00	2017-12-02	21:20:46	0.889421	Sun	7	33	2017-02-12 21:20	#N/A
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       332 Feb 13 08:56 Alger_Orders_20170213085522.csv.20170213085651131	8:56	2/13/2017	8:55:22	2017-13-02	8:56:51	0.372813	Mon	1	1	2017-13-2 8:56:51	50
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3176 Feb 13 16:21 alps_Orders_02132017022000.csv.20170213162119476	16:21	2/13/2017	2:20:00	2017-13-02	16:21:19	0.68147	Mon	1	2	2017-13-2 16:21:19	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1445 Feb 13 04:33 SSC_BAM_FXREQ_20170213_093007.csv.pgp.ndm05.20170213043336746	4:33	2/13/2017	9:30:07	2017-13-02	4:33:36	0.19	Mon	1	3	2017-13-2 4:33:36	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1415 Feb 13 05:31 SSC_BAM_FXREQ_20170213_103009.csv.pgp.ndm05.20170213053140627	5:31	2/13/2017	10:30:09	2017-13-02	5:31:40	0.230324	Mon	1	3	2017-13-2 5:31:40	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1455 Feb 13 06:32 SSC_BAM_FXREQ_20170213_113012.csv.pgp.ndm05.20170213063211951	6:32	2/13/2017	11:30:12	2017-13-02	6:32:11	0.27235	Mon	1	3	2017-13-2 6:32:11	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Feb 13 07:32 SSC_BAM_FXREQ_20170213_123014.csv.pgp.ndm05.20170213073217587	7:32	2/13/2017	12:30:14	2017-13-02	7:32:17	0.314086	Mon	1	3	2017-13-2 7:32:17	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb 13 09:32 SSC_BAM_FXREQ_20170213_143017.csv.pgp.ndm05.20170213093223907	9:32	2/13/2017	14:30:17	2017-13-02	9:32:23	0.397488	Mon	1	3	2017-13-2 9:32:23	50
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1406 Feb 13 11:32 SSC_BAM_FXREQ_20170213_163023.csv.pgp.ndm05.20170213113229185	11:32	2/13/2017	16:30:23	2017-13-02	11:32:29	0.480891	Mon	1	3	2017-13-2 11:32:29	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063912664	6:39			2017-13-02	6:39:12	0.277222	Mon	1	4	2017-13-2 6:39:12	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063912883	6:39			2017-13-02	6:39:12	0.277222	Mon	1	4	2017-13-2 6:39:12	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063913081	6:39			2017-13-02	6:39:13	0.277234	Mon	1	4	2017-13-2 6:39:13	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063913275	6:39			2017-13-02	6:39:13	0.277234	Mon	1	4	2017-13-2 6:39:13	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063913468	6:39			2017-13-02	6:39:13	0.277234	Mon	1	4	2017-13-2 6:39:13	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063913665	6:39			2017-13-02	6:39:13	0.277234	Mon	1	4	2017-13-2 6:39:13	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063913881	6:39			2017-13-02	6:39:13	0.277234	Mon	1	4	2017-13-2 6:39:13	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063914077	6:39			2017-13-02	6:39:14	0.277245	Mon	1	4	2017-13-2 6:39:14	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063914293	6:39			2017-13-02	6:39:14	0.277245	Mon	1	4	2017-13-2 6:39:14	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063914490	6:39			2017-13-02	6:39:14	0.277245	Mon	1	4	2017-13-2 6:39:14	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063914690	6:39			2017-13-02	6:39:14	0.277245	Mon	1	4	2017-13-2 6:39:14	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063914889	6:39			2017-13-02	6:39:14	0.277245	Mon	1	4	2017-13-2 6:39:14	50
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 13 06:39 BCRTOFX.txt.20170213063915075	6:39			2017-13-02	6:39:15	0.277257	Mon	1	4	2017-13-2 6:39:15	50
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7952 Feb 13 14:35 BRA_BRA_Ver_20170213.csv.20170213143514736	14:35	2/13/2017		2017-13-02	14:35:14	0.607801	Mon	1	5	2017-13-2 14:35:14	50
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Feb 13 04:34 scbcnhtrades1.in.201702131730.20170213043437251	4:34	2/13/2017	17:30:00	2017-13-02	4:34:37	0.190706	Mon	1	7	2017-13-2 4:34:37	50
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 13 04:34 scbcnhtrades2.in.201702131730.20170213043437440	4:34	2/13/2017	17:30:00	2017-13-02	4:34:37	0.190706	Mon	1	7	2017-13-2 4:34:37	50
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1145 Feb 13 10:08 SPOT_FET_Instructions_StateStreet_20170213-160035.csv.20170213100856473	10:08	2/13/2017	16:00:35	2017-13-02	10:08:56	0.42287	Mon	1	7	2017-13-2 10:08:56	50
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       120 Feb 13 16:37 02132017_GAM_GAM_STAR_GS.20170213.csv.20170213163721157	16:37	2/13/2017		2017-13-02	16:37:21	0.692604	Mon	1	9	2017-13-2 16:37:21	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Feb 13 10:34 trade10.dat.20170213103457842	10:34			2017-13-02	10:34:57	0.440938	Mon	1	10	2017-13-2 10:34:57	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Feb 13 12:35 trade10.dat.20170213123506228	12:35			2017-13-02	12:35:06	0.524375	Mon	1	10	2017-13-2 12:35:06	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 13 14:35 trade10.dat.20170213143514333	14:35			2017-13-02	14:35:14	0.607801	Mon	1	10	2017-13-2 14:35:14	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     50340 Feb 13 16:23 trade10.dat.20170213162319898	16:23			2017-13-02	16:23:19	0.682859	Mon	1	10	2017-13-2 16:23:19	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb 13 17:05 trade10.dat.20170213170523340	17:05			2017-13-02	17:05:23	0.712072	Mon	1	10	2017-13-2 17:05:23	50
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 13 18:03 trade10.dat.20170213180327563	18:03			2017-13-02	18:03:27	0.752396	Mon	1	10	2017-13-2 18:03:27	50
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       216 Feb 13 01:18 FSS_Orders_20170213.csv.20170213011826147	1:18	2/13/2017		2017-13-02	1:18:26	0.054468	Mon	1	13	2017-13-2 1:18:26	50
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    377384 Feb 13 09:04 passporttrans.20170213.csv.20170213090451663	9:04	2/13/2017		2017-13-02	9:04:51	0.378368	Mon	1	15	2017-13-2 9:04:51	50
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2038 Feb 13 08:32 HighlandCapitalManagementRecon201702130730.csv.20170213083250243	8:32	2/13/2017	7:30:00	2017-13-02	8:32:50	0.356134	Mon	1	16	2017-13-2 8:32:50	50
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       484 Feb 13 00:52 HSBC-LKR.in.13022017-1.20170213005224862	 00:5	2/13/2017		2017-13-02	0:52:24	0.036389	Mon	1	17	2017-13-2 0:52:24	50
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       211 Feb 13 01:32 HSBC-LKR.in.13022017-2.20170213013227280	 01:3	2/13/2017		2017-13-02	1:32:27	0.064201	Mon	1	17	2017-13-2 1:32:27	50
John Hancock Investments	HAN_TRANS_HANVER_20170213.csv.20170213153716891	15:37	2/13/2017		2017-13-02	15:37:16	0.65088	Mon	1	18	2017-13-2 15:37:16	50
John Hancock Investments	HAN_TRANS_HANVER_20170213.csv.20170213153716891	15:37	2/13/2017		2017-13-02	15:37:16	0.65088	Mon	1	18	2017-13-2 15:37:16	50
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 13 16:59 PAXStateStreetFX_Orders_021317.txt.20170213165922194	16:59	2/13/2017		2017-13-02	16:59:22	0.707894	Mon	1	23	2017-13-2 16:59:22	50
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb 13 02:46 FT_fx_20170213_084429.csv.20170213024630194	2:46	2/13/2017	8:44:29	2017-13-02	2:46:30	0.115625	Mon	1	26	2017-13-2 2:46:30	50
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 13 03:00 FT_fx_20170213_085737.csv.20170213030032034	3:00	2/13/2017	8:57:37	2017-13-02	3:00:32	0.12537	Mon	1	26	2017-13-2 3:00:32	50
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 13 03:16 INV_fx_20170213_091343.csv.20170213031633560	3:16	2/13/2017	9:13:43	2017-13-02	3:16:33	0.136493	Mon	1	26	2017-13-2 3:16:33	50
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 13 04:40 INV_fx_20170213_103739.csv.20170213044037810	4:40	2/13/2017	10:37:39	2017-13-02	4:40:37	0.194873	Mon	1	26	2017-13-2 4:40:37	50
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb 13 05:20 FT_fx_20170213_111814.csv.20170213052039973	5:20	2/13/2017	11:18:14	2017-13-02	5:20:39	0.222674	Mon	1	26	2017-13-2 5:20:39	50
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 13 03:22 citicnhtrades.in.201702131608.20170213032234237	3:22	2/13/2017	16:08:00	2017-13-02	3:22:34	0.140671	Mon	1	28	2017-13-2 3:22:34	50
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 13 04:32 citicnhtrades.in.201702131727.20170213043236562	4:32	2/13/2017	17:27:00	2017-13-02	4:32:36	0.189306	Mon	1	28	2017-13-2 4:32:36	50
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       299 Feb 13 04:34 hsbccnhtrades.in.201702131727.20170213043437094	4:34	2/13/2017	17:27:00	2017-13-02	4:34:37	0.190706	Mon	1	29	2017-13-2 4:34:37	50
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     29411 Feb 13 10:24 RSWGD1-17_SSGM_Confirmed_File__20170213.csv.20170213102457492	10:24	2/13/2017		2017-13-02	10:24:57	0.433993	Mon	1	30	2017-13-2 10:24:57	50
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3415 Feb 13 09:30 TIAACREFREPAT.csv.20170213093053398	9:30			2017-13-02	9:30:53	0.396447	Mon	1	32	2017-13-2 9:30:53	50
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       677 Feb 13 13:31 TIAACREFREPAT.csv.20170213133110652	13:31			2017-13-02	13:31:10	0.56331	Mon	1	32	2017-13-2 13:31:10	50
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       193 Feb 14 09:05 Alger_Orders_20170214090326.csv.20170214090547178	9:05	2/14/2017	9:03:26	2017-14-02	9:05:47	0.379016	Tue	2	1	2017-14-2 9:05:47	51
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Feb 14 14:10 Alger_Orders_20170214140616.csv.20170214141020696	14:10	2/14/2017	14:06:16	2017-14-02	14:10:20	0.590509	Tue	2	1	2017-14-2 14:10:20	51
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        65 Feb 14 15:52 Alger_Orders_20170214154942.csv.20170214155225703	15:52	2/14/2017	15:49:42	2017-14-02	15:52:25	0.6614	Tue	2	1	2017-14-2 15:52:25	51
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      5282 Feb 14 10:52 alps_Orders_02142017010000.csv.20170214105206403	10:52	2/14/2017	1:00:00	2017-14-02	10:52:06	0.452847	Tue	2	2	2017-14-2 10:52:06	51
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      5334 Feb 14 12:02 alps_Orders_02142017010000.csv.20170214120212001	12:02	2/14/2017	1:00:00	2017-14-02	12:02:12	0.501528	Tue	2	2	2017-14-2 12:02:12	51
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      8050 Feb 14 12:46 alps_Orders_02142017105000.csv.20170214124616408	12:46	2/14/2017	10:50:00	2017-14-02	12:46:16	0.53213	Tue	2	2	2017-14-2 12:46:16	51
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1772 Feb 14 17:28 alps_Orders_02142017110000.csv.20170214172834015	17:28	2/14/2017	11:00:00	2017-14-02	17:28:34	0.728171	Tue	2	2	2017-14-2 17:28:34	51
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1448 Feb 14 04:33 SSC_BAM_FXREQ_20170214_093016.csv.pgp.ndm05.20170214043300522	4:33	2/14/2017	9:30:16	2017-14-02	4:33:00	0.189583	Tue	2	3	2017-14-2 4:33:00	51
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb 14 07:33 SSC_BAM_FXREQ_20170214_123022.csv.pgp.ndm05.20170214073313058	7:33	2/14/2017	12:30:22	2017-14-02	7:33:13	0.314734	Tue	2	3	2017-14-2 7:33:13	51
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1446 Feb 14 11:31 SSC_BAM_FXREQ_20170214_163032.csv.pgp.ndm05.20170214113135904	11:31	2/14/2017	16:30:32	2017-14-02	11:31:35	0.480266	Tue	2	3	2017-14-2 11:31:35	51
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1443 Feb 14 12:31 SSC_BAM_FXREQ_20170214_173034.csv.pgp.ndm05.20170214123144627	12:31	2/14/2017	17:30:34	2017-14-02	12:31:44	0.522037	Tue	2	3	2017-14-2 12:31:44	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063905721	6:39			2017-14-02	6:39:05	0.277141	Tue	2	4	2017-14-2 6:39:05	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063905974	6:39			2017-14-02	6:39:05	0.277141	Tue	2	4	2017-14-2 6:39:05	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063906970	6:39			2017-14-02	6:39:06	0.277153	Tue	2	4	2017-14-2 6:39:06	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063906173	6:39			2017-14-02	6:39:06	0.277153	Tue	2	4	2017-14-2 6:39:06	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063906369	6:39			2017-14-02	6:39:06	0.277153	Tue	2	4	2017-14-2 6:39:06	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063906581	6:39			2017-14-02	6:39:06	0.277153	Tue	2	4	2017-14-2 6:39:06	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063906776	6:39			2017-14-02	6:39:06	0.277153	Tue	2	4	2017-14-2 6:39:06	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063907173	6:39			2017-14-02	6:39:07	0.277164	Tue	2	4	2017-14-2 6:39:07	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063907372	6:39			2017-14-02	6:39:07	0.277164	Tue	2	4	2017-14-2 6:39:07	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063907568	6:39			2017-14-02	6:39:07	0.277164	Tue	2	4	2017-14-2 6:39:07	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063907791	6:39			2017-14-02	6:39:07	0.277164	Tue	2	4	2017-14-2 6:39:07	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063907973	6:39			2017-14-02	6:39:07	0.277164	Tue	2	4	2017-14-2 6:39:07	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063908174	6:39			2017-14-02	6:39:08	0.277176	Tue	2	4	2017-14-2 6:39:08	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063908375	6:39			2017-14-02	6:39:08	0.277176	Tue	2	4	2017-14-2 6:39:08	51
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 14 06:39 BCRTOFX.txt.20170214063908597	6:39			2017-14-02	6:39:08	0.277176	Tue	2	4	2017-14-2 6:39:08	51
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      6092 Feb 14 14:36 BRA_BRA_Ver_20170214.csv.20170214143622901	14:36	2/14/2017		2017-14-02	14:36:22	0.608588	Tue	2	5	2017-14-2 14:36:22	51
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       355 Feb 14 10:34 CDPSfx_BRLorder.20170214.103500.csv.20170214103405295	10:34	2/14/2017	10:35:00	2017-14-02	10:34:05	0.440336	Tue	2	6	2017-14-2 10:34:05	51
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       111 Feb 14 04:25 scbcnhtrades1.in.201702141715.20170214042559829	4:25	2/14/2017	17:15:00	2017-14-02	4:25:59	0.184711	Tue	2	7	2017-14-2 4:25:59	51
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 14 04:26 scbcnhtrades2.in.201702141715.20170214042600117	4:26	2/14/2017	17:15:00	2017-14-02	4:26:00	0.184722	Tue	2	7	2017-14-2 4:26:00	51
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1287 Feb 14 09:37 SPOT_FET_Instructions_StateStreet_20170214-152535.csv.20170214093759618	9:37	2/14/2017	15:25:35	2017-14-02	9:37:59	0.401377	Tue	2	7	2017-14-2 9:37:59	51
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       238 Feb 14 17:02 02142017_GAM_GAM_STAR_GS.20170214.csv.20170214170231433	17:02	2/14/2017		2017-14-02	17:02:31	0.710081	Tue	2	9	2017-14-2 17:02:31	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 14 10:34 trade10.dat.20170214103405431	10:34			2017-14-02	10:34:05	0.440336	Tue	2	10	2017-14-2 10:34:05	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 14 12:34 trade10.dat.20170214123415839	12:34			2017-14-02	12:34:15	0.523785	Tue	2	10	2017-14-2 12:34:15	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 14 14:34 trade10.dat.20170214143422398	14:34			2017-14-02	14:34:22	0.607199	Tue	2	10	2017-14-2 14:34:22	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     22130 Feb 14 16:24 trade10.dat.20170214162428412	16:24			2017-14-02	16:24:28	0.683657	Tue	2	10	2017-14-2 16:24:28	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 14 17:04 trade10.dat.20170214170432246	17:04			2017-14-02	17:04:32	0.711481	Tue	2	10	2017-14-2 17:04:32	51
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 14 18:04 trade10.dat.20170214180437278	18:04			2017-14-02	18:04:37	0.753206	Tue	2	10	2017-14-2 18:04:37	51
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       214 Feb 14 01:07 FSS_Orders_20170214.csv.20170214010748392	1:07	2/14/2017		2017-14-02	1:07:48	0.047083	Tue	2	13	2017-14-2 1:07:48	51
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    372087 Feb 14 09:05 passporttrans.20170214.csv.20170214090546613	9:05	2/14/2017		2017-14-02	9:05:46	0.379005	Tue	2	15	2017-14-2 9:05:46	51
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2028 Feb 14 08:31 HighlandCapitalManagementRecon201702140730.csv.20170214083144585	8:31	2/14/2017	7:30:00	2017-14-02	8:31:44	0.35537	Tue	2	16	2017-14-2 8:31:44	51
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr      1214 Feb 14 02:57 HSBC-LKR.in.14022017-1.20170214025754695	 02:5	2/14/2017		2017-14-02	2:57:54	0.123542	Tue	2	17	2017-14-2 2:57:54	51
John Hancock Investments	HAN_TRANS_HANVER_20170214.csv.20170214153424733	15:34	2/14/2017		2017-14-02	15:34:24	0.648889	Tue	2	18	2017-14-2 15:34:24	51
John Hancock Investments	HAN_TRANS_HANVER_20170214.csv.20170214153424733	15:34	2/14/2017		2017-14-02	15:34:24	0.648889	Tue	2	18	2017-14-2 15:34:24	51
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       240 Feb 14 05:36 NOS_SFX_20170213-14.csv.20170214053604064	5:36	2/13/2017		2017-14-02	5:36:04	0.23338	Tue	2	21	2017-14-2 5:36:04	51
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 14 11:32 PAXStateStreetFX_Orders_021417.txt.20170214113206277	11:32	2/14/2017		2017-14-02	11:32:06	0.480625	Tue	2	23	2017-14-2 11:32:06	51
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 14 16:08 PAXStateStreetFX_Orders_021417.txt.20170214160826869	16:08	2/14/2017		2017-14-02	16:08:26	0.672523	Tue	2	23	2017-14-2 16:08:26	51
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       209 Feb 14 12:32 PGI_Orders_20170214113019.csv.20170214123215070	12:32	2/14/2017	11:30:19	2017-14-02	12:32:15	0.522396	Tue	2	24	2017-14-2 12:32:15	51
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       303 Feb 14 02:51 FT_fx_20170214_084937.csv.20170214025154102	2:51	2/14/2017	8:49:37	2017-14-02	2:51:54	0.119375	Tue	2	26	2017-14-2 2:51:54	51
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 14 03:25 INV_fx_20170214_092243.csv.20170214032556734	3:25	2/14/2017	9:22:43	2017-14-02	3:25:56	0.143009	Tue	2	26	2017-14-2 3:25:56	51
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb 14 04:40 INV_fx_20170214_103833.csv.20170214044001024	4:40	2/14/2017	10:38:33	2017-14-02	4:40:01	0.194456	Tue	2	26	2017-14-2 4:40:01	51
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Feb 14 04:42 FT_fx_20170214_103911.csv.20170214044201426	4:42	2/14/2017	10:39:11	2017-14-02	4:42:01	0.195845	Tue	2	26	2017-14-2 4:42:01	51
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 14 05:14 FT_fx_20170214_111158.csv.20170214051403227	5:14	2/14/2017	11:11:58	2017-14-02	5:14:03	0.21809	Tue	2	26	2017-14-2 5:14:03	51
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr      1121 Feb 14 03:39 citicnhtrades.in.201702141635.20170214033957288	3:39	2/14/2017	16:35:00	2017-14-02	3:39:57	0.152743	Tue	2	28	2017-14-2 3:39:57	51
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 14 04:17 citicnhtrades.in.201702141713.20170214041758740	4:17	2/14/2017	17:13:00	2017-14-02	4:17:58	0.179144	Tue	2	28	2017-14-2 4:17:58	51
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       429 Feb 14 04:17 hsbccnhtrades.in.201702141713.20170214041759039	4:17	2/14/2017	17:13:00	2017-14-02	4:17:59	0.179155	Tue	2	29	2017-14-2 4:17:59	51
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     29325 Feb 14 10:10 RSWGD1-17_SSGM_Confirmed_File__20170214.csv.20170214101002936	10:10	2/14/2017		2017-14-02	10:10:02	0.423634	Tue	2	30	2017-14-2 10:10:02	51
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       174 Feb 14 10:24 tcwgt20170214.csv.20170214102404214	10:24	2/14/2017		2017-14-02	10:24:04	0.43338	Tue	2	31	2017-14-2 10:24:04	51
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6527 Feb 14 09:31 TIAACREFREPAT.csv.20170214093148557	9:31			2017-14-02	9:31:48	0.397083	Tue	2	32	2017-14-2 9:31:48	51
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       316 Feb 14 10:32 TIAACREFREPAT.csv.20170214103204659	10:32			2017-14-02	10:32:04	0.438935	Tue	2	32	2017-14-2 10:32:04	51
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       520 Feb 14 21:24 tokyofundtrades.in.201702151003.20170214212421053	 21:2	2/15/2017	10:03:00	2017-14-02	21:24:21	0.89191	Tue	2	33	2017-14-2 21:24:21	51
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       456 Feb 14 22:06 tokyofundtrades.in.201702151052.20170214220622804	 22:0	2/15/2017	10:52:00	2017-14-02	22:06:22	0.921088	Tue	2	33	2017-14-2 22:06:22	51
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       128 Feb 15 11:07 Alger_Orders_20170215110534.csv.20170215110717974	11:07	2/15/2017	11:05:34	2017-15-02	11:07:17	0.463391	Wed	3	1	2017-15-2 11:07:17	52
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1401 Feb 15 04:31 SSC_BAM_FXREQ_20170215_093016.csv.pgp.ndm05.20170215043146463	4:31	2/15/2017	9:30:16	2017-15-02	4:31:46	0.188727	Wed	3	3	2017-15-2 4:31:46	52
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb 15 09:32 SSC_BAM_FXREQ_20170215_143025.csv.pgp.ndm05.20170215093209004	9:32	2/15/2017	14:30:25	2017-15-02	9:32:09	0.397326	Wed	3	3	2017-15-2 9:32:09	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063953431	6:39			2017-15-02	6:39:53	0.277697	Wed	3	4	2017-15-2 6:39:53	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063953697	6:39			2017-15-02	6:39:53	0.277697	Wed	3	4	2017-15-2 6:39:53	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063953879	6:39			2017-15-02	6:39:53	0.277697	Wed	3	4	2017-15-2 6:39:53	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063954050	6:39			2017-15-02	6:39:54	0.277708	Wed	3	4	2017-15-2 6:39:54	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063954293	6:39			2017-15-02	6:39:54	0.277708	Wed	3	4	2017-15-2 6:39:54	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063954465	6:39			2017-15-02	6:39:54	0.277708	Wed	3	4	2017-15-2 6:39:54	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063954657	6:39			2017-15-02	6:39:54	0.277708	Wed	3	4	2017-15-2 6:39:54	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063954873	6:39			2017-15-02	6:39:54	0.277708	Wed	3	4	2017-15-2 6:39:54	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063955046	6:39			2017-15-02	6:39:55	0.27772	Wed	3	4	2017-15-2 6:39:55	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063955288	6:39			2017-15-02	6:39:55	0.27772	Wed	3	4	2017-15-2 6:39:55	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063955455	6:39			2017-15-02	6:39:55	0.27772	Wed	3	4	2017-15-2 6:39:55	52
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 15 06:39 BCRTOFX.txt.20170215063955671	6:39			2017-15-02	6:39:55	0.27772	Wed	3	4	2017-15-2 6:39:55	52
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      8616 Feb 15 14:35 BRA_BRA_Ver_20170215.csv.20170215143516098	14:35	2/15/2017		2017-15-02	14:35:16	0.607824	Wed	3	5	2017-15-2 14:35:16	52
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       111 Feb 15 04:04 scbcnhtrades1.in.201702151655.20170215040444503	4:04	2/15/2017	16:55:00	2017-15-02	4:04:44	0.169954	Wed	3	7	2017-15-2 4:04:44	52
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 15 04:04 scbcnhtrades2.in.201702151655.20170215040444748	4:04	2/15/2017	16:55:00	2017-15-02	4:04:44	0.169954	Wed	3	7	2017-15-2 4:04:44	52
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       170 Feb 15 05:16 scbcnhtrades1.in.201702151814.20170215051649954	5:16	2/15/2017	18:14:00	2017-15-02	5:16:49	0.220012	Wed	3	7	2017-15-2 5:16:49	52
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 15 05:16 scbcnhtrades2.in.201702151814.20170215051650361	5:16	2/15/2017	18:14:00	2017-15-02	5:16:50	0.220023	Wed	3	7	2017-15-2 5:16:50	52
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1443 Feb 15 10:29 SPOT_FET_Instructions_StateStreet_20170215-161945.csv.20170215102913531	10:29	2/15/2017	16:19:45	2017-15-02	10:29:13	0.436956	Wed	3	7	2017-15-2 10:29:13	52
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       490 Feb 15 16:47 02152017_GAM_GAM_STAR_GS.20170215.csv.20170215164724516	16:47	2/15/2017		2017-15-02	16:47:24	0.699583	Wed	3	9	2017-15-2 16:47:24	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb 15 10:35 trade10.dat.20170215103514401	10:35			2017-15-02	10:35:14	0.441134	Wed	3	10	2017-15-2 10:35:14	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Feb 15 12:35 trade10.dat.20170215123507647	12:35			2017-15-02	12:35:07	0.524387	Wed	3	10	2017-15-2 12:35:07	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 15 14:33 trade10.dat.20170215143315565	14:33			2017-15-02	14:33:15	0.606424	Wed	3	10	2017-15-2 14:33:15	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 15 16:23 trade10.dat.20170215162322506	16:23			2017-15-02	16:23:22	0.682894	Wed	3	10	2017-15-2 16:23:22	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 15 17:03 trade10.dat.20170215170325776	17:03			2017-15-02	17:03:25	0.710706	Wed	3	10	2017-15-2 17:03:25	52
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 15 18:04 trade10.dat.20170215180400623	18:04			2017-15-02	18:04:00	0.752778	Wed	3	10	2017-15-2 18:04:00	52
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       774 Feb 15 06:38 UKFCMCurrencyTemplate150217.csv.20170215063853141	6:38			2017-15-02	6:38:53	0.277002	Wed	3	11	2017-15-2 6:38:53	52
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       214 Feb 15 01:26 FSS_Orders_20170215.csv.20170215012635256	1:26	2/15/2017		2017-15-02	1:26:35	0.060127	Wed	3	13	2017-15-2 1:26:35	52
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    420440 Feb 15 08:55 passporttrans.20170215.csv.20170215085504111	8:55	2/15/2017		2017-15-02	8:55:04	0.371574	Wed	3	15	2017-15-2 8:55:04	52
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1843 Feb 15 08:33 HighlandCapitalManagementRecon201702150730.csv.20170215083301380	8:33	2/15/2017	7:30:00	2017-15-02	8:33:01	0.356262	Wed	3	16	2017-15-2 8:33:01	52
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       670 Feb 15 03:00 HSBC-LKR.in.15022017-1.20170215030041151	 03:0	2/15/2017		2017-15-02	3:00:41	0.125475	Wed	3	17	2017-15-2 3:00:41	52
John Hancock Investments	HAN_TRANS_HANVER_20170215.csv.20170215153718168	15:37	2/15/2017		2017-15-02	15:37:18	0.650903	Wed	3	18	2017-15-2 15:37:18	52
John Hancock Investments	HAN_TRANS_HANVER_20170215.csv.20170215153718168	15:37	2/15/2017		2017-15-02	15:37:18	0.650903	Wed	3	18	2017-15-2 15:37:18	52
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Feb 15 13:03 NOS_SFX_20170215.csv.20170215130309756	13:03	2/15/2017		2017-15-02	13:03:09	0.543854	Wed	3	21	2017-15-2 13:03:09	52
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Feb 15 13:33 NOS_SFX_BRL_20170215.csv.20170215133311805	13:33	2/15/2017		2017-15-02	13:33:11	0.564711	Wed	3	21	2017-15-2 13:33:11	52
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 15 16:21 PAXStateStreetFX_Orders_021517.txt.20170215162121969	16:21	2/15/2017		2017-15-02	16:21:21	0.681493	Wed	3	23	2017-15-2 16:21:21	52
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       144 Feb 15 09:13 PresimaOrders.csv.20170215091306149	9:13			2017-15-02	9:13:06	0.384097	Wed	3	25	2017-15-2 9:13:06	52
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Feb 15 03:00 FT_fx_20170215_085858.csv.20170215030040811	3:00	2/15/2017	8:58:58	2017-15-02	3:00:40	0.125463	Wed	3	26	2017-15-2 3:00:40	52
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 15 03:20 INV_fx_20170215_091732.csv.20170215032042039	3:20	2/15/2017	9:17:32	2017-15-02	3:20:42	0.139375	Wed	3	26	2017-15-2 3:20:42	52
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 15 04:40 FT_fx_20170215_103824.csv.20170215044046965	4:40	2/15/2017	10:38:24	2017-15-02	4:40:46	0.194977	Wed	3	26	2017-15-2 4:40:46	52
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 15 04:58 FT_fx_20170215_105608.csv.20170215045847685	4:58	2/15/2017	10:56:08	2017-15-02	4:58:47	0.207488	Wed	3	26	2017-15-2 4:58:47	52
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 15 05:22 INV_fx_20170215_111916.csv.20170215052250751	5:22	2/15/2017	11:19:16	2017-15-02	5:22:50	0.22419	Wed	3	26	2017-15-2 5:22:50	52
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       890 Feb 15 03:36 citicnhtrades.in.201702151626.20170215033643584	3:36	2/15/2017	16:26:00	2017-15-02	3:36:43	0.150498	Wed	3	28	2017-15-2 3:36:43	52
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       429 Feb 15 04:26 hsbccnhtrades.in.201702141713.20170215042645765	4:26	2/14/2017	17:13:00	2017-15-02	4:26:45	0.185243	Wed	3	29	2017-15-2 4:26:45	52
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       599 Feb 15 04:30 hsbccnhtrades.in.201702151720.20170215043046077	4:30	2/15/2017	17:20:00	2017-15-02	4:30:46	0.188032	Wed	3	29	2017-15-2 4:30:46	52
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27690 Feb 15 10:21 RSWGD1-17_SSGM_Confirmed_File__20170215.csv.20170215102112828	10:21	2/15/2017		2017-15-02	10:21:12	0.431389	Wed	3	30	2017-15-2 10:21:12	52
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       517 Feb 15 09:43 tcwta20170215.csv.20170215094310366	9:43	2/15/2017		2017-15-02	9:43:10	0.404977	Wed	3	31	2017-15-2 9:43:10	52
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     19477 Feb 15 09:33 TIAACREFREPAT.csv.20170215093309360	9:33			2017-15-02	9:33:09	0.398021	Wed	3	32	2017-15-2 9:33:09	52
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       755 Feb 15 21:24 tokyofundtrades.in.201702161006.20170215212416026	 21:2	2/16/2017	10:06:00	2017-15-02	21:24:16	0.891852	Wed	3	33	2017-15-2 21:24:16	52
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb 16 08:44 Alger_Orders_20170216084212.csv.20170216084429070	8:44	2/16/2017	8:42:12	2017-16-02	8:44:29	0.364225	Thu	4	1	2017-16-2 8:44:29	53
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb 16 08:52 Alger_Orders_20170216085027.csv.20170216085229659	8:52	2/16/2017	8:50:27	2017-16-02	8:52:29	0.36978	Thu	4	1	2017-16-2 8:52:29	53
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       191 Feb 16 14:27 Alger_Orders_20170216142440.csv.20170216142700583	14:27	2/16/2017	14:24:40	2017-16-02	14:27:00	0.602083	Thu	4	1	2017-16-2 14:27:00	53
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3289 Feb 16 11:24 alps_Orders_02162017092000.csv.20170216112446376	11:24	2/16/2017	9:20:00	2017-16-02	11:24:46	0.475532	Thu	4	2	2017-16-2 11:24:46	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063920178	6:39			2017-16-02	6:39:20	0.277315	Thu	4	4	2017-16-2 6:39:20	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063920442	6:39			2017-16-02	6:39:20	0.277315	Thu	4	4	2017-16-2 6:39:20	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063920641	6:39			2017-16-02	6:39:20	0.277315	Thu	4	4	2017-16-2 6:39:20	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063920850	6:39			2017-16-02	6:39:20	0.277315	Thu	4	4	2017-16-2 6:39:20	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063921056	6:39			2017-16-02	6:39:21	0.277326	Thu	4	4	2017-16-2 6:39:21	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063921257	6:39			2017-16-02	6:39:21	0.277326	Thu	4	4	2017-16-2 6:39:21	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063921445	6:39			2017-16-02	6:39:21	0.277326	Thu	4	4	2017-16-2 6:39:21	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063921638	6:39			2017-16-02	6:39:21	0.277326	Thu	4	4	2017-16-2 6:39:21	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063921854	6:39			2017-16-02	6:39:21	0.277326	Thu	4	4	2017-16-2 6:39:21	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063922067	6:39			2017-16-02	6:39:22	0.277338	Thu	4	4	2017-16-2 6:39:22	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063922302	6:39			2017-16-02	6:39:22	0.277338	Thu	4	4	2017-16-2 6:39:22	53
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 16 06:39 BCRTOFX.txt.20170216063922495	6:39			2017-16-02	6:39:22	0.277338	Thu	4	4	2017-16-2 6:39:22	53
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      6579 Feb 16 14:37 BRA_BRA_Ver_20170216.csv.20170216143702554	14:37	2/16/2017		2017-16-02	14:37:02	0.609051	Thu	4	5	2017-16-2 14:37:02	53
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Feb 16 11:34 CDPSfx_IDRorder.20170216.113500.csv.20170216113447243	11:34	2/16/2017	11:35:00	2017-16-02	11:34:47	0.482488	Thu	4	6	2017-16-2 11:34:47	53
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       358 Feb 16 16:35 CDPSfx_TWDorder.20170216.162500.csv.20170216163509316	16:35	2/16/2017	16:25:00	2017-16-02	16:35:09	0.691076	Thu	4	6	2017-16-2 16:35:09	53
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       168 Feb 16 04:16 scbcnhtrades1.in.201702161708.20170216041612884	4:16	2/16/2017	17:08:00	2017-16-02	4:16:12	0.177917	Thu	4	7	2017-16-2 4:16:12	53
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 16 04:16 scbcnhtrades2.in.201702161708.20170216041613269	4:16	2/16/2017	17:08:00	2017-16-02	4:16:13	0.177928	Thu	4	7	2017-16-2 4:16:13	53
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       223 Feb 16 05:10 scbcnhtrades1.in.201702161807.20170216051016913	5:10	2/16/2017	18:07:00	2017-16-02	5:10:16	0.215463	Thu	4	7	2017-16-2 5:10:16	53
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 16 05:12 scbcnhtrades2.in.201702161807.20170216051217155	5:12	2/16/2017	18:07:00	2017-16-02	5:12:17	0.216863	Thu	4	7	2017-16-2 5:12:17	53
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       723 Feb 16 08:58 SPOT_FET_Instructions_StateStreet_20170216-144946.csv.20170216085830314	8:58	2/16/2017	14:49:46	2017-16-02	8:58:30	0.373958	Thu	4	7	2017-16-2 8:58:30	53
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 16 17:41 02162017_GAM_GAM_STAR_GS.20170216.csv.20170216174115030	17:41	2/16/2017		2017-16-02	17:41:15	0.736979	Thu	4	9	2017-16-2 17:41:15	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Feb 16 10:34 trade10.dat.20170216103408490	10:34			2017-16-02	10:34:08	0.44037	Thu	4	10	2017-16-2 10:34:08	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Feb 16 12:34 trade10.dat.20170216123454323	12:34			2017-16-02	12:34:54	0.524236	Thu	4	10	2017-16-2 12:34:54	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Feb 16 14:35 trade10.dat.20170216143501977	14:35			2017-16-02	14:35:01	0.60765	Thu	4	10	2017-16-2 14:35:01	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb 16 16:25 trade10.dat.20170216162508345	16:25			2017-16-02	16:25:08	0.68412	Thu	4	10	2017-16-2 16:25:08	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 16 17:05 trade10.dat.20170216170512196	17:05			2017-16-02	17:05:12	0.711944	Thu	4	10	2017-16-2 17:05:12	53
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 16 18:04 trade10.dat.20170216180447079	18:04			2017-16-02	18:04:47	0.753322	Thu	4	10	2017-16-2 18:04:47	53
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       214 Feb 16 00:11 FSS_Orders_20170216.csv.20170216001152823	0:11	2/16/2017		2017-16-02	0:11:52	0.008241	Thu	4	13	2017-16-2 0:11:52	53
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    359062 Feb 16 09:10 passporttrans.20170216.csv.20170216091031652	9:10	2/16/2017		2017-16-02	9:10:31	0.382303	Thu	4	15	2017-16-2 9:10:31	53
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2233 Feb 16 08:32 HighlandCapitalManagementRecon201702160730.csv.20170216083228361	8:32	2/16/2017	7:30:00	2017-16-02	8:32:28	0.35588	Thu	4	16	2017-16-2 8:32:28	53
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       212 Feb 16 00:11 HSBC-LKR.in.16022017-1.20170216001153245	 00:1	2/16/2017		2017-16-02	0:11:53	0.008252	Thu	4	17	2017-16-2 0:11:53	53
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       662 Feb 16 03:04 HSBC-LKR.in.16022017-2.20170216030407762	 03:0	2/16/2017		2017-16-02	3:04:07	0.127859	Thu	4	17	2017-16-2 3:04:07	53
John Hancock Investments	HAN_TRANS_HANVER_20170216.csv.20170216153504777	15:35	2/16/2017		2017-16-02	15:35:04	0.649352	Thu	4	18	2017-16-2 15:35:04	53
John Hancock Investments	HAN_TRANS_HANVER_20170216.csv.20170216153504777	15:35	2/16/2017		2017-16-02	15:35:04	0.649352	Thu	4	18	2017-16-2 15:35:04	53
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       179 Feb 16 05:50 NOS_SFX_20170216.csv.20170216055018539	5:50	2/16/2017		2017-16-02	5:50:18	0.243264	Thu	4	21	2017-16-2 5:50:18	53
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 16 16:37 PAXStateStreetFX_Orders_021617.txt.20170216163709943	16:37	2/16/2017		2017-16-02	16:37:09	0.692465	Thu	4	23	2017-16-2 16:37:09	53
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       368 Feb 16 02:46 FT_fx_20170216_084316.csv.20170216024606702	2:46	2/16/2017	8:43:16	2017-16-02	2:46:06	0.115347	Thu	4	26	2017-16-2 2:46:06	53
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 16 03:24 INV_fx_20170216_092152.csv.20170216032410940	3:24	2/16/2017	9:21:52	2017-16-02	3:24:10	0.141782	Thu	4	26	2017-16-2 3:24:10	53
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Feb 16 04:34 FT_fx_20170216_103234.csv.20170216043414891	4:34	2/16/2017	10:32:34	2017-16-02	4:34:14	0.19044	Thu	4	26	2017-16-2 4:34:14	53
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 16 05:30 FT_fx_20170216_112736.csv.20170216053017733	5:30	2/16/2017	11:27:36	2017-16-02	5:30:17	0.229363	Thu	4	26	2017-16-2 5:30:17	53
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       535 Feb 16 03:14 citicnhtrades.in.201702161607.20170216031408787	3:14	2/16/2017	16:07:00	2017-16-02	3:14:08	0.134815	Thu	4	28	2017-16-2 3:14:08	53
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 16 04:30 citicnhtrades.in.201702161719.20170216043014139	4:30	2/16/2017	17:19:00	2017-16-02	4:30:14	0.187662	Thu	4	28	2017-16-2 4:30:14	53
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       748 Feb 16 04:30 hsbccnhtrades.in.201702161722.20170216043014497	4:30	2/16/2017	17:22:00	2017-16-02	4:30:14	0.187662	Thu	4	29	2017-16-2 4:30:14	53
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     30845 Feb 16 10:32 RSWGD1-17_SSGM_Confirmed_File__20170216.csv.20170216103238062	10:32	2/16/2017		2017-16-02	10:32:38	0.439329	Thu	4	30	2017-16-2 10:32:38	53
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3738 Feb 16 09:32 TIAACREFREPAT.csv.20170216093232642	9:32			2017-16-02	9:32:32	0.397593	Thu	4	32	2017-16-2 9:32:32	53
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       756 Feb 16 21:31 tokyofundtrades.in.201702171022.20170216213103800	 21:3	2/17/2017	10:22:00	2017-16-02	21:31:03	0.896563	Thu	4	33	2017-16-2 21:31:03	53
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb 17 08:53 Alger_Orders_20170217085016.csv.20170217085329028	8:53	2/17/2017	8:50:16	2017-17-02	8:53:29	0.370475	Fri	5	1	2017-17-2 8:53:29	54
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        63 Feb 17 14:09 Alger_Orders_20170217140754.csv.20170217140943925	14:09	2/17/2017	14:07:54	2017-17-02	14:09:43	0.590081	Fri	5	1	2017-17-2 14:09:43	54
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      7327 Feb 17 10:19 alps_Orders_02172017092000.csv.20170217101939754	10:19	2/17/2017	9:20:00	2017-17-02	10:19:39	0.430313	Fri	5	2	2017-17-2 10:19:39	54
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      4173 Feb 17 12:14 alps_Orders_02172017095000.csv.20170217121407531	12:14	2/17/2017	9:50:00	2017-17-02	12:14:07	0.509803	Fri	5	2	2017-17-2 12:14:07	54
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      2146 Feb 17 16:51 alps_Orders_02172017097000.csv.20170217165155928	16:51	2/17/2017	10:10:00	2017-17-02	16:51:55	0.70272	Fri	5	2	2017-17-2 16:51:55	54
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1511 Feb 17 04:31 SSC_BAM_FXREQ_20170217_093014.csv.pgp.ndm05.20170217043143637	4:31	2/17/2017	9:30:14	2017-17-02	4:31:43	0.188692	Fri	5	3	2017-17-2 4:31:43	54
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1433 Feb 17 08:32 SSC_BAM_FXREQ_20170217_133022.csv.pgp.ndm05.20170217083227325	8:32	2/17/2017	13:30:22	2017-17-02	8:32:27	0.355868	Fri	5	3	2017-17-2 8:32:27	54
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb 17 10:32 SSC_BAM_FXREQ_20170217_153028.csv.pgp.ndm05.20170217103240907	10:32	2/17/2017	15:30:28	2017-17-02	10:32:40	0.439352	Fri	5	3	2017-17-2 10:32:40	54
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Feb 17 11:32 SSC_BAM_FXREQ_20170217_163031.csv.pgp.ndm05.20170217113233678	11:32	2/17/2017	16:30:31	2017-17-02	11:32:33	0.480938	Fri	5	3	2017-17-2 11:32:33	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063919531	6:39			2017-17-02	6:39:19	0.277303	Fri	5	4	2017-17-2 6:39:19	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063919846	6:39			2017-17-02	6:39:19	0.277303	Fri	5	4	2017-17-2 6:39:19	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063920049	6:39			2017-17-02	6:39:20	0.277315	Fri	5	4	2017-17-2 6:39:20	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063920230	6:39			2017-17-02	6:39:20	0.277315	Fri	5	4	2017-17-2 6:39:20	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063920431	6:39			2017-17-02	6:39:20	0.277315	Fri	5	4	2017-17-2 6:39:20	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063920638	6:39			2017-17-02	6:39:20	0.277315	Fri	5	4	2017-17-2 6:39:20	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063920848	6:39			2017-17-02	6:39:20	0.277315	Fri	5	4	2017-17-2 6:39:20	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063921053	6:39			2017-17-02	6:39:21	0.277326	Fri	5	4	2017-17-2 6:39:21	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063921270	6:39			2017-17-02	6:39:21	0.277326	Fri	5	4	2017-17-2 6:39:21	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063921447	6:39			2017-17-02	6:39:21	0.277326	Fri	5	4	2017-17-2 6:39:21	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063921668	6:39			2017-17-02	6:39:21	0.277326	Fri	5	4	2017-17-2 6:39:21	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063921849	6:39			2017-17-02	6:39:21	0.277326	Fri	5	4	2017-17-2 6:39:21	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063922235	6:39			2017-17-02	6:39:22	0.277338	Fri	5	4	2017-17-2 6:39:22	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063922036	6:39			2017-17-02	6:39:22	0.277338	Fri	5	4	2017-17-2 6:39:22	54
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 17 06:39 BCRTOFX.txt.20170217063922442	6:39			2017-17-02	6:39:22	0.277338	Fri	5	4	2017-17-2 6:39:22	54
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7038 Feb 17 14:35 BRA_BRA_Ver_20170217.csv.20170217143546554	14:35	2/17/2017		2017-17-02	14:35:46	0.608171	Fri	5	5	2017-17-2 14:35:46	54
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       358 Feb 17 16:33 CDPSfx_TWDorder.20170217.162500.csv.20170217163353206	16:33	2/17/2017	16:25:00	2017-17-02	16:33:53	0.690197	Fri	5	6	2017-17-2 16:33:53	54
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       280 Feb 17 04:11 scbcnhtrades1.in.201702171705.20170217041111247	4:11	2/17/2017	17:05:00	2017-17-02	4:11:11	0.174433	Fri	5	7	2017-17-2 4:11:11	54
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 17 04:11 scbcnhtrades2.in.201702171705.20170217041111711	4:11	2/17/2017	17:05:00	2017-17-02	4:11:11	0.174433	Fri	5	7	2017-17-2 4:11:11	54
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1143 Feb 17 09:35 SPOT_FET_Instructions_StateStreet_20170217-152650.csv.20170217093536869	9:35	2/17/2017	15:26:50	2017-17-02	9:35:36	0.399722	Fri	5	7	2017-17-2 9:35:36	54
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       491 Feb 17 17:23 02172017_GAM_GAM_STAR_GS.20170217.csv.20170217172358496	17:23	2/17/2017		2017-17-02	17:23:58	0.724977	Fri	5	9	2017-17-2 17:23:58	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb 17 10:35 trade10.dat.20170217103541447	10:35			2017-17-02	10:35:41	0.441447	Fri	5	10	2017-17-2 10:35:41	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Feb 17 12:34 trade10.dat.20170217123408575	12:34			2017-17-02	12:34:08	0.523704	Fri	5	10	2017-17-2 12:34:08	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     19960 Feb 17 14:33 trade10.dat.20170217143345893	14:33			2017-17-02	14:33:45	0.606771	Fri	5	10	2017-17-2 14:33:45	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     57718 Feb 17 16:23 trade10.dat.20170217162352343	16:23			2017-17-02	16:23:52	0.683241	Fri	5	10	2017-17-2 16:23:52	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 17 17:03 trade10.dat.20170217170356743	17:03			2017-17-02	17:03:56	0.711065	Fri	5	10	2017-17-2 17:03:56	54
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 17 18:04 trade10.dat.20170217180402184	18:04			2017-17-02	18:04:02	0.752801	Fri	5	10	2017-17-2 18:04:02	54
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    387499 Feb 17 08:55 passporttrans.20170217.csv.20170217085529489	8:55	2/17/2017		2017-17-02	8:55:29	0.371863	Fri	5	15	2017-17-2 8:55:29	54
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1846 Feb 17 08:31 HighlandCapitalManagementRecon201702170730.csv.20170217083126942	8:31	2/17/2017	7:30:00	2017-17-02	8:31:26	0.355162	Fri	5	16	2017-17-2 8:31:26	54
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       389 Feb 17 01:15 HSBC-LKR.in.17022017-1.20170217011521298	 01:1	2/17/2017		2017-17-02	1:15:21	0.052326	Fri	5	17	2017-17-2 1:15:21	54
John Hancock Investments	HAN_TRANS_HANVER_20170217.csv.20170217153348890	15:33	2/17/2017		2017-17-02	15:33:48	0.648472	Fri	5	18	2017-17-2 15:33:48	54
John Hancock Investments	HAN_TRANS_HANVER_20170217.csv.20170217153348890	15:33	2/17/2017		2017-17-02	15:33:48	0.648472	Fri	5	18	2017-17-2 15:33:48	54
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 17 16:09 PAXStateStreetFX_Orders_021717.txt.20170217160951102	16:09	2/17/2017		2017-17-02	16:09:51	0.673507	Fri	5	23	2017-17-2 16:09:51	54
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       209 Feb 17 09:29 PGI_Orders_20170217082757.csv.20170217092934724	9:29	2/17/2017	8:27:57	2017-17-02	9:29:34	0.395532	Fri	5	24	2017-17-2 9:29:34	54
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       441 Feb 17 14:00 PGI_Orders_20170217125844.csv.20170217140012788	14:00	2/17/2017	12:58:44	2017-17-02	14:00:12	0.583472	Fri	5	24	2017-17-2 14:00:12	54
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       373 Feb 17 03:17 FT_fx_20170217_091413.csv.20170217031737709	3:17	2/17/2017	9:14:13	2017-17-02	3:17:37	0.137234	Fri	5	26	2017-17-2 3:17:37	54
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       228 Feb 17 03:23 INV_fx_20170217_092131.csv.20170217032339135	3:23	2/17/2017	9:21:31	2017-17-02	3:23:39	0.141424	Fri	5	26	2017-17-2 3:23:39	54
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 17 04:57 INV_fx_20170217_105516.csv.20170217045715094	4:57	2/17/2017	10:55:16	2017-17-02	4:57:15	0.206424	Fri	5	26	2017-17-2 4:57:15	54
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb 17 05:31 FT_fx_20170217_112956.csv.20170217053117315	5:31	2/17/2017	11:29:56	2017-17-02	5:31:17	0.230058	Fri	5	26	2017-17-2 5:31:17	54
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       297 Feb 17 03:19 citicnhtrades.in.201702171614.20170217031938136	3:19	2/17/2017	16:14:00	2017-17-02	3:19:38	0.138634	Fri	5	28	2017-17-2 3:19:38	54
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 17 04:27 citicnhtrades.in.201702171722.20170217042713049	4:27	2/17/2017	17:22:00	2017-17-02	4:27:13	0.185567	Fri	5	28	2017-17-2 4:27:13	54
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       248 Feb 17 04:27 hsbccnhtrades.in.201702171722.20170217042713297	4:27	2/17/2017	17:22:00	2017-17-02	4:27:13	0.185567	Fri	5	29	2017-17-2 4:27:13	54
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28955 Feb 17 10:23 RSWGD1-17_SSGM_Confirmed_File__20170217.csv.20170217102340350	10:23	2/17/2017		2017-17-02	10:23:40	0.433102	Fri	5	30	2017-17-2 10:23:40	54
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3342 Feb 17 09:31 TIAACREFREPAT.csv.20170217093135784	9:31			2017-17-02	9:31:35	0.396933	Fri	5	32	2017-17-2 9:31:35	54
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       638 Feb 19 21:19 tokyofundtrades.in.201702200953.20170219211911458	 21:1	2/20/2017	9:53:00	2017-19-02	21:19:11	0.888322	Sun	7	33	2017-19-2 21:19:11	#N/A
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063942351	6:39			2017-20-02	6:39:42	0.277569	Mon	1	4	2017-20-2 6:39:42	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063942688	6:39			2017-20-02	6:39:42	0.277569	Mon	1	4	2017-20-2 6:39:42	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063942895	6:39			2017-20-02	6:39:42	0.277569	Mon	1	4	2017-20-2 6:39:42	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063943083	6:39			2017-20-02	6:39:43	0.277581	Mon	1	4	2017-20-2 6:39:43	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063943304	6:39			2017-20-02	6:39:43	0.277581	Mon	1	4	2017-20-2 6:39:43	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063943487	6:39			2017-20-02	6:39:43	0.277581	Mon	1	4	2017-20-2 6:39:43	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063943717	6:39			2017-20-02	6:39:43	0.277581	Mon	1	4	2017-20-2 6:39:43	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063943869	6:39			2017-20-02	6:39:43	0.277581	Mon	1	4	2017-20-2 6:39:43	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063944084	6:39			2017-20-02	6:39:44	0.277593	Mon	1	4	2017-20-2 6:39:44	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063944411	6:39			2017-20-02	6:39:44	0.277593	Mon	1	4	2017-20-2 6:39:44	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063944682	6:39			2017-20-02	6:39:44	0.277593	Mon	1	4	2017-20-2 6:39:44	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063944882	6:39			2017-20-02	6:39:44	0.277593	Mon	1	4	2017-20-2 6:39:44	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063945081	6:39			2017-20-02	6:39:45	0.277604	Mon	1	4	2017-20-2 6:39:45	55
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 20 06:39 BCRTOFX.txt.20170220063945309	6:39			2017-20-02	6:39:45	0.277604	Mon	1	4	2017-20-2 6:39:45	55
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       168 Feb 20 04:01 scbcnhtrades1.in.201702201655.20170220040133636	4:01	2/20/2017	16:55:00	2017-20-02	4:01:33	0.167743	Mon	1	7	2017-20-2 4:01:33	55
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 20 04:01 scbcnhtrades2.in.201702201655.20170220040133903	4:01	2/20/2017	16:55:00	2017-20-02	4:01:33	0.167743	Mon	1	7	2017-20-2 4:01:33	55
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 20 05:07 scbcnhtrades2.in.201702201757.20170220050738709	5:07	2/20/2017	17:57:00	2017-20-02	5:07:38	0.213634	Mon	1	7	2017-20-2 5:07:38	55
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Feb 20 05:07 scbcnhtrades1.in.201702201757.20170220050739009	5:07	2/20/2017	17:57:00	2017-20-02	5:07:39	0.213646	Mon	1	7	2017-20-2 5:07:39	55
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       118 Feb 20 16:49 02202017_GAM_GAM_STAR_GS.20170220.csv.20170220164952946	16:49	2/20/2017		2017-20-02	16:49:52	0.701296	Mon	1	9	2017-20-2 16:49:52	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 10:33 trade10.dat.20170220103329032	10:33			2017-20-02	10:33:29	0.439919	Mon	1	10	2017-20-2 10:33:29	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 12:33 trade10.dat.20170220123338516	12:33			2017-20-02	12:33:38	0.523356	Mon	1	10	2017-20-2 12:33:38	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 14:33 trade10.dat.20170220143346652	14:33			2017-20-02	14:33:46	0.606782	Mon	1	10	2017-20-2 14:33:46	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 16:23 trade10.dat.20170220162351291	16:23			2017-20-02	16:23:51	0.683229	Mon	1	10	2017-20-2 16:23:51	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 17:03 trade10.dat.20170220170354566	17:03			2017-20-02	17:03:54	0.711042	Mon	1	10	2017-20-2 17:03:54	55
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 20 18:03 trade10.dat.20170220180358110	18:03			2017-20-02	18:03:58	0.752755	Mon	1	10	2017-20-2 18:03:58	55
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       291 Feb 20 01:17 FSS_Orders_20170220.csv.20170220011722738	1:17	2/20/2017		2017-20-02	1:17:22	0.053727	Mon	1	13	2017-20-2 1:17:22	55
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    132559 Feb 20 08:49 passporttrans.20170220.csv.20170220084922321	8:49	2/20/2017		2017-20-02	8:49:22	0.367616	Mon	1	15	2017-20-2 8:49:22	55
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Feb 20 08:31 HighlandCapitalManagementRecon201702200730.csv.20170220083151529	8:31	2/20/2017	7:30:00	2017-20-02	8:31:51	0.355451	Mon	1	16	2017-20-2 8:31:51	55
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       573 Feb 20 01:53 HSBC-LKR.in.20022017-1.20170220015324748	 01:5	2/20/2017		2017-20-02	1:53:24	0.07875	Mon	1	17	2017-20-2 1:53:24	55
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       238 Feb 20 13:01 NOS_SFX_20170220.csv.20170220130141452	13:01	2/20/2017		2017-20-02	13:01:41	0.542836	Mon	1	21	2017-20-2 13:01:41	55
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       738 Feb 20 14:21 PGI_Orders_20170220131857.csv.20170220142145528	14:21	2/20/2017	13:18:57	2017-20-02	14:21:45	0.598438	Mon	1	24	2017-20-2 14:21:45	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Feb 20 03:07 FT_fx_20170220_090601.csv.20170220030729657	3:07	2/20/2017	9:06:01	2017-20-02	3:07:29	0.130197	Mon	1	26	2017-20-2 3:07:29	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Feb 20 03:15 INV_fx_20170220_091303.csv.20170220031530204	3:15	2/20/2017	9:13:03	2017-20-02	3:15:30	0.135764	Mon	1	26	2017-20-2 3:15:30	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 20 04:23 FT_fx_20170220_102100.csv.20170220042335148	4:23	2/20/2017	10:21:00	2017-20-02	4:23:35	0.183044	Mon	1	26	2017-20-2 4:23:35	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb 20 04:45 INV_fx_20170220_104410.csv.20170220044536307	4:45	2/20/2017	10:44:10	2017-20-02	4:45:36	0.198333	Mon	1	26	2017-20-2 4:45:36	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 20 05:01 FT_fx_20170220_105930.csv.20170220050137034	5:01	2/20/2017	10:59:30	2017-20-02	5:01:37	0.209456	Mon	1	26	2017-20-2 5:01:37	55
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 20 06:17 FT_fx_20170220_121440.csv.20170220061741263	6:17	2/20/2017	12:14:40	2017-20-02	6:17:41	0.26228	Mon	1	26	2017-20-2 6:17:41	55
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       464 Feb 20 03:17 citicnhtrades.in.201702201607.20170220031730661	3:17	2/20/2017	16:07:00	2017-20-02	3:17:30	0.137153	Mon	1	28	2017-20-2 3:17:30	55
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 20 04:27 citicnhtrades.in.201702201715.20170220042735487	4:27	2/20/2017	17:15:00	2017-20-02	4:27:35	0.185822	Mon	1	28	2017-20-2 4:27:35	55
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       590 Feb 20 04:27 hsbccnhtrades.in.201702201715.20170220042735645	4:27	2/20/2017	17:15:00	2017-20-02	4:27:35	0.185822	Mon	1	29	2017-20-2 4:27:35	55
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     25826 Feb 20 10:43 RSWGD1-17_SSGM_Confirmed_File__20170220.csv.20170220104329806	10:43	2/20/2017		2017-20-02	10:43:29	0.446863	Mon	1	30	2017-20-2 10:43:29	55
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       456 Feb 20 21:36 tokyofundtrades.in.201702211017.20170220213611392	 21:3	2/21/2017	10:17:00	2017-20-02	21:36:11	0.900127	Mon	1	33	2017-20-2 21:36:11	55
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      2692 Feb 21 10:30 alps_Orders_02212017083000.csv.20170221103008367	10:30	2/21/2017	8:30:00	2017-21-02	10:30:08	0.437593	Tue	2	2	2017-21-2 10:30:08	56
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1917 Feb 21 16:40 alps_Orders_02212017024000.csv.20170221164051796	16:40	2/21/2017	2:40:00	2017-21-02	16:40:51	0.695035	Tue	2	2	2017-21-2 16:40:51	56
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1553 Feb 21 08:32 SSC_BAM_FXREQ_20170221_133022.csv.pgp.ndm05.20170221083258451	8:32	2/21/2017	13:30:22	2017-21-02	8:32:58	0.356227	Tue	2	3	2017-21-2 8:32:58	56
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1441 Feb 21 13:33 SSC_BAM_FXREQ_20170221_183032.csv.pgp.ndm05.20170221133339755	13:33	2/21/2017	18:30:32	2017-21-02	13:33:39	0.565035	Tue	2	3	2017-21-2 13:33:39	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063947833	6:39			2017-21-02	6:39:47	0.277627	Tue	2	4	2017-21-2 6:39:47	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063948224	6:39			2017-21-02	6:39:48	0.277639	Tue	2	4	2017-21-2 6:39:48	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063948435	6:39			2017-21-02	6:39:48	0.277639	Tue	2	4	2017-21-2 6:39:48	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063948615	6:39			2017-21-02	6:39:48	0.277639	Tue	2	4	2017-21-2 6:39:48	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063948815	6:39			2017-21-02	6:39:48	0.277639	Tue	2	4	2017-21-2 6:39:48	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063949059	6:39			2017-21-02	6:39:49	0.27765	Tue	2	4	2017-21-2 6:39:49	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063949278	6:39			2017-21-02	6:39:49	0.27765	Tue	2	4	2017-21-2 6:39:49	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063949438	6:39			2017-21-02	6:39:49	0.27765	Tue	2	4	2017-21-2 6:39:49	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063949633	6:39			2017-21-02	6:39:49	0.27765	Tue	2	4	2017-21-2 6:39:49	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063949815	6:39			2017-21-02	6:39:49	0.27765	Tue	2	4	2017-21-2 6:39:49	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063950225	6:39			2017-21-02	6:39:50	0.277662	Tue	2	4	2017-21-2 6:39:50	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063950024	6:39			2017-21-02	6:39:50	0.277662	Tue	2	4	2017-21-2 6:39:50	56
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 21 06:39 BCRTOFX.txt.20170221063950417	6:39			2017-21-02	6:39:50	0.277662	Tue	2	4	2017-21-2 6:39:50	56
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr     13399 Feb 21 14:38 BRA_BRA_Ver_20170221.csv.20170221143843831	14:38	2/21/2017		2017-21-02	14:38:43	0.61022	Tue	2	5	2017-21-2 14:38:43	56
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       353 Feb 21 10:34 CDPSfx_BRLorder.20170221.103500.csv.20170221103408739	10:34	2/21/2017	10:35:00	2017-21-02	10:34:08	0.44037	Tue	2	6	2017-21-2 10:34:08	56
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1449 Feb 21 00:19 SPOT_FET_Instructions_StateStreet_20170220-161254.csv.20170221001950903	0:19	2/20/2017	16:12:54	2017-21-02	0:19:50	0.013773	Tue	2	7	2017-21-2 0:19:50	56
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       224 Feb 21 04:32 scbcnhtrades1.in.201702211721.20170221043211072	4:32	2/21/2017	17:21:00	2017-21-02	4:32:11	0.189016	Tue	2	7	2017-21-2 4:32:11	56
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 21 04:32 scbcnhtrades2.in.201702211722.20170221043211401	4:32	2/21/2017	17:22:00	2017-21-02	4:32:11	0.189016	Tue	2	7	2017-21-2 4:32:11	56
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1570 Feb 21 09:42 SPOT_FET_Instructions_StateStreet_20170221-152957.csv.20170221094205240	9:42	2/21/2017	15:29:57	2017-21-02	9:42:05	0.404225	Tue	2	7	2017-21-2 9:42:05	56
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       379 Feb 21 17:12 02212017_GAM_GAM_STAR_GS.20170221.csv.20170221171254229	17:12	2/21/2017		2017-21-02	17:12:54	0.717292	Tue	2	9	2017-21-2 17:12:54	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     19526 Feb 21 10:34 trade10.dat.20170221103409209	10:34			2017-21-02	10:34:09	0.440382	Tue	2	10	2017-21-2 10:34:09	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb 21 12:34 trade10.dat.20170221123436206	12:34			2017-21-02	12:34:36	0.524028	Tue	2	10	2017-21-2 12:34:36	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     30376 Feb 21 14:34 trade10.dat.20170221143443146	14:34			2017-21-02	14:34:43	0.607442	Tue	2	10	2017-21-2 14:34:43	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     82890 Feb 21 16:24 trade10.dat.20170221162449667	16:24			2017-21-02	16:24:49	0.6839	Tue	2	10	2017-21-2 16:24:49	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 21 17:04 trade10.dat.20170221170453499	17:04			2017-21-02	17:04:53	0.711725	Tue	2	10	2017-21-2 17:04:53	56
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 21 18:04 trade10.dat.20170221180459027	18:04			2017-21-02	18:04:59	0.753461	Tue	2	10	2017-21-2 18:04:59	56
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       774 Feb 21 05:50 UKFCMCurrencyTemplate150217.csv.20170221055016060	5:50			2017-21-02	5:50:16	0.243241	Tue	2	11	2017-21-2 5:50:16	56
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       990 Feb 21 06:32 UKFCMCurrencyTemplate210217.csv.20170221063217189	6:32			2017-21-02	6:32:17	0.272419	Tue	2	11	2017-21-2 6:32:17	56
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    526728 Feb 21 09:30 passporttrans.20170221.csv.20170221093033760	9:30	2/21/2017		2017-21-02	9:30:33	0.396215	Tue	2	15	2017-21-2 9:30:33	56
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Feb 21 08:32 HighlandCapitalManagementRecon201702210730.csv.20170221083228094	8:32	2/21/2017	7:30:00	2017-21-02	8:32:28	0.35588	Tue	2	16	2017-21-2 8:32:28	56
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr      2048 Feb 21 02:52 HSBC-LKR.in.21022017-1.20170221025204632	 02:5	2/21/2017		2017-21-02	2:52:04	0.119491	Tue	2	17	2017-21-2 2:52:04	56
John Hancock Investments	HAN_TRANS_HANVER_20170221.csv.20170221153846999	15:38	2/21/2017		2017-21-02	15:38:46	0.651921	Tue	2	18	2017-21-2 15:38:46	56
John Hancock Investments	HAN_TRANS_HANVER_20170221.csv.20170221153846999	15:38	2/21/2017		2017-21-02	15:38:46	0.651921	Tue	2	18	2017-21-2 15:38:46	56
National Pension Service (NPS)	-rw-r--r--   1 ftpgmrin ftpgmr      1632 Feb 21 02:14 20170223CA_NPSA.csv.20170221021403313	2:14	2/23/2017		2017-21-02	2:14:03	0.09309	Tue	2	20	2017-21-2 2:14:03	56
National Pension Service (NPS)	-rw-r--r--   1 ftpgmrin ftpgmr      1641 Feb 21 19:31 20170223CA_NPSA.csv.20170221193105121	19:31	2/23/2017		2017-21-02	19:31:05	0.813252	Tue	2	20	2017-21-2 19:31:05	56
National Pension Service (NPS)	-rw-r--r--   1 ftpgmrin ftpgmr      1640 Feb 21 19:53 20170223CA_NPSA.csv.20170221195306774	19:53	2/23/2017		2017-21-02	19:53:06	0.828542	Tue	2	20	2017-21-2 19:53:06	56
National Pension Service (NPS)	-rw-r--r--   1 ftpgmrin ftpgmr      1638 Feb 21 20:17 20170223CA_NPSA.csv.20170221201708664	20:17	2/23/2017		2017-21-02	20:17:08	0.845231	Tue	2	20	2017-21-2 20:17:08	56
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 21 15:00 PAXStateStreetFX_Orders_022117.txt.20170221150044653	15:00	2/21/2017		2017-21-02	15:00:44	0.625509	Tue	2	23	2017-21-2 15:00:44	56
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 21 15:34 PAXStateStreetFX_Orders_022117.txt.20170221153446340	15:34	2/21/2017		2017-21-02	15:34:46	0.649144	Tue	2	23	2017-21-2 15:34:46	56
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 21 16:26 PAXStateStreetFX_Orders_022117.txt.20170221162650411	16:26	2/21/2017		2017-21-02	16:26:50	0.685301	Tue	2	23	2017-21-2 16:26:50	56
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       205 Feb 21 10:48 PGI_Orders_20170221094621.csv.20170221104809795	10:48	2/21/2017	9:46:21	2017-21-02	10:48:09	0.450104	Tue	2	24	2017-21-2 10:48:09	56
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 21 03:10 INV_fx_20170221_090741.csv.20170221031005304	3:10	2/21/2017	9:07:41	2017-21-02	3:10:05	0.132002	Tue	2	26	2017-21-2 3:10:05	56
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       305 Feb 21 03:12 FT_fx_20170221_090806.csv.20170221031205818	3:12	2/21/2017	9:08:06	2017-21-02	3:12:05	0.133391	Tue	2	26	2017-21-2 3:12:05	56
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Feb 21 04:30 FT_fx_20170221_102701.csv.20170221043009918	4:30	2/21/2017	10:27:01	2017-21-02	4:30:09	0.187604	Tue	2	26	2017-21-2 4:30:09	56
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 21 04:44 INV_fx_20170221_104152.csv.20170221044412375	4:44	2/21/2017	10:41:52	2017-21-02	4:44:12	0.197361	Tue	2	26	2017-21-2 4:44:12	56
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Feb 21 05:42 FT_fx_20170221_113836.csv.20170221054215164	5:42	2/21/2017	11:38:36	2017-21-02	5:42:15	0.237674	Tue	2	26	2017-21-2 5:42:15	56
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       296 Feb 21 03:22 citicnhtrades.in.201702211608.20170221032206647	3:22	2/21/2017	16:08:00	2017-21-02	3:22:06	0.140347	Tue	2	28	2017-21-2 3:22:06	56
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 21 04:32 citicnhtrades.in.201702211716.20170221043210693	4:32	2/21/2017	17:16:00	2017-21-02	4:32:10	0.189005	Tue	2	28	2017-21-2 4:32:10	56
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       861 Feb 21 04:32 hsbccnhtrades.in.201702211716.20170221043210914	4:32	2/21/2017	17:16:00	2017-21-02	4:32:10	0.189005	Tue	2	29	2017-21-2 4:32:10	56
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     26355 Feb 21 10:08 RSWGD1-17_SSGM_Confirmed_File__20170221.csv.20170221100807129	10:08	2/21/2017		2017-21-02	10:08:07	0.422303	Tue	2	30	2017-21-2 10:08:07	56
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4983 Feb 21 09:32 TIAACREFREPAT.csv.20170221093234258	9:32			2017-21-02	9:32:34	0.397616	Tue	2	32	2017-21-2 9:32:34	56
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       535 Feb 21 13:30 TIAACREFREPAT.csv.20170221133038897	13:30			2017-21-02	13:30:38	0.56294	Tue	2	32	2017-21-2 13:30:38	56
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       407 Feb 21 21:28 tokyofundtrades.in.201702221004.20170221212846133	 21:2	2/22/2017	10:04:00	2017-21-02	21:28:46	0.894977	Tue	2	33	2017-21-2 21:28:46	56
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       258 Feb 22 11:35 Alger_Orders_20170222113352.csv.20170222113535651	11:35	2/22/2017	11:33:52	2017-22-02	11:35:35	0.483044	Wed	3	1	2017-22-2 11:35:35	57
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3281 Feb 22 11:49 alps_Orders_02222017095000.csv.20170222114939636	11:49	2/22/2017	9:50:00	2017-22-02	11:49:39	0.492813	Wed	3	2	2017-22-2 11:49:39	57
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1408 Feb 22 04:33 SSC_BAM_FXREQ_20170222_093000.csv.pgp.ndm05.20170222043310605	4:33	2/22/2017	9:30:00	2017-22-02	4:33:10	0.189699	Wed	3	3	2017-22-2 4:33:10	57
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1441 Feb 22 13:32 SSC_BAM_FXREQ_20170222_183019.csv.pgp.ndm05.20170222133217122	13:32	2/22/2017	18:30:19	2017-22-02	13:32:17	0.564086	Wed	3	3	2017-22-2 13:32:17	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064146651	6:41			2017-22-02	6:41:46	0.279005	Wed	3	4	2017-22-2 6:41:46	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064147037	6:41			2017-22-02	6:41:47	0.279016	Wed	3	4	2017-22-2 6:41:47	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064147222	6:41			2017-22-02	6:41:47	0.279016	Wed	3	4	2017-22-2 6:41:47	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064147442	6:41			2017-22-02	6:41:47	0.279016	Wed	3	4	2017-22-2 6:41:47	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064147618	6:41			2017-22-02	6:41:47	0.279016	Wed	3	4	2017-22-2 6:41:47	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064147817	6:41			2017-22-02	6:41:47	0.279016	Wed	3	4	2017-22-2 6:41:47	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064148045	6:41			2017-22-02	6:41:48	0.279028	Wed	3	4	2017-22-2 6:41:48	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064148221	6:41			2017-22-02	6:41:48	0.279028	Wed	3	4	2017-22-2 6:41:48	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064148405	6:41			2017-22-02	6:41:48	0.279028	Wed	3	4	2017-22-2 6:41:48	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064148618	6:41			2017-22-02	6:41:48	0.279028	Wed	3	4	2017-22-2 6:41:48	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064148817	6:41			2017-22-02	6:41:48	0.279028	Wed	3	4	2017-22-2 6:41:48	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064149015	6:41			2017-22-02	6:41:49	0.279039	Wed	3	4	2017-22-2 6:41:49	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064149216	6:41			2017-22-02	6:41:49	0.279039	Wed	3	4	2017-22-2 6:41:49	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064149414	6:41			2017-22-02	6:41:49	0.279039	Wed	3	4	2017-22-2 6:41:49	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064149612	6:41			2017-22-02	6:41:49	0.279039	Wed	3	4	2017-22-2 6:41:49	57
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 22 06:41 BCRTOFX.txt.20170222064149821	6:41			2017-22-02	6:41:49	0.279039	Wed	3	4	2017-22-2 6:41:49	57
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7078 Feb 22 14:37 BRA_BRA_Ver_20170222.csv.20170222143722675	14:37	2/22/2017		2017-22-02	14:37:22	0.609282	Wed	3	5	2017-22-2 14:37:22	57
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       337 Feb 22 04:09 scbcnhtrades1.in.201702221701.20170222040908187	4:09	2/22/2017	17:01:00	2017-22-02	4:09:08	0.173009	Wed	3	7	2017-22-2 4:09:08	57
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 22 04:09 scbcnhtrades2.in.201702221701.20170222040908469	4:09	2/22/2017	17:01:00	2017-22-02	4:09:08	0.173009	Wed	3	7	2017-22-2 4:09:08	57
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        55 Feb 22 05:03 scbcnhtrades1.in.201702221756.20170222050312016	5:03	2/22/2017	17:56:00	2017-22-02	5:03:12	0.210556	Wed	3	7	2017-22-2 5:03:12	57
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 22 05:03 scbcnhtrades2.in.201702221756.20170222050312256	5:03	2/22/2017	17:56:00	2017-22-02	5:03:12	0.210556	Wed	3	7	2017-22-2 5:03:12	57
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       867 Feb 22 09:05 SPOT_FET_Instructions_StateStreet_20170222-145147.csv.20170222090528507	9:05	2/22/2017	14:51:47	2017-22-02	9:05:28	0.378796	Wed	3	7	2017-22-2 9:05:28	57
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       260 Feb 22 17:25 02222017_GAM_GAM_STAR_GS.20170222.csv.20170222172533157	17:25	2/22/2017		2017-22-02	17:25:33	0.726076	Wed	3	9	2017-22-2 17:25:33	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3468 Feb 22 10:35 trade10.dat.20170222103506262	10:35			2017-22-02	10:35:06	0.441042	Wed	3	10	2017-22-2 10:35:06	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb 22 12:33 trade10.dat.20170222123343277	12:33			2017-22-02	12:33:43	0.523414	Wed	3	10	2017-22-2 12:33:43	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 22 14:35 trade10.dat.20170222143521796	14:35			2017-22-02	14:35:21	0.607882	Wed	3	10	2017-22-2 14:35:21	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     15186 Feb 22 16:25 trade10.dat.20170222162527579	16:25			2017-22-02	16:25:27	0.68434	Wed	3	10	2017-22-2 16:25:27	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 22 17:03 trade10.dat.20170222170330757	17:03			2017-22-02	17:03:30	0.710764	Wed	3	10	2017-22-2 17:03:30	57
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 22 18:03 trade10.dat.20170222180336936	18:03			2017-22-02	18:03:36	0.7525	Wed	3	10	2017-22-2 18:03:36	57
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       214 Feb 22 01:56 FSS_Orders_20170222.csv.20170222015659548	1:56	2/22/2017		2017-22-02	1:56:59	0.081238	Wed	3	13	2017-22-2 1:56:59	57
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    346224 Feb 22 08:59 passporttrans.20170222.csv.20170222085927495	8:59	2/22/2017		2017-22-02	8:59:27	0.374618	Wed	3	15	2017-22-2 8:59:27	57
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2033 Feb 22 08:31 HighlandCapitalManagementRecon201702220730.csv.20170222083125902	8:31	2/22/2017	7:30:00	2017-22-02	8:31:25	0.35515	Wed	3	16	2017-22-2 8:31:25	57
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       754 Feb 22 02:29 HSBC-LKR.in.22022017-1.20170222022901871	 02:2	2/22/2017		2017-22-02	2:29:01	0.103484	Wed	3	17	2017-22-2 2:29:01	57
John Hancock Investments	HAN_TRANS_HANVER_20170222.csv.20170222153724794	15:37	2/22/2017		2017-22-02	15:37:24	0.650972	Wed	3	18	2017-22-2 15:37:24	57
John Hancock Investments	HAN_TRANS_HANVER_20170222.csv.20170222153724794	15:37	2/22/2017		2017-22-02	15:37:24	0.650972	Wed	3	18	2017-22-2 15:37:24	57
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 22 16:27 PAXStateStreetFX_Orders_022217.txt.20170222162728248	16:27	2/22/2017		2017-22-02	16:27:28	0.685741	Wed	3	23	2017-22-2 16:27:28	57
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       208 Feb 22 11:05 PresimaOrders.csv.20170222110509698	11:05			2017-22-02	11:05:09	0.46191	Wed	3	25	2017-22-2 11:05:09	57
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       204 Feb 22 14:35 PresimaOrders.csv.20170222143522168	14:35			2017-22-02	14:35:22	0.607894	Wed	3	25	2017-22-2 14:35:22	57
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb 22 02:55 FT_fx_20170222_085139.csv.20170222025503054	2:55	2/22/2017	8:51:39	2017-22-02	2:55:03	0.121563	Wed	3	26	2017-22-2 2:55:03	57
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 22 03:19 INV_fx_20170222_091743.csv.20170222031904668	3:19	2/22/2017	9:17:43	2017-22-02	3:19:04	0.138241	Wed	3	26	2017-22-2 3:19:04	57
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Feb 22 03:47 FT_fx_20170222_093326.csv.20170222034706762	3:47	2/22/2017	9:33:26	2017-22-02	3:47:06	0.157708	Wed	3	26	2017-22-2 3:47:06	57
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 22 04:59 FT_fx_20170222_105715.csv.20170222045911621	4:59	2/22/2017	10:57:15	2017-22-02	4:59:11	0.207766	Wed	3	26	2017-22-2 4:59:11	57
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 22 05:41 FT_fx_20170222_113910.csv.20170222054114300	5:41	2/22/2017	11:39:10	2017-22-02	5:41:14	0.236968	Wed	3	26	2017-22-2 5:41:14	57
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       177 Feb 22 03:15 citicnhtrades.in.201702221609.20170222031504132	3:15	2/22/2017	16:09:00	2017-22-02	3:15:04	0.135463	Wed	3	28	2017-22-2 3:15:04	57
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 22 04:23 citicnhtrades.in.201702221714.20170222042309437	4:23	2/22/2017	17:14:00	2017-22-02	4:23:09	0.182743	Wed	3	28	2017-22-2 4:23:09	57
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr      1161 Feb 22 04:23 hsbccnhtrades.in.201702221714.20170222042309628	4:23	2/22/2017	17:14:00	2017-22-02	4:23:09	0.182743	Wed	3	29	2017-22-2 4:23:09	57
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28456 Feb 22 10:27 RSWGD1-17_SSGM_Confirmed_File__20170222.csv.20170222102705457	10:27	2/22/2017		2017-22-02	10:27:05	0.435475	Wed	3	30	2017-22-2 10:27:05	57
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       524 Feb 22 09:25 tcwta20170222.csv.20170222092500315	9:25	2/22/2017		2017-22-02	9:25:00	0.392361	Wed	3	31	2017-22-2 9:25:00	57
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      1816 Feb 22 09:31 TIAACREFREPAT.csv.20170222093100706	9:31			2017-22-02	9:31:00	0.396528	Wed	3	32	2017-22-2 9:31:00	57
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       427 Feb 22 13:31 TIAACREFREPAT.csv.20170222133116570	13:31			2017-22-02	13:31:16	0.56338	Wed	3	32	2017-22-2 13:31:16	57
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      3051 Feb 22 21:45 tokyofundtrades.in.201702231036.20170222214551597	 21:4	2/23/2017	10:36:00	2017-22-02	21:45:51	0.90684	Wed	3	33	2017-22-2 21:45:51	57
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Feb 23 11:12 Alger_Orders_20170223110950.csv.20170223111213306	11:12	2/23/2017	11:09:50	2017-23-02	11:12:13	0.466817	Thu	4	1	2017-23-2 11:12:13	58
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      5671 Feb 23 16:30 alps_Orders_02232017023000.csv.20170223163045373	16:30	2/23/2017	2:30:00	2017-23-02	16:30:45	0.688021	Thu	4	2	2017-23-2 16:30:45	58
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1423 Feb 23 05:32 SSC_BAM_FXREQ_20170223_103016.csv.pgp.ndm05.20170223053216724	5:32	2/23/2017	10:30:16	2017-23-02	5:32:16	0.230741	Thu	4	3	2017-23-2 5:32:16	58
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1404 Feb 23 10:33 SSC_BAM_FXREQ_20170223_153028.csv.pgp.ndm05.20170223103309550	10:33	2/23/2017	15:30:28	2017-23-02	10:33:09	0.439688	Thu	4	3	2017-23-2 10:33:09	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064019034	6:40			2017-23-02	6:40:19	0.277998	Thu	4	4	2017-23-2 6:40:19	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064019285	6:40			2017-23-02	6:40:19	0.277998	Thu	4	4	2017-23-2 6:40:19	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064019471	6:40			2017-23-02	6:40:19	0.277998	Thu	4	4	2017-23-2 6:40:19	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064019699	6:40			2017-23-02	6:40:19	0.277998	Thu	4	4	2017-23-2 6:40:19	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064019870	6:40			2017-23-02	6:40:19	0.277998	Thu	4	4	2017-23-2 6:40:19	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064020079	6:40			2017-23-02	6:40:20	0.278009	Thu	4	4	2017-23-2 6:40:20	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064020274	6:40			2017-23-02	6:40:20	0.278009	Thu	4	4	2017-23-2 6:40:20	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064020526	6:40			2017-23-02	6:40:20	0.278009	Thu	4	4	2017-23-2 6:40:20	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064020674	6:40			2017-23-02	6:40:20	0.278009	Thu	4	4	2017-23-2 6:40:20	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064020902	6:40			2017-23-02	6:40:20	0.278009	Thu	4	4	2017-23-2 6:40:20	58
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 23 06:40 BCRTOFX.txt.20170223064021088	6:40			2017-23-02	6:40:21	0.278021	Thu	4	4	2017-23-2 6:40:21	58
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      6547 Feb 23 14:38 BRA_BRA_Ver_20170223.csv.20170223143838756	14:38	2/23/2017		2017-23-02	14:38:38	0.610162	Thu	4	5	2017-23-2 14:38:38	58
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       330 Feb 23 13:06 CDPSfx_BRLorder.20170223.130403.csv.20170223130632800	13:06	2/23/2017	13:04:03	2017-23-02	13:06:32	0.546204	Thu	4	6	2017-23-2 13:06:32	58
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       389 Feb 23 04:14 scbcnhtrades1.in.201702231702.20170223041411352	4:14	2/23/2017	17:02:00	2017-23-02	4:14:11	0.176516	Thu	4	7	2017-23-2 4:14:11	58
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 23 04:14 scbcnhtrades2.in.201702231702.20170223041411751	4:14	2/23/2017	17:02:00	2017-23-02	4:14:11	0.176516	Thu	4	7	2017-23-2 4:14:11	58
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Feb 23 05:12 scbcnhtrades1.in.201702231759.20170223051215517	5:12	2/23/2017	17:59:00	2017-23-02	5:12:15	0.21684	Thu	4	7	2017-23-2 5:12:15	58
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 23 05:12 scbcnhtrades2.in.201702231759.20170223051215837	5:12	2/23/2017	17:59:00	2017-23-02	5:12:15	0.21684	Thu	4	7	2017-23-2 5:12:15	58
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1719 Feb 23 09:04 SPOT_FET_Instructions_StateStreet_20170223-144942.csv.20170223090401379	9:04	2/23/2017	14:49:42	2017-23-02	9:04:01	0.377789	Thu	4	7	2017-23-2 9:04:01	58
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       516 Feb 23 17:12 02232017_GAM_GAM_STAR_GS.20170223.csv.20170223171248300	17:12	2/23/2017		2017-23-02	17:12:48	0.717222	Thu	4	9	2017-23-2 17:12:48	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5204 Feb 23 10:34 trade10.dat.20170223103409874	10:34			2017-23-02	10:34:09	0.440382	Thu	4	10	2017-23-2 10:34:09	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Feb 23 12:34 trade10.dat.20170223123430920	12:34			2017-23-02	12:34:30	0.523958	Thu	4	10	2017-23-2 12:34:30	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1298 Feb 23 14:34 trade10.dat.20170223143438096	14:34			2017-23-02	14:34:38	0.607384	Thu	4	10	2017-23-2 14:34:38	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr    196164 Feb 23 16:24 trade10.dat.20170223162443942	16:24			2017-23-02	16:24:43	0.683831	Thu	4	10	2017-23-2 16:24:43	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 23 17:04 trade10.dat.20170223170447155	17:04			2017-23-02	17:04:47	0.711655	Thu	4	10	2017-23-2 17:04:47	58
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 23 18:04 trade10.dat.20170223180452856	18:04			2017-23-02	18:04:52	0.75338	Thu	4	10	2017-23-2 18:04:52	58
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr      1045 Feb 23 05:46 UKFCMCurrencyTemplate230217.csv.20170223054617547	5:46			2017-23-02	5:46:17	0.240475	Thu	4	11	2017-23-2 5:46:17	58
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    360712 Feb 23 08:54 passporttrans.20170223.csv.20170223085400704	8:54	2/23/2017		2017-23-02	8:54:00	0.370833	Thu	4	15	2017-23-2 8:54:00	58
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      6643 Feb 23 08:32 HighlandCapitalManagementRecon201702230730.csv.20170223083229726	8:32	2/23/2017	7:30:00	2017-23-02	8:32:29	0.355891	Thu	4	16	2017-23-2 8:32:29	58
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       432 Feb 23 11:00 Highland_Orders_20170223csv.20170223110010965	11:00	2/23/2017		2017-23-02	11:00:10	0.458449	Thu	4	16	2017-23-2 11:00:10	58
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       665 Feb 23 01:34 HSBC-LKR.in.23022017-1.20170223013402032	 01:3	2/23/2017		2017-23-02	1:34:02	0.065301	Thu	4	17	2017-23-2 1:34:02	58
John Hancock Investments	HAN_TRANS_HANVER_20170223.csv.20170223153440472	15:34	2/23/2017		2017-23-02	15:34:40	0.649074	Thu	4	18	2017-23-2 15:34:40	58
John Hancock Investments	HAN_TRANS_HANVER_20170223.csv.20170223153440472	15:34	2/23/2017		2017-23-02	15:34:40	0.649074	Thu	4	18	2017-23-2 15:34:40	58
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 23 09:20 PAXStateStreetFX_Orders_022317.txt.20170223092003141	9:20	2/23/2017		2017-23-02	9:20:03	0.388924	Thu	4	23	2017-23-2 9:20:03	58
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 23 16:28 PAXStateStreetFX_Orders_022317.txt.20170223162844871	16:28	2/23/2017		2017-23-02	16:28:44	0.68662	Thu	4	23	2017-23-2 16:28:44	58
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       300 Feb 23 02:58 FT_fx_20170223_085658.csv.20170223025806791	2:58	2/23/2017	8:56:58	2017-23-02	2:58:06	0.123681	Thu	4	26	2017-23-2 2:58:06	58
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 23 03:16 INV_fx_20170223_091254.csv.20170223031607626	3:16	2/23/2017	9:12:54	2017-23-02	3:16:07	0.136192	Thu	4	26	2017-23-2 3:16:07	58
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 23 05:08 FT_fx_20170223_110532.csv.20170223050815070	5:08	2/23/2017	11:05:32	2017-23-02	5:08:15	0.214063	Thu	4	26	2017-23-2 5:08:15	58
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       298 Feb 23 05:46 FT_fx_20170223_114402.csv.20170223054617246	5:46	2/23/2017	11:44:02	2017-23-02	5:46:17	0.240475	Thu	4	26	2017-23-2 5:46:17	58
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       297 Feb 23 03:22 citicnhtrades.in.201702231615.20170223032208580	3:22	2/23/2017	16:15:00	2017-23-02	3:22:08	0.14037	Thu	4	28	2017-23-2 3:22:08	58
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 23 04:24 citicnhtrades.in.201702231713.20170223042412214	4:24	2/23/2017	17:13:00	2017-23-02	4:24:12	0.183472	Thu	4	28	2017-23-2 4:24:12	58
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       668 Feb 23 04:24 hsbccnhtrades.in.201702231713.20170223042412672	4:24	2/23/2017	17:13:00	2017-23-02	4:24:12	0.183472	Thu	4	29	2017-23-2 4:24:12	58
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     30660 Feb 23 10:20 RSWGD1-17_SSGM_Confirmed_File__20170223.csv.20170223102008180	10:20	2/23/2017		2017-23-02	10:20:08	0.430648	Thu	4	30	2017-23-2 10:20:08	58
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2607 Feb 23 09:32 TIAACREFREPAT.csv.20170223093205297	9:32			2017-23-02	9:32:05	0.39728	Thu	4	32	2017-23-2 9:32:05	58
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       320 Feb 23 13:32 TIAACREFREPAT.csv.20170223133233952	13:32			2017-23-02	13:32:33	0.564271	Thu	4	32	2017-23-2 13:32:33	58
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       223 Feb 23 10:30 TrinityStreetFX_022317.csv.20170223103009066	10:30			2017-23-02	10:30:09	0.437604	Thu	4	34	2017-23-2 10:30:09	58
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3287 Feb 24 11:58 alps_Orders_02242017095500.csv.20170224115831637	11:58	2/24/2017	9:55:00	2017-24-02	11:58:31	0.49897	Fri	5	2	2017-24-2 11:58:31	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1532 Feb 24 04:33 SSC_BAM_FXREQ_20170224_093010.csv.pgp.ndm05.20170224043337018	4:33	2/24/2017	9:30:10	2017-24-02	4:33:37	0.190012	Fri	5	3	2017-24-2 4:33:37	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1912 Feb 24 07:31 SSC_BAM_FXREQ_20170224_123017.csv.pgp.ndm05.20170224073148279	7:31	2/24/2017	12:30:17	2017-24-02	7:31:48	0.31375	Fri	5	3	2017-24-2 7:31:48	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Feb 24 09:31 SSC_BAM_FXREQ_20170224_143021.csv.pgp.ndm05.20170224093155895	9:31	2/24/2017	14:30:21	2017-24-02	9:31:55	0.397164	Fri	5	3	2017-24-2 9:31:55	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Feb 24 10:32 SSC_BAM_FXREQ_20170224_153025.csv.pgp.ndm05.20170224103201216	10:32	2/24/2017	15:30:25	2017-24-02	10:32:01	0.4389	Fri	5	3	2017-24-2 10:32:01	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1405 Feb 24 11:32 SSC_BAM_FXREQ_20170224_163028.csv.pgp.ndm05.20170224113222057	11:32	2/24/2017	16:30:28	2017-24-02	11:32:22	0.48081	Fri	5	3	2017-24-2 11:32:22	59
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1452 Feb 24 12:32 SSC_BAM_FXREQ_20170224_173031.csv.pgp.ndm05.20170224123235327	12:32	2/24/2017	17:30:31	2017-24-02	12:32:35	0.522627	Fri	5	3	2017-24-2 12:32:35	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064042763	6:40			2017-24-02	6:40:42	0.278264	Fri	5	4	2017-24-2 6:40:42	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064043062	6:40			2017-24-02	6:40:43	0.278275	Fri	5	4	2017-24-2 6:40:43	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064043251	6:40			2017-24-02	6:40:43	0.278275	Fri	5	4	2017-24-2 6:40:43	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064043460	6:40			2017-24-02	6:40:43	0.278275	Fri	5	4	2017-24-2 6:40:43	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064043645	6:40			2017-24-02	6:40:43	0.278275	Fri	5	4	2017-24-2 6:40:43	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064043892	6:40			2017-24-02	6:40:43	0.278275	Fri	5	4	2017-24-2 6:40:43	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064044091	6:40			2017-24-02	6:40:44	0.278287	Fri	5	4	2017-24-2 6:40:44	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064044240	6:40			2017-24-02	6:40:44	0.278287	Fri	5	4	2017-24-2 6:40:44	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064044453	6:40			2017-24-02	6:40:44	0.278287	Fri	5	4	2017-24-2 6:40:44	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064044653	6:40			2017-24-02	6:40:44	0.278287	Fri	5	4	2017-24-2 6:40:44	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064044854	6:40			2017-24-02	6:40:44	0.278287	Fri	5	4	2017-24-2 6:40:44	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064045045	6:40			2017-24-02	6:40:45	0.278299	Fri	5	4	2017-24-2 6:40:45	59
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 24 06:40 BCRTOFX.txt.20170224064045245	6:40			2017-24-02	6:40:45	0.278299	Fri	5	4	2017-24-2 6:40:45	59
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      5412 Feb 24 14:40 BRA_BRA_Ver_20170224.csv.20170224144043616	14:40	2/24/2017		2017-24-02	14:40:43	0.611609	Fri	5	5	2017-24-2 14:40:43	59
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       552 Feb 24 04:13 scbcnhtrades1.in.201702241704.20170224041303623	4:13	2/24/2017	17:04:00	2017-24-02	4:13:03	0.175729	Fri	5	7	2017-24-2 4:13:03	59
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 24 04:13 scbcnhtrades2.in.201702241704.20170224041304033	4:13	2/24/2017	17:04:00	2017-24-02	4:13:04	0.175741	Fri	5	7	2017-24-2 4:13:04	59
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1146 Feb 24 08:49 SPOT_FET_Instructions_StateStreet_20170224-144203.csv.20170224084921990	8:49	2/24/2017	14:42:03	2017-24-02	8:49:21	0.367604	Fri	5	7	2017-24-2 8:49:21	59
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       363 Feb 24 16:48 02242017_GAM_GAM_STAR_GS.20170224.csv.20170224164853048	16:48	2/24/2017		2017-24-02	16:48:53	0.700613	Fri	5	9	2017-24-2 16:48:53	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     34716 Feb 24 10:36 trade10.dat.20170224103601619	10:36			2017-24-02	10:36:01	0.441678	Fri	5	10	2017-24-2 10:36:01	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb 24 12:34 trade10.dat.20170224123435924	12:34			2017-24-02	12:34:35	0.524016	Fri	5	10	2017-24-2 12:34:35	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     50774 Feb 24 14:34 trade10.dat.20170224143442991	14:34			2017-24-02	14:34:42	0.607431	Fri	5	10	2017-24-2 14:34:42	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     23432 Feb 24 16:24 trade10.dat.20170224162449605	16:24			2017-24-02	16:24:49	0.6839	Fri	5	10	2017-24-2 16:24:49	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4770 Feb 24 17:04 trade10.dat.20170224170423808	17:04			2017-24-02	17:04:23	0.711377	Fri	5	10	2017-24-2 17:04:23	59
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 24 18:04 trade10.dat.20170224180429450	18:04			2017-24-02	18:04:29	0.753113	Fri	5	10	2017-24-2 18:04:29	59
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       213 Feb 24 00:11 FSS_Orders_20170224.csv.20170224001113163	0:11	2/24/2017		2017-24-02	0:11:13	0.007789	Fri	5	13	2017-24-2 0:11:13	59
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    307379 Feb 24 08:53 passporttrans.20170224.csv.20170224085322529	8:53	2/24/2017		2017-24-02	8:53:22	0.370394	Fri	5	15	2017-24-2 8:53:22	59
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Feb 24 08:31 HighlandCapitalManagementRecon201702240730.csv.20170224083120561	8:31	2/24/2017	7:30:00	2017-24-02	8:31:20	0.355093	Fri	5	16	2017-24-2 8:31:20	59
John Hancock Investments	HAN_TRANS_HANVER_20170224.csv.20170224153846821	15:38	2/24/2017		2017-24-02	15:38:46	0.651921	Fri	5	18	2017-24-2 15:38:46	59
John Hancock Investments	HAN_TRANS_HANVER_20170224.csv.20170224153846821	15:38	2/24/2017		2017-24-02	15:38:46	0.651921	Fri	5	18	2017-24-2 15:38:46	59
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 24 16:46 PAXStateStreetFX_Orders_022417.txt.20170224164652031	16:46	2/24/2017		2017-24-02	16:46:52	0.699213	Fri	5	23	2017-24-2 16:46:52	59
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 24 16:48 PAXStateStreetFX_Orders_022417.txt.20170224164852612	16:48	2/24/2017		2017-24-02	16:48:52	0.700602	Fri	5	23	2017-24-2 16:48:52	59
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       832 Feb 24 14:22 PGI_Orders_20170224132056.csv.20170224142241683	14:22	2/24/2017	13:20:56	2017-24-02	14:22:41	0.599086	Fri	5	24	2017-24-2 14:22:41	59
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       205 Feb 24 11:36 PresimaOrders.csv.20170224113628401	11:36			2017-24-02	11:36:28	0.483657	Fri	5	25	2017-24-2 11:36:28	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb 24 03:12 FT_fx_20170224_091055.csv.20170224031259020	3:12	2/24/2017	9:10:55	2017-24-02	3:12:59	0.134016	Fri	5	26	2017-24-2 3:12:59	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 24 03:14 INV_fx_20170224_091219.csv.20170224031459623	3:14	2/24/2017	9:12:19	2017-24-02	3:14:59	0.135405	Fri	5	26	2017-24-2 3:14:59	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Feb 24 04:29 INV_fx_20170224_102657.csv.20170224042905885	4:29	2/24/2017	10:26:57	2017-24-02	4:29:05	0.186863	Fri	5	26	2017-24-2 4:29:05	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Feb 24 04:31 FT_fx_20170224_102834.csv.20170224043106389	4:31	2/24/2017	10:28:34	2017-24-02	4:31:06	0.188264	Fri	5	26	2017-24-2 4:31:06	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 24 04:47 INV_fx_20170224_104422.csv.20170224044707716	4:47	2/24/2017	10:44:22	2017-24-02	4:47:07	0.199387	Fri	5	26	2017-24-2 4:47:07	59
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       228 Feb 24 05:59 FT_fx_20170224_115659.csv.20170224055911066	5:59	2/24/2017	11:56:59	2017-24-02	5:59:11	0.249433	Fri	5	26	2017-24-2 5:59:11	59
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb 24 03:19 citicnhtrades.in.201702241611.20170224031900221	3:19	2/24/2017	16:11:00	2017-24-02	3:19:00	0.138194	Fri	5	28	2017-24-2 3:19:00	59
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 24 04:21 citicnhtrades.in.201702241715.20170224042104825	4:21	2/24/2017	17:15:00	2017-24-02	4:21:04	0.181296	Fri	5	28	2017-24-2 4:21:04	59
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       348 Feb 24 04:21 hsbccnhtrades.in.201702241715.20170224042105047	4:21	2/24/2017	17:15:00	2017-24-02	4:21:05	0.181308	Fri	5	29	2017-24-2 4:21:05	59
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     29124 Feb 24 10:03 RSWGD1-17_SSGM_Confirmed_File__20170224.csv.20170224100357914	10:03	2/24/2017		2017-24-02	10:03:57	0.41941	Fri	5	30	2017-24-2 10:03:57	59
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      4433 Feb 24 09:31 TIAACREFREPAT.csv.20170224093125268	9:31			2017-24-02	9:31:25	0.396817	Fri	5	32	2017-24-2 9:31:25	59
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       312 Feb 24 10:32 TIAACREFREPAT.csv.20170224103201062	10:32			2017-24-02	10:32:01	0.4389	Fri	5	32	2017-24-2 10:32:01	59
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 24 10:26 TrinityStreetFX_022417.csv.20170224102600228	10:26			2017-24-02	10:26:00	0.434722	Fri	5	34	2017-24-2 10:26:00	59
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       364 Feb 26 22:07 FSS_Orders_20170227.csv.20170226220729697	22:07	2/27/2017		2017-26-02	22:07:29	0.921863	Sun	7	13	2017-26-2 22:07:29	#N/A
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      1389 Feb 26 21:19 tokyofundtrades.in.201702271005.20170226211927244	 21:1	2/27/2017	10:05:00	2017-26-02	21:19:27	0.888507	Sun	7	33	2017-26-2 21:19:27	#N/A
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb 27 09:23 Alger_Orders_20170227092129.csv.20170227092344460	9:23	2/27/2017	9:21:29	2017-27-02	9:23:44	0.391481	Mon	1	1	2017-27-2 9:23:44	60
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       129 Feb 27 13:10 Alger_Orders_20170227130701.csv.20170227131005654	13:10	2/27/2017	13:07:01	2017-27-02	13:10:05	0.548669	Mon	1	1	2017-27-2 13:10:05	60
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3279 Feb 27 14:28 alps_Orders_02272017123000.csv.20170227142811727	14:28	2/27/2017	12:30:00	2017-27-02	14:28:11	0.602905	Mon	1	2	2017-27-2 14:28:11	60
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1686 Feb 27 04:32 SSC_BAM_FXREQ_20170227_093011.csv.pgp.ndm05.20170227043225210	4:32	2/27/2017	9:30:11	2017-27-02	4:32:25	0.189178	Mon	1	3	2017-27-2 4:32:25	60
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1427 Feb 27 05:32 SSC_BAM_FXREQ_20170227_103014.csv.pgp.ndm05.20170227053229076	5:32	2/27/2017	10:30:14	2017-27-02	5:32:29	0.230891	Mon	1	3	2017-27-2 5:32:29	60
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1407 Feb 27 11:33 SSC_BAM_FXREQ_20170227_163028.csv.pgp.ndm05.20170227113323324	11:33	2/27/2017	16:30:28	2017-27-02	11:33:23	0.481516	Mon	1	3	2017-27-2 11:33:23	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064030990	6:40			2017-27-02	6:40:30	0.278125	Mon	1	4	2017-27-2 6:40:30	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064031384	6:40			2017-27-02	6:40:31	0.278137	Mon	1	4	2017-27-2 6:40:31	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064031568	6:40			2017-27-02	6:40:31	0.278137	Mon	1	4	2017-27-2 6:40:31	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064031770	6:40			2017-27-02	6:40:31	0.278137	Mon	1	4	2017-27-2 6:40:31	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064031977	6:40			2017-27-02	6:40:31	0.278137	Mon	1	4	2017-27-2 6:40:31	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064032192	6:40			2017-27-02	6:40:32	0.278148	Mon	1	4	2017-27-2 6:40:32	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064032377	6:40			2017-27-02	6:40:32	0.278148	Mon	1	4	2017-27-2 6:40:32	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064032564	6:40			2017-27-02	6:40:32	0.278148	Mon	1	4	2017-27-2 6:40:32	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064032766	6:40			2017-27-02	6:40:32	0.278148	Mon	1	4	2017-27-2 6:40:32	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064032958	6:40			2017-27-02	6:40:32	0.278148	Mon	1	4	2017-27-2 6:40:32	60
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 27 06:40 BCRTOFX.txt.20170227064033168	6:40			2017-27-02	6:40:33	0.27816	Mon	1	4	2017-27-2 6:40:33	60
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      6710 Feb 27 14:36 BRA_BRA_Ver_20170227.csv.20170227143613353	14:36	2/27/2017		2017-27-02	14:36:13	0.608484	Mon	1	5	2017-27-2 14:36:13	60
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       358 Feb 27 16:33 CDPSfx_KRWorder.20170227.163500.csv.20170227163350761	16:33	2/27/2017	16:35:00	2017-27-02	16:33:50	0.690162	Mon	1	6	2017-27-2 16:33:50	60
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       224 Feb 27 04:23 scbcnhtrades1.in.201702271712.20170227042323351	4:23	2/27/2017	17:12:00	2017-27-02	4:23:23	0.182905	Mon	1	7	2017-27-2 4:23:23	60
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 27 04:23 scbcnhtrades2.in.201702271712.20170227042323719	4:23	2/27/2017	17:12:00	2017-27-02	4:23:23	0.182905	Mon	1	7	2017-27-2 4:23:23	60
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Feb 27 05:01 scbcnhtrades1.in.201702271756.20170227050126556	5:01	2/27/2017	17:56:00	2017-27-02	5:01:26	0.209329	Mon	1	7	2017-27-2 5:01:26	60
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 27 05:03 scbcnhtrades2.in.201702271756.20170227050327002	5:03	2/27/2017	17:56:00	2017-27-02	5:03:27	0.210729	Mon	1	7	2017-27-2 5:03:27	60
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1432 Feb 27 09:51 SPOT_FET_Instructions_StateStreet_20170227-154213.csv.20170227095117016	9:51	2/27/2017	15:42:13	2017-27-02	9:51:17	0.410613	Mon	1	7	2017-27-2 9:51:17	60
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       118 Feb 27 16:32 02272017_GAM_GAM_STAR_GS.20170227.csv.20170227163220172	16:32	2/27/2017		2017-27-02	16:32:20	0.68912	Mon	1	9	2017-27-2 16:32:20	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      3902 Feb 27 10:35 trade10.dat.20170227103520406	10:35			2017-27-02	10:35:20	0.441204	Mon	1	10	2017-27-2 10:35:20	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 27 12:34 trade10.dat.20170227123402949	12:34			2017-27-02	12:34:02	0.523634	Mon	1	10	2017-27-2 12:34:02	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 27 14:34 trade10.dat.20170227143412733	14:34			2017-27-02	14:34:12	0.607083	Mon	1	10	2017-27-2 14:34:12	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     16922 Feb 27 16:24 trade10.dat.20170227162418172	16:24			2017-27-02	16:24:18	0.683542	Mon	1	10	2017-27-2 16:24:18	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 27 17:03 trade10.dat.20170227170353030	17:03			2017-27-02	17:03:53	0.71103	Mon	1	10	2017-27-2 17:03:53	60
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 27 18:03 trade10.dat.20170227180356838	18:03			2017-27-02	18:03:56	0.752731	Mon	1	10	2017-27-2 18:03:56	60
Glendon	-rw-r--r--   1 ftpgmrin ftpgmr       158 Feb 27 11:17 GlendonOrders.csv.20170227111756214	11:17			2017-27-02	11:17:56	0.470787	Mon	1	14	2017-27-2 11:17:56	60
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    385718 Feb 27 08:55 passporttrans.20170227.csv.20170227085541653	8:55	2/27/2017		2017-27-02	8:55:41	0.372002	Mon	1	15	2017-27-2 8:55:41	60
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1653 Feb 27 08:31 HighlandCapitalManagementRecon201702270730.csv.20170227083140497	8:31	2/27/2017	7:30:00	2017-27-02	8:31:40	0.355324	Mon	1	16	2017-27-2 8:31:40	60
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       758 Feb 27 02:13 HSBC-LKR.in.27022017-1.20170227021310981	 02:1	2/27/2017		2017-27-02	2:13:10	0.092477	Mon	1	17	2017-27-2 2:13:10	60
John Hancock Investments	HAN_TRANS_HANVER_20170227.csv.20170227153414955	15:34	2/27/2017		2017-27-02	15:34:14	0.648773	Mon	1	18	2017-27-2 15:34:14	60
John Hancock Investments	HAN_TRANS_HANVER_20170227.csv.20170227153414955	15:34	2/27/2017		2017-27-02	15:34:14	0.648773	Mon	1	18	2017-27-2 15:34:14	60
Northern Trust Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2151 Feb 27 08:25 SNBEM-FX-TradeDate28.02.2017.csv.20170227082539796	8:25	2/28/2017		2017-27-02	8:25:39	0.351146	Mon	1	22	2017-27-2 8:25:39	60
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 27 16:24 PAXStateStreetFX_Orders_022717.txt.20170227162418451	16:24	2/27/2017		2017-27-02	16:24:18	0.683542	Mon	1	23	2017-27-2 16:24:18	60
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       202 Feb 27 15:40 PGI_Orders_20170227143906.csv.20170227154015586	15:40	2/27/2017	14:39:06	2017-27-02	15:40:15	0.652951	Mon	1	24	2017-27-2 15:40:15	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       306 Feb 27 03:09 FT_fx_20170227_090559.csv.20170227030917789	3:09	2/27/2017	9:05:59	2017-27-02	3:09:17	0.131447	Mon	1	26	2017-27-2 3:09:17	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 27 03:15 INV_fx_20170227_091424.csv.20170227031519144	3:15	2/27/2017	9:14:24	2017-27-02	3:15:19	0.135637	Mon	1	26	2017-27-2 3:15:19	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Feb 27 04:15 FT_fx_20170227_101030.csv.20170227041522900	4:15	2/27/2017	10:10:30	2017-27-02	4:15:22	0.177338	Mon	1	26	2017-27-2 4:15:22	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Feb 27 04:27 INV_fx_20170227_102437.csv.20170227042724233	4:27	2/27/2017	10:24:37	2017-27-02	4:27:24	0.185694	Mon	1	26	2017-27-2 4:27:24	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb 27 04:41 INV_fx_20170227_103851.csv.20170227044125662	4:41	2/27/2017	10:38:51	2017-27-02	4:41:25	0.195428	Mon	1	26	2017-27-2 4:41:25	60
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Feb 27 06:53 FT_fx_20170227_125058.csv.20170227065333706	6:53	2/27/2017	12:50:58	2017-27-02	6:53:33	0.287188	Mon	1	26	2017-27-2 6:53:33	60
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr        56 Feb 27 03:15 citicnhtrades.in.201702271607.20170227031518832	3:15	2/27/2017	16:07:00	2017-27-02	3:15:18	0.135625	Mon	1	28	2017-27-2 3:15:18	60
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 27 04:29 citicnhtrades.in.201702271715.20170227042924844	4:29	2/27/2017	17:15:00	2017-27-02	4:29:24	0.187083	Mon	1	28	2017-27-2 4:29:24	60
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr      1165 Feb 27 04:29 hsbccnhtrades.in.201702271715.20170227042924533	4:29	2/27/2017	17:15:00	2017-27-02	4:29:24	0.187083	Mon	1	29	2017-27-2 4:29:24	60
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     26400 Feb 27 10:27 RSWGD1-17_SSGM_Confirmed_File__20170227.csv.20170227102719221	10:27	2/27/2017		2017-27-02	10:27:19	0.435637	Mon	1	30	2017-27-2 10:27:19	60
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       512 Feb 27 09:43 tcwta20170227.csv.20170227094316112	9:43	2/27/2017		2017-27-02	9:43:16	0.405046	Mon	1	31	2017-27-2 9:43:16	60
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      8353 Feb 27 09:31 TIAACREFREPAT.csv.20170227093144930	9:31			2017-27-02	9:31:44	0.397037	Mon	1	32	2017-27-2 9:31:44	60
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       312 Feb 27 10:31 TIAACREFREPAT.csv.20170227103119783	10:31			2017-27-02	10:31:19	0.438414	Mon	1	32	2017-27-2 10:31:19	60
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       888 Feb 27 20:58 tokyofundtrades.in.201702280944.20170227205809760	 20:5	2/28/2017	9:44:00	2017-27-02	20:58:09	0.873715	Mon	1	33	2017-27-2 20:58:09	60
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       234 Feb 27 05:05 TrinityStreetFX_022717.csv.20170227050527463	5:05			2017-27-02	5:05:27	0.212118	Mon	1	34	2017-27-2 5:05:27	60
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       174 Feb 27 11:03 TrinityStreetFX_022817.csv.20170227110323493	11:03			2017-27-02	11:03:23	0.460683	Mon	1	34	2017-27-2 11:03:23	60
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       260 Feb 28 08:58 Alger_Orders_20170228085527.csv.20170228085826357	8:58	2/28/2017	8:55:27	2017-28-02	8:58:26	0.373912	Tue	2	1	2017-28-2 8:58:26	61
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Feb 28 11:53 Alger_Orders_20170228115150.csv.20170228115354124	11:53	2/28/2017	11:51:50	2017-28-02	11:53:54	0.495764	Tue	2	1	2017-28-2 11:53:54	61
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      3208 Feb 28 12:07 alps_Orders_02282017095000.csv.20170228120755986	12:07	2/28/2017	9:50:00	2017-28-02	12:07:55	0.505498	Tue	2	2	2017-28-2 12:07:55	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064145919	6:41			2017-28-02	6:41:45	0.278993	Tue	2	4	2017-28-2 6:41:45	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064146208	6:41			2017-28-02	6:41:46	0.279005	Tue	2	4	2017-28-2 6:41:46	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064146403	6:41			2017-28-02	6:41:46	0.279005	Tue	2	4	2017-28-2 6:41:46	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064146666	6:41			2017-28-02	6:41:46	0.279005	Tue	2	4	2017-28-2 6:41:46	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064146820	6:41			2017-28-02	6:41:46	0.279005	Tue	2	4	2017-28-2 6:41:46	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147005	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147207	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147396	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147592	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147813	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064147992	6:41			2017-28-02	6:41:47	0.279016	Tue	2	4	2017-28-2 6:41:47	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064148192	6:41			2017-28-02	6:41:48	0.279028	Tue	2	4	2017-28-2 6:41:48	61
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Feb 28 06:41 BCRTOFX.txt.20170228064148419	6:41			2017-28-02	6:41:48	0.279028	Tue	2	4	2017-28-2 6:41:48	61
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      9260 Feb 28 14:35 BRA_BRA_Ver_20170228.csv.20170228143537669	14:35	2/28/2017		2017-28-02	14:35:37	0.608067	Tue	2	5	2017-28-2 14:35:37	61
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       223 Feb 28 04:14 scbcnhtrades1.in.201702281707.20170228041438264	4:14	2/28/2017	17:07:00	2017-28-02	4:14:38	0.176829	Tue	2	7	2017-28-2 4:14:38	61
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 28 04:14 scbcnhtrades2.in.201702281707.20170228041438639	4:14	2/28/2017	17:07:00	2017-28-02	4:14:38	0.176829	Tue	2	7	2017-28-2 4:14:38	61
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       724 Feb 28 10:00 SPOT_FET_Instructions_StateStreet_20170228-155035.csv.20170228100032549	10:00	2/28/2017	15:50:35	2017-28-02	10:00:32	0.417037	Tue	2	7	2017-28-2 10:00:32	61
Crux Asset Management Limited	-rw-r--r--   1 ftpgmrin ftpgmr       363 Feb 28 12:29 CRUX_20170228.csv.20170228122958256	12:29	2/28/2017		2017-28-02	12:29:58	0.52081	Tue	2	8	2017-28-2 12:29:58	61
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       371 Feb 28 16:49 02282017_GAM_GAM_STAR_GS.20170228.csv.20170228164945897	16:49	2/28/2017		2017-28-02	16:49:45	0.701215	Tue	2	9	2017-28-2 16:49:45	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr       864 Feb 28 10:34 trade10.dat.20170228103435865	10:34			2017-28-02	10:34:35	0.440683	Tue	2	10	2017-28-2 10:34:35	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      1732 Feb 28 12:33 trade10.dat.20170228123358902	12:33			2017-28-02	12:33:58	0.523588	Tue	2	10	2017-28-2 12:33:58	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      7374 Feb 28 14:35 trade10.dat.20170228143537460	14:35			2017-28-02	14:35:37	0.608067	Tue	2	10	2017-28-2 14:35:37	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6072 Feb 28 16:23 trade10.dat.20170228162342978	16:23			2017-28-02	16:23:42	0.683125	Tue	2	10	2017-28-2 16:23:42	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 28 17:03 trade10.dat.20170228170347566	17:03			2017-28-02	17:03:47	0.710961	Tue	2	10	2017-28-2 17:03:47	61
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Feb 28 18:03 trade10.dat.20170228180353726	18:03			2017-28-02	18:03:53	0.752697	Tue	2	10	2017-28-2 18:03:53	61
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    374508 Feb 28 09:00 passporttrans.20170228.csv.20170228090026875	9:00	2/28/2017		2017-28-02	9:00:26	0.375301	Tue	2	15	2017-28-2 9:00:26	61
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2428 Feb 28 08:32 HighlandCapitalManagementRecon201702280730.csv.20170228083225340	8:32	2/28/2017	7:30:00	2017-28-02	8:32:25	0.355845	Tue	2	16	2017-28-2 8:32:25	61
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       854 Feb 28 02:02 HSBC-LKR.in.28022017-1.20170228020226728	 02:0	2/28/2017		2017-28-02	2:02:26	0.085023	Tue	2	17	2017-28-2 2:02:26	61
John Hancock Investments	HAN_TRANS_HANVER_20170228.csv.20170228153739656	15:37	2/28/2017		2017-28-02	15:37:39	0.651146	Tue	2	18	2017-28-2 15:37:39	61
John Hancock Investments	HAN_TRANS_HANVER_20170228.csv.20170228153739656	15:37	2/28/2017		2017-28-02	15:37:39	0.651146	Tue	2	18	2017-28-2 15:37:39	61
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 28 10:36 PAXStateStreetFX_Orders_022817.txt.20170228103636360	10:36	2/28/2017		2017-28-02	10:36:36	0.442083	Tue	2	23	2017-28-2 10:36:36	61
PAX	-rw-r--r--   1 ftpgmrin ftpgmr       342 Feb 28 16:15 PAXStateStreetFX_Orders_022817.txt.20170228161542302	16:15	2/28/2017		2017-28-02	16:15:42	0.677569	Tue	2	23	2017-28-2 16:15:42	61
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       203 Feb 28 12:55 PGI_Orders_20170228115334.csv.20170228125530200	12:55	2/28/2017	11:53:34	2017-28-02	12:55:30	0.538542	Tue	2	24	2017-28-2 12:55:30	61
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Feb 28 03:20 INV_fx_20170228_091744.csv.20170228032035669	3:20	2/28/2017	9:17:44	2017-28-02	3:20:35	0.139294	Tue	2	26	2017-28-2 3:20:35	61
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       368 Feb 28 03:20 FT_fx_20170228_091919.csv.20170228032036032	3:20	2/28/2017	9:19:19	2017-28-02	3:20:36	0.139306	Tue	2	26	2017-28-2 3:20:36	61
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Feb 28 05:10 FT_fx_20170228_110730.csv.20170228051013444	5:10	2/28/2017	11:07:30	2017-28-02	5:10:13	0.215428	Tue	2	26	2017-28-2 5:10:13	61
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Feb 28 04:36 citicnhtrades.in.201702281721.20170228043640887	4:36	2/28/2017	17:21:00	2017-28-02	4:36:40	0.19213	Tue	2	28	2017-28-2 4:36:40	61
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       488 Feb 28 04:36 hsbccnhtrades.in.201702281721.20170228043641194	4:36	2/28/2017	17:21:00	2017-28-02	4:36:41	0.192141	Tue	2	29	2017-28-2 4:36:41	61
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27600 Feb 28 10:44 RSWGD1-17_SSGM_Confirmed_File__20170228.csv.20170228104437238	10:44	2/28/2017		2017-28-02	10:44:37	0.44765	Tue	2	30	2017-28-2 10:44:37	61
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       512 Feb 28 09:44 tcwta20170228.csv.20170228094431625	9:44	2/28/2017		2017-28-02	9:44:31	0.405914	Tue	2	31	2017-28-2 9:44:31	61
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      9839 Feb 28 09:30 TIAACREFREPAT.csv.20170228093030097	9:30			2017-28-02	9:30:30	0.396181	Tue	2	32	2017-28-2 9:30:30	61
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       311 Feb 28 13:31 TIAACREFREPAT.csv.20170228133133241	13:31			2017-28-02	13:31:33	0.563576	Tue	2	32	2017-28-2 13:31:33	61
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      1242 Feb 28 21:12 tokyofundtrades.in.201703010946.20170228211208096	 21:1	3/1/2017	9:46:00	2017-28-02	21:12:08	0.883426	Tue	2	33	2017-28-2 21:12:08	61
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       625 Feb 28 22:12 tokyofundtrades.in.201703011053.20170228221210279	 22:1	3/1/2017	10:53:00	2017-28-02	22:12:10	0.925116	Tue	2	33	2017-28-2 22:12:10	61
Alger	-rw-r--r--   1 ftpgmrin ftpgmr       320 Mar  1 15:41 Alger_Orders_20170301153721.csv.20170301154109700	15:41	3/1/2017	15:37:21	2017-01-03	15:41:09	0.653576	Wed	3	1	2017-03-01 15:41	62
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1819 Mar  1 11:34 alps_Orders_03012017095000.csv.20170301113448519	11:34	1/3/2017	9:50:00	2017-01-03	11:34:48	0.4825	Wed	3	2	2017-03-01 11:34	62
Alps	-rw-r--r--   1 ftpgmrin ftpgmr      1080 Mar  1 16:57 alps_Orders_03012017097000.csv.20170301165717926	16:57	1/3/2017	10:10:00	2017-01-03	16:57:17	0.706447	Wed	3	2	2017-03-01 16:57	62
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1403 Mar  1 10:33 SSC_BAM_FXREQ_20170301_153025.csv.pgp.ndm05.20170301103304202	10:33	3/1/2017	15:30:25	2017-01-03	10:33:04	0.43963	Wed	3	3	2017-03-01 10:33	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064042705	6:40			2017-01-03	6:40:42	0.278264	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064043104	6:40			2017-01-03	6:40:43	0.278275	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064043309	6:40			2017-01-03	6:40:43	0.278275	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064043504	6:40			2017-01-03	6:40:43	0.278275	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064043686	6:40			2017-01-03	6:40:43	0.278275	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064043906	6:40			2017-01-03	6:40:43	0.278275	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064044088	6:40			2017-01-03	6:40:44	0.278287	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064044289	6:40			2017-01-03	6:40:44	0.278287	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064044484	6:40			2017-01-03	6:40:44	0.278287	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064044687	6:40			2017-01-03	6:40:44	0.278287	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064044909	6:40			2017-01-03	6:40:44	0.278287	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064045090	6:40			2017-01-03	6:40:45	0.278299	Wed	3	4	2017-03-01 06:40	62
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  1 06:40 BCRTOFX.txt.20170301064045295	6:40			2017-01-03	6:40:45	0.278299	Wed	3	4	2017-03-01 06:40	62
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7540 Mar  1 14:39 BRA_BRA_Ver_20170301.csv.20170301143906503	14:39	3/1/2017		2017-01-03	14:39:06	0.610486	Wed	3	5	2017-03-01 14:39	62
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Mar  1 16:35 CDPSfx_TWDorder.20170301.163500.csv.20170301163515263	16:35	3/1/2017	16:35:00	2017-01-03	16:35:15	0.691146	Wed	3	6	2017-03-01 16:35	62
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       167 Mar  1 04:16 scbcnhtrades1.in.201703011707.20170301041632809	4:16	3/1/2017	17:07:00	2017-01-03	4:16:32	0.178148	Wed	3	7	2017-03-01 04:16	62
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  1 04:18 scbcnhtrades2.in.201703011707.20170301041803087	4:18	3/1/2017	17:07:00	2017-01-03	4:18:03	0.179201	Wed	3	7	2017-03-01 04:18	62
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Mar  1 05:04 scbcnhtrades1.in.201703011757.20170301050407214	5:04	3/1/2017	17:57:00	2017-01-03	5:04:07	0.211192	Wed	3	7	2017-03-01 05:04	62
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  1 05:04 scbcnhtrades2.in.201703011757.20170301050407563	5:04	3/1/2017	17:57:00	2017-01-03	5:04:07	0.211192	Wed	3	7	2017-03-01 05:04	62
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       862 Mar  1 10:04 SPOT_FET_Instructions_StateStreet_20170301-155039.csv.20170301100431869	10:04	3/1/2017	15:50:39	2017-01-03	10:04:31	0.419803	Wed	3	7	2017-03-01 10:04	62
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       258 Mar  1 16:53 03012017_GAM_GAM_STAR_GS.20170301.csv.20170301165317244	16:53	3/1/2017		2017-01-03	16:53:17	0.703669	Wed	3	9	2017-03-01 16:53	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  1 10:34 trade10.dat.20170301103434865	10:34			2017-01-03	10:34:34	0.440671	Wed	3	10	2017-03-01 10:34	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      4336 Mar  1 12:34 trade10.dat.20170301123458459	12:34			2017-01-03	12:34:58	0.524282	Wed	3	10	2017-03-01 12:34	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     66398 Mar  1 14:35 trade10.dat.20170301143506002	14:35			2017-01-03	14:35:06	0.607708	Wed	3	10	2017-03-01 14:35	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr     19960 Mar  1 16:25 trade10.dat.20170301162513658	16:25			2017-01-03	16:25:13	0.684178	Wed	3	10	2017-03-01 16:25	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  1 17:05 trade10.dat.20170301170518818	17:05			2017-01-03	17:05:18	0.712014	Wed	3	10	2017-03-01 17:05	62
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  1 18:04 trade10.dat.20170301180454339	18:04			2017-01-03	18:04:54	0.753403	Wed	3	10	2017-03-01 18:04	62
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    403023 Mar  1 09:30 passporttrans.20170301.csv.20170301093028547	9:30	3/1/2017		2017-01-03	9:30:28	0.396157	Wed	3	15	2017-03-01 09:30	62
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      2639 Mar  1 08:32 HighlandCapitalManagementRecon201703010730.csv.20170301083223938	8:32	3/1/2017	7:30:00	2017-01-03	8:32:23	0.355822	Wed	3	16	2017-03-01 08:32	62
Highland	-rw-r--r--   1 ftpgmrin ftpgmr       184 Mar  1 10:40 Highland_Orders_20170301csv.20170301104035247	10:40	3/1/2017		2017-01-03	10:40:35	0.44485	Wed	3	16	2017-03-01 10:40	62
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       582 Mar  1 01:32 HSBC-LKR.in.01032017-1.20170301013222208	 01:3	1/3/2017		2017-01-03	1:32:22	0.064144	Wed	3	17	2017-03-01 01:32	62
John Hancock Investments	HAN_TRANS_HANVER_20170301.csv.20170301153909307	15:39	3/1/2017		2017-01-03	15:39:09	0.652188	Wed	3	18	2017-03-01 15:39	62
John Hancock Investments	HAN_TRANS_HANVER_20170301.csv.20170301153909307	15:39	3/1/2017		2017-01-03	15:39:09	0.652188	Wed	3	18	2017-03-01 15:39	62
Northern Trust Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2149 Mar  1 04:12 SNBEM-FX-TradeDate01.03.2017.csv.20170301041232144	4:12	3/1/2017		2017-01-03	4:12:32	0.17537	Wed	3	22	2017-03-01 04:12	62
Presima - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       209 Mar  1 10:04 PresimaOrders.csv.20170301100431283	10:04			2017-01-03	10:04:31	0.419803	Wed	3	25	2017-03-01 10:04	62
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       373 Mar  1 02:52 FT_fx_20170301_084938.csv.20170301025226711	2:52	3/1/2017	8:49:38	2017-01-03	2:52:26	0.119745	Wed	3	26	2017-03-01 02:52	62
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Mar  1 04:14 INV_fx_20170301_101100.csv.20170301041432466	4:14	3/1/2017	10:11:00	2017-01-03	4:14:32	0.176759	Wed	3	26	2017-03-01 04:14	62
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       301 Mar  1 04:50 FT_fx_20170301_104823.csv.20170301045006130	4:50	3/1/2017	10:48:23	2017-01-03	4:50:06	0.201458	Wed	3	26	2017-03-01 04:50	62
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Mar  1 04:52 INV_fx_20170301_104945.csv.20170301045206564	4:52	3/1/2017	10:49:45	2017-01-03	4:52:06	0.202847	Wed	3	26	2017-03-01 04:52	62
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  1 04:20 citicnhtrades.in.201703011712.20170301042003459	4:20	3/1/2017	17:12:00	2017-01-03	4:20:03	0.18059	Wed	3	28	2017-03-01 04:20	62
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       490 Mar  1 04:20 hsbccnhtrades.in.201703011712.20170301042003755	4:20	3/1/2017	17:12:00	2017-01-03	4:20:03	0.18059	Wed	3	29	2017-03-01 04:20	62
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     29483 Mar  1 12:18 RSWGD1-17_SSGM_Confirmed_File__20170301.csv.20170301121854256	12:18	3/1/2017		2017-01-03	12:18:54	0.513125	Wed	3	30	2017-03-01 12:18	62
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       511 Mar  1 09:32 tcwta20170301.csv.20170301093229598	9:32	3/1/2017		2017-01-03	9:32:29	0.397558	Wed	3	31	2017-03-01 09:32	62
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr     18997 Mar  1 09:30 TIAACREFREPAT.csv.20170301093028894	9:30			2017-01-03	9:30:28	0.396157	Wed	3	32	2017-03-01 09:30	62
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      2403 Mar  1 21:15 tokyofundtrades.in.201703020946.20170301211508519	 21:1	3/2/2017	9:46:00	2017-01-03	21:15:08	0.885509	Wed	3	33	2017-03-01 21:15	62
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       234 Mar  1 04:08 TrinityStreetFX_030117.csv.20170301040831543	4:08			2017-01-03	4:08:31	0.172581	Wed	3	34	2017-03-01 04:08	62
Alger	-rw-r--r--   1 ftpgmrin ftpgmr        64 Mar  2 09:04 Alger_Orders_20170302090004.csv.20170302090359998	9:04	3/2/2017	9:00:04	2017-02-03	9:03:59	0.377766	Thu	4	1	2017-03-02 09:03	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      4651 Mar  2 04:31 SSC_BAM_FXREQ_20170302_093018.csv.pgp.ndm05.20170302043110388	4:31	3/2/2017	9:30:18	2017-02-03	4:31:10	0.18831	Thu	4	3	2017-03-02 04:31	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1649 Mar  2 06:31 SSC_BAM_FXREQ_20170302_113039.csv.pgp.ndm05.20170302063145562	6:31	3/2/2017	11:30:39	2017-02-03	6:31:45	0.272049	Thu	4	3	2017-03-02 06:31	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2182 Mar  2 07:31 SSC_BAM_FXREQ_20170302_123050.csv.pgp.ndm05.20170302073155412	7:31	3/2/2017	12:30:50	2017-02-03	7:31:55	0.313831	Thu	4	3	2017-03-02 07:31	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1621 Mar  2 08:31 SSC_BAM_FXREQ_20170302_133058.csv.pgp.ndm05.20170302083158475	8:31	3/2/2017	13:30:58	2017-02-03	8:31:58	0.355532	Thu	4	3	2017-03-02 08:31	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2603 Mar  2 09:34 SSC_BAM_FXREQ_20170302_143107.csv.pgp.ndm05.20170302093405111	9:34	3/2/2017	14:31:07	2017-02-03	9:34:05	0.398669	Thu	4	3	2017-03-02 09:34	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1435 Mar  2 10:34 SSC_BAM_FXREQ_20170302_153119.csv.pgp.ndm05.20170302103411002	10:34	3/2/2017	15:31:19	2017-02-03	10:34:11	0.440405	Thu	4	3	2017-03-02 10:34	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1488 Mar  2 11:34 SSC_BAM_FXREQ_20170302_163125.csv.pgp.ndm05.20170302113415360	11:34	3/2/2017	16:31:25	2017-02-03	11:34:15	0.482118	Thu	4	3	2017-03-02 11:34	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      2121 Mar  2 12:34 SSC_BAM_FXREQ_20170302_173127.csv.pgp.ndm05.20170302123428896	12:34	3/2/2017	17:31:27	2017-02-03	12:34:28	0.523935	Thu	4	3	2017-03-02 12:34	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1400 Mar  2 13:34 SSC_BAM_FXREQ_20170302_183132.csv.pgp.ndm05.20170302133432704	13:34	3/2/2017	18:31:32	2017-02-03	13:34:32	0.565648	Thu	4	3	2017-03-02 13:34	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064016208	6:40			2017-02-03	6:40:16	0.277963	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064016540	6:40			2017-02-03	6:40:16	0.277963	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064016729	6:40			2017-02-03	6:40:16	0.277963	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064016944	6:40			2017-02-03	6:40:16	0.277963	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064017125	6:40			2017-02-03	6:40:17	0.277975	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064017339	6:40			2017-02-03	6:40:17	0.277975	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064017545	6:40			2017-02-03	6:40:17	0.277975	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064017725	6:40			2017-02-03	6:40:17	0.277975	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064017923	6:40			2017-02-03	6:40:17	0.277975	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064018766	6:40			2017-02-03	6:40:18	0.277986	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064018141	6:40			2017-02-03	6:40:18	0.277986	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064018346	6:40			2017-02-03	6:40:18	0.277986	Thu	4	4	2017-03-02 06:40	63
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  2 06:40 BCRTOFX.txt.20170302064018545	6:40			2017-02-03	6:40:18	0.277986	Thu	4	4	2017-03-02 06:40	63
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      7586 Mar  2 14:40 BRA_BRA_Ver_20170302.csv.20170302144008231	14:40	3/2/2017		2017-02-03	14:40:08	0.611204	Thu	4	5	2017-03-02 14:40	63
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       222 Mar  2 04:07 scbcnhtrades1.in.201703021659.20170302040737656	4:07	3/2/2017	16:59:00	2017-02-03	4:07:37	0.171956	Thu	4	7	2017-03-02 04:07	63
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  2 04:07 scbcnhtrades2.in.201703021659.20170302040737868	4:07	3/2/2017	16:59:00	2017-02-03	4:07:37	0.171956	Thu	4	7	2017-03-02 04:07	63
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1006 Mar  2 10:24 SPOT_FET_Instructions_StateStreet_20170302-152708.csv.20170302102409986	10:24	3/2/2017	15:27:08	2017-02-03	10:24:09	0.433438	Thu	4	7	2017-03-02 10:24	63
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       109 Mar  2 16:54 03022017_GAM_GAM_STAR_GS.20170302.csv.20170302165418375	16:54	3/2/2017		2017-02-03	16:54:18	0.704375	Thu	4	9	2017-03-02 16:54	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr    161444 Mar  2 10:34 trade10.dat.20170302103410648	10:34			2017-02-03	10:34:10	0.440394	Thu	4	10	2017-03-02 10:34	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2600 Mar  2 12:33 trade10.dat.20170302123358420	12:33			2017-02-03	12:33:58	0.523588	Thu	4	10	2017-03-02 12:33	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6506 Mar  2 14:36 trade10.dat.20170302143607794	14:36			2017-02-03	14:36:07	0.608414	Thu	4	10	2017-03-02 14:36	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      8676 Mar  2 16:24 trade10.dat.20170302162415172	16:24			2017-02-03	16:24:15	0.683507	Thu	4	10	2017-03-02 16:24	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  2 17:04 trade10.dat.20170302170419524	17:04			2017-02-03	17:04:19	0.711331	Thu	4	10	2017-03-02 17:04	63
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  2 18:04 trade10.dat.20170302180425044	18:04			2017-02-03	18:04:25	0.753067	Thu	4	10	2017-03-02 18:04	63
FCM UK	-rw-r--r--   1 ftpgmrin ftpgmr       980 Mar  2 06:47 UKFCMCurrencyTemplate020317.csv.20170302064749283	6:47			2017-02-03	6:47:49	0.283206	Thu	4	11	2017-03-02 06:47	63
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    361585 Mar  2 09:20 passporttrans.20170302.csv.20170302092002575	9:20	3/2/2017		2017-02-03	9:20:02	0.388912	Thu	4	15	2017-03-02 09:20	63
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1659 Mar  2 08:31 HighlandCapitalManagementRecon201703020730.csv.20170302083128187	8:31	3/2/2017	7:30:00	2017-02-03	8:31:28	0.355185	Thu	4	16	2017-03-02 08:31	63
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       490 Mar  2 01:27 HSBC-LKR.in.02032017-1.20170302012722803	 01:2	2/3/2017		2017-02-03	1:27:22	0.060671	Thu	4	17	2017-03-02 01:27	63
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr      1035 Mar  2 02:47 HSBC-LKR.in.02032017-2.20170302024731814	 02:4	2/3/2017		2017-02-03	2:47:31	0.116331	Thu	4	17	2017-03-02 02:47	63
John Hancock Investments	HAN_TRANS_HANVER_20170302.csv.20170302153810902	15:38	3/2/2017		2017-02-03	15:38:10	0.651505	Thu	4	18	2017-03-02 15:38	63
John Hancock Investments	HAN_TRANS_HANVER_20170302.csv.20170302153810902	15:38	3/2/2017		2017-02-03	15:38:10	0.651505	Thu	4	18	2017-03-02 15:38	63
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       304 Mar  2 02:45 FT_fx_20170302_084246.csv.20170302024531385	2:45	3/2/2017	8:42:46	2017-02-03	2:45:31	0.114942	Thu	4	26	2017-03-02 02:45	63
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Mar  2 03:39 INV_fx_20170302_093802.csv.20170302033935425	3:39	3/2/2017	9:38:02	2017-02-03	3:39:35	0.152488	Thu	4	26	2017-03-02 03:39	63
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       234 Mar  2 04:11 FT_fx_20170302_100953.csv.20170302041138187	4:11	3/2/2017	10:09:53	2017-02-03	4:11:38	0.174745	Thu	4	26	2017-03-02 04:11	63
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       232 Mar  2 04:43 INV_fx_20170302_104044.csv.20170302044341241	4:43	3/2/2017	10:40:44	2017-02-03	4:43:41	0.197002	Thu	4	26	2017-03-02 04:43	63
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Mar  2 04:59 FT_fx_20170302_105812.csv.20170302045941938	4:59	3/2/2017	10:58:12	2017-02-03	4:59:41	0.208113	Thu	4	26	2017-03-02 04:59	63
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       233 Mar  2 03:17 citicnhtrades.in.201703021609.20170302031733371	3:17	3/2/2017	16:09:00	2017-02-03	3:17:33	0.137188	Thu	4	28	2017-03-02 03:17	63
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  2 04:23 citicnhtrades.in.201703021714.20170302042339510	4:23	3/2/2017	17:14:00	2017-02-03	4:23:39	0.18309	Thu	4	28	2017-03-02 04:23	63
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       305 Mar  2 04:23 hsbccnhtrades.in.201703021714.20170302042339787	4:23	3/2/2017	17:14:00	2017-02-03	4:23:39	0.18309	Thu	4	29	2017-03-02 04:23	63
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     31763 Mar  2 10:16 RSWGD1-17_SSGM_Confirmed_File__20170302.csv.20170302101608877	10:16	3/2/2017		2017-02-03	10:16:08	0.42787	Thu	4	30	2017-03-02 10:16	63
TCW	-rw-r--r--   1 ftpgmrin ftpgmr       519 Mar  2 09:26 tcwta20170302.csv.20170302092603628	9:26	3/2/2017		2017-02-03	9:26:03	0.39309	Thu	4	31	2017-03-02 09:26	63
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      5481 Mar  2 09:32 TIAACREFREPAT.csv.20170302093204160	9:32			2017-02-03	9:32:04	0.397269	Thu	4	32	2017-03-02 09:32	63
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       328 Mar  2 13:32 TIAACREFREPAT.csv.20170302133201964	13:32			2017-02-03	13:32:01	0.5639	Thu	4	32	2017-03-02 13:32	63
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr       427 Mar  2 15:32 TIAACREFREPAT.csv.20170302153210240	15:32			2017-02-03	15:32:10	0.647338	Thu	4	32	2017-03-02 15:32	63
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr       883 Mar  2 21:22 tokyofundtrades.in.201703030957.20170302212243260	 21:2	3/3/2017	9:57:00	2017-02-03	21:22:43	0.890775	Thu	4	33	2017-03-02 21:22	63
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       236 Mar  2 04:03 TrinityStreetFX_030217.csv.20170302040336682	4:03			2017-02-03	4:03:36	0.169167	Thu	4	34	2017-03-02 04:03	63
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1530 Mar  3 04:32 SSC_BAM_FXREQ_20170303_093019.csv.pgp.ndm05.20170303043219029	4:32	3/3/2017	9:30:19	2017-03-03	4:32:19	0.189109	Fri	5	3	2017-03-03 04:32	64
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1419 Mar  3 10:33 SSC_BAM_FXREQ_20170303_153036.csv.pgp.ndm05.20170303103318661	10:33	3/3/2017	15:30:36	2017-03-03	10:33:18	0.439792	Fri	5	3	2017-03-03 10:33	64
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1422 Mar  3 12:33 SSC_BAM_FXREQ_20170303_173041.csv.pgp.ndm05.20170303123310673	12:33	3/3/2017	17:30:41	2017-03-03	12:33:10	0.523032	Fri	5	3	2017-03-03 12:33	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064055477	6:40			2017-03-03	6:40:55	0.278414	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064055853	6:40			2017-03-03	6:40:55	0.278414	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064056043	6:40			2017-03-03	6:40:56	0.278426	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064056252	6:40			2017-03-03	6:40:56	0.278426	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064056438	6:40			2017-03-03	6:40:56	0.278426	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064056645	6:40			2017-03-03	6:40:56	0.278426	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064056853	6:40			2017-03-03	6:40:56	0.278426	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064057047	6:40			2017-03-03	6:40:57	0.278438	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064057242	6:40			2017-03-03	6:40:57	0.278438	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064057453	6:40			2017-03-03	6:40:57	0.278438	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064057646	6:40			2017-03-03	6:40:57	0.278438	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064057847	6:40			2017-03-03	6:40:57	0.278438	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064058046	6:40			2017-03-03	6:40:58	0.278449	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064058251	6:40			2017-03-03	6:40:58	0.278449	Fri	5	4	2017-03-03 06:40	64
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  3 06:40 BCRTOFX.txt.20170303064058448	6:40			2017-03-03	6:40:58	0.278449	Fri	5	4	2017-03-03 06:40	64
Brandes Investment Partners	-rw-r--r--   1 ftpgmrin ftpgmr      5799 Mar  3 14:35 BRA_BRA_Ver_20170303.csv.20170303143549871	14:35	3/3/2017		2017-03-03	14:35:49	0.608206	Fri	5	5	2017-03-03 14:35	64
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       355 Mar  3 14:33 CDPSfx_BRLorder.20170303.143500.csv.20170303143349072	14:33	3/3/2017	14:35:00	2017-03-03	14:33:49	0.606817	Fri	5	6	2017-03-03 14:33	64
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       360 Mar  3 16:33 CDPSfx_IDRorder.20170303.163500.csv.20170303163357016	16:33	3/3/2017	16:35:00	2017-03-03	16:33:57	0.690243	Fri	5	6	2017-03-03 16:33	64
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       357 Mar  3 16:35 CDPSfx_THBorder.20170303.163500.csv.20170303163557404	16:35	3/3/2017	16:35:00	2017-03-03	16:35:57	0.691632	Fri	5	6	2017-03-03 16:35	64
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       358 Mar  3 16:35 CDPSfx_TWDorder.20170303.163500.csv.20170303163557687	16:35	3/3/2017	16:35:00	2017-03-03	16:35:57	0.691632	Fri	5	6	2017-03-03 16:35	64
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       112 Mar  3 04:02 scbcnhtrades1.in.201703031657.20170303040245955	4:02	3/3/2017	16:57:00	2017-03-03	4:02:45	0.168576	Fri	5	7	2017-03-03 04:02	64
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  3 04:02 scbcnhtrades2.in.201703031657.20170303040246305	4:02	3/3/2017	16:57:00	2017-03-03	4:02:46	0.168588	Fri	5	7	2017-03-03 04:02	64
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       110 Mar  3 05:22 scbcnhtrades1.in.201703031809.20170303052251949	5:22	3/3/2017	18:09:00	2017-03-03	5:22:51	0.224201	Fri	5	7	2017-03-03 05:22	64
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  3 05:22 scbcnhtrades2.in.201703031809.20170303052252313	5:22	3/3/2017	18:09:00	2017-03-03	5:22:52	0.224213	Fri	5	7	2017-03-03 05:22	64
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1158 Mar  3 09:21 SPOT_FET_Instructions_StateStreet_20170303-150601.csv.20170303092110018	9:21	3/3/2017	15:06:01	2017-03-03	9:21:10	0.389699	Fri	5	7	2017-03-03 09:21	64
Dalton Investments LLC	-rw-r--r--   1 ftpgmrin ftpgmr       242 Mar  3 16:21 03032017_GAM_GAM_STAR_GS.20170303.csv.20170303162155114	16:21	3/3/2017		2017-03-03	16:21:55	0.681887	Fri	5	9	2017-03-03 16:21	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      6506 Mar  3 10:35 trade10.dat.20170303103519186	10:35			2017-03-03	10:35:19	0.441192	Fri	5	10	2017-03-03 10:35	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Mar  3 12:33 trade10.dat.20170303123341166	12:33			2017-03-03	12:33:41	0.523391	Fri	5	10	2017-03-03 12:33	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Mar  3 14:35 trade10.dat.20170303143549381	14:35			2017-03-03	14:35:49	0.608206	Fri	5	10	2017-03-03 14:35	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      5204 Mar  3 16:23 trade10.dat.20170303162355568	16:23			2017-03-03	16:23:55	0.683275	Fri	5	10	2017-03-03 16:23	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  3 17:04 trade10.dat.20170303170402403	17:04			2017-03-03	17:04:02	0.711134	Fri	5	10	2017-03-03 17:04	64
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr         0 Mar  3 18:03 trade10.dat.20170303180343752	18:03			2017-03-03	18:03:43	0.752581	Fri	5	10	2017-03-03 18:03	64
FSS - FSS	-rw-r--r--   1 ftpgmrin ftpgmr       361 Mar  3 00:08 FSS_Orders_20170303.csv.20170303000852425	0:08	3/3/2017		2017-03-03	0:08:52	0.006157	Fri	5	13	2017-03-03 00:08	64
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    361355 Mar  3 09:29 passporttrans.20170303.csv.20170303092911097	9:29	3/3/2017		2017-03-03	9:29:11	0.395266	Fri	5	15	2017-03-03 09:29	64
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1428 Mar  3 08:31 HighlandCapitalManagementRecon201703030730.csv.20170303083107568	8:31	3/3/2017	7:30:00	2017-03-03	8:31:07	0.354942	Fri	5	16	2017-03-03 08:31	64
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       489 Mar  3 01:06 HSBC-LKR.in.03032017-2.20170303010656850	 01:0	3/3/2017		2017-03-03	1:06:56	0.046481	Fri	5	17	2017-03-03 01:06	64
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       847 Mar  3 02:03 HSBC-LKR.in.03032017-1.20170303020301833	 02:0	3/3/2017		2017-03-03	2:03:01	0.085428	Fri	5	17	2017-03-03 02:03	64
John Hancock Investments	HAN_TRANS_HANVER_20170303.csv.20170303153552189	15:35	3/3/2017		2017-03-03	15:35:52	0.649907	Fri	5	18	2017-03-03 15:35	64
John Hancock Investments	HAN_TRANS_HANVER_20170303.csv.20170303153552189	15:35	3/3/2017		2017-03-03	15:35:52	0.649907	Fri	5	18	2017-03-03 15:35	64
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       236 Mar  3 10:55 NOS_SFX_20170303.csv.20170303105520752	10:55	3/3/2017		2017-03-03	10:55:20	0.455093	Fri	5	21	2017-03-03 10:55	64
PGI	-rw-r--r--   1 ftpgmrin ftpgmr       909 Mar  3 16:09 PGI_Orders_20170303150654.csv.20170303160954132	16:09	3/3/2017	15:06:54	2017-03-03	16:09:54	0.673542	Fri	5	24	2017-03-03 16:09	64
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Mar  3 02:56 FT_fx_20170303_085410.csv.20170303025640537	2:56	3/3/2017	8:54:10	2017-03-03	2:56:40	0.122685	Fri	5	26	2017-03-03 02:56	64
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       231 Mar  3 03:56 INV_fx_20170303_095407.csv.20170303035645267	3:56	3/3/2017	9:54:07	2017-03-03	3:56:45	0.16441	Fri	5	26	2017-03-03 03:56	64
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       236 Mar  3 04:12 FT_fx_20170303_101001.csv.20170303041247079	4:12	3/3/2017	10:10:01	2017-03-03	4:12:47	0.175544	Fri	5	26	2017-03-03 04:12	64
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       229 Mar  3 05:06 FT_fx_20170303_110430.csv.20170303050651251	5:06	3/3/2017	11:04:30	2017-03-03	5:06:51	0.21309	Fri	5	26	2017-03-03 05:06	64
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       235 Mar  3 06:08 INV_fx_20170303_120610.csv.20170303060854134	6:08	3/3/2017	12:06:10	2017-03-03	6:08:54	0.256181	Fri	5	26	2017-03-03 06:08	64
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       293 Mar  3 03:12 citicnhtrades.in.201703031607.20170303031242132	3:12	3/3/2017	16:07:00	2017-03-03	3:12:42	0.133819	Fri	5	28	2017-03-03 03:12	64
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  3 04:24 citicnhtrades.in.201703031715.20170303042448430	4:24	3/3/2017	17:15:00	2017-03-03	4:24:48	0.183889	Fri	5	28	2017-03-03 04:24	64
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr      1302 Mar  3 04:24 hsbccnhtrades.in.201703031715.20170303042448627	4:24	3/3/2017	17:15:00	2017-03-03	4:24:48	0.183889	Fri	5	29	2017-03-03 04:24	64
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     28204 Mar  3 10:49 RSWGD1-17_SSGM_Confirmed_File__20170303.csv.20170303104920300	10:49	3/3/2017		2017-03-03	10:49:20	0.450926	Fri	5	30	2017-03-03 10:49	64
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      6044 Mar  3 09:31 TIAACREFREPAT.csv.20170303093111559	9:31			2017-03-03	9:31:11	0.396655	Fri	5	32	2017-03-03 09:31	64
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      3723 Mar  3 10:31 TIAACREFREPAT.csv.20170303103118346	10:31			2017-03-03	10:31:18	0.438403	Fri	5	32	2017-03-03 10:31	64
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       234 Mar  3 08:31 TrinityStreetFX_030317.csv.20170303083107292	8:31			2017-03-03	8:31:07	0.354942	Fri	5	34	2017-03-03 08:31	64
Tokyo Funds	 -rw-r--r--   1 ftpgmrin ftpgmr      1377 Mar  5 21:31 tokyofundtrades.in.201703061003.20170305213123904	 21:3	3/6/2017	10:03:00	2017-05-03	21:31:23	0.896794	Sun	7	33	2017-03-05 21:31	#N/A
Baring Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr      1402 Mar  6 05:33 SSC_BAM_FXREQ_20170306_103019.csv.pgp.ndm05.20170306053320873	5:33	3/6/2017	10:30:19	2017-06-03	5:33:20	0.231481	Mon	1	3	2017-03-06 05:33	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063924064	6:39			2017-06-03	6:39:24	0.277361	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063924341	6:39			2017-06-03	6:39:24	0.277361	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063924563	6:39			2017-06-03	6:39:24	0.277361	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063924751	6:39			2017-06-03	6:39:24	0.277361	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063924946	6:39			2017-06-03	6:39:24	0.277361	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063925151	6:39			2017-06-03	6:39:25	0.277373	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063925359	6:39			2017-06-03	6:39:25	0.277373	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063925555	6:39			2017-06-03	6:39:25	0.277373	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063925759	6:39			2017-06-03	6:39:25	0.277373	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063925962	6:39			2017-06-03	6:39:25	0.277373	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063926147	6:39			2017-06-03	6:39:26	0.277384	Mon	1	4	2017-03-06 06:39	65
BCR (Banca Corrispondente)	-rw-r--r--   1 ftpgmrin ftpgmr      1500 Mar  6 06:39 BCRTOFX.txt.20170306063926365	6:39			2017-06-03	6:39:26	0.277384	Mon	1	4	2017-03-06 06:39	65
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Mar  6 07:34 CDPSfx_BRLorder.20170306.073500.csv.20170306073359923	7:34	3/6/2017	7:35:00	2017-06-03	7:33:59	0.315266	Mon	1	6	2017-03-06 07:33	65
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Mar  6 08:34 CDPSfx_BRLorder.20170306.083500.csv.20170306083401987	8:34	3/6/2017	8:35:00	2017-06-03	8:34:01	0.356956	Mon	1	6	2017-03-06 08:34	65
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Mar  6 09:33 CDPSfx_BRLorder.20170306.093500.csv.20170306093336047	9:33	3/6/2017	9:35:00	2017-06-03	9:33:36	0.398333	Mon	1	6	2017-03-06 09:33	65
CDP Capital 	-rw-r--r--   1 ftpgmrin ftpgmr       356 Mar  6 10:33 CDPSfx_BRLorder.20170306.103500.csv.20170306103339734	10:33	3/6/2017	10:35:00	2017-06-03	10:33:39	0.440035	Mon	1	6	2017-03-06 10:33	65
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr       441 Mar  6 04:19 scbcnhtrades1.in.201703061712.20170306041946348	4:19	3/6/2017	17:12:00	2017-06-03	4:19:46	0.180394	Mon	1	7	2017-03-06 04:19	65
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        57 Mar  6 04:19 scbcnhtrades2.in.201703061712.20170306041946555	4:19	3/6/2017	17:12:00	2017-06-03	4:19:46	0.180394	Mon	1	7	2017-03-06 04:19	65
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr        56 Mar  6 05:05 scbcnhtrades1.in.201703061757.20170306050548734	5:05	3/6/2017	17:57:00	2017-06-03	5:05:48	0.212361	Mon	1	7	2017-03-06 05:05	65
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  6 05:05 scbcnhtrades2.in.201703061757.20170306050549053	5:05	3/6/2017	17:57:00	2017-06-03	5:05:49	0.212373	Mon	1	7	2017-03-06 05:05	65
Client Name Not Available	-rw-r--r--   1 ftpgmrin ftpgmr      1292 Mar  6 09:55 SPOT_FET_Instructions_StateStreet_20170306-152724.csv.20170306095536711	9:55	3/6/2017	15:27:24	2017-06-03	9:55:36	0.413611	Mon	1	7	2017-03-06 09:55	65
DuPont Capital Management	-rw-r--r--   1 ftpgmrin ftpgmr      2166 Mar  6 10:33 trade10.dat.20170306103339984	10:33			2017-06-03	10:33:39	0.440035	Mon	1	10	2017-03-06 10:33	65
Goldman Sachs Asset Management (GSAM)	-rw-r--r--   1 ftpgmrin ftpgmr    372048 Mar  6 08:54 passporttrans.20170306.csv.20170306085402715	8:54	3/6/2017		2017-06-03	8:54:02	0.370856	Mon	1	15	2017-03-06 08:54	65
Highland	-rw-r--r--   1 ftpgmrin ftpgmr      1663 Mar  6 08:32 HighlandCapitalManagementRecon201703060730.csv.20170306083201525	8:32	3/6/2017	7:30:00	2017-06-03	8:32:01	0.355567	Mon	1	16	2017-03-06 08:32	65
HSBC LKR	 -rw-r--r--   1 ftpgmrin ftpgmr       576 Mar  6 01:35 HSBC-LKR.in.06032017-1.20170306013534870	 01:3	6/3/2017		2017-06-03	1:35:34	0.066366	Mon	1	17	2017-03-06 01:35	65
North of South Capital	-rw-r--r--   1 ftpgmrin ftpgmr       180 Mar  6 07:09 NOS_SFX_20170306.csv.20170306070958351	7:09	3/6/2017		2017-06-03	7:09:58	0.298588	Mon	1	21	2017-03-06 07:09	65
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Mar  6 02:53 FT_fx_20170306_085156.csv.20170306025341312	2:53	3/6/2017	8:51:56	2017-06-03	2:53:41	0.120613	Mon	1	26	2017-03-06 02:53	65
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       299 Mar  6 04:01 INV_fx_20170306_095911.csv.20170306040145581	4:01	3/6/2017	9:59:11	2017-06-03	4:01:45	0.167882	Mon	1	26	2017-03-06 04:01	65
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       302 Mar  6 05:01 FT_fx_20170306_105929.csv.20170306050148178	5:01	3/6/2017	10:59:29	2017-06-03	5:01:48	0.209583	Mon	1	26	2017-03-06 05:01	65
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       229 Mar  6 05:15 INV_fx_20170306_111306.csv.20170306051550137	5:15	3/6/2017	11:13:06	2017-06-03	5:15:50	0.219329	Mon	1	26	2017-03-06 05:15	65
Previnet S.p.A	-rw-r--r--   1 ftpgmrin ftpgmr       233 Mar  6 05:49 INV_fx_20170306_114817.csv.20170306054951999	5:49	3/6/2017	11:48:17	2017-06-03	5:49:51	0.242951	Mon	1	26	2017-03-06 05:49	65
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr       176 Mar  6 03:13 citicnhtrades.in.201703061608.20170306031342398	3:13	3/6/2017	16:08:00	2017-06-03	3:13:42	0.134514	Mon	1	28	2017-03-06 03:13	65
Stock Connect - Citibank	-rw-r--r--   1 ftpgmrin ftpgmr         2 Mar  6 04:23 citicnhtrades.in.201703061716.20170306042346913	4:23	3/6/2017	17:16:00	2017-06-03	4:23:46	0.183171	Mon	1	28	2017-03-06 04:23	65
Stock Connect - HSBC	-rw-r--r--   1 ftpgmrin ftpgmr       805 Mar  6 04:23 hsbccnhtrades.in.201703061716.20170306042347100	4:23	3/6/2017	17:16:00	2017-06-03	4:23:47	0.183183	Mon	1	29	2017-03-06 04:23	65
Swiss and Global	-rw-r--r--   1 ftpgmrin ftpgmr     27251 Mar  6 10:21 RSWGD1-17_SSGM_Confirmed_File__20170306.csv.20170306102138140	10:21	3/6/2017		2017-06-03	10:21:38	0.43169	Mon	1	30	2017-03-06 10:21	65
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2864 Mar  6 09:31 TIAACREFREPAT.csv.20170306093135621	9:31			2017-06-03	9:31:35	0.396933	Mon	1	32	2017-03-06 09:31	65
TIAA-Cref - Repatriation	-rw-r--r--   1 ftpgmrin ftpgmr      2477 Mar  6 10:31 TIAACREFREPAT.csv.20170306103139204	10:31			2017-06-03	10:31:39	0.438646	Mon	1	32	2017-03-06 10:31	65
Trinity Street Asset Management	-rw-r--r--   1 ftpgmrin ftpgmr       236 Mar  6 06:31 TrinityStreetFX_030617.csv.20170306063153551	6:31			2017-06-03	6:31:53	0.272141	Mon	1	34	2017-03-06 06:31	65
NACC3	capitalOrders		8/21/2016	21:20:01	2016-22-08	0:21:02	0.014606	Monday	1	19	2016-22-8 0:21:02	16
NACC3	capitalOrders		8/28/2016	21:20:02	2016-29-08	0:22:45	0.015799	Monday	1	19	2016-29-8 0:22:45	21
NACC3	capitalOrders		8/22/2016	21:20:03	2016-23-08	0:21:28	0.014907	Tuesday	2	19	2016-23-8 0:21:28	17
NACC3	capitalOrders		9/1/2016	21:20:03	2016-02-09	0:22:48	0.015833	Friday	5	19	2016-09-02 00:22	25
NACC3	capitalOrders		9/2/2016	21:20:03	2016-03-09	0:21:10	0.014699	Saturday	6	19	2016-09-03 00:21	#N/A
NACC3	capitalOrders		9/4/2016	21:20:03	2016-05-09	0:22:06	0.015347	Monday	1	19	2016-09-05 00:22	26
NACC3	capitalOrders		9/8/2016	21:20:04	2016-09-09	0:24:04	0.016713	Friday	5	19	2016-09-09 00:24	30
NACC3	capitalOrders		9/12/2016	21:20:04	2016-13-09	0:22:08	0.01537	Tuesday	2	19	2016-13-9 0:22:08	32
NACC3	capitalOrders		8/10/2016	21:20:05	2016-11-08	0:21:44	0.015093	Thursday	4	19	2016-08-11 00:21	9
NACC3	capitalOrders		8/24/2016	21:20:05	2016-25-08	0:22:41	0.015752	Thursday	4	19	2016-25-8 0:22:41	19
NACC3	capitalOrders		9/14/2016	21:20:05	2016-15-09	0:21:32	0.014954	Thursday	4	19	2016-15-9 0:21:32	34
NACC3	capitalOrders		8/7/2016	21:20:06	2016-08-08	0:21:30	0.014931	Monday	1	19	2016-08-08 00:21	6
NACC3	capitalOrders		8/15/2016	21:20:06	2016-16-08	0:23:22	0.016227	Tuesday	2	19	2016-16-8 0:23:22	12
NACC3	capitalOrders		8/23/2016	21:20:06	2016-24-08	0:22:24	0.015556	Wednesday	3	19	2016-24-8 0:22:24	18
NACC3	capitalOrders		8/29/2016	21:20:06	2016-30-08	0:21:01	0.014595	Tuesday	2	19	2016-30-8 0:21:01	22
NACC3	capitalOrders		9/15/2016	21:20:06	2016-16-09	0:22:01	0.015289	Friday	5	19	2016-16-9 0:22:01	35
NACC3	capitalOrders		9/22/2016	21:20:06	2016-23-09	0:22:09	0.015382	Friday	5	19	2016-23-9 0:22:09	40
NACC3	capitalOrders		9/25/2016	21:20:06	2016-26-09	0:21:20	0.014815	Monday	1	19	2016-26-9 0:21:20	41
NACC3	capitalOrders		8/1/2016	21:20:07	2016-02-08	0:22:24	0.015556	Tuesday	2	19	2016-08-02 00:22	2
NACC3	capitalOrders		8/8/2016	21:20:07	2016-09-08	0:22:16	0.015463	Tuesday	2	19	2016-08-09 00:22	7
NACC3	capitalOrders		8/31/2016	21:20:07	2016-01-09	0:21:59	0.015266	Thursday	4	19	2016-09-01 00:21	24
NACC3	capitalOrders		8/17/2016	21:20:09	2016-18-08	0:22:06	0.015347	Thursday	4	19	2016-18-8 0:22:06	14
NACC3	capitalOrders		9/16/2016	21:20:09	2016-17-09	0:22:43	0.015775	Saturday	6	19	2016-17-9 0:22:43	#N/A
NACC3	capitalOrders		9/6/2016	21:20:13	2016-07-09	0:21:02	0.014606	Wednesday	3	19	2016-09-07 00:21	28
NACC3	capitalOrders		9/13/2016	21:20:44	2016-14-09	0:22:36	0.015694	Wednesday	3	19	2016-14-9 0:22:36	33
NACC3	capitalOrders		8/14/2016	21:21:01	2016-15-08	0:22:59	0.015961	Monday	1	19	2016-15-8 0:22:59	11
NACC3	capitalOrders		8/25/2016	21:21:01	2016-26-08	0:23:30	0.016319	Friday	5	19	2016-26-8 0:23:30	20
NACC3	capitalOrders		8/26/2016	21:21:01	2016-27-08	0:21:47	0.015127	Saturday	6	19	2016-27-8 0:21:47	#N/A
NACC3	capitalOrders		9/9/2016	21:21:01	2016-10-09	0:22:50	0.015856	Saturday	6	19	2016-09-10 00:22	#N/A
NACC3	capitalOrders		9/21/2016	21:21:01	2016-22-09	0:23:38	0.016412	Thursday	4	19	2016-22-9 0:23:38	39
NACC3	capitalOrders		9/11/2016	21:21:01	2016-12-09	0:23:41	0.016447	Monday	1	19	2016-09-12 00:23	31
NACC3	capitalOrders		9/18/2016	21:21:01	2016-19-09	0:23:43	0.01647	Monday	1	19	2016-19-9 0:23:43	36
NACC3	capitalOrders		8/3/2016	21:21:02	2016-04-08	0:22:04	0.015324	Thursday	4	19	2016-08-04 00:22	4
NACC3	capitalOrders		8/5/2016	21:21:02	2016-06-08	0:21:55	0.01522	Saturday	6	19	2016-08-06 00:21	#N/A
NACC3	capitalOrders		8/16/2016	21:21:02	2016-17-08	0:21:45	0.015104	Wednesday	3	19	2016-17-8 0:21:45	13
NACC3	capitalOrders		8/19/2016	21:21:02	2016-20-08	0:23:26	0.016273	Saturday	6	19	2016-20-8 0:23:26	#N/A
NACC3	capitalOrders		9/5/2016	21:21:02	2016-06-09	0:22:48	0.015833	Tuesday	2	19	2016-09-06 00:22	27
NACC3	capitalOrders		9/19/2016	21:21:02	2016-20-09	0:22:36	0.015694	Tuesday	2	19	2016-20-9 0:22:36	37
NACC3	capitalOrders		8/11/2016	21:21:04	2016-12-08	0:22:52	0.01588	Friday	5	19	2016-08-12 00:22	10
NACC3	capitalOrders		8/2/2016	21:21:11	2016-03-08	0:23:26	0.016273	Wednesday	3	19	2016-08-03 00:23	3
NACC3	capitalOrders		8/12/2016	22:20:02	2016-13-08	1:21:19	0.05647	Saturday	6	19	2016-13-8 1:21:19	#N/A
NACC3	capitalOrders		9/7/2016	22:20:02	2016-08-09	1:21:20	0.056481	Thursday	4	19	2016-09-08 01:21	29
NACC3	capitalOrders		8/9/2016	22:20:04	2016-10-08	1:21:05	0.056308	Wednesday	3	19	2016-08-10 01:21	8
NACC3	capitalOrders		8/30/2016	22:20:04	2016-31-08	1:21:46	0.056782	Wednesday	3	19	2016-31-8 1:21:46	23
NACC3	capitalOrders		9/20/2016	22:20:05	2016-21-09	1:21:14	0.056412	Wednesday	3	19	2016-21-9 1:21:14	38
NACC3	capitalOrders		8/18/2016	22:20:06	2016-19-08	1:23:04	0.057685	Friday	5	19	2016-19-8 1:23:04	15
NACC3	capitalOrders		9/23/2016	22:20:13	2016-24-09	1:20:43	0.056053	Saturday	6	19	2016-24-9 1:20:43	#N/A
NACC3	capitalOrders		8/4/2016	22:21:03	2016-05-08	1:23:07	0.05772	Friday	5	19	2016-08-05 01:23	5
NACC3	capitalOrders		9/5/2016	21:20:05	2016-06-09	0:22:48	0.015833	Tuesday	2	19	2016-09-06 00:22	27
NACC3	capitalOrders		8/17/2016	21:21:01	2016-18-08	0:22:06	0.015347	Thursday	4	19	2016-18-8 0:22:06	14
NACC3	capitalOrders		9/8/2016	21:21:01	2016-09-09	0:24:04	0.016713	Friday	5	19	2016-09-09 00:24	30
NACC3	capitalOrders		9/12/2016	21:21:01	2016-13-09	0:22:08	0.01537	Tuesday	2	19	2016-13-9 0:22:08	32
NACC3	capitalOrders		8/21/2016	21:21:01	2016-22-08	0:23:02	0.015995	Monday	1	19	2016-22-8 0:23:02	16
NACC3	capitalOrders		8/28/2016	21:21:01	2016-29-08	0:22:45	0.015799	Monday	1	19	2016-29-8 0:22:45	21
NACC3	capitalOrders		9/4/2016	21:21:01	2016-05-09	0:22:06	0.015347	Monday	1	19	2016-09-05 00:22	26
NACC3	capitalOrders		8/15/2016	21:21:02	2016-16-08	0:23:22	0.016227	Tuesday	2	19	2016-16-8 0:23:22	12
NACC3	capitalOrders		8/22/2016	21:21:02	2016-23-08	0:23:28	0.016296	Tuesday	2	19	2016-23-8 0:23:28	17
NACC3	capitalOrders		8/7/2016	21:21:02	2016-08-08	0:21:31	0.014942	Monday	1	19	2016-08-08 00:21	6
NACC3	capitalOrders		8/24/2016	21:21:02	2016-25-08	0:22:41	0.015752	Thursday	4	19	2016-25-8 0:22:41	19
NACC3	capitalOrders		9/2/2016	21:21:02	2016-03-09	0:23:10	0.016088	Saturday	6	19	2016-09-03 00:23	#N/A
NACC3	capitalOrders		9/14/2016	21:21:02	2016-15-09	0:25:33	0.017743	Thursday	4	19	2016-15-9 0:25:33	34
NACC3	capitalOrders		9/22/2016	21:21:02	2016-23-09	0:22:10	0.015394	Friday	5	19	2016-23-9 0:22:10	40
NACC3	capitalOrders		9/25/2016	21:21:02	2016-26-09	0:23:20	0.016204	Monday	1	19	2016-26-9 0:23:20	41
NACC3	capitalOrders		8/8/2016	21:21:03	2016-09-08	0:22:17	0.015475	Tuesday	2	19	2016-08-09 00:22	7
NACC3	capitalOrders		9/15/2016	21:21:03	2016-16-09	0:22:02	0.015301	Friday	5	19	2016-16-9 0:22:02	35
NACC3	capitalOrders		8/29/2016	21:21:06	2016-30-08	0:23:01	0.015984	Tuesday	2	19	2016-30-8 0:23:01	22
NACC3	capitalOrders		8/1/2016	21:21:08	2016-02-08	0:24:25	0.016956	Tuesday	2	19	2016-08-02 00:24	2
NACC3	capitalOrders		9/1/2016	21:21:08	2016-02-09	0:22:49	0.015845	Friday	5	19	2016-09-02 00:22	25
NACC3	capitalOrders		9/6/2016	21:21:15	2016-07-09	0:23:03	0.016007	Wednesday	3	19	2016-09-07 00:23	28
NACC3	capitalOrders		9/18/2016	22:20:02	2016-19-09	1:21:45	0.056771	Monday	1	19	2016-19-9 1:21:45	36
NACC3	capitalOrders		8/11/2016	22:20:03	2016-12-08	1:20:55	0.056192	Friday	5	19	2016-08-12 01:20	10
NACC3	capitalOrders		8/14/2016	22:20:03	2016-15-08	1:21:02	0.056273	Monday	1	19	2016-15-8 1:21:02	11
NACC3	capitalOrders		9/11/2016	22:20:03	2016-12-09	1:21:43	0.056748	Monday	1	19	2016-09-12 01:21	31
NACC3	capitalOrders		8/26/2016	22:20:04	2016-27-08	1:21:49	0.056817	Saturday	6	19	2016-27-8 1:21:49	#N/A
NACC3	capitalOrders		8/16/2016	22:20:05	2016-17-08	1:21:47	0.056794	Wednesday	3	19	2016-17-8 1:21:47	13
NACC3	capitalOrders		8/2/2016	22:20:09	2016-03-08	1:21:28	0.056574	Wednesday	3	19	2016-08-03 01:21	3
NACC3	capitalOrders		8/3/2016	22:20:11	2016-04-08	1:22:06	0.057014	Thursday	4	19	2016-08-04 01:22	4
NACC3	capitalOrders		8/19/2016	22:20:11	2016-20-08	1:21:28	0.056574	Saturday	6	19	2016-20-8 1:21:28	#N/A
NACC3	capitalOrders		9/21/2016	22:20:11	2016-22-09	1:21:40	0.056713	Thursday	4	19	2016-22-9 1:21:40	39
NACC3	capitalOrders		8/23/2016	22:20:12	2016-24-08	1:22:26	0.057245	Wednesday	3	19	2016-24-8 1:22:26	18
NACC3	capitalOrders		8/5/2016	22:20:14	2016-06-08	1:21:57	0.05691	Saturday	6	19	2016-08-06 01:21	#N/A
NACC3	capitalOrders		9/19/2016	22:20:16	2016-20-09	1:22:40	0.057407	Tuesday	2	19	2016-20-9 1:22:40	37
NACC3	capitalOrders		8/10/2016	22:20:19	2016-11-08	1:21:46	0.056782	Thursday	4	19	2016-08-11 01:21	9
NACC3	capitalOrders		8/25/2016	22:20:23	2016-26-08	1:23:03	0.057674	Friday	5	19	2016-26-8 1:23:03	20
NACC3	capitalOrders		9/9/2016	22:20:23	2016-10-09	1:22:52	0.057546	Saturday	6	19	2016-09-10 01:22	#N/A
NACC3	capitalOrders		8/9/2016	22:21:01	2016-10-08	1:23:06	0.057708	Wednesday	3	19	2016-08-10 01:23	8
NACC3	capitalOrders		8/12/2016	22:21:01	2016-13-08	1:23:20	0.05787	Saturday	6	19	2016-13-8 1:23:20	#N/A
NACC3	capitalOrders		9/7/2016	22:21:01	2016-08-09	1:23:20	0.05787	Thursday	4	19	2016-09-08 01:23	29
NACC3	capitalOrders		9/13/2016	22:21:01	2016-14-09	1:22:39	0.057396	Wednesday	3	19	2016-14-9 1:22:39	33
NACC3	capitalOrders		8/31/2016	22:21:02	2016-01-09	1:22:02	0.056968	Thursday	4	19	2016-09-01 01:22	24
NACC3	capitalOrders		9/16/2016	22:21:02	2016-17-09	1:22:45	0.057465	Saturday	6	19	2016-17-9 1:22:45	#N/A
NACC3	capitalOrders		9/20/2016	22:21:02	2016-21-09	1:23:15	0.057813	Wednesday	3	19	2016-21-9 1:23:15	38
NACC3	capitalOrders		9/23/2016	22:21:11	2016-24-09	1:22:43	0.057442	Saturday	6	19	2016-24-9 1:22:43	#N/A
NACC3	capitalOrders		8/18/2016	22:21:15	2016-19-08	1:23:05	0.057697	Friday	5	19	2016-19-8 1:23:05	15
NACC3	capitalOrders		8/4/2016	22:21:31	2016-05-08	1:23:07	0.05772	Friday	5	19	2016-08-05 01:23	5
NACC3	capitalOrders		8/21/2016	22:20:03	2016-22-08	1:21:05	0.056308	Monday	1	19	2016-22-8 1:21:05	16
NACC3	capitalOrders		9/4/2016	22:20:03	2016-05-09	1:22:08	0.057037	Monday	1	19	2016-09-05 01:22	26
NACC3	capitalOrders		9/1/2016	22:20:04	2016-02-09	1:22:50	0.057523	Friday	5	19	2016-09-02 01:22	25
NACC3	capitalOrders		9/8/2016	22:20:04	2016-09-09	1:22:06	0.057014	Friday	5	19	2016-09-09 01:22	30
NACC3	capitalOrders		8/28/2016	22:20:04	2016-29-08	1:22:48	0.0575	Monday	1	19	2016-29-8 1:22:48	21
NACC3	capitalOrders		9/12/2016	22:20:06	2016-13-09	1:22:10	0.05706	Tuesday	2	19	2016-13-9 1:22:10	32
NACC3	capitalOrders		9/25/2016	22:20:06	2016-26-09	1:21:22	0.056505	Monday	1	19	2016-26-9 1:21:22	41
NACC3	capitalOrders		9/2/2016	22:20:07	2016-03-09	1:21:12	0.056389	Saturday	6	19	2016-09-03 01:21	#N/A
NACC3	capitalOrders		9/15/2016	22:20:07	2016-16-09	1:22:04	0.056991	Friday	5	19	2016-16-9 1:22:04	35
NACC3	capitalOrders		9/5/2016	22:20:08	2016-06-09	1:22:50	0.057523	Tuesday	2	19	2016-09-06 01:22	27
NACC3	capitalOrders		8/15/2016	22:20:10	2016-16-08	1:21:24	0.056528	Tuesday	2	19	2016-16-8 1:21:24	12
NACC3	capitalOrders		8/22/2016	22:20:12	2016-23-08	1:21:30	0.056597	Tuesday	2	19	2016-23-8 1:21:30	17
NACC3	capitalOrders		8/17/2016	22:20:22	2016-18-08	1:22:08	0.057037	Thursday	4	19	2016-18-8 1:22:08	14
NACC3	capitalOrders		8/23/2016	22:21:01	2016-24-08	1:22:27	0.057257	Wednesday	3	19	2016-24-8 1:22:27	18
NACC3	capitalOrders		8/14/2016	22:21:01	2016-15-08	1:23:02	0.057662	Monday	1	19	2016-15-8 1:23:02	11
NACC3	capitalOrders		9/11/2016	22:21:01	2016-12-09	1:23:44	0.058148	Monday	1	19	2016-09-12 01:23	31
NACC3	capitalOrders		9/18/2016	22:21:01	2016-19-09	1:21:46	0.056782	Monday	1	19	2016-19-9 1:21:46	36
NACC3	capitalOrders		8/7/2016	22:21:02	2016-08-08	1:23:32	0.058009	Monday	1	19	2016-08-08 01:23	6
NACC3	capitalOrders		8/3/2016	22:21:02	2016-04-08	1:22:06	0.057014	Thursday	4	19	2016-08-04 01:22	4
NACC3	capitalOrders		8/24/2016	22:21:02	2016-25-08	1:22:43	0.057442	Thursday	4	19	2016-25-8 1:22:43	19
NACC3	capitalOrders		8/26/2016	22:21:02	2016-27-08	1:21:50	0.056829	Saturday	6	19	2016-27-8 1:21:50	#N/A
NACC3	capitalOrders		9/14/2016	22:21:02	2016-15-09	1:23:35	0.058044	Thursday	4	19	2016-15-9 1:23:35	34
NACC3	capitalOrders		8/16/2016	22:21:04	2016-17-08	1:21:48	0.056806	Wednesday	3	19	2016-17-8 1:21:48	13
NACC3	capitalOrders		9/21/2016	22:21:08	2016-22-09	1:23:41	0.058113	Thursday	4	19	2016-22-9 1:23:41	39
NACC3	capitalOrders		8/5/2016	22:21:14	2016-06-08	1:23:58	0.05831	Saturday	6	19	2016-08-06 01:23	#N/A
NACC3	capitalOrders		8/10/2016	22:21:16	2016-11-08	1:21:46	0.056782	Thursday	4	19	2016-08-11 01:21	9
NACC3	capitalOrders		8/11/2016	22:21:16	2016-12-08	1:22:55	0.057581	Friday	5	19	2016-08-12 01:22	10
NACC3	capitalOrders		9/9/2016	22:21:17	2016-10-09	1:22:52	0.057546	Saturday	6	19	2016-09-10 01:22	#N/A
NACC3	capitalOrders		8/19/2016	22:21:18	2016-20-08	1:23:28	0.057963	Saturday	6	19	2016-20-8 1:23:28	#N/A
NACC3	capitalOrders		8/25/2016	22:21:23	2016-26-08	1:23:03	0.057674	Friday	5	19	2016-26-8 1:23:03	20
NACC3	capitalOrders		9/19/2016	22:21:30	2016-20-09	1:22:40	0.057407	Tuesday	2	19	2016-20-9 1:22:40	37
NACC3	capitalOrders		9/7/2016	23:20:02	2016-08-09	2:21:22	0.098171	Thursday	4	19	2016-09-08 02:21	29
NACC3	capitalOrders		8/29/2016	23:20:03	2016-30-08	2:21:04	0.097963	Tuesday	2	19	2016-30-8 2:21:04	22
NACC3	capitalOrders		9/6/2016	23:20:04	2016-07-09	2:21:06	0.097986	Wednesday	3	19	2016-09-07 02:21	28
NACC3	capitalOrders		9/22/2016	23:20:04	2016-23-09	2:22:15	0.098785	Friday	5	19	2016-23-9 2:22:15	40
NACC3	capitalOrders		8/12/2016	23:20:05	2016-13-08	2:21:22	0.098171	Saturday	6	19	2016-13-8 2:21:22	#N/A
NACC3	capitalOrders		9/13/2016	23:20:05	2016-14-09	2:20:42	0.097708	Wednesday	3	19	2016-14-9 2:20:42	33
NACC3	capitalOrders		8/8/2016	23:20:06	2016-09-08	2:22:22	0.098866	Tuesday	2	19	2016-08-09 02:22	7
NACC3	capitalOrders		8/9/2016	23:20:06	2016-10-08	2:21:08	0.098009	Wednesday	3	19	2016-08-10 02:21	8
NACC3	capitalOrders		8/31/2016	23:20:06	2016-01-09	2:22:03	0.098646	Thursday	4	19	2016-09-01 02:22	24
NACC3	capitalOrders		9/16/2016	23:20:06	2016-17-09	2:22:47	0.099155	Saturday	6	19	2016-17-9 2:22:47	#N/A
NACC3	capitalOrders		8/1/2016	23:20:08	2016-02-08	2:22:29	0.098947	Tuesday	2	19	2016-08-02 02:22	2
NACC3	capitalOrders		9/20/2016	23:20:22	2016-21-09	2:21:18	0.098125	Wednesday	3	19	2016-21-9 2:21:18	38
NACC3	capitalOrders		8/2/2016	23:21:01	2016-03-08	2:21:31	0.098275	Wednesday	3	19	2016-08-03 02:21	3
NACC3	capitalOrders		8/4/2016	0:20:03	2016-04-08	3:22:14	0.14044	Thursday	4	19	2016-08-04 03:22	4
NACC3	capitalOrders		8/30/2016	0:20:03	2016-30-08	3:21:07	0.139664	Tuesday	2	19	2016-30-8 3:21:07	22
NACC3	capitalOrders		8/18/2016	0:20:04	2016-18-08	3:22:13	0.140428	Thursday	4	19	2016-18-8 3:22:13	14
NACC3	capitalOrders		9/23/2016	0:20:05	2016-23-09	3:22:20	0.140509	Friday	5	19	2016-23-9 3:22:20	40
NACC3	capitalOrders		8/21/2016	22:21:01	2016-22-08	1:23:05	0.057697	Monday	1	19	2016-22-8 1:23:05	16
NACC3	capitalOrders		8/28/2016	22:21:01	2016-29-08	1:22:48	0.0575	Monday	1	19	2016-29-8 1:22:48	21
NACC3	capitalOrders		9/4/2016	22:21:01	2016-05-09	1:22:09	0.057049	Monday	1	19	2016-09-05 01:22	26
NACC3	capitalOrders		9/5/2016	22:21:02	2016-06-09	1:22:50	0.057523	Tuesday	2	19	2016-09-06 01:22	27
NACC3	capitalOrders		9/8/2016	22:21:02	2016-09-09	1:22:06	0.057014	Friday	5	19	2016-09-09 01:22	30
NACC3	capitalOrders		9/12/2016	22:21:02	2016-13-09	1:22:10	0.05706	Tuesday	2	19	2016-13-9 1:22:10	32
NACC3	capitalOrders		8/17/2016	22:21:03	2016-18-08	1:22:08	0.057037	Thursday	4	19	2016-18-8 1:22:08	14
NACC3	capitalOrders		9/2/2016	22:21:03	2016-03-09	1:23:13	0.057789	Saturday	6	19	2016-09-03 01:23	#N/A
NACC3	capitalOrders		8/22/2016	22:21:16	2016-23-08	1:23:30	0.057986	Tuesday	2	19	2016-23-8 1:23:30	17
NACC3	capitalOrders		8/15/2016	22:21:20	2016-16-08	1:23:25	0.057928	Tuesday	2	19	2016-16-8 1:23:25	12
NACC3	capitalOrders		8/7/2016	23:20:04	2016-08-08	2:21:34	0.09831	Monday	1	19	2016-08-08 02:21	6
NACC3	capitalOrders		8/11/2016	23:20:04	2016-12-08	2:22:58	0.099282	Friday	5	19	2016-08-12 02:22	10
NACC3	capitalOrders		8/24/2016	23:20:04	2016-25-08	2:22:46	0.099144	Thursday	4	19	2016-25-8 2:22:46	19
NACC3	capitalOrders		9/14/2016	23:20:04	2016-15-09	2:21:09	0.098021	Thursday	4	19	2016-15-9 2:21:09	34
NACC3	capitalOrders		9/11/2016	23:20:04	2016-12-09	2:21:45	0.098438	Monday	1	19	2016-09-12 02:21	31
NACC3	capitalOrders		9/18/2016	23:20:05	2016-19-09	2:21:48	0.098472	Monday	1	19	2016-19-9 2:21:48	36
NACC3	capitalOrders		8/14/2016	23:20:07	2016-15-08	2:21:04	0.097963	Monday	1	19	2016-15-8 2:21:04	11
NACC3	capitalOrders		9/25/2016	23:20:07	2016-26-09	2:21:23	0.098183	Monday	1	19	2016-26-9 2:21:23	41
NACC3	capitalOrders		9/15/2016	23:20:14	2016-16-09	2:21:43	0.098414	Friday	5	19	2016-16-9 2:21:43	35
NACC3	capitalOrders		8/9/2016	23:21:01	2016-10-08	2:23:08	0.099398	Wednesday	3	19	2016-08-10 02:23	8
NACC3	capitalOrders		8/23/2016	23:21:01	2016-24-08	2:22:28	0.098935	Wednesday	3	19	2016-24-8 2:22:28	18
NACC3	capitalOrders		9/1/2016	23:21:01	2016-02-09	2:22:52	0.099213	Friday	5	19	2016-09-02 02:22	25
NACC3	capitalOrders		9/6/2016	23:21:01	2016-07-09	2:23:07	0.099387	Wednesday	3	19	2016-09-07 02:23	28
NACC3	capitalOrders		9/7/2016	23:21:01	2016-08-09	2:23:22	0.09956	Thursday	4	19	2016-09-08 02:23	29
NACC3	capitalOrders		9/13/2016	23:21:01	2016-14-09	2:22:42	0.099097	Wednesday	3	19	2016-14-9 2:22:42	33
NACC3	capitalOrders		8/29/2016	23:21:02	2016-30-08	2:23:04	0.099352	Tuesday	2	19	2016-30-8 2:23:04	22
NACC3	capitalOrders		8/31/2016	23:21:02	2016-01-09	2:22:04	0.098657	Thursday	4	19	2016-09-01 02:22	24
NACC3	capitalOrders		9/22/2016	23:21:02	2016-23-09	2:22:15	0.098785	Friday	5	19	2016-23-9 2:22:15	40
NACC3	capitalOrders		8/12/2016	23:21:03	2016-13-08	2:23:23	0.099572	Saturday	6	19	2016-13-8 2:23:23	#N/A
NACC3	capitalOrders		8/1/2016	23:21:05	2016-02-08	2:22:29	0.098947	Tuesday	2	19	2016-08-02 02:22	2
NACC3	capitalOrders		9/20/2016	23:21:31	2016-21-09	2:23:18	0.099514	Wednesday	3	19	2016-21-9 2:23:18	38
NACC3	capitalOrders		8/8/2016	23:21:36	2016-09-08	2:22:22	0.098866	Tuesday	2	19	2016-08-09 02:22	7
NACC3	capitalOrders		8/3/2016	0:20:04	2016-03-08	3:21:35	0.139988	Wednesday	3	19	2016-08-03 03:21	3
NACC3	capitalOrders		8/5/2016	0:20:04	2016-05-08	3:21:12	0.139722	Friday	5	19	2016-08-05 03:21	5
NACC3	capitalOrders		8/26/2016	0:20:05	2016-26-08	3:21:07	0.139664	Friday	5	19	2016-26-8 3:21:07	20
NACC3	capitalOrders		8/19/2016	0:20:06	2016-19-08	3:23:09	0.141076	Friday	5	19	2016-19-8 3:23:09	15
NACC3	capitalOrders		8/25/2016	0:20:06	2016-25-08	3:20:48	0.139444	Thursday	4	19	2016-25-8 3:20:48	19
NACC3	capitalOrders		9/19/2016	0:20:06	2016-19-09	3:21:50	0.140162	Monday	1	19	2016-19-9 3:21:50	36
NACC3	capitalOrders		8/16/2016	0:20:19	2016-16-08	3:21:29	0.139919	Tuesday	2	19	2016-16-8 3:21:29	12
NACC3	capitalOrders		8/10/2016	0:21:01	2016-10-08	3:23:11	0.1411	Wednesday	3	19	2016-08-10 03:23	8
NACC3	capitalOrders		8/18/2016	0:21:01	2016-18-08	3:22:14	0.14044	Thursday	4	19	2016-18-8 3:22:14	14
NACC3	capitalOrders		8/30/2016	0:21:01	2016-30-08	3:23:08	0.141065	Tuesday	2	19	2016-30-8 3:23:08	22
NACC3	capitalOrders		9/23/2016	0:21:01	2016-23-09	3:22:20	0.140509	Friday	5	19	2016-23-9 3:22:20	40
NACC3	capitalOrders		8/4/2016	0:21:02	2016-04-08	3:22:15	0.140451	Thursday	4	19	2016-08-04 03:22	4
NACC3	capitalOrders		9/9/2016	1:20:03	2016-09-09	4:22:12	0.182083	Friday	5	19	2016-09-09 04:22	30
NACC3	capitalOrders		8/2/2016	1:20:04	2016-02-08	4:22:34	0.182338	Tuesday	2	19	2016-08-02 04:22	2
NACC3	capitalOrders		9/16/2016	1:20:05	2016-16-09	4:21:50	0.181829	Friday	5	19	2016-16-9 4:21:50	35
NACC3	capitalOrders		9/21/2016	1:20:05	2016-21-09	4:20:56	0.181204	Wednesday	3	19	2016-21-9 4:20:56	38
NACC3	capitalOrders		8/21/2016	23:20:03	2016-22-08	2:21:07	0.097998	Monday	1	19	2016-22-8 2:21:07	16
NACC3	capitalOrders		9/4/2016	23:20:03	2016-05-09	2:22:11	0.098738	Monday	1	19	2016-09-05 02:22	26
NACC3	capitalOrders		9/8/2016	23:20:06	2016-09-09	2:22:37	0.099039	Friday	5	19	2016-09-09 02:22	30
NACC3	capitalOrders		8/14/2016	23:21:01	2016-15-08	2:23:04	0.099352	Monday	1	19	2016-15-8 2:23:04	11
NACC3	capitalOrders		8/24/2016	23:21:01	2016-25-08	2:22:46	0.099144	Thursday	4	19	2016-25-8 2:22:46	19
NACC3	capitalOrders		8/28/2016	23:21:01	2016-29-08	2:22:50	0.09919	Monday	1	19	2016-29-8 2:22:50	21
NACC3	capitalOrders		9/11/2016	23:21:01	2016-12-09	2:23:46	0.099838	Monday	1	19	2016-09-12 02:23	31
NACC3	capitalOrders		9/18/2016	23:21:01	2016-19-09	2:21:48	0.098472	Monday	1	19	2016-19-9 2:21:48	36
NACC3	capitalOrders		9/25/2016	23:21:01	2016-26-09	2:23:24	0.099583	Monday	1	19	2016-26-9 2:23:24	41
NACC3	capitalOrders		9/5/2016	23:21:02	2016-06-09	2:22:52	0.099213	Tuesday	2	19	2016-09-06 02:22	27
NACC3	capitalOrders		8/7/2016	23:21:03	2016-08-08	2:23:35	0.099711	Monday	1	19	2016-08-08 02:23	6
NACC3	capitalOrders		9/15/2016	23:21:40	2016-16-09	2:23:43	0.099803	Friday	5	19	2016-16-9 2:23:43	35
NACC3	capitalOrders		8/11/2016	0:20:02	2016-11-08	3:21:52	0.140185	Thursday	4	19	2016-08-11 03:21	9
NACC3	capitalOrders		8/22/2016	0:20:03	2016-22-08	3:21:10	0.139699	Monday	1	19	2016-22-8 3:21:10	16
NACC3	capitalOrders		8/29/2016	0:20:03	2016-29-08	3:22:54	0.140903	Monday	1	19	2016-29-8 3:22:54	21
NACC3	capitalOrders		8/17/2016	0:20:04	2016-17-08	3:21:52	0.140185	Wednesday	3	19	2016-17-8 3:21:52	13
NACC3	capitalOrders		9/2/2016	0:20:04	2016-02-09	3:22:56	0.140926	Friday	5	19	2016-09-02 03:22	25
NACC3	capitalOrders		9/6/2016	0:20:04	2016-06-09	3:20:54	0.139514	Tuesday	2	19	2016-09-06 03:20	27
NACC3	capitalOrders		9/12/2016	0:20:04	2016-12-09	3:21:49	0.14015	Monday	1	19	2016-09-12 03:21	31
NACC3	capitalOrders		8/23/2016	0:20:05	2016-23-08	3:21:34	0.139977	Tuesday	2	19	2016-23-8 3:21:34	17
NACC3	capitalOrders		8/31/2016	0:20:05	2016-31-08	3:21:52	0.140185	Wednesday	3	19	2016-31-8 3:21:52	23
NACC3	capitalOrders		9/22/2016	0:20:05	2016-22-09	3:21:48	0.140139	Thursday	4	19	2016-22-9 3:21:48	39
NACC3	capitalOrders		8/9/2016	0:20:06	2016-09-08	3:22:25	0.140567	Tuesday	2	19	2016-08-09 03:22	7
NACC3	capitalOrders		9/13/2016	0:20:06	2016-13-09	3:22:15	0.140451	Tuesday	2	19	2016-13-9 3:22:15	32
NACC3	capitalOrders		9/20/2016	0:20:09	2016-20-09	3:22:18	0.140486	Tuesday	2	19	2016-20-9 3:22:18	37
NACC3	capitalOrders		8/1/2016	0:21:01	2016-01-08	3:23:52	0.141574	Monday	1	19	2016-08-01 03:23	1
NACC3	capitalOrders		8/12/2016	0:21:01	2016-12-08	3:23:02	0.140995	Friday	5	19	2016-08-12 03:23	10
NACC3	capitalOrders		8/16/2016	0:21:01	2016-16-08	3:23:29	0.141308	Tuesday	2	19	2016-16-8 3:23:29	12
NACC3	capitalOrders		8/26/2016	0:21:01	2016-26-08	3:23:08	0.141065	Friday	5	19	2016-26-8 3:23:08	20
NACC3	capitalOrders		8/5/2016	0:21:02	2016-05-08	3:23:12	0.141111	Friday	5	19	2016-08-05 03:23	5
NACC3	capitalOrders		8/15/2016	0:21:02	2016-15-08	3:23:08	0.141065	Monday	1	19	2016-15-8 3:23:08	11
NACC3	capitalOrders		8/19/2016	0:21:02	2016-19-08	3:23:10	0.141088	Friday	5	19	2016-19-8 3:23:10	15
NACC3	capitalOrders		8/25/2016	0:21:02	2016-25-08	3:22:49	0.140845	Thursday	4	19	2016-25-8 3:22:49	19
NACC3	capitalOrders		9/1/2016	0:21:02	2016-01-09	3:22:07	0.140359	Thursday	4	19	2016-09-01 03:22	24
NACC3	capitalOrders		9/7/2016	0:21:02	2016-07-09	3:23:09	0.141076	Wednesday	3	19	2016-09-07 03:23	28
NACC3	capitalOrders		9/19/2016	0:21:02	2016-19-09	3:21:50	0.140162	Monday	1	19	2016-19-9 3:21:50	36
NACC3	capitalOrders		8/8/2016	0:21:03	2016-08-08	3:23:37	0.1414	Monday	1	19	2016-08-08 03:23	6
NACC3	capitalOrders		9/14/2016	0:21:03	2016-14-09	3:22:46	0.14081	Wednesday	3	19	2016-14-9 3:22:46	33
NACC3	capitalOrders		8/3/2016	0:21:06	2016-03-08	3:23:35	0.141377	Wednesday	3	19	2016-08-03 03:23	3
NACC3	capitalOrders		8/18/2016	1:20:04	2016-18-08	4:22:18	0.182153	Thursday	4	19	2016-18-8 4:22:18	14
NACC3	capitalOrders		8/4/2016	1:20:05	2016-04-08	4:22:22	0.182199	Thursday	4	19	2016-08-04 04:22	4
NACC3	capitalOrders		8/10/2016	1:20:05	2016-10-08	5:05:17	0.212002	Wednesday	3	19	2016-08-10 05:05	8
NACC3	capitalOrders		9/23/2016	1:20:06	2016-23-09	4:22:24	0.182222	Friday	5	19	2016-23-9 4:22:24	40
NACC3	capitalOrders		8/30/2016	1:21:01	2016-30-08	4:23:10	0.182755	Tuesday	2	19	2016-30-8 4:23:10	22
NACC3	capitalOrders		9/9/2016	1:21:01	2016-09-09	4:22:13	0.182095	Friday	5	19	2016-09-09 04:22	30
NACC3	capitalOrders		8/2/2016	1:21:02	2016-02-08	4:22:34	0.182338	Tuesday	2	19	2016-08-02 04:22	2
NACC3	capitalOrders		9/16/2016	1:21:02	2016-16-09	4:21:50	0.181829	Friday	5	19	2016-16-9 4:21:50	35
NACC3	capitalOrders		9/21/2016	1:21:02	2016-21-09	4:22:57	0.182604	Wednesday	3	19	2016-21-9 4:22:57	38
NACC3	capitalOrders		9/4/2016	23:21:01	2016-05-09	2:22:11	0.098738	Monday	1	19	2016-09-05 02:22	26
NACC3	capitalOrders		8/21/2016	23:21:02	2016-22-08	2:23:08	0.099398	Monday	1	19	2016-22-8 2:23:08	16
NACC3	capitalOrders		9/8/2016	23:21:13	2016-09-09	2:22:38	0.099051	Friday	5	19	2016-09-09 02:22	30
NACC3	capitalOrders		9/5/2016	0:20:03	2016-05-09	3:22:14	0.14044	Monday	1	19	2016-09-05 03:22	26
NACC3	capitalOrders		8/24/2016	0:20:05	2016-24-08	3:22:30	0.140625	Wednesday	3	19	2016-24-8 3:22:30	18
NACC3	capitalOrders		9/15/2016	0:20:05	2016-15-09	3:21:14	0.139745	Thursday	4	19	2016-15-9 3:21:14	34
NACC3	capitalOrders		8/11/2016	0:21:01	2016-11-08	3:21:52	0.140185	Thursday	4	19	2016-08-11 03:21	9
NACC3	capitalOrders		8/17/2016	0:21:01	2016-17-08	3:21:52	0.140185	Wednesday	3	19	2016-17-8 3:21:52	13
NACC3	capitalOrders		8/23/2016	0:21:01	2016-23-08	3:21:34	0.139977	Tuesday	2	19	2016-23-8 3:21:34	17
NACC3	capitalOrders		8/29/2016	0:21:01	2016-29-08	3:22:54	0.140903	Monday	1	19	2016-29-8 3:22:54	21
NACC3	capitalOrders		8/31/2016	0:21:01	2016-31-08	3:23:52	0.141574	Wednesday	3	19	2016-31-8 3:23:52	23
NACC3	capitalOrders		9/12/2016	0:21:01	2016-12-09	3:21:49	0.14015	Monday	1	19	2016-09-12 03:21	31
NACC3	capitalOrders		9/13/2016	0:21:01	2016-13-09	3:22:15	0.140451	Tuesday	2	19	2016-13-9 3:22:15	32
NACC3	capitalOrders		9/22/2016	0:21:01	2016-22-09	3:23:48	0.141528	Thursday	4	19	2016-22-9 3:23:48	39
NACC3	capitalOrders		9/2/2016	0:21:02	2016-02-09	3:22:57	0.140938	Friday	5	19	2016-09-02 03:22	25
NACC3	capitalOrders		9/6/2016	0:21:02	2016-06-09	3:22:55	0.140914	Tuesday	2	19	2016-09-06 03:22	27
NACC3	capitalOrders		9/20/2016	0:21:02	2016-20-09	3:22:18	0.140486	Tuesday	2	19	2016-20-9 3:22:18	37
NACC3	capitalOrders		8/12/2016	1:20:02	2016-12-08	4:20:35	0.180961	Friday	5	19	2016-08-12 04:20	10
NACC3	capitalOrders		8/5/2016	1:20:03	2016-05-08	4:21:15	0.181424	Friday	5	19	2016-08-05 04:21	5
NACC3	capitalOrders		8/8/2016	1:20:03	2016-08-08	4:21:40	0.181713	Monday	1	19	2016-08-08 04:21	6
NACC3	capitalOrders		8/22/2016	1:20:03	2016-22-08	4:21:14	0.181412	Monday	1	19	2016-22-8 4:21:14	16
NACC3	capitalOrders		8/1/2016	1:20:04	2016-01-08	4:21:55	0.181887	Monday	1	19	2016-08-01 04:21	1
NACC3	capitalOrders		9/7/2016	1:20:04	2016-07-09	4:21:12	0.181389	Wednesday	3	19	2016-09-07 04:21	28
NACC3	capitalOrders		9/14/2016	1:20:05	2016-14-09	4:20:48	0.181111	Wednesday	3	19	2016-14-9 4:20:48	33
NACC3	capitalOrders		8/15/2016	1:20:06	2016-15-08	4:21:10	0.181366	Monday	1	19	2016-15-8 4:21:10	11
NACC3	capitalOrders		9/1/2016	1:20:06	2016-01-09	4:22:09	0.182049	Thursday	4	19	2016-09-01 04:22	24
NACC3	capitalOrders		8/3/2016	1:20:10	2016-03-08	4:21:38	0.18169	Wednesday	3	19	2016-08-03 04:21	3
NACC3	capitalOrders		8/19/2016	1:21:01	2016-19-08	4:22:44	0.182454	Friday	5	19	2016-19-8 4:22:44	15
NACC3	capitalOrders		8/26/2016	1:21:01	2016-26-08	4:23:10	0.182755	Friday	5	19	2016-26-8 4:23:10	20
NACC3	capitalOrders		8/9/2016	1:21:02	2016-09-08	4:36:29	0.192002	Tuesday	2	19	2016-08-09 04:36	7
NACC3	capitalOrders		8/10/2016	1:21:02	2016-10-08	5:05:17	0.212002	Wednesday	3	19	2016-08-10 05:05	8
NACC3	capitalOrders		8/16/2016	1:21:02	2016-16-08	4:23:32	0.183009	Tuesday	2	19	2016-16-8 4:23:32	12
NACC3	capitalOrders		8/18/2016	1:21:02	2016-18-08	4:22:18	0.182153	Thursday	4	19	2016-18-8 4:22:18	14
NACC3	capitalOrders		8/25/2016	1:21:02	2016-25-08	4:22:51	0.182535	Thursday	4	19	2016-25-8 4:22:51	19
NACC3	capitalOrders		9/19/2016	1:21:02	2016-19-09	4:21:53	0.181863	Monday	1	19	2016-19-9 4:21:53	36
NACC3	capitalOrders		9/23/2016	1:21:02	2016-23-09	4:22:24	0.182222	Friday	5	19	2016-23-9 4:22:24	40
NACC3	capitalOrders		8/2/2016	4:20:02	2016-02-08	7:21:10	0.306366	Tuesday	2	19	2016-08-02 07:21	2
NACC3	capitalOrders		8/4/2016	4:20:02	2016-04-08	7:22:53	0.307558	Thursday	4	19	2016-08-04 07:22	4
NACC3	capitalOrders		9/9/2016	4:20:04	2016-09-09	7:22:25	0.307234	Friday	5	19	2016-09-09 07:22	30
NACC3	capitalOrders		9/16/2016	4:20:04	2016-16-09	7:22:05	0.307002	Friday	5	19	2016-16-9 7:22:05	35
NACC3	capitalOrders		9/21/2016	4:20:08	2016-21-09	7:21:09	0.306354	Wednesday	3	19	2016-21-9 7:21:09	38
NACC3	capitalOrders		8/30/2016	4:20:30	2016-30-08	7:21:19	0.30647	Tuesday	2	19	2016-30-8 7:21:19	22
NACC3	capitalOrders		8/7/2016	17:20:02	2016-07-08	20:21:44	0.848426	Sunday	7	19	2016-08-07 20:21	#N/A
NACC3	capitalOrders		8/14/2016	17:20:02	2016-14-08	20:20:47	0.847766	Sunday	7	19	2016-14-8 20:20:47	#N/A
NACC3	capitalOrders		9/25/2016	17:20:04	2016-25-09	20:21:40	0.84838	Sunday	7	19	2016-25-9 20:21:40	#N/A
NACC3	capitalOrders		9/18/2016	17:20:05	2016-18-09	20:21:34	0.84831	Sunday	7	19	2016-18-9 20:21:34	#N/A
NACC3	capitalOrders		9/11/2016	17:20:06	2016-11-09	20:21:32	0.848287	Sunday	7	19	2016-09-11 20:21	#N/A
NACC3	capitalOrders		8/28/2016	17:20:07	2016-28-08	20:22:36	0.849028	Sunday	7	19	2016-28-8 20:22:36	#N/A
NACC3	capitalOrders		9/8/2016	0:20:29	2016-08-09	3:21:24	0.139861	Thursday	4	19	2016-09-08 03:21	29
NACC3	capitalOrders		9/5/2016	0:21:01	2016-05-09	3:22:14	0.14044	Monday	1	19	2016-09-05 03:22	26
NACC3	capitalOrders		8/24/2016	0:21:02	2016-24-08	3:22:31	0.140637	Wednesday	3	19	2016-24-8 3:22:31	18
NACC3	capitalOrders		9/15/2016	0:21:02	2016-15-09	3:23:14	0.141134	Thursday	4	19	2016-15-9 3:23:14	34
NACC3	capitalOrders		8/29/2016	1:20:03	2016-29-08	4:20:56	0.181204	Monday	1	19	2016-29-8 4:20:56	21
NACC3	capitalOrders		9/2/2016	1:20:04	2016-02-09	4:22:59	0.182627	Friday	5	19	2016-09-02 04:22	25
NACC3	capitalOrders		9/6/2016	1:20:04	2016-06-09	4:20:27	0.180868	Tuesday	2	19	2016-09-06 04:20	27
NACC3	capitalOrders		9/12/2016	1:20:04	2016-12-09	4:21:52	0.181852	Monday	1	19	2016-09-12 04:21	31
NACC3	capitalOrders		8/23/2016	1:20:05	2016-23-08	4:21:37	0.181678	Tuesday	2	19	2016-23-8 4:21:37	17
NACC3	capitalOrders		8/31/2016	1:20:05	2016-31-08	4:21:54	0.181875	Wednesday	3	19	2016-31-8 4:21:54	23
NACC3	capitalOrders		8/11/2016	1:20:06	2016-11-08	4:21:56	0.181898	Thursday	4	19	2016-08-11 04:21	9
NACC3	capitalOrders		8/17/2016	1:20:06	2016-17-08	4:21:55	0.181887	Wednesday	3	19	2016-17-8 4:21:55	13
NACC3	capitalOrders		9/13/2016	1:20:35	2016-13-09	4:22:18	0.182153	Tuesday	2	19	2016-13-9 4:22:18	32
NACC3	capitalOrders		8/1/2016	1:21:01	2016-01-08	4:21:56	0.181898	Monday	1	19	2016-08-01 04:21	1
NACC3	capitalOrders		8/12/2016	1:21:01	2016-12-08	4:22:36	0.182361	Friday	5	19	2016-08-12 04:22	10
NACC3	capitalOrders		9/22/2016	1:21:01	2016-22-09	4:21:51	0.18184	Thursday	4	19	2016-22-9 4:21:51	39
NACC3	capitalOrders		8/22/2016	1:21:02	2016-22-08	4:23:15	0.182813	Monday	1	19	2016-22-8 4:23:15	16
NACC3	capitalOrders		9/20/2016	1:21:02	2016-20-09	4:22:22	0.182199	Tuesday	2	19	2016-20-9 4:22:22	37
NACC3	capitalOrders		8/19/2016	4:20:01	2016-19-08	7:20:55	0.306192	Friday	5	19	2016-19-8 7:20:55	15
NACC3	capitalOrders		8/10/2016	4:20:02	2016-10-08	7:21:29	0.306586	Wednesday	3	19	2016-08-10 07:21	8
NACC3	capitalOrders		8/18/2016	4:20:02	2016-18-08	7:22:32	0.307315	Thursday	4	19	2016-18-8 7:22:32	14
NACC3	capitalOrders		8/26/2016	4:20:02	2016-26-08	7:21:23	0.306516	Friday	5	19	2016-26-8 7:21:23	20
NACC3	capitalOrders		8/3/2016	4:20:03	2016-03-08	7:21:50	0.306829	Wednesday	3	19	2016-08-03 07:21	3
NACC3	capitalOrders		8/5/2016	4:20:03	2016-05-08	7:21:13	0.3064	Friday	5	19	2016-08-05 07:21	5
NACC3	capitalOrders		8/25/2016	4:20:03	2016-25-08	7:21:04	0.306296	Thursday	4	19	2016-25-8 7:21:04	19
NACC3	capitalOrders		8/8/2016	4:20:05	2016-08-08	7:21:59	0.306933	Monday	1	19	2016-08-08 07:21	6
NACC3	capitalOrders		9/23/2016	4:20:07	2016-23-09	7:22:40	0.307407	Friday	5	19	2016-23-9 7:22:40	40
NACC3	capitalOrders		9/1/2016	4:20:08	2016-01-09	7:22:21	0.307188	Thursday	4	19	2016-09-01 07:22	24
NACC3	capitalOrders		9/14/2016	4:20:11	2016-14-09	7:21:02	0.306273	Wednesday	3	19	2016-14-9 7:21:02	33
NACC3	capitalOrders		8/9/2016	4:20:13	2016-09-08	7:22:52	0.307546	Tuesday	2	19	2016-08-09 07:22	7
NACC3	capitalOrders		8/16/2016	4:20:15	2016-16-08	7:23:43	0.308137	Tuesday	2	19	2016-16-8 7:23:43	12
NACC3	capitalOrders		8/15/2016	4:20:23	2016-15-08	7:22:54	0.307569	Monday	1	19	2016-15-8 7:22:54	11
NACC3	capitalOrders		9/19/2016	4:20:27	2016-19-09	7:22:06	0.307014	Monday	1	19	2016-19-9 7:22:06	36
NACC3	capitalOrders		8/2/2016	4:21:01	2016-02-08	7:23:11	0.307766	Tuesday	2	19	2016-08-02 07:23	2
NACC3	capitalOrders		9/9/2016	4:21:01	2016-09-09	7:22:26	0.307245	Friday	5	19	2016-09-09 07:22	30
NACC3	capitalOrders		9/16/2016	4:21:02	2016-16-09	7:22:05	0.307002	Friday	5	19	2016-16-9 7:22:05	35
NACC3	capitalOrders		8/4/2016	4:21:03	2016-04-08	7:22:53	0.307558	Thursday	4	19	2016-08-04 07:22	4
NACC3	capitalOrders		9/7/2016	4:21:07	2016-07-09	7:23:23	0.307905	Wednesday	3	19	2016-09-07 07:23	28
NACC3	capitalOrders		9/21/2016	4:21:13	2016-21-09	7:23:09	0.307743	Wednesday	3	19	2016-21-9 7:23:09	38
NACC3	capitalOrders		8/30/2016	4:21:19	2016-30-08	7:23:20	0.30787	Tuesday	2	19	2016-30-8 7:23:20	22
NACC3	capitalOrders		8/21/2016	17:20:04	2016-21-08	20:20:51	0.847813	Sunday	7	19	2016-21-8 20:20:51	#N/A
NACC3	capitalOrders		9/4/2016	17:20:04	2016-04-09	20:21:57	0.848576	Sunday	7	19	2016-09-04 20:21	#N/A
NACC3	capitalOrders		8/7/2016	17:21:01	2016-07-08	20:23:45	0.849826	Sunday	7	19	2016-08-07 20:23	#N/A
NACC3	capitalOrders		8/14/2016	17:21:01	2016-14-08	20:22:47	0.849155	Sunday	7	19	2016-14-8 20:22:47	#N/A
NACC3	capitalOrders		8/28/2016	17:21:01	2016-28-08	20:22:36	0.849028	Sunday	7	19	2016-28-8 20:22:36	#N/A
NACC3	capitalOrders		9/11/2016	17:21:01	2016-11-09	20:23:33	0.849688	Sunday	7	19	2016-09-11 20:23	#N/A
NACC3	capitalOrders		9/18/2016	17:21:01	2016-18-09	20:23:34	0.849699	Sunday	7	19	2016-18-9 20:23:34	#N/A
NACC3	capitalOrders		9/25/2016	17:21:01	2016-25-09	20:23:40	0.849769	Sunday	7	19	2016-25-9 20:23:40	#N/A
NACC3	capitalOrders		9/8/2016	0:21:19	2016-08-09	3:23:24	0.14125	Thursday	4	19	2016-09-08 03:23	29
NACC3	capitalOrders		9/5/2016	1:20:03	2016-05-09	4:22:16	0.18213	Monday	1	19	2016-09-05 04:22	26
NACC3	capitalOrders		8/17/2016	1:21:01	2016-17-08	4:21:55	0.181887	Wednesday	3	19	2016-17-8 4:21:55	13
NACC3	capitalOrders		8/31/2016	1:21:01	2016-31-08	4:21:55	0.181887	Wednesday	3	19	2016-31-8 4:21:55	23
NACC3	capitalOrders		9/12/2016	1:21:01	2016-12-09	4:23:52	0.183241	Monday	1	19	2016-09-12 04:23	31
NACC3	capitalOrders		8/11/2016	1:21:02	2016-11-08	4:21:57	0.18191	Thursday	4	19	2016-08-11 04:21	9
NACC3	capitalOrders		8/23/2016	1:21:02	2016-23-08	4:23:38	0.183079	Tuesday	2	19	2016-23-8 4:23:38	17
NACC3	capitalOrders		8/29/2016	1:21:02	2016-29-08	4:22:56	0.182593	Monday	1	19	2016-29-8 4:22:56	21
NACC3	capitalOrders		9/2/2016	1:21:02	2016-02-09	4:22:59	0.182627	Friday	5	19	2016-09-02 04:22	25
NACC3	capitalOrders		9/6/2016	1:21:03	2016-06-09	4:22:27	0.182257	Tuesday	2	19	2016-09-06 04:22	27
NACC3	capitalOrders		9/13/2016	1:21:58	2016-13-09	4:24:19	0.183553	Tuesday	2	19	2016-13-9 4:24:19	32
NACC3	capitalOrders		8/12/2016	4:20:02	2016-12-08	7:21:06	0.306319	Friday	5	19	2016-08-12 07:21	10
NACC3	capitalOrders		8/24/2016	4:20:03	2016-24-08	7:22:15	0.307118	Wednesday	3	19	2016-24-8 7:22:15	18
NACC3	capitalOrders		9/15/2016	4:20:03	2016-15-09	7:21:29	0.306586	Thursday	4	19	2016-15-9 7:21:29	34
NACC3	capitalOrders		8/1/2016	4:20:04	2016-01-08	7:22:02	0.306968	Monday	1	19	2016-08-01 07:22	1
NACC3	capitalOrders		8/22/2016	4:20:05	2016-22-08	7:21:26	0.306551	Monday	1	19	2016-22-8 7:21:26	16
NACC3	capitalOrders		9/22/2016	4:20:07	2016-22-09	7:21:34	0.306644	Thursday	4	19	2016-22-9 7:21:34	39
NACC3	capitalOrders		9/20/2016	4:20:10	2016-20-09	7:22:38	0.307384	Tuesday	2	19	2016-20-9 7:22:38	37
NACC3	capitalOrders		9/7/2016	4:20:23	2016-07-09	7:23:23	0.307905	Wednesday	3	19	2016-09-07 07:23	28
NACC3	capitalOrders		8/5/2016	4:21:01	2016-05-08	7:23:13	0.307789	Friday	5	19	2016-08-05 07:23	5
NACC3	capitalOrders		9/1/2016	4:21:01	2016-01-09	7:22:21	0.307188	Thursday	4	19	2016-09-01 07:22	24
NACC3	capitalOrders		9/23/2016	4:21:01	2016-23-09	7:22:40	0.307407	Friday	5	19	2016-23-9 7:22:40	40
NACC3	capitalOrders		8/3/2016	4:21:02	2016-03-08	7:23:51	0.308229	Wednesday	3	19	2016-08-03 07:23	3
NACC3	capitalOrders		8/8/2016	4:21:02	2016-08-08	7:21:59	0.306933	Monday	1	19	2016-08-08 07:21	6
NACC3	capitalOrders		8/10/2016	4:21:02	2016-10-08	7:23:29	0.307975	Wednesday	3	19	2016-08-10 07:23	8
NACC3	capitalOrders		8/19/2016	4:21:02	2016-19-08	7:22:56	0.307593	Friday	5	19	2016-19-8 7:22:56	15
NACC3	capitalOrders		8/25/2016	4:21:02	2016-25-08	7:23:04	0.307685	Thursday	4	19	2016-25-8 7:23:04	19
NACC3	capitalOrders		8/26/2016	4:21:02	2016-26-08	7:23:24	0.307917	Friday	5	19	2016-26-8 7:23:24	20
NACC3	capitalOrders		8/9/2016	4:21:03	2016-09-08	7:22:52	0.307546	Tuesday	2	19	2016-08-09 07:22	7
NACC3	capitalOrders		8/15/2016	4:21:03	2016-15-08	7:22:55	0.307581	Monday	1	19	2016-15-8 7:22:55	11
NACC3	capitalOrders		8/18/2016	4:21:04	2016-18-08	7:22:32	0.307315	Thursday	4	19	2016-18-8 7:22:32	14
NACC3	capitalOrders		9/14/2016	4:21:11	2016-14-09	7:23:02	0.307662	Wednesday	3	19	2016-14-9 7:23:02	33
NACC3	capitalOrders		8/16/2016	4:21:16	2016-16-08	7:23:43	0.308137	Tuesday	2	19	2016-16-8 7:23:43	12
NACC3	capitalOrders		9/19/2016	4:21:25	2016-19-09	7:24:07	0.308414	Monday	1	19	2016-19-9 7:24:07	36
NACC3	capitalOrders		8/2/2016	5:20:02	2016-02-08	8:21:14	0.348079	Tuesday	2	19	2016-08-02 08:21	2
NACC3	capitalOrders		8/4/2016	5:20:03	2016-04-08	8:22:25	0.3489	Thursday	4	19	2016-08-04 08:22	4
NACC3	capitalOrders		9/16/2016	5:20:05	2016-16-09	8:22:07	0.348692	Friday	5	19	2016-16-9 8:22:07	35
NACC3	capitalOrders		9/9/2016	5:21:02	2016-09-09	8:22:28	0.348935	Friday	5	19	2016-09-09 08:22	30
NACC3	capitalOrders		9/21/2016	6:20:02	2016-21-09	9:21:15	0.389757	Wednesday	3	19	2016-21-9 9:21:15	38
NACC3	capitalOrders		8/30/2016	6:20:05	2016-30-08	9:21:26	0.389884	Tuesday	2	19	2016-30-8 9:21:26	22
NACC3	capitalOrders		8/21/2016	17:21:01	2016-21-08	20:22:51	0.849201	Sunday	7	19	2016-21-8 20:22:51	#N/A
NACC3	capitalOrders		9/4/2016	17:21:02	2016-04-09	20:21:57	0.848576	Sunday	7	19	2016-09-04 20:21	#N/A
NACC3	capitalOrders		8/7/2016	18:20:02	2016-07-08	21:21:48	0.890139	Sunday	7	19	2016-08-07 21:21	#N/A
NACC3	capitalOrders		8/14/2016	18:20:02	2016-14-08	21:20:49	0.889456	Sunday	7	19	2016-14-8 21:20:49	#N/A
NACC3	capitalOrders		9/25/2016	18:20:04	2016-25-09	21:21:42	0.890069	Sunday	7	19	2016-25-9 21:21:42	#N/A
NACC3	capitalOrders		8/28/2016	18:21:01	2016-28-08	21:22:38	0.890718	Sunday	7	19	2016-28-8 21:22:38	#N/A
NACC3	capitalOrders		9/11/2016	18:21:01	2016-11-09	21:23:34	0.891366	Sunday	7	19	2016-09-11 21:23	#N/A
NACC3	capitalOrders		9/18/2016	18:21:01	2016-18-09	21:23:37	0.8914	Sunday	7	19	2016-18-9 21:23:37	#N/A
NACC3	capitalOrders		9/5/2016	1:21:01	2016-05-09	4:22:16	0.18213	Monday	1	19	2016-09-05 04:22	26
NACC3	capitalOrders		8/11/2016	4:20:02	2016-11-08	7:22:01	0.306956	Thursday	4	19	2016-08-11 07:22	9
NACC3	capitalOrders		9/8/2016	4:20:02	2016-08-09	7:21:39	0.306701	Thursday	4	19	2016-09-08 07:21	29
NACC3	capitalOrders		9/2/2016	4:20:04	2016-02-09	7:22:43	0.307442	Friday	5	19	2016-09-02 07:22	25
NACC3	capitalOrders		9/12/2016	4:20:04	2016-12-09	7:21:33	0.306632	Monday	1	19	2016-09-12 07:21	31
NACC3	capitalOrders		8/17/2016	4:20:05	2016-17-08	7:22:07	0.307025	Wednesday	3	19	2016-17-8 7:22:07	13
NACC3	capitalOrders		9/6/2016	4:20:07	2016-06-09	7:22:39	0.307396	Tuesday	2	19	2016-09-06 07:22	27
NACC3	capitalOrders		8/31/2016	4:20:08	2016-31-08	7:22:04	0.306991	Wednesday	3	19	2016-31-8 7:22:04	23
NACC3	capitalOrders		8/29/2016	4:20:13	2016-29-08	8:19:08	0.34662	Monday	1	19	2016-29-8 8:19:08	21
NACC3	capitalOrders		9/13/2016	4:20:15	2016-13-09	7:22:31	0.307303	Tuesday	2	19	2016-13-9 7:22:31	32
NACC3	capitalOrders		8/23/2016	4:20:16	2016-23-08	7:21:51	0.30684	Tuesday	2	19	2016-23-8 7:21:51	17
NACC3	capitalOrders		8/12/2016	4:21:01	2016-12-08	7:23:06	0.307708	Friday	5	19	2016-08-12 07:23	10
NACC3	capitalOrders		8/24/2016	4:21:01	2016-24-08	7:22:16	0.30713	Wednesday	3	19	2016-24-8 7:22:16	18
NACC3	capitalOrders		9/15/2016	4:21:01	2016-15-09	7:23:29	0.307975	Thursday	4	19	2016-15-9 7:23:29	34
NACC3	capitalOrders		8/1/2016	4:21:02	2016-01-08	7:22:03	0.306979	Monday	1	19	2016-08-01 07:22	1
NACC3	capitalOrders		9/22/2016	4:21:02	2016-22-09	7:21:34	0.306644	Thursday	4	19	2016-22-9 7:21:34	39
NACC3	capitalOrders		8/22/2016	4:21:13	2016-22-08	7:23:27	0.307951	Monday	1	19	2016-22-8 7:23:27	16
NACC3	capitalOrders		9/20/2016	4:21:27	2016-20-09	7:22:38	0.307384	Tuesday	2	19	2016-20-9 7:22:38	37
NACC3	capitalOrders		8/10/2016	5:20:02	2016-10-08	8:21:31	0.348275	Wednesday	3	19	2016-08-10 08:21	8
NACC3	capitalOrders		8/26/2016	5:20:02	2016-26-08	8:21:25	0.348206	Friday	5	19	2016-26-8 8:21:25	20
NACC3	capitalOrders		8/3/2016	5:20:04	2016-03-08	8:21:53	0.34853	Wednesday	3	19	2016-08-03 08:21	3
NACC3	capitalOrders		8/25/2016	5:20:04	2016-25-08	8:21:06	0.347986	Thursday	4	19	2016-25-8 8:21:06	19
NACC3	capitalOrders		8/18/2016	5:20:05	2016-18-08	8:22:34	0.349005	Thursday	4	19	2016-18-8 8:22:34	14
NACC3	capitalOrders		8/19/2016	5:20:05	2016-19-08	8:20:59	0.347905	Friday	5	19	2016-19-8 8:20:59	15
NACC3	capitalOrders		8/5/2016	5:20:06	2016-05-08	8:21:16	0.348102	Friday	5	19	2016-08-05 08:21	5
NACC3	capitalOrders		8/8/2016	5:20:07	2016-08-08	8:22:03	0.348646	Monday	1	19	2016-08-08 08:22	6
NACC3	capitalOrders		8/2/2016	5:21:01	2016-02-08	8:23:14	0.349468	Tuesday	2	19	2016-08-02 08:23	2
NACC3	capitalOrders		9/1/2016	5:21:01	2016-01-09	8:22:22	0.348866	Thursday	4	19	2016-09-01 08:22	24
NACC3	capitalOrders		9/23/2016	5:21:01	2016-23-09	8:22:13	0.348762	Friday	5	19	2016-23-9 8:22:13	40
NACC3	capitalOrders		9/16/2016	5:21:04	2016-16-09	8:22:07	0.348692	Friday	5	19	2016-16-9 8:22:07	35
NACC3	capitalOrders		9/7/2016	6:20:01	2016-07-09	9:21:28	0.389907	Wednesday	3	19	2016-09-07 09:21	28
NACC3	capitalOrders		9/9/2016	6:20:03	2016-09-09	9:22:33	0.39066	Friday	5	19	2016-09-09 09:22	30
NACC3	capitalOrders		8/9/2016	6:20:04	2016-09-08	9:22:32	0.390648	Tuesday	2	19	2016-08-09 09:22	7
NACC3	capitalOrders		9/14/2016	6:20:04	2016-14-09	9:21:08	0.389676	Wednesday	3	19	2016-14-9 9:21:08	33
NACC3	capitalOrders		8/4/2016	6:20:05	2016-04-08	9:20:30	0.389236	Thursday	4	19	2016-08-04 09:20	4
NACC3	capitalOrders		8/16/2016	6:20:05	2016-16-08	9:21:49	0.39015	Tuesday	2	19	2016-16-8 9:21:49	12
NACC3	capitalOrders		9/19/2016	6:20:05	2016-19-09	9:22:12	0.390417	Monday	1	19	2016-19-9 9:22:12	36
NACC3	capitalOrders		8/15/2016	6:20:06	2016-15-08	9:21:00	0.389583	Monday	1	19	2016-15-8 9:21:00	11
NACC3	capitalOrders		8/30/2016	6:21:02	2016-30-08	9:23:26	0.391273	Tuesday	2	19	2016-30-8 9:23:26	22
NACC3	capitalOrders		9/21/2016	6:21:02	2016-21-09	9:23:15	0.391146	Wednesday	3	19	2016-21-9 9:23:15	38
NACC3	capitalOrders		8/7/2016	18:21:01	2016-07-08	21:23:49	0.891539	Sunday	7	19	2016-08-07 21:23	#N/A
NACC3	capitalOrders		8/14/2016	18:21:01	2016-14-08	21:22:50	0.890856	Sunday	7	19	2016-14-8 21:22:50	#N/A
NACC3	capitalOrders		8/21/2016	18:21:01	2016-21-08	21:22:54	0.890903	Sunday	7	19	2016-21-8 21:22:54	#N/A
NACC3	capitalOrders		9/25/2016	18:21:01	2016-25-09	21:23:43	0.89147	Sunday	7	19	2016-25-9 21:23:43	#N/A
NACC3	capitalOrders		9/4/2016	18:21:02	2016-04-09	21:21:59	0.890266	Sunday	7	19	2016-09-04 21:21	#N/A
NACC3	capitalOrders		9/18/2016	19:20:04	2016-18-09	22:21:39	0.931701	Sunday	7	19	2016-18-9 22:21:39	#N/A
NACC3	capitalOrders		9/11/2016	19:20:05	2016-11-09	22:21:36	0.931667	Sunday	7	19	2016-09-11 22:21	#N/A
NACC3	capitalOrders		8/28/2016	19:20:06	2016-28-08	22:22:41	0.932419	Sunday	7	19	2016-28-8 22:22:41	#N/A
NACC3	capitalOrders		9/5/2016	4:20:23	2016-05-09	7:22:29	0.30728	Monday	1	19	2016-09-05 07:22	26
NACC3	capitalOrders		8/17/2016	4:21:01	2016-17-08	7:22:07	0.307025	Wednesday	3	19	2016-17-8 7:22:07	13
NACC3	capitalOrders		9/2/2016	4:21:01	2016-02-09	7:22:43	0.307442	Friday	5	19	2016-09-02 07:22	25
NACC3	capitalOrders		9/8/2016	4:21:01	2016-08-09	7:21:39	0.306701	Thursday	4	19	2016-09-08 07:21	29
NACC3	capitalOrders		8/11/2016	4:21:02	2016-11-08	7:22:01	0.306956	Thursday	4	19	2016-08-11 07:22	9
NACC3	capitalOrders		8/31/2016	4:21:02	2016-31-08	7:22:05	0.307002	Wednesday	3	19	2016-31-8 7:22:05	23
NACC3	capitalOrders		9/13/2016	4:21:08	2016-13-09	7:22:31	0.307303	Tuesday	2	19	2016-13-9 7:22:31	32
NACC3	capitalOrders		9/12/2016	4:21:10	2016-12-09	7:23:34	0.308032	Monday	1	19	2016-09-12 07:23	31
NACC3	capitalOrders		8/29/2016	4:21:13	2016-29-08	8:19:09	0.346632	Monday	1	19	2016-29-8 8:19:09	21
NACC3	capitalOrders		8/23/2016	4:21:21	2016-23-08	7:23:51	0.308229	Tuesday	2	19	2016-23-8 7:23:51	17
NACC3	capitalOrders		9/6/2016	4:21:25	2016-06-09	7:22:39	0.307396	Tuesday	2	19	2016-09-06 07:22	27
NACC3	capitalOrders		8/1/2016	5:20:04	2016-01-08	8:22:05	0.348669	Monday	1	19	2016-08-01 08:22	1
NACC3	capitalOrders		8/12/2016	5:20:04	2016-12-08	8:21:09	0.348021	Friday	5	19	2016-08-12 08:21	10
NACC3	capitalOrders		8/24/2016	5:20:06	2016-24-08	8:22:17	0.348808	Wednesday	3	19	2016-24-8 8:22:17	18
NACC3	capitalOrders		9/15/2016	5:20:06	2016-15-09	8:21:31	0.348275	Thursday	4	19	2016-15-9 8:21:31	34
NACC3	capitalOrders		8/22/2016	5:20:07	2016-22-08	8:21:29	0.348252	Monday	1	19	2016-22-8 8:21:29	16
NACC3	capitalOrders		8/5/2016	5:21:01	2016-05-08	8:23:16	0.349491	Friday	5	19	2016-08-05 08:23	5
NACC3	capitalOrders		8/3/2016	5:21:02	2016-03-08	8:21:53	0.34853	Wednesday	3	19	2016-08-03 08:21	3
NACC3	capitalOrders		8/10/2016	5:21:02	2016-10-08	8:23:32	0.349676	Wednesday	3	19	2016-08-10 08:23	8
NACC3	capitalOrders		9/22/2016	5:21:02	2016-22-09	8:23:36	0.349722	Thursday	4	19	2016-22-9 8:23:36	39
NACC3	capitalOrders		8/19/2016	5:21:04	2016-19-08	8:22:59	0.349294	Friday	5	19	2016-19-8 8:22:59	15
NACC3	capitalOrders		8/2/2016	6:20:03	2016-02-08	9:20:52	0.389491	Tuesday	2	19	2016-08-02 09:20	2
NACC3	capitalOrders		9/1/2016	6:20:03	2016-01-09	9:22:25	0.390567	Thursday	4	19	2016-09-01 09:22	24
NACC3	capitalOrders		9/16/2016	6:20:05	2016-16-09	9:22:12	0.390417	Friday	5	19	2016-16-9 9:22:12	35
NACC3	capitalOrders		9/20/2016	6:20:05	2016-20-09	9:20:43	0.389387	Tuesday	2	19	2016-20-9 9:20:43	37
NACC3	capitalOrders		9/23/2016	6:20:05	2016-23-09	9:22:17	0.390475	Friday	5	19	2016-23-9 9:22:17	40
NACC3	capitalOrders		8/26/2016	6:20:06	2016-26-08	9:21:30	0.389931	Friday	5	19	2016-26-8 9:21:30	20
NACC3	capitalOrders		8/25/2016	6:21:01	2016-25-08	9:22:40	0.390741	Thursday	4	19	2016-25-8 9:22:40	19
NACC3	capitalOrders		9/7/2016	6:21:01	2016-07-09	9:23:29	0.391308	Wednesday	3	19	2016-09-07 09:23	28
NACC3	capitalOrders		9/14/2016	6:21:01	2016-14-09	9:23:09	0.391076	Wednesday	3	19	2016-14-9 9:23:09	33
NACC3	capitalOrders		9/19/2016	6:21:01	2016-19-09	9:22:12	0.390417	Monday	1	19	2016-19-9 9:22:12	36
NACC3	capitalOrders		8/4/2016	6:21:02	2016-04-08	9:22:30	0.390625	Thursday	4	19	2016-08-04 09:22	4
NACC3	capitalOrders		8/8/2016	6:21:02	2016-08-08	9:22:08	0.39037	Monday	1	19	2016-08-08 09:22	6
NACC3	capitalOrders		8/9/2016	6:21:02	2016-09-08	9:22:32	0.390648	Tuesday	2	19	2016-08-09 09:22	7
NACC3	capitalOrders		8/15/2016	6:21:02	2016-15-08	9:23:01	0.390984	Monday	1	19	2016-15-8 9:23:01	11
NACC3	capitalOrders		8/16/2016	6:21:02	2016-16-08	9:23:50	0.391551	Tuesday	2	19	2016-16-8 9:23:50	12
NACC3	capitalOrders		8/18/2016	6:21:02	2016-18-08	9:22:39	0.390729	Thursday	4	19	2016-18-8 9:22:39	14
NACC3	capitalOrders		9/9/2016	7:20:03	2016-09-09	10:22:38	0.432384	Friday	5	19	2016-09-09 10:22	30
NACC3	capitalOrders		8/30/2016	7:20:05	2016-30-08	10:21:31	0.431609	Tuesday	2	19	2016-30-8 10:21:31	22
NACC3	capitalOrders		9/21/2016	7:20:05	2016-21-09	10:21:20	0.431481	Wednesday	3	19	2016-21-9 10:21:20	38
NACC3	capitalOrders		8/14/2016	19:20:04	2016-14-08	22:22:53	0.932558	Sunday	7	19	2016-14-8 22:22:53	#N/A
NACC3	capitalOrders		8/21/2016	19:20:04	2016-21-08	22:20:57	0.931215	Sunday	7	19	2016-21-8 22:20:57	#N/A
NACC3	capitalOrders		9/4/2016	19:20:04	2016-04-09	22:22:02	0.931968	Sunday	7	19	2016-09-04 22:22	#N/A
NACC3	capitalOrders		8/7/2016	19:20:05	2016-07-08	22:21:53	0.931863	Sunday	7	19	2016-08-07 22:21	#N/A
NACC3	capitalOrders		9/25/2016	19:20:05	2016-25-09	22:21:44	0.931759	Sunday	7	19	2016-25-9 22:21:44	#N/A
NACC3	capitalOrders		8/28/2016	19:21:01	2016-28-08	22:22:41	0.932419	Sunday	7	19	2016-28-8 22:22:41	#N/A
NACC3	capitalOrders		9/11/2016	19:21:01	2016-11-09	22:21:36	0.931667	Sunday	7	19	2016-09-11 22:21	#N/A
NACC3	capitalOrders		9/18/2016	19:21:01	2016-18-09	22:21:39	0.931701	Sunday	7	19	2016-18-9 22:21:39	#N/A
NACC3	capitalOrders		9/5/2016	4:21:14	2016-05-09	7:22:29	0.30728	Monday	1	19	2016-09-05 07:22	26
NACC3	capitalOrders		9/8/2016	5:20:03	2016-08-09	8:21:41	0.348391	Thursday	4	19	2016-09-08 08:21	29
NACC3	capitalOrders		9/12/2016	5:20:04	2016-12-09	8:21:36	0.348333	Monday	1	19	2016-09-12 08:21	31
NACC3	capitalOrders		8/11/2016	5:20:06	2016-11-08	8:22:06	0.348681	Thursday	4	19	2016-08-11 08:22	9
NACC3	capitalOrders		8/17/2016	5:21:01	2016-17-08	8:22:09	0.348715	Wednesday	3	19	2016-17-8 8:22:09	13
NACC3	capitalOrders		8/24/2016	5:21:01	2016-24-08	8:22:18	0.348819	Wednesday	3	19	2016-24-8 8:22:18	18
NACC3	capitalOrders		9/2/2016	5:21:01	2016-02-09	8:22:45	0.349132	Friday	5	19	2016-09-02 08:22	25
NACC3	capitalOrders		9/15/2016	5:21:01	2016-15-09	8:23:32	0.349676	Thursday	4	19	2016-15-9 8:23:32	34
NACC3	capitalOrders		8/12/2016	5:21:02	2016-12-08	8:23:09	0.34941	Friday	5	19	2016-08-12 08:23	10
NACC3	capitalOrders		8/31/2016	6:20:02	2016-31-08	9:21:42	0.390069	Wednesday	3	19	2016-31-8 9:21:42	23
NACC3	capitalOrders		8/23/2016	6:20:03	2016-23-08	9:22:00	0.390278	Tuesday	2	19	2016-23-8 9:22:00	17
NACC3	capitalOrders		9/13/2016	6:20:03	2016-13-09	9:22:07	0.390359	Tuesday	2	19	2016-13-9 9:22:07	32
NACC3	capitalOrders		9/6/2016	6:20:04	2016-06-09	9:20:45	0.38941	Tuesday	2	19	2016-09-06 09:20	27
NACC3	capitalOrders		8/29/2016	6:20:05	2016-29-08	9:22:43	0.390775	Monday	1	19	2016-29-8 9:22:43	21
NACC3	capitalOrders		8/1/2016	6:20:06	2016-01-08	9:22:10	0.390394	Monday	1	19	2016-08-01 09:22	1
NACC3	capitalOrders		8/10/2016	6:20:06	2016-10-08	9:21:10	0.389699	Wednesday	3	19	2016-08-10 09:21	8
NACC3	capitalOrders		9/22/2016	6:20:06	2016-22-09	9:21:40	0.390046	Thursday	4	19	2016-22-9 9:21:40	39
NACC3	capitalOrders		8/19/2016	6:20:07	2016-19-08	9:21:03	0.389618	Friday	5	19	2016-19-8 9:21:03	15
NACC3	capitalOrders		8/5/2016	6:21:01	2016-05-08	9:23:21	0.391215	Friday	5	19	2016-08-05 09:23	5
NACC3	capitalOrders		8/26/2016	6:21:01	2016-26-08	9:21:30	0.389931	Friday	5	19	2016-26-8 9:21:30	20
NACC3	capitalOrders		9/1/2016	6:21:01	2016-01-09	9:22:26	0.390579	Thursday	4	19	2016-09-01 09:22	24
NACC3	capitalOrders		9/20/2016	6:21:01	2016-20-09	9:22:44	0.390787	Tuesday	2	19	2016-20-9 9:22:44	37
NACC3	capitalOrders		8/2/2016	6:21:02	2016-02-08	9:22:52	0.39088	Tuesday	2	19	2016-08-02 09:22	2
NACC3	capitalOrders		8/22/2016	6:21:02	2016-22-08	9:23:03	0.391007	Monday	1	19	2016-22-8 9:23:03	16
NACC3	capitalOrders		9/23/2016	6:21:02	2016-23-09	9:22:18	0.390486	Friday	5	19	2016-23-9 9:22:18	40
NACC3	capitalOrders		9/16/2016	6:21:04	2016-16-09	9:22:12	0.390417	Friday	5	19	2016-16-9 9:22:12	35
NACC3	capitalOrders		8/25/2016	7:20:02	2016-25-08	10:20:45	0.431076	Thursday	4	19	2016-25-8 10:20:45	19
NACC3	capitalOrders		9/7/2016	7:20:02	2016-07-09	10:21:03	0.431285	Wednesday	3	19	2016-09-07 10:21	28
NACC3	capitalOrders		8/3/2016	7:20:03	2016-03-08	10:21:33	0.431632	Wednesday	3	19	2016-08-03 10:21	3
NACC3	capitalOrders		8/18/2016	7:20:04	2016-18-08	10:22:43	0.432442	Thursday	4	19	2016-18-8 10:22:43	14
NACC3	capitalOrders		9/14/2016	7:20:04	2016-14-09	10:21:14	0.431412	Wednesday	3	19	2016-14-9 10:21:14	33
NACC3	capitalOrders		8/8/2016	7:20:05	2016-08-08	10:22:13	0.432095	Monday	1	19	2016-08-08 10:22	6
NACC3	capitalOrders		9/9/2016	7:21:01	2016-09-09	10:22:38	0.432384	Friday	5	19	2016-09-09 10:22	30
NACC3	capitalOrders		8/4/2016	7:21:02	2016-04-08	10:22:37	0.432373	Thursday	4	19	2016-08-04 10:22	4
NACC3	capitalOrders		8/15/2016	7:21:02	2016-15-08	10:23:04	0.432685	Monday	1	19	2016-15-8 10:23:04	11
NACC3	capitalOrders		9/19/2016	7:21:02	2016-19-09	10:22:16	0.43213	Monday	1	19	2016-19-9 10:22:16	36
NACC3	capitalOrders		8/16/2016	8:20:04	2016-16-08	11:21:28	0.473241	Tuesday	2	19	2016-16-8 11:21:28	12
NACC3	capitalOrders		8/9/2016	8:20:06	2016-09-08	11:20:40	0.472685	Tuesday	2	19	2016-08-09 11:20	7
NACC3	capitalOrders		8/30/2016	8:21:01	2016-30-08	11:23:36	0.474722	Tuesday	2	19	2016-30-8 11:23:36	22
NACC3	capitalOrders		9/21/2016	8:21:01	2016-21-09	11:23:24	0.474583	Wednesday	3	19	2016-21-9 11:23:24	38
NACC3	capitalOrders		8/7/2016	19:21:01	2016-07-08	22:23:54	0.933264	Sunday	7	19	2016-08-07 22:23	#N/A
NACC3	capitalOrders		8/14/2016	19:21:01	2016-14-08	22:22:54	0.932569	Sunday	7	19	2016-14-8 22:22:54	#N/A
NACC3	capitalOrders		9/25/2016	19:21:01	2016-25-09	22:23:44	0.933148	Sunday	7	19	2016-25-9 22:23:44	#N/A
NACC3	capitalOrders		8/21/2016	19:21:02	2016-21-08	22:22:57	0.932604	Sunday	7	19	2016-21-8 22:22:57	#N/A
NACC3	capitalOrders		9/11/2016	20:20:05	2016-11-09	23:21:38	0.973356	Sunday	7	19	2016-09-11 23:21	#N/A
NACC3	capitalOrders		9/18/2016	20:20:06	2016-18-09	23:21:41	0.973391	Sunday	7	19	2016-18-9 23:21:41	#N/A
NACC3	capitalOrders		8/28/2016	20:21:01	2016-28-08	23:22:43	0.974109	Sunday	7	19	2016-28-8 23:22:43	#N/A
NACC3	capitalOrders		9/4/2016	20:21:01	2016-04-09	23:22:03	0.973646	Sunday	7	19	2016-09-04 23:22	#N/A
NACC3	capitalOrders		9/8/2016	5:21:02	2016-08-09	8:53:44	0.370648	Thursday	4	19	2016-09-08 08:53	29
NACC3	capitalOrders		9/2/2016	6:20:02	2016-02-09	9:20:49	0.389456	Friday	5	19	2016-09-02 09:20	25
NACC3	capitalOrders		8/17/2016	6:20:03	2016-17-08	9:21:44	0.390093	Wednesday	3	19	2016-17-8 9:21:44	13
NACC3	capitalOrders		9/5/2016	6:20:04	2016-05-09	9:22:35	0.390683	Monday	1	19	2016-09-05 09:22	26
NACC3	capitalOrders		9/15/2016	6:20:05	2016-15-09	9:21:35	0.389988	Thursday	4	19	2016-15-9 9:21:35	34
NACC3	capitalOrders		8/1/2016	6:21:01	2016-01-08	9:22:10	0.390394	Monday	1	19	2016-08-01 09:22	1
NACC3	capitalOrders		8/11/2016	6:21:01	2016-11-08	9:22:11	0.390405	Thursday	4	19	2016-08-11 09:22	9
NACC3	capitalOrders		8/23/2016	6:21:01	2016-23-08	9:22:00	0.390278	Tuesday	2	19	2016-23-8 9:22:00	17
NACC3	capitalOrders		8/31/2016	6:21:01	2016-31-08	9:21:42	0.390069	Wednesday	3	19	2016-31-8 9:21:42	23
NACC3	capitalOrders		9/12/2016	6:21:01	2016-12-09	9:21:40	0.390046	Monday	1	19	2016-09-12 09:21	31
NACC3	capitalOrders		8/12/2016	6:21:02	2016-12-08	9:23:13	0.391123	Friday	5	19	2016-08-12 09:23	10
NACC3	capitalOrders		8/24/2016	6:21:02	2016-24-08	9:22:22	0.390532	Wednesday	3	19	2016-24-8 9:22:22	18
NACC3	capitalOrders		8/29/2016	6:21:02	2016-29-08	9:22:43	0.390775	Monday	1	19	2016-29-8 9:22:43	21
NACC3	capitalOrders		9/13/2016	6:21:02	2016-13-09	9:22:07	0.390359	Tuesday	2	19	2016-13-9 9:22:07	32
NACC3	capitalOrders		9/22/2016	6:21:02	2016-22-09	9:23:40	0.391435	Thursday	4	19	2016-22-9 9:23:40	39
NACC3	capitalOrders		8/19/2016	6:21:04	2016-19-08	9:23:03	0.391007	Friday	5	19	2016-19-8 9:23:03	15
NACC3	capitalOrders		9/6/2016	6:21:05	2016-06-09	9:22:45	0.390799	Tuesday	2	19	2016-09-06 09:22	27
NACC3	capitalOrders		8/5/2016	7:20:02	2016-05-08	10:21:25	0.431539	Friday	5	19	2016-08-05 10:21	5
NACC3	capitalOrders		9/1/2016	7:20:03	2016-01-09	10:22:30	0.432292	Thursday	4	19	2016-09-01 10:22	24
NACC3	capitalOrders		8/22/2016	7:20:04	2016-22-08	10:21:07	0.431331	Monday	1	19	2016-22-8 10:21:07	16
NACC3	capitalOrders		9/23/2016	7:20:05	2016-23-09	10:22:22	0.432199	Friday	5	19	2016-23-9 10:22:22	40
NACC3	capitalOrders		8/3/2016	7:21:01	2016-03-08	10:21:34	0.431644	Wednesday	3	19	2016-08-03 10:21	3
NACC3	capitalOrders		8/10/2016	7:21:01	2016-10-08	10:23:15	0.432813	Wednesday	3	19	2016-08-10 10:23	8
NACC3	capitalOrders		8/26/2016	7:21:01	2016-26-08	10:23:34	0.433032	Friday	5	19	2016-26-8 10:23:34	20
NACC3	capitalOrders		8/2/2016	7:21:02	2016-02-08	10:22:58	0.432616	Tuesday	2	19	2016-08-02 10:22	2
NACC3	capitalOrders		8/8/2016	7:21:02	2016-08-08	10:22:13	0.432095	Monday	1	19	2016-08-08 10:22	6
NACC3	capitalOrders		8/18/2016	7:21:02	2016-18-08	10:22:43	0.432442	Thursday	4	19	2016-18-8 10:22:43	14
NACC3	capitalOrders		8/25/2016	7:21:02	2016-25-08	10:22:45	0.432465	Thursday	4	19	2016-25-8 10:22:45	19
NACC3	capitalOrders		9/7/2016	7:21:02	2016-07-09	10:23:03	0.432674	Wednesday	3	19	2016-09-07 10:23	28
NACC3	capitalOrders		9/14/2016	7:21:02	2016-14-09	10:23:14	0.432801	Wednesday	3	19	2016-14-9 10:23:14	33
NACC3	capitalOrders		9/20/2016	7:21:02	2016-20-09	10:22:48	0.4325	Tuesday	2	19	2016-20-9 10:22:48	37
NACC3	capitalOrders		8/15/2016	8:20:01	2016-15-08	11:21:08	0.473009	Monday	1	19	2016-15-8 11:21:08	11
NACC3	capitalOrders		8/4/2016	8:20:03	2016-04-08	11:20:42	0.472708	Thursday	4	19	2016-08-04 11:20	4
NACC3	capitalOrders		9/9/2016	8:20:04	2016-09-09	11:22:41	0.474086	Friday	5	19	2016-09-09 11:22	30
NACC3	capitalOrders		9/16/2016	8:20:04	2016-16-09	11:22:20	0.473843	Friday	5	19	2016-16-9 11:22:20	35
NACC3	capitalOrders		9/19/2016	8:20:05	2016-19-09	11:22:21	0.473854	Monday	1	19	2016-19-9 11:22:21	36
NACC3	capitalOrders		8/9/2016	8:21:01	2016-09-08	11:22:41	0.474086	Tuesday	2	19	2016-08-09 11:22	7
NACC3	capitalOrders		8/16/2016	8:21:02	2016-16-08	11:21:28	0.473241	Tuesday	2	19	2016-16-8 11:21:28	12
NACC3	capitalOrders		9/21/2016	9:20:04	2016-21-09	12:21:29	0.514919	Wednesday	3	19	2016-21-9 12:21:29	38
NACC3	capitalOrders		8/30/2016	9:20:07	2016-30-08	12:21:38	0.515023	Tuesday	2	19	2016-30-8 12:21:38	22
NACC3	capitalOrders		8/14/2016	20:20:05	2016-14-08	23:20:56	0.97287	Sunday	7	19	2016-14-8 23:20:56	#N/A
NACC3	capitalOrders		9/25/2016	20:20:05	2016-25-09	23:21:16	0.973102	Sunday	7	19	2016-25-9 23:21:16	#N/A
NACC3	capitalOrders		8/7/2016	20:21:01	2016-07-08	23:23:56	0.974954	Sunday	7	19	2016-08-07 23:23	#N/A
NACC3	capitalOrders		9/11/2016	20:21:01	2016-11-09	23:23:39	0.974757	Sunday	7	19	2016-09-11 23:23	#N/A
NACC3	capitalOrders		9/18/2016	20:21:01	2016-18-09	23:21:41	0.973391	Sunday	7	19	2016-18-9 23:21:41	#N/A
NACC3	capitalOrders		8/17/2016	6:21:01	2016-17-08	9:21:44	0.390093	Wednesday	3	19	2016-17-8 9:21:44	13
NACC3	capitalOrders		9/2/2016	6:21:02	2016-02-09	9:22:49	0.390845	Friday	5	19	2016-09-02 09:22	25
NACC3	capitalOrders		9/5/2016	6:21:02	2016-05-09	9:22:35	0.390683	Monday	1	19	2016-09-05 09:22	26
NACC3	capitalOrders		9/8/2016	6:21:02	2016-08-09	9:23:47	0.391516	Thursday	4	19	2016-09-08 09:23	29
NACC3	capitalOrders		9/15/2016	6:21:02	2016-15-09	9:23:36	0.391389	Thursday	4	19	2016-15-9 9:23:36	34
NACC3	capitalOrders		8/23/2016	7:20:03	2016-23-08	10:22:04	0.431991	Tuesday	2	19	2016-23-8 10:22:04	17
NACC3	capitalOrders		8/31/2016	7:20:03	2016-31-08	10:21:46	0.431782	Wednesday	3	19	2016-31-8 10:21:46	23
NACC3	capitalOrders		8/12/2016	7:20:04	2016-12-08	10:21:18	0.431458	Friday	5	19	2016-08-12 10:21	10
NACC3	capitalOrders		8/24/2016	7:20:04	2016-24-08	10:22:27	0.432257	Wednesday	3	19	2016-24-8 10:22:27	18
NACC3	capitalOrders		9/12/2016	7:20:04	2016-12-09	10:21:45	0.431771	Monday	1	19	2016-09-12 10:21	31
NACC3	capitalOrders		9/13/2016	7:20:04	2016-14-09	10:42:48	0.446389	Wednesday	3	19	2016-14-9 10:42:48	33
NACC3	capitalOrders		8/11/2016	7:20:05	2016-11-08	10:22:15	0.432118	Thursday	4	19	2016-08-11 10:22	9
NACC3	capitalOrders		8/1/2016	7:21:01	2016-01-08	10:22:15	0.432118	Monday	1	19	2016-08-01 10:22	1
NACC3	capitalOrders		8/5/2016	7:21:01	2016-05-08	10:23:26	0.43294	Friday	5	19	2016-08-05 10:23	5
NACC3	capitalOrders		9/1/2016	7:21:01	2016-01-09	10:22:31	0.432303	Thursday	4	19	2016-09-01 10:22	24
NACC3	capitalOrders		9/22/2016	7:21:01	2016-22-09	10:21:46	0.431782	Thursday	4	19	2016-22-9 10:21:46	39
NACC3	capitalOrders		8/10/2016	8:20:02	2016-10-08	11:21:19	0.473137	Wednesday	3	19	2016-08-10 11:21	8
NACC3	capitalOrders		8/19/2016	8:20:02	2016-19-08	11:21:11	0.473044	Friday	5	19	2016-19-8 11:21:11	15
NACC3	capitalOrders		8/25/2016	8:20:02	2016-25-08	11:20:48	0.472778	Thursday	4	19	2016-25-8 11:20:48	19
NACC3	capitalOrders		9/6/2016	8:20:02	2016-06-09	11:20:53	0.472836	Tuesday	2	19	2016-09-06 11:20	27
NACC3	capitalOrders		8/29/2016	8:20:03	2016-29-08	11:22:50	0.47419	Monday	1	19	2016-29-8 11:22:50	21
NACC3	capitalOrders		9/7/2016	8:20:03	2016-07-09	11:21:06	0.472986	Wednesday	3	19	2016-09-07 11:21	28
NACC3	capitalOrders		8/2/2016	8:20:04	2016-02-08	11:21:02	0.47294	Tuesday	2	19	2016-08-02 11:21	2
NACC3	capitalOrders		8/3/2016	8:20:04	2016-03-08	11:21:37	0.473345	Wednesday	3	19	2016-08-03 11:21	3
NACC3	capitalOrders		8/22/2016	8:20:04	2016-22-08	11:21:11	0.473044	Monday	1	19	2016-22-8 11:21:11	16
NACC3	capitalOrders		8/8/2016	8:20:05	2016-08-08	11:21:47	0.473461	Monday	1	19	2016-08-08 11:21	6
NACC3	capitalOrders		9/23/2016	8:20:05	2016-23-09	11:22:26	0.473912	Friday	5	19	2016-23-9 11:22:26	40
NACC3	capitalOrders		8/18/2016	8:20:06	2016-18-08	11:20:46	0.472755	Thursday	4	19	2016-18-8 11:20:46	14
NACC3	capitalOrders		8/26/2016	8:20:06	2016-26-08	11:21:37	0.473345	Friday	5	19	2016-26-8 11:21:37	20
NACC3	capitalOrders		9/20/2016	8:20:06	2016-20-09	11:20:53	0.472836	Tuesday	2	19	2016-20-9 11:20:53	37
NACC3	capitalOrders		9/9/2016	8:21:02	2016-09-09	11:22:41	0.474086	Friday	5	19	2016-09-09 11:22	30
NACC3	capitalOrders		9/14/2016	8:21:02	2016-14-09	11:22:50	0.47419	Wednesday	3	19	2016-14-9 11:22:50	33
NACC3	capitalOrders		9/16/2016	8:21:02	2016-16-09	11:22:21	0.473854	Friday	5	19	2016-16-9 11:22:21	35
NACC3	capitalOrders		9/19/2016	8:21:02	2016-19-09	11:22:22	0.473866	Monday	1	19	2016-19-9 11:22:22	36
NACC3	capitalOrders		8/15/2016	9:20:03	2016-15-08	12:21:11	0.514711	Monday	1	19	2016-15-8 12:21:11	11
NACC3	capitalOrders		8/4/2016	9:21:02	2016-04-08	12:22:46	0.51581	Thursday	4	19	2016-08-04 12:22	4
NACC3	capitalOrders		8/9/2016	9:21:02	2016-09-08	12:22:45	0.515799	Tuesday	2	19	2016-08-09 12:22	7
NACC3	capitalOrders		8/16/2016	9:21:02	2016-16-08	12:23:33	0.516354	Tuesday	2	19	2016-16-8 12:23:33	12
NACC3	capitalOrders		8/30/2016	9:21:02	2016-30-08	12:23:39	0.516424	Tuesday	2	19	2016-30-8 12:23:39	22
NACC3	capitalOrders		9/21/2016	9:21:02	2016-21-09	12:23:29	0.516308	Wednesday	3	19	2016-21-9 12:23:29	38
NACC3	capitalOrders		8/14/2016	20:21:01	2016-14-08	23:22:57	0.974271	Sunday	7	19	2016-14-8 23:22:57	#N/A
NACC3	capitalOrders		9/25/2016	20:21:01	2016-25-09	23:23:17	0.974502	Sunday	7	19	2016-25-9 23:23:17	#N/A
NACC3	capitalOrders		9/2/2016	7:20:03	2016-02-09	10:22:54	0.432569	Friday	5	19	2016-09-02 10:22	25
NACC3	capitalOrders		9/5/2016	7:20:04	2016-05-09	10:22:08	0.432037	Monday	1	19	2016-09-05 10:22	26
NACC3	capitalOrders		9/8/2016	7:20:05	2016-08-09	10:21:53	0.431863	Thursday	4	19	2016-09-08 10:21	29
NACC3	capitalOrders		8/17/2016	7:20:06	2016-17-08	10:21:49	0.431817	Wednesday	3	19	2016-17-8 10:21:49	13
NACC3	capitalOrders		8/11/2016	7:21:01	2016-11-08	10:22:16	0.43213	Thursday	4	19	2016-08-11 10:22	9
NACC3	capitalOrders		8/23/2016	7:21:01	2016-23-08	10:22:05	0.432002	Tuesday	2	19	2016-23-8 10:22:05	17
NACC3	capitalOrders		8/24/2016	7:21:01	2016-24-08	10:22:28	0.432269	Wednesday	3	19	2016-24-8 10:22:28	18
NACC3	capitalOrders		8/31/2016	7:21:01	2016-31-08	10:23:47	0.433183	Wednesday	3	19	2016-31-8 10:23:47	23
NACC3	capitalOrders		9/12/2016	7:21:01	2016-12-09	10:21:45	0.431771	Monday	1	19	2016-09-12 10:21	31
NACC3	capitalOrders		9/15/2016	7:21:02	2016-15-09	10:23:41	0.433113	Thursday	4	19	2016-15-9 10:23:41	34
NACC3	capitalOrders		8/12/2016	7:21:03	2016-12-08	10:23:19	0.432859	Friday	5	19	2016-08-12 10:23	10
NACC3	capitalOrders		8/1/2016	8:20:02	2016-01-08	11:22:19	0.473831	Monday	1	19	2016-08-01 11:22	1
NACC3	capitalOrders		8/5/2016	8:20:02	2016-05-08	11:21:29	0.473252	Friday	5	19	2016-08-05 11:21	5
NACC3	capitalOrders		9/22/2016	8:20:02	2016-22-09	11:21:50	0.473495	Thursday	4	19	2016-22-9 11:21:50	39
NACC3	capitalOrders		9/1/2016	8:20:04	2016-01-09	11:22:35	0.474016	Thursday	4	19	2016-09-01 11:22	24
NACC3	capitalOrders		8/10/2016	8:21:01	2016-10-08	11:23:20	0.474537	Wednesday	3	19	2016-08-10 11:23	8
NACC3	capitalOrders		8/19/2016	8:21:01	2016-19-08	11:23:12	0.474444	Friday	5	19	2016-19-8 11:23:12	15
NACC3	capitalOrders		8/22/2016	8:21:01	2016-22-08	11:23:12	0.474444	Monday	1	19	2016-22-8 11:23:12	16
NACC3	capitalOrders		8/25/2016	8:21:01	2016-25-08	11:22:49	0.474178	Thursday	4	19	2016-25-8 11:22:49	19
NACC3	capitalOrders		8/29/2016	8:21:01	2016-29-08	11:22:51	0.474201	Monday	1	19	2016-29-8 11:22:51	21
NACC3	capitalOrders		9/13/2016	8:21:01	2016-13-09	11:22:16	0.473796	Tuesday	2	19	2016-13-9 11:22:16	32
NACC3	capitalOrders		9/23/2016	8:21:01	2016-23-09	11:22:27	0.473924	Friday	5	19	2016-23-9 11:22:27	40
NACC3	capitalOrders		8/2/2016	8:21:02	2016-02-08	11:23:03	0.47434	Tuesday	2	19	2016-08-02 11:23	2
NACC3	capitalOrders		8/3/2016	8:21:02	2016-03-08	11:23:38	0.474745	Wednesday	3	19	2016-08-03 11:23	3
NACC3	capitalOrders		8/26/2016	8:21:02	2016-26-08	11:23:38	0.474745	Friday	5	19	2016-26-8 11:23:38	20
NACC3	capitalOrders		9/6/2016	8:21:02	2016-06-09	11:22:54	0.474236	Tuesday	2	19	2016-09-06 11:22	27
NACC3	capitalOrders		9/7/2016	9:20:03	2016-07-09	12:21:11	0.514711	Wednesday	3	19	2016-09-07 12:21	28
NACC3	capitalOrders		9/14/2016	9:20:04	2016-14-09	12:20:54	0.514514	Wednesday	3	19	2016-14-9 12:20:54	33
NACC3	capitalOrders		8/8/2016	9:20:06	2016-08-08	12:21:53	0.515197	Monday	1	19	2016-08-08 12:21	6
NACC3	capitalOrders		9/16/2016	9:20:06	2016-16-09	12:22:26	0.515579	Friday	5	19	2016-16-9 12:22:26	35
NACC3	capitalOrders		8/15/2016	9:21:02	2016-15-08	12:23:12	0.516111	Monday	1	19	2016-15-8 12:23:12	11
NACC3	capitalOrders		8/18/2016	9:21:02	2016-18-08	12:22:50	0.515856	Thursday	4	19	2016-18-8 12:22:50	14
NACC3	capitalOrders		9/9/2016	9:21:02	2016-09-09	12:22:44	0.515787	Friday	5	19	2016-09-09 12:22	30
NACC3	capitalOrders		9/19/2016	9:21:02	2016-19-09	12:21:55	0.51522	Monday	1	19	2016-19-9 12:21:55	36
NACC3	capitalOrders		9/20/2016	9:21:02	2016-20-09	12:22:59	0.515961	Tuesday	2	19	2016-20-9 12:22:59	37
NACC3	capitalOrders		8/4/2016	10:20:02	2016-04-08	13:20:50	0.556134	Thursday	4	19	2016-08-04 13:20	4
NACC3	capitalOrders		8/9/2016	10:20:03	2016-09-08	13:20:49	0.556123	Tuesday	2	19	2016-08-09 13:20	7
NACC3	capitalOrders		9/21/2016	10:20:05	2016-21-09	13:21:33	0.556632	Wednesday	3	19	2016-21-9 13:21:33	38
NACC3	capitalOrders		8/16/2016	10:20:08	2016-16-08	13:21:36	0.556667	Tuesday	2	19	2016-16-8 13:21:36	12
NACC3	capitalOrders		8/30/2016	10:21:01	2016-30-08	13:23:42	0.558125	Tuesday	2	19	2016-30-8 13:23:42	22
NACC3	capitalOrders		8/17/2016	7:21:02	2016-17-08	10:21:49	0.431817	Wednesday	3	19	2016-17-8 10:21:49	13
NACC3	capitalOrders		9/5/2016	7:21:02	2016-05-09	10:22:08	0.432037	Monday	1	19	2016-09-05 10:22	26
NACC3	capitalOrders		8/31/2016	8:20:03	2016-31-08	11:21:50	0.473495	Wednesday	3	19	2016-31-8 11:21:50	23
NACC3	capitalOrders		9/2/2016	8:20:03	2016-02-09	11:20:59	0.472905	Friday	5	19	2016-09-02 11:20	25
NACC3	capitalOrders		9/12/2016	8:20:04	2016-12-09	11:21:49	0.473484	Monday	1	19	2016-09-12 11:21	31
NACC3	capitalOrders		9/15/2016	8:20:04	2016-15-09	11:21:45	0.473438	Thursday	4	19	2016-15-9 11:21:45	34
NACC3	capitalOrders		8/24/2016	8:20:05	2016-24-08	11:22:31	0.47397	Wednesday	3	19	2016-24-8 11:22:31	18
NACC3	capitalOrders		8/23/2016	8:20:06	2016-23-08	11:22:08	0.473704	Tuesday	2	19	2016-23-8 11:22:08	17
NACC3	capitalOrders		8/1/2016	8:21:01	2016-01-08	11:22:20	0.473843	Monday	1	19	2016-08-01 11:22	1
NACC3	capitalOrders		8/11/2016	8:21:01	2016-11-08	11:22:21	0.473854	Thursday	4	19	2016-08-11 11:22	9
NACC3	capitalOrders		9/8/2016	8:21:01	2016-08-09	11:21:56	0.473565	Thursday	4	19	2016-09-08 11:21	29
NACC3	capitalOrders		8/5/2016	8:21:02	2016-05-08	11:23:30	0.474653	Friday	5	19	2016-08-05 11:23	5
NACC3	capitalOrders		9/1/2016	8:21:02	2016-01-09	11:22:36	0.474028	Thursday	4	19	2016-09-01 11:22	24
NACC3	capitalOrders		9/22/2016	8:21:02	2016-22-09	11:21:50	0.473495	Thursday	4	19	2016-22-9 11:21:50	39
NACC3	capitalOrders		8/12/2016	8:21:03	2016-12-08	11:23:23	0.474572	Friday	5	19	2016-08-12 11:23	10
NACC3	capitalOrders		8/10/2016	9:20:02	2016-10-08	12:21:24	0.514861	Wednesday	3	19	2016-08-10 12:21	8
NACC3	capitalOrders		8/29/2016	9:20:03	2016-29-08	12:20:54	0.514514	Monday	1	19	2016-29-8 12:20:54	21
NACC3	capitalOrders		9/6/2016	9:20:03	2016-06-09	12:20:56	0.514537	Tuesday	2	19	2016-09-06 12:20	27
NACC3	capitalOrders		8/19/2016	9:20:04	2016-19-08	12:21:15	0.514757	Friday	5	19	2016-19-8 12:21:15	15
NACC3	capitalOrders		9/13/2016	9:20:05	2016-13-09	12:22:20	0.515509	Tuesday	2	19	2016-13-9 12:22:20	32
NACC3	capitalOrders		8/3/2016	9:20:07	2016-03-08	12:21:42	0.515069	Wednesday	3	19	2016-08-03 12:21	3
NACC3	capitalOrders		8/26/2016	9:20:08	2016-26-08	12:21:41	0.515058	Friday	5	19	2016-26-8 12:21:41	20
NACC3	capitalOrders		8/22/2016	9:20:11	2016-22-08	12:21:15	0.514757	Monday	1	19	2016-22-8 12:21:15	16
NACC3	capitalOrders		8/2/2016	9:21:02	2016-02-08	12:23:08	0.516065	Tuesday	2	19	2016-08-02 12:23	2
NACC3	capitalOrders		8/25/2016	9:21:02	2016-25-08	12:22:52	0.51588	Thursday	4	19	2016-25-8 12:22:52	19
NACC3	capitalOrders		9/7/2016	9:21:02	2016-07-09	12:23:12	0.516111	Wednesday	3	19	2016-09-07 12:23	28
NACC3	capitalOrders		9/14/2016	9:21:02	2016-14-09	12:22:55	0.515914	Wednesday	3	19	2016-14-9 12:22:55	33
NACC3	capitalOrders		9/16/2016	9:21:02	2016-16-09	12:22:26	0.515579	Friday	5	19	2016-16-9 12:22:26	35
NACC3	capitalOrders		9/23/2016	9:21:02	2016-23-09	12:22:30	0.515625	Friday	5	19	2016-23-9 12:22:30	40
NACC3	capitalOrders		8/8/2016	9:21:03	2016-08-08	12:21:53	0.515197	Monday	1	19	2016-08-08 12:21	6
NACC3	capitalOrders		9/9/2016	10:20:03	2016-09-09	13:22:49	0.557512	Friday	5	19	2016-09-09 13:22	30
NACC3	capitalOrders		9/20/2016	10:20:03	2016-20-09	13:20:32	0.555926	Tuesday	2	19	2016-20-9 13:20:32	37
NACC3	capitalOrders		8/15/2016	10:20:05	2016-15-08	13:21:17	0.556447	Monday	1	19	2016-15-8 13:21:17	11
NACC3	capitalOrders		9/19/2016	10:20:05	2016-19-09	13:21:59	0.556933	Monday	1	19	2016-19-9 13:21:59	36
NACC3	capitalOrders		8/18/2016	10:20:06	2016-18-08	13:22:24	0.557222	Thursday	4	19	2016-18-8 13:22:24	14
NACC3	capitalOrders		8/4/2016	10:21:02	2016-04-08	13:22:51	0.557535	Thursday	4	19	2016-08-04 13:22	4
NACC3	capitalOrders		8/9/2016	10:21:02	2016-09-08	13:22:49	0.557512	Tuesday	2	19	2016-08-09 13:22	7
NACC3	capitalOrders		8/16/2016	10:21:02	2016-16-08	13:21:36	0.556667	Tuesday	2	19	2016-16-8 13:21:36	12
NACC3	capitalOrders		8/30/2016	17:20:03	2016-30-08	20:21:34	0.84831	Tuesday	2	19	2016-30-8 20:21:34	22
NACC3	capitalOrders		9/21/2016	17:20:06	2016-21-09	20:21:27	0.848229	Wednesday	3	19	2016-21-9 20:21:27	38
NACC3	capitalOrders		8/24/2016	8:21:01	2016-24-08	11:22:32	0.473981	Wednesday	3	19	2016-24-8 11:22:32	18
NACC3	capitalOrders		8/31/2016	8:21:01	2016-31-08	11:23:51	0.474896	Wednesday	3	19	2016-31-8 11:23:51	23
NACC3	capitalOrders		8/17/2016	8:21:02	2016-17-08	11:21:54	0.473542	Wednesday	3	19	2016-17-8 11:21:54	13
NACC3	capitalOrders		8/23/2016	8:21:02	2016-23-08	11:22:09	0.473715	Tuesday	2	19	2016-23-8 11:22:09	17
NACC3	capitalOrders		9/2/2016	8:21:02	2016-02-09	11:33:01	0.481262	Friday	5	19	2016-09-02 11:33	25
NACC3	capitalOrders		9/12/2016	8:21:02	2016-12-09	11:23:50	0.474884	Monday	1	19	2016-09-12 11:23	31
NACC3	capitalOrders		9/15/2016	8:21:02	2016-15-09	11:23:46	0.474838	Thursday	4	19	2016-15-9 11:23:46	34
NACC3	capitalOrders		8/12/2016	9:20:02	2016-12-08	12:21:26	0.514884	Friday	5	19	2016-08-12 12:21	10
NACC3	capitalOrders		8/5/2016	9:20:03	2016-05-08	12:21:34	0.514977	Friday	5	19	2016-08-05 12:21	5
NACC3	capitalOrders		9/22/2016	9:20:03	2016-22-09	12:21:55	0.51522	Thursday	4	19	2016-22-9 12:21:55	39
NACC3	capitalOrders		8/11/2016	9:20:04	2016-11-08	12:22:32	0.515648	Thursday	4	19	2016-08-11 12:22	9
NACC3	capitalOrders		8/1/2016	9:20:05	2016-01-08	12:22:23	0.515544	Monday	1	19	2016-08-01 12:22	1
NACC3	capitalOrders		9/1/2016	9:20:05	2016-01-09	12:22:39	0.515729	Thursday	4	19	2016-09-01 12:22	24
NACC3	capitalOrders		9/5/2016	9:20:05	2016-05-09	12:22:15	0.515451	Monday	1	19	2016-09-05 12:22	26
NACC3	capitalOrders		9/8/2016	9:20:05	2016-08-09	12:22:00	0.515278	Thursday	4	19	2016-09-08 12:22	29
NACC3	capitalOrders		8/3/2016	9:21:02	2016-03-08	12:21:43	0.515081	Wednesday	3	19	2016-08-03 12:21	3
NACC3	capitalOrders		8/10/2016	9:21:02	2016-10-08	12:23:24	0.51625	Wednesday	3	19	2016-08-10 12:23	8
NACC3	capitalOrders		8/19/2016	9:21:02	2016-19-08	12:23:16	0.516157	Friday	5	19	2016-19-8 12:23:16	15
NACC3	capitalOrders		8/22/2016	9:21:02	2016-22-08	12:23:16	0.516157	Monday	1	19	2016-22-8 12:23:16	16
NACC3	capitalOrders		8/26/2016	9:21:02	2016-26-08	12:23:42	0.516458	Friday	5	19	2016-26-8 12:23:42	20
NACC3	capitalOrders		9/6/2016	9:21:02	2016-06-09	12:22:57	0.515938	Tuesday	2	19	2016-09-06 12:22	27
NACC3	capitalOrders		9/13/2016	9:21:02	2016-13-09	12:22:20	0.515509	Tuesday	2	19	2016-13-9 12:22:20	32
NACC3	capitalOrders		8/29/2016	9:21:03	2016-29-08	12:22:55	0.515914	Monday	1	19	2016-29-8 12:22:55	21
NACC3	capitalOrders		8/25/2016	10:20:03	2016-25-08	13:20:55	0.556192	Thursday	4	19	2016-25-8 13:20:55	19
NACC3	capitalOrders		9/7/2016	10:20:03	2016-07-09	13:21:15	0.556424	Wednesday	3	19	2016-09-07 13:21	28
NACC3	capitalOrders		9/23/2016	10:20:04	2016-23-09	13:22:34	0.557338	Friday	5	19	2016-23-9 13:22:34	40
NACC3	capitalOrders		8/2/2016	10:20:06	2016-02-08	13:21:11	0.556377	Tuesday	2	19	2016-08-02 13:21	2
NACC3	capitalOrders		9/14/2016	10:20:06	2016-14-09	13:20:58	0.556227	Wednesday	3	19	2016-14-9 13:20:58	33
NACC3	capitalOrders		8/18/2016	10:21:02	2016-18-08	13:22:25	0.557234	Thursday	4	19	2016-18-8 13:22:25	14
NACC3	capitalOrders		9/16/2016	10:21:02	2016-16-09	13:22:01	0.556956	Friday	5	19	2016-16-9 13:22:01	35
NACC3	capitalOrders		9/19/2016	10:21:02	2016-19-09	13:22:00	0.556944	Monday	1	19	2016-19-9 13:22:00	36
NACC3	capitalOrders		8/4/2016	17:20:03	2016-04-08	20:20:51	0.847813	Thursday	4	19	2016-08-04 20:20	4
NACC3	capitalOrders		8/8/2016	17:20:03	2016-08-08	20:22:30	0.848958	Monday	1	19	2016-08-08 20:22	6
NACC3	capitalOrders		8/15/2016	17:20:03	2016-15-08	20:21:09	0.848021	Monday	1	19	2016-15-8 20:21:09	11
NACC3	capitalOrders		8/9/2016	17:20:05	2016-09-08	20:21:17	0.848113	Tuesday	2	19	2016-08-09 20:21	7
NACC3	capitalOrders		8/16/2016	17:20:05	2016-16-08	20:22:01	0.848623	Tuesday	2	19	2016-16-8 20:22:01	12
NACC3	capitalOrders		9/20/2016	17:20:05	2016-20-09	20:20:58	0.847894	Tuesday	2	19	2016-20-9 20:20:58	37
NACC3	capitalOrders		9/9/2016	17:20:07	2016-09-09	20:22:40	0.849074	Friday	5	19	2016-09-09 20:22	30
NACC3	capitalOrders		8/30/2016	17:21:02	2016-30-08	20:23:34	0.849699	Tuesday	2	19	2016-30-8 20:23:34	22
NACC3	capitalOrders		9/21/2016	17:21:02	2016-21-09	20:23:27	0.849618	Wednesday	3	19	2016-21-9 20:23:27	38
NACC3	capitalOrders		8/31/2016	9:20:03	2016-31-08	12:21:55	0.51522	Wednesday	3	19	2016-31-8 12:21:55	23
NACC3	capitalOrders		8/17/2016	9:20:04	2016-17-08	12:21:57	0.515243	Wednesday	3	19	2016-17-8 12:21:57	13
NACC3	capitalOrders		9/2/2016	9:20:04	2016-02-09	12:21:04	0.51463	Friday	5	19	2016-09-02 12:21	25
NACC3	capitalOrders		9/12/2016	9:20:04	2016-12-09	12:21:56	0.515231	Monday	1	19	2016-09-12 12:21	31
NACC3	capitalOrders		9/15/2016	9:20:04	2016-15-09	12:21:49	0.51515	Thursday	4	19	2016-15-9 12:21:49	34
NACC3	capitalOrders		9/8/2016	9:21:01	2016-08-09	12:22:00	0.515278	Thursday	4	19	2016-09-08 12:22	29
NACC3	capitalOrders		8/1/2016	9:21:02	2016-01-08	12:22:23	0.515544	Monday	1	19	2016-08-01 12:22	1
NACC3	capitalOrders		8/5/2016	9:21:02	2016-05-08	12:23:34	0.516366	Friday	5	19	2016-08-05 12:23	5
NACC3	capitalOrders		8/11/2016	9:21:02	2016-11-08	12:22:32	0.515648	Thursday	4	19	2016-08-11 12:22	9
NACC3	capitalOrders		8/23/2016	9:21:02	2016-23-08	12:21:43	0.515081	Tuesday	2	19	2016-23-8 12:21:43	17
NACC3	capitalOrders		8/24/2016	9:21:02	2016-24-08	12:22:35	0.515683	Wednesday	3	19	2016-24-8 12:22:35	18
NACC3	capitalOrders		9/1/2016	9:21:02	2016-01-09	12:22:40	0.515741	Thursday	4	19	2016-09-01 12:22	24
NACC3	capitalOrders		9/5/2016	9:21:02	2016-05-09	12:22:16	0.515463	Monday	1	19	2016-09-05 12:22	26
NACC3	capitalOrders		9/22/2016	9:21:02	2016-22-09	12:21:55	0.51522	Thursday	4	19	2016-22-9 12:21:55	39
NACC3	capitalOrders		8/12/2016	9:21:03	2016-12-08	12:23:27	0.516285	Friday	5	19	2016-08-12 12:23	10
NACC3	capitalOrders		8/10/2016	10:20:03	2016-10-08	13:21:29	0.556586	Wednesday	3	19	2016-08-10 13:21	8
NACC3	capitalOrders		9/6/2016	10:20:03	2016-06-09	13:21:00	0.55625	Tuesday	2	19	2016-09-06 13:21	27
NACC3	capitalOrders		8/29/2016	10:20:06	2016-29-08	13:20:59	0.556238	Monday	1	19	2016-29-8 13:20:59	21
NACC3	capitalOrders		9/13/2016	10:20:07	2016-13-09	13:22:24	0.557222	Tuesday	2	19	2016-13-9 13:22:24	32
NACC3	capitalOrders		8/2/2016	10:21:02	2016-02-08	13:23:12	0.557778	Tuesday	2	19	2016-08-02 13:23	2
NACC3	capitalOrders		8/25/2016	10:21:02	2016-25-08	13:22:56	0.557593	Thursday	4	19	2016-25-8 13:22:56	19
NACC3	capitalOrders		8/26/2016	10:21:02	2016-26-08	13:23:45	0.55816	Friday	5	19	2016-26-8 13:23:45	20
NACC3	capitalOrders		9/7/2016	10:21:02	2016-07-09	13:23:16	0.557824	Wednesday	3	19	2016-09-07 13:23	28
NACC3	capitalOrders		9/23/2016	10:21:02	2016-23-09	13:22:34	0.557338	Friday	5	19	2016-23-9 13:22:34	40
NACC3	capitalOrders		8/3/2016	17:20:03	2016-03-08	20:22:21	0.848854	Wednesday	3	19	2016-08-03 20:22	3
NACC3	capitalOrders		8/19/2016	17:20:03	2016-19-08	20:21:13	0.848067	Friday	5	19	2016-19-8 20:21:13	15
NACC3	capitalOrders		8/18/2016	17:20:04	2016-18-08	20:22:49	0.849178	Thursday	4	19	2016-18-8 20:22:49	14
NACC3	capitalOrders		8/22/2016	17:20:04	2016-22-08	20:21:46	0.848449	Monday	1	19	2016-22-8 20:21:46	16
NACC3	capitalOrders		9/14/2016	17:20:05	2016-14-09	20:21:22	0.848171	Wednesday	3	19	2016-14-9 20:21:22	33
NACC3	capitalOrders		9/16/2016	17:20:05	2016-16-09	20:22:29	0.848947	Friday	5	19	2016-16-9 20:22:29	35
NACC3	capitalOrders		9/19/2016	17:20:05	2016-19-09	20:22:24	0.848889	Monday	1	19	2016-19-9 20:22:24	36
NACC3	capitalOrders		8/8/2016	17:21:01	2016-08-08	20:22:30	0.848958	Monday	1	19	2016-08-08 20:22	6
NACC3	capitalOrders		8/15/2016	17:21:01	2016-15-08	20:23:09	0.84941	Monday	1	19	2016-15-8 20:23:09	11
NACC3	capitalOrders		8/16/2016	17:21:01	2016-16-08	20:22:01	0.848623	Tuesday	2	19	2016-16-8 20:22:01	12
NACC3	capitalOrders		8/4/2016	17:21:02	2016-04-08	20:22:51	0.849201	Thursday	4	19	2016-08-04 20:22	4
NACC3	capitalOrders		8/9/2016	17:21:02	2016-09-08	20:23:17	0.849502	Tuesday	2	19	2016-08-09 20:23	7
NACC3	capitalOrders		9/9/2016	17:21:02	2016-09-09	20:22:40	0.849074	Friday	5	19	2016-09-09 20:22	30
NACC3	capitalOrders		9/20/2016	17:21:02	2016-20-09	20:22:58	0.849282	Tuesday	2	19	2016-20-9 20:22:58	37
NACC3	capitalOrders		8/30/2016	18:20:05	2016-30-08	21:21:36	0.89	Tuesday	2	19	2016-30-8 21:21:36	22
NACC3	capitalOrders		9/21/2016	19:20:05	2016-21-09	22:21:32	0.93162	Wednesday	3	19	2016-21-9 22:21:32	38
NACC3	capitalOrders		8/17/2016	9:21:02	2016-17-08	12:21:57	0.515243	Wednesday	3	19	2016-17-8 12:21:57	13
NACC3	capitalOrders		8/31/2016	9:21:02	2016-31-08	12:21:55	0.51522	Wednesday	3	19	2016-31-8 12:21:55	23
NACC3	capitalOrders		9/2/2016	9:21:02	2016-02-09	12:23:04	0.516019	Friday	5	19	2016-09-02 12:23	25
NACC3	capitalOrders		9/12/2016	9:21:02	2016-12-09	12:21:56	0.515231	Monday	1	19	2016-09-12 12:21	31
NACC3	capitalOrders		8/12/2016	10:20:02	2016-12-08	13:21:01	0.556262	Friday	5	19	2016-08-12 13:21	10
NACC3	capitalOrders		8/24/2016	10:20:04	2016-24-08	13:22:39	0.557396	Wednesday	3	19	2016-24-8 13:22:39	18
NACC3	capitalOrders		9/15/2016	10:20:04	2016-15-09	13:21:23	0.556516	Thursday	4	19	2016-15-9 13:21:23	34
NACC3	capitalOrders		8/11/2016	10:20:05	2016-11-08	13:22:36	0.557361	Thursday	4	19	2016-08-11 13:22	9
NACC3	capitalOrders		8/23/2016	10:20:05	2016-23-08	13:21:46	0.556782	Tuesday	2	19	2016-23-8 13:21:46	17
NACC3	capitalOrders		8/1/2016	10:20:06	2016-01-08	13:22:06	0.557014	Monday	1	19	2016-08-01 13:22	1
NACC3	capitalOrders		8/5/2016	10:20:06	2016-05-08	13:21:39	0.556701	Friday	5	19	2016-08-05 13:21	5
NACC3	capitalOrders		9/22/2016	10:20:07	2016-22-09	13:21:59	0.556933	Thursday	4	19	2016-22-9 13:21:59	39
NACC3	capitalOrders		9/13/2016	10:21:01	2016-13-09	13:22:24	0.557222	Tuesday	2	19	2016-13-9 13:22:24	32
NACC3	capitalOrders		9/1/2016	10:21:02	2016-01-09	13:22:44	0.557454	Thursday	4	19	2016-09-01 13:22	24
NACC3	capitalOrders		9/5/2016	10:21:02	2016-05-09	13:22:20	0.557176	Monday	1	19	2016-09-05 13:22	26
NACC3	capitalOrders		9/6/2016	10:21:02	2016-06-09	13:23:01	0.55765	Tuesday	2	19	2016-09-06 13:23	27
NACC3	capitalOrders		9/8/2016	10:21:02	2016-08-09	13:24:04	0.55838	Thursday	4	19	2016-09-08 13:24	29
NACC3	capitalOrders		8/10/2016	17:20:03	2016-10-08	20:49:33	0.867743	Wednesday	3	19	2016-08-10 20:49	8
NACC3	capitalOrders		8/25/2016	17:20:03	2016-25-08	20:21:19	0.848137	Thursday	4	19	2016-25-8 20:21:19	19
NACC3	capitalOrders		8/29/2016	17:20:05	2016-29-08	20:21:20	0.848148	Monday	1	19	2016-29-8 20:21:20	21
NACC3	capitalOrders		9/7/2016	17:20:05	2016-07-09	20:21:39	0.848368	Wednesday	3	19	2016-09-07 20:21	28
NACC3	capitalOrders		8/26/2016	17:20:06	2016-26-08	20:21:38	0.848356	Friday	5	19	2016-26-8 20:21:38	20
NACC3	capitalOrders		9/23/2016	17:20:06	2016-23-09	20:20:59	0.847905	Friday	5	19	2016-23-9 20:20:59	40
NACC3	capitalOrders		8/2/2016	17:20:08	2016-02-08	20:21:11	0.848044	Tuesday	2	19	2016-08-02 20:21	2
NACC3	capitalOrders		9/16/2016	17:21:01	2016-16-09	20:22:30	0.848958	Friday	5	19	2016-16-9 20:22:30	35
NACC3	capitalOrders		8/3/2016	17:21:02	2016-03-08	20:22:21	0.848854	Wednesday	3	19	2016-08-03 20:22	3
NACC3	capitalOrders		8/18/2016	17:21:02	2016-18-08	20:22:49	0.849178	Thursday	4	19	2016-18-8 20:22:49	14
NACC3	capitalOrders		8/19/2016	17:21:02	2016-19-08	20:23:13	0.849456	Friday	5	19	2016-19-8 20:23:13	15
NACC3	capitalOrders		8/22/2016	17:21:02	2016-22-08	20:23:46	0.849838	Monday	1	19	2016-22-8 20:23:46	16
NACC3	capitalOrders		9/14/2016	17:21:02	2016-14-09	20:23:23	0.849572	Wednesday	3	19	2016-14-9 20:23:23	33
NACC3	capitalOrders		9/19/2016	17:21:02	2016-19-09	20:22:24	0.848889	Monday	1	19	2016-19-9 20:22:24	36
NACC3	capitalOrders		8/8/2016	18:20:03	2016-08-08	21:22:33	0.89066	Monday	1	19	2016-08-08 21:22	6
NACC3	capitalOrders		8/4/2016	18:20:06	2016-04-08	21:22:54	0.890903	Thursday	4	19	2016-08-04 21:22	4
NACC3	capitalOrders		9/20/2016	18:20:06	2016-20-09	21:21:02	0.889606	Tuesday	2	19	2016-20-9 21:21:02	37
NACC3	capitalOrders		8/15/2016	18:20:11	2016-15-08	21:21:11	0.889711	Monday	1	19	2016-15-8 21:21:11	11
NACC3	capitalOrders		8/16/2016	18:21:01	2016-16-08	21:22:04	0.890324	Tuesday	2	19	2016-16-8 21:22:04	12
NACC3	capitalOrders		8/9/2016	19:20:02	2016-09-08	22:20:55	0.931192	Tuesday	2	19	2016-08-09 22:20	7
NACC3	capitalOrders		9/9/2016	19:20:04	2016-09-09	22:20:45	0.931076	Friday	5	19	2016-09-09 22:20	30
NACC3	capitalOrders		8/30/2016	19:21:01	2016-30-08	22:23:39	0.93309	Tuesday	2	19	2016-30-8 22:23:39	22
NACC3	capitalOrders		9/21/2016	19:21:06	2016-21-09	22:23:33	0.933021	Wednesday	3	19	2016-21-9 22:23:33	38
NACC3	capitalOrders		8/31/2016	10:20:03	2016-31-08	13:21:58	0.556921	Wednesday	3	19	2016-31-8 13:21:58	23
NACC3	capitalOrders		9/2/2016	10:20:05	2016-02-09	13:23:08	0.557731	Friday	5	19	2016-09-02 13:23	25
NACC3	capitalOrders		9/12/2016	10:20:05	2016-12-09	13:22:01	0.556956	Monday	1	19	2016-09-12 13:22	31
NACC3	capitalOrders		8/1/2016	10:21:02	2016-01-08	13:22:07	0.557025	Monday	1	19	2016-08-01 13:22	1
NACC3	capitalOrders		8/5/2016	10:21:02	2016-05-08	13:23:40	0.558102	Friday	5	19	2016-08-05 13:23	5
NACC3	capitalOrders		8/17/2016	10:21:02	2016-17-08	13:22:01	0.556956	Wednesday	3	19	2016-17-8 13:22:01	13
NACC3	capitalOrders		8/23/2016	10:21:02	2016-23-08	13:21:47	0.556794	Tuesday	2	19	2016-23-8 13:21:47	17
NACC3	capitalOrders		9/15/2016	10:21:02	2016-15-09	13:23:23	0.557905	Thursday	4	19	2016-15-9 13:23:23	34
NACC3	capitalOrders		9/22/2016	10:21:02	2016-22-09	13:21:59	0.556933	Thursday	4	19	2016-22-9 13:21:59	39
NACC3	capitalOrders		8/12/2016	10:21:04	2016-12-08	13:23:01	0.55765	Friday	5	19	2016-08-12 13:23	10
NACC3	capitalOrders		8/24/2016	17:20:03	2016-24-08	20:20:31	0.847581	Wednesday	3	19	2016-24-8 20:20:31	18
NACC3	capitalOrders		9/8/2016	17:20:03	2016-08-09	20:21:54	0.848542	Thursday	4	19	2016-09-08 20:21	29
NACC3	capitalOrders		8/11/2016	17:20:05	2016-11-08	20:20:39	0.847674	Thursday	4	19	2016-08-11 20:20	9
NACC3	capitalOrders		9/1/2016	17:20:05	2016-01-09	20:22:37	0.849039	Thursday	4	19	2016-09-01 20:22	24
NACC3	capitalOrders		9/13/2016	17:20:05	2016-13-09	20:22:51	0.849201	Tuesday	2	19	2016-13-9 20:22:51	32
NACC3	capitalOrders		9/6/2016	17:20:06	2016-06-09	20:20:51	0.847813	Tuesday	2	19	2016-09-06 20:20	27
NACC3	capitalOrders		9/5/2016	17:20:07	2016-05-09	20:22:40	0.849074	Monday	1	19	2016-09-05 20:22	26
NACC3	capitalOrders		8/2/2016	17:21:01	2016-02-08	20:23:12	0.849444	Tuesday	2	19	2016-08-02 20:23	2
NACC3	capitalOrders		8/25/2016	17:21:01	2016-25-08	20:23:19	0.849525	Thursday	4	19	2016-25-8 20:23:19	19
NACC3	capitalOrders		8/10/2016	17:21:02	2016-10-08	20:49:33	0.867743	Wednesday	3	19	2016-08-10 20:49	8
NACC3	capitalOrders		8/26/2016	17:21:02	2016-26-08	20:23:39	0.849757	Friday	5	19	2016-26-8 20:23:39	20
NACC3	capitalOrders		8/29/2016	17:21:02	2016-29-08	20:23:20	0.849537	Monday	1	19	2016-29-8 20:23:20	21
NACC3	capitalOrders		9/7/2016	17:21:02	2016-07-09	20:23:39	0.849757	Wednesday	3	19	2016-09-07 20:23	28
NACC3	capitalOrders		9/23/2016	17:21:02	2016-23-09	20:23:00	0.849306	Friday	5	19	2016-23-9 20:23:00	40
NACC3	capitalOrders		8/3/2016	18:20:03	2016-03-08	21:21:55	0.89022	Wednesday	3	19	2016-08-03 21:21	3
NACC3	capitalOrders		8/18/2016	18:20:05	2016-18-08	21:22:51	0.890868	Thursday	4	19	2016-18-8 21:22:51	14
NACC3	capitalOrders		8/19/2016	18:20:05	2016-19-08	21:21:16	0.889769	Friday	5	19	2016-19-8 21:21:16	15
NACC3	capitalOrders		9/14/2016	18:20:05	2016-14-09	21:21:25	0.889873	Wednesday	3	19	2016-14-9 21:21:25	33
NACC3	capitalOrders		9/16/2016	18:20:05	2016-16-09	21:22:33	0.89066	Friday	5	19	2016-16-9 21:22:33	35
NACC3	capitalOrders		9/19/2016	18:20:06	2016-19-09	21:22:27	0.89059	Monday	1	19	2016-19-9 21:22:27	36
NACC3	capitalOrders		8/8/2016	18:21:01	2016-08-08	21:22:33	0.89066	Monday	1	19	2016-08-08 21:22	6
NACC3	capitalOrders		8/15/2016	18:21:01	2016-15-08	21:23:11	0.8911	Monday	1	19	2016-15-8 21:23:11	11
NACC3	capitalOrders		8/4/2016	18:21:02	2016-04-08	21:22:54	0.890903	Thursday	4	19	2016-08-04 21:22	4
NACC3	capitalOrders		8/16/2016	19:20:03	2016-16-08	22:22:08	0.932037	Tuesday	2	19	2016-16-8 22:22:08	12
NACC3	capitalOrders		8/22/2016	19:20:04	2016-22-08	22:21:22	0.931505	Monday	1	19	2016-22-8 22:21:22	16
NACC3	capitalOrders		8/9/2016	19:21:01	2016-09-08	22:22:56	0.932593	Tuesday	2	19	2016-08-09 22:22	7
NACC3	capitalOrders		9/9/2016	19:21:01	2016-09-09	22:22:45	0.932465	Friday	5	19	2016-09-09 22:22	30
NACC3	capitalOrders		9/20/2016	19:21:01	2016-20-09	22:23:05	0.932697	Tuesday	2	19	2016-20-9 22:23:05	37
NACC3	capitalOrders		9/21/2016	20:20:05	2016-21-09	23:21:35	0.973322	Wednesday	3	19	2016-21-9 23:21:35	38
NACC3	capitalOrders		8/30/2016	20:20:08	2016-30-08	23:21:42	0.973403	Tuesday	2	19	2016-30-8 23:21:42	22
NACC3	capitalOrders		8/31/2016	10:21:02	2016-31-08	13:21:58	0.556921	Wednesday	3	19	2016-31-8 13:21:58	23
NACC3	capitalOrders		9/12/2016	10:21:02	2016-12-09	13:22:02	0.556968	Monday	1	19	2016-09-12 13:22	31
NACC3	capitalOrders		9/22/2016	17:20:02	2016-22-09	20:22:23	0.848877	Thursday	4	19	2016-22-9 20:22:23	39
NACC3	capitalOrders		8/17/2016	17:20:04	2016-17-08	20:22:25	0.8489	Wednesday	3	19	2016-17-8 20:22:25	13
NACC3	capitalOrders		9/15/2016	17:20:04	2016-15-09	20:21:48	0.848472	Thursday	4	19	2016-15-9 20:21:48	34
NACC3	capitalOrders		8/1/2016	17:20:05	2016-01-08	20:22:39	0.849063	Monday	1	19	2016-08-01 20:22	1
NACC3	capitalOrders		8/23/2016	17:20:05	2016-23-08	20:22:12	0.84875	Tuesday	2	19	2016-23-8 20:22:12	17
NACC3	capitalOrders		9/2/2016	17:20:05	2016-02-09	20:21:00	0.847917	Friday	5	19	2016-09-02 20:21	25
NACC3	capitalOrders		8/5/2016	17:20:06	2016-05-08	20:21:41	0.848391	Friday	5	19	2016-08-05 20:21	5
NACC3	capitalOrders		8/12/2016	17:20:07	2016-12-08	20:21:32	0.848287	Friday	5	19	2016-08-12 20:21	10
NACC3	capitalOrders		9/1/2016	17:21:01	2016-01-09	20:22:38	0.849051	Thursday	4	19	2016-09-01 20:22	24
NACC3	capitalOrders		8/24/2016	17:21:02	2016-24-08	20:22:32	0.848981	Wednesday	3	19	2016-24-8 20:22:32	18
NACC3	capitalOrders		9/5/2016	17:21:02	2016-05-09	20:22:40	0.849074	Monday	1	19	2016-09-05 20:22	26
NACC3	capitalOrders		9/6/2016	17:21:02	2016-06-09	20:22:52	0.849213	Tuesday	2	19	2016-09-06 20:22	27
NACC3	capitalOrders		9/8/2016	17:21:02	2016-08-09	20:21:55	0.848553	Thursday	4	19	2016-09-08 20:21	29
NACC3	capitalOrders		9/13/2016	17:21:02	2016-13-09	20:22:51	0.849201	Tuesday	2	19	2016-13-9 20:22:51	32
NACC3	capitalOrders		8/11/2016	17:21:03	2016-11-08	20:22:40	0.849074	Thursday	4	19	2016-08-11 20:22	9
NACC3	capitalOrders		8/25/2016	18:20:08	2016-25-08	21:21:22	0.889838	Thursday	4	19	2016-25-8 21:21:22	19
NACC3	capitalOrders		9/16/2016	18:21:01	2016-16-09	21:22:33	0.89066	Friday	5	19	2016-16-9 21:22:33	35
NACC3	capitalOrders		8/2/2016	18:21:02	2016-02-08	21:23:15	0.891146	Tuesday	2	19	2016-08-02 21:23	2
NACC3	capitalOrders		8/10/2016	18:21:02	2016-10-08	21:23:36	0.891389	Wednesday	3	19	2016-08-10 21:23	8
NACC3	capitalOrders		8/18/2016	18:21:02	2016-18-08	21:22:52	0.89088	Thursday	4	19	2016-18-8 21:22:52	14
NACC3	capitalOrders		8/19/2016	18:21:02	2016-19-08	21:23:17	0.891169	Friday	5	19	2016-19-8 21:23:17	15
NACC3	capitalOrders		8/29/2016	18:21:02	2016-29-08	21:23:22	0.891227	Monday	1	19	2016-29-8 21:23:22	21
NACC3	capitalOrders		9/7/2016	18:21:02	2016-07-09	21:23:41	0.891447	Wednesday	3	19	2016-09-07 21:23	28
NACC3	capitalOrders		9/23/2016	18:21:02	2016-23-09	21:23:03	0.891007	Friday	5	19	2016-23-9 21:23:03	40
NACC3	capitalOrders		8/8/2016	19:20:04	2016-08-08	22:22:08	0.932037	Monday	1	19	2016-08-08 22:22	6
NACC3	capitalOrders		8/26/2016	19:20:04	2016-26-08	22:21:43	0.931748	Friday	5	19	2016-26-8 22:21:43	20
NACC3	capitalOrders		9/19/2016	19:20:06	2016-19-09	22:22:30	0.932292	Monday	1	19	2016-19-9 22:22:30	36
NACC3	capitalOrders		8/15/2016	19:21:01	2016-15-08	22:23:15	0.932813	Monday	1	19	2016-15-8 22:23:15	11
NACC3	capitalOrders		8/16/2016	19:21:01	2016-16-08	22:22:08	0.932037	Tuesday	2	19	2016-16-8 22:22:08	12
NACC3	capitalOrders		8/22/2016	19:21:01	2016-22-08	22:21:22	0.931505	Monday	1	19	2016-22-8 22:21:22	16
NACC3	capitalOrders		9/14/2016	19:21:01	2016-14-09	22:23:28	0.932963	Wednesday	3	19	2016-14-9 22:23:28	33
NACC3	capitalOrders		8/4/2016	19:21:02	2016-04-08	22:22:58	0.932616	Thursday	4	19	2016-08-04 22:22	4
NACC3	capitalOrders		8/3/2016	19:21:06	2016-03-08	22:21:58	0.931921	Wednesday	3	19	2016-08-03 22:21	3
NACC3	capitalOrders		9/20/2016	20:20:08	2016-20-09	23:21:09	0.973021	Tuesday	2	19	2016-20-9 23:21:09	37
NACC3	capitalOrders		9/9/2016	20:20:09	2016-09-09	23:22:48	0.974167	Friday	5	19	2016-09-09 23:22	30
NACC3	capitalOrders		8/9/2016	20:20:16	2016-09-08	23:23:01	0.974317	Tuesday	2	19	2016-08-09 23:23	7
NACC3	capitalOrders		8/30/2016	20:21:02	2016-31-08	0:17:44	0.012315	Wednesday	3	19	2016-31-8 0:17:44	23
NACC3	capitalOrders		9/12/2016	17:20:05	2016-12-09	20:21:55	0.848553	Monday	1	19	2016-09-12 20:21	31
NACC3	capitalOrders		8/31/2016	17:20:08	2016-31-08	20:22:20	0.848843	Wednesday	3	19	2016-31-8 20:22:20	23
NACC3	capitalOrders		8/1/2016	17:21:01	2016-01-08	20:22:39	0.849063	Monday	1	19	2016-08-01 20:22	1
NACC3	capitalOrders		9/2/2016	17:21:01	2016-02-09	20:23:01	0.849317	Friday	5	19	2016-09-02 20:23	25
NACC3	capitalOrders		9/22/2016	17:21:01	2016-22-09	20:22:23	0.848877	Thursday	4	19	2016-22-9 20:22:23	39
NACC3	capitalOrders		8/5/2016	17:21:02	2016-05-08	20:21:41	0.848391	Friday	5	19	2016-08-05 20:21	5
NACC3	capitalOrders		8/12/2016	17:21:02	2016-12-08	20:23:32	0.849676	Friday	5	19	2016-08-12 20:23	10
NACC3	capitalOrders		8/17/2016	17:21:02	2016-17-08	20:22:25	0.8489	Wednesday	3	19	2016-17-8 20:22:25	13
NACC3	capitalOrders		9/15/2016	17:21:02	2016-15-09	20:21:49	0.848484	Thursday	4	19	2016-15-9 20:21:49	34
NACC3	capitalOrders		8/23/2016	17:21:03	2016-23-08	20:22:12	0.84875	Tuesday	2	19	2016-23-8 20:22:12	17
NACC3	capitalOrders		9/13/2016	18:20:05	2016-13-09	21:22:54	0.890903	Tuesday	2	19	2016-13-9 21:22:54	32
NACC3	capitalOrders		8/11/2016	18:20:06	2016-11-08	21:20:42	0.889375	Thursday	4	19	2016-08-11 21:20	9
NACC3	capitalOrders		8/24/2016	18:20:06	2016-24-08	21:22:34	0.890671	Wednesday	3	19	2016-24-8 21:22:34	18
NACC3	capitalOrders		9/1/2016	18:21:01	2016-01-09	21:22:40	0.890741	Thursday	4	19	2016-09-01 21:22	24
NACC3	capitalOrders		8/25/2016	18:21:02	2016-25-08	21:23:22	0.891227	Thursday	4	19	2016-25-8 21:23:22	19
NACC3	capitalOrders		8/29/2016	19:20:03	2016-29-08	22:21:25	0.931539	Monday	1	19	2016-29-8 22:21:25	21
NACC3	capitalOrders		9/7/2016	19:20:03	2016-07-09	22:21:44	0.931759	Wednesday	3	19	2016-09-07 22:21	28
NACC3	capitalOrders		8/10/2016	19:20:04	2016-10-08	22:21:39	0.931701	Wednesday	3	19	2016-08-10 22:21	8
NACC3	capitalOrders		9/5/2016	19:20:04	2016-05-09	22:22:44	0.932454	Monday	1	19	2016-09-05 22:22	26
NACC3	capitalOrders		8/18/2016	19:20:05	2016-18-08	22:20:56	0.931204	Thursday	4	19	2016-18-8 22:20:56	14
NACC3	capitalOrders		8/19/2016	19:20:05	2016-19-08	22:21:19	0.93147	Friday	5	19	2016-19-8 22:21:19	15
NACC3	capitalOrders		9/6/2016	19:20:05	2016-06-09	22:20:56	0.931204	Tuesday	2	19	2016-09-06 22:20	27
NACC3	capitalOrders		9/8/2016	19:20:05	2016-08-09	22:21:59	0.931933	Thursday	4	19	2016-09-08 22:21	29
NACC3	capitalOrders		9/16/2016	19:20:05	2016-16-09	22:22:37	0.932373	Friday	5	19	2016-16-9 22:22:37	35
NACC3	capitalOrders		9/23/2016	19:20:05	2016-23-09	22:20:36	0.930972	Friday	5	19	2016-23-9 22:20:36	40
NACC3	capitalOrders		8/2/2016	19:20:09	2016-02-08	22:21:19	0.93147	Tuesday	2	19	2016-08-02 22:21	2
NACC3	capitalOrders		8/8/2016	19:21:01	2016-08-08	22:22:08	0.932037	Monday	1	19	2016-08-08 22:22	6
NACC3	capitalOrders		9/19/2016	19:21:01	2016-19-09	22:22:30	0.932292	Monday	1	19	2016-19-9 22:22:30	36
NACC3	capitalOrders		8/26/2016	19:21:02	2016-26-08	22:21:43	0.931748	Friday	5	19	2016-26-8 22:21:43	20
NACC3	capitalOrders		8/15/2016	20:20:04	2016-15-08	23:21:19	0.973137	Monday	1	19	2016-15-8 23:21:19	11
NACC3	capitalOrders		9/14/2016	20:20:04	2016-14-09	23:21:30	0.973264	Wednesday	3	19	2016-14-9 23:21:30	33
NACC3	capitalOrders		8/3/2016	20:20:05	2016-03-08	23:22:01	0.973623	Wednesday	3	19	2016-08-03 23:22	3
NACC3	capitalOrders		8/16/2016	20:20:08	2016-16-08	23:21:42	0.973403	Tuesday	2	19	2016-16-8 23:21:42	12
NACC3	capitalOrders		8/4/2016	20:20:13	2016-04-08	23:21:02	0.97294	Thursday	4	19	2016-08-04 23:21	4
NACC3	capitalOrders		8/22/2016	20:21:01	2016-22-08	23:23:25	0.974595	Monday	1	19	2016-22-8 23:23:25	16
NACC3	capitalOrders		9/9/2016	20:21:01	2016-09-09	23:22:48	0.974167	Friday	5	19	2016-09-09 23:22	30
NACC3	capitalOrders		8/30/2016	20:21:02	2016-31-08	0:49:45	0.034549	Wednesday	3	19	2016-31-8 0:49:45	23
NACC3	capitalOrders		9/20/2016	20:21:06	2016-20-09	23:23:09	0.97441	Tuesday	2	19	2016-20-9 23:23:09	37
NACC3	capitalOrders		8/9/2016	20:21:10	2016-09-08	23:23:01	0.974317	Tuesday	2	19	2016-08-09 23:23	7
NACC3	capitalOrders		8/31/2016	17:21:02	2016-31-08	20:22:20	0.848843	Wednesday	3	19	2016-31-8 20:22:20	23
NACC3	capitalOrders		9/12/2016	17:21:02	2016-12-09	20:21:56	0.848565	Monday	1	19	2016-09-12 20:21	31
NACC3	capitalOrders		8/17/2016	18:20:04	2016-17-08	21:22:28	0.890602	Wednesday	3	19	2016-17-8 21:22:28	13
NACC3	capitalOrders		9/15/2016	18:20:04	2016-15-09	21:21:52	0.890185	Thursday	4	19	2016-15-9 21:21:52	34
NACC3	capitalOrders		9/2/2016	18:20:05	2016-02-09	21:21:03	0.889618	Friday	5	19	2016-09-02 21:21	25
NACC3	capitalOrders		9/22/2016	18:20:05	2016-22-09	21:21:57	0.890243	Thursday	4	19	2016-22-9 21:21:57	39
NACC3	capitalOrders		8/12/2016	18:20:07	2016-12-08	21:21:35	0.889988	Friday	5	19	2016-08-12 21:21	10
NACC3	capitalOrders		8/1/2016	18:21:01	2016-01-08	21:22:42	0.890764	Monday	1	19	2016-08-01 21:22	1
NACC3	capitalOrders		9/13/2016	18:21:02	2016-13-09	21:22:54	0.890903	Tuesday	2	19	2016-13-9 21:22:54	32
NACC3	capitalOrders		8/5/2016	19:20:02	2016-05-08	22:21:48	0.931806	Friday	5	19	2016-08-05 22:21	5
NACC3	capitalOrders		9/1/2016	19:20:04	2016-01-09	22:20:43	0.931053	Thursday	4	19	2016-09-01 22:20	24
NACC3	capitalOrders		8/23/2016	19:20:05	2016-23-08	22:22:18	0.932153	Tuesday	2	19	2016-23-8 22:22:18	17
NACC3	capitalOrders		8/11/2016	19:20:07	2016-11-08	22:20:46	0.931088	Thursday	4	19	2016-08-11 22:20	9
NACC3	capitalOrders		8/10/2016	19:21:01	2016-10-08	22:21:39	0.931701	Wednesday	3	19	2016-08-10 22:21	8
NACC3	capitalOrders		8/24/2016	19:21:01	2016-24-08	22:22:36	0.932361	Wednesday	3	19	2016-24-8 22:22:36	18
NACC3	capitalOrders		9/6/2016	19:21:01	2016-06-09	22:22:57	0.932604	Tuesday	2	19	2016-09-06 22:22	27
NACC3	capitalOrders		9/8/2016	19:21:01	2016-08-09	22:22:00	0.931944	Thursday	4	19	2016-09-08 22:22	29
NACC3	capitalOrders		8/18/2016	19:21:02	2016-18-08	22:22:57	0.932604	Thursday	4	19	2016-18-8 22:22:57	14
NACC3	capitalOrders		8/19/2016	19:21:02	2016-19-08	22:23:20	0.93287	Friday	5	19	2016-19-8 22:23:20	15
NACC3	capitalOrders		9/5/2016	19:21:02	2016-05-09	22:22:44	0.932454	Monday	1	19	2016-09-05 22:22	26
NACC3	capitalOrders		9/16/2016	19:21:02	2016-16-09	22:22:37	0.932373	Friday	5	19	2016-16-9 22:22:37	35
NACC3	capitalOrders		8/29/2016	19:21:05	2016-29-08	22:23:25	0.932928	Monday	1	19	2016-29-8 22:23:25	21
NACC3	capitalOrders		8/26/2016	20:20:04	2016-26-08	23:21:46	0.973449	Friday	5	19	2016-26-8 23:21:46	20
NACC3	capitalOrders		8/25/2016	20:20:06	2016-25-08	23:21:27	0.973229	Thursday	4	19	2016-25-8 23:21:27	19
NACC3	capitalOrders		9/19/2016	20:20:06	2016-19-09	23:22:34	0.974005	Monday	1	19	2016-19-9 23:22:34	36
NACC3	capitalOrders		9/23/2016	20:20:06	2016-23-09	23:22:39	0.974063	Friday	5	19	2016-23-9 23:22:39	40
NACC3	capitalOrders		9/7/2016	20:20:07	2016-07-09	23:21:45	0.973438	Wednesday	3	19	2016-09-07 23:21	28
NACC3	capitalOrders		8/2/2016	20:20:09	2016-02-08	23:21:22	0.973171	Tuesday	2	19	2016-08-02 23:21	2
NACC3	capitalOrders		8/8/2016	20:21:01	2016-08-08	23:22:12	0.97375	Monday	1	19	2016-08-08 23:22	6
NACC3	capitalOrders		8/16/2016	20:21:01	2016-16-08	23:23:42	0.974792	Tuesday	2	19	2016-16-8 23:23:42	12
NACC3	capitalOrders		9/14/2016	20:21:01	2016-14-09	23:23:30	0.974653	Wednesday	3	19	2016-14-9 23:23:30	33
NACC3	capitalOrders		8/15/2016	20:21:02	2016-15-08	23:23:19	0.974525	Monday	1	19	2016-15-8 23:23:19	11
NACC3	capitalOrders		8/4/2016	20:21:09	2016-04-08	23:23:03	0.97434	Thursday	4	19	2016-08-04 23:23	4
NACC3	capitalOrders		9/12/2016	18:20:06	2016-12-09	21:21:59	0.890266	Monday	1	19	2016-09-12 21:21	31
NACC3	capitalOrders		9/2/2016	18:21:01	2016-02-09	21:23:03	0.891007	Friday	5	19	2016-09-02 21:23	25
NACC3	capitalOrders		9/22/2016	18:21:01	2016-22-09	21:21:57	0.890243	Thursday	4	19	2016-22-9 21:21:57	39
NACC3	capitalOrders		8/12/2016	18:21:02	2016-12-08	21:23:36	0.891389	Friday	5	19	2016-08-12 21:23	10
NACC3	capitalOrders		8/17/2016	18:21:02	2016-17-08	21:22:28	0.890602	Wednesday	3	19	2016-17-8 21:22:28	13
NACC3	capitalOrders		8/31/2016	19:20:04	2016-31-08	22:22:25	0.932234	Wednesday	3	19	2016-31-8 22:22:25	23
NACC3	capitalOrders		8/1/2016	19:20:06	2016-01-08	22:22:46	0.932477	Monday	1	19	2016-08-01 22:22	1
NACC3	capitalOrders		8/5/2016	19:21:01	2016-05-08	22:21:48	0.931806	Friday	5	19	2016-08-05 22:21	5
NACC3	capitalOrders		9/15/2016	19:21:01	2016-15-09	22:21:55	0.931887	Thursday	4	19	2016-15-9 22:21:55	34
NACC3	capitalOrders		8/11/2016	19:21:02	2016-11-08	22:22:47	0.932488	Thursday	4	19	2016-08-11 22:22	9
NACC3	capitalOrders		8/23/2016	19:21:02	2016-23-08	22:22:18	0.932153	Tuesday	2	19	2016-23-8 22:22:18	17
NACC3	capitalOrders		9/13/2016	19:21:02	2016-13-09	22:22:59	0.932627	Tuesday	2	19	2016-13-9 22:22:59	32
NACC3	capitalOrders		9/1/2016	19:21:03	2016-01-09	22:22:43	0.932442	Thursday	4	19	2016-09-01 22:22	24
NACC3	capitalOrders		8/24/2016	20:20:03	2016-24-08	23:22:38	0.974051	Wednesday	3	19	2016-24-8 23:22:38	18
NACC3	capitalOrders		9/5/2016	20:20:04	2016-05-09	23:22:46	0.974144	Monday	1	19	2016-09-05 23:22	26
NACC3	capitalOrders		8/18/2016	20:20:05	2016-18-08	23:23:00	0.974306	Thursday	4	19	2016-18-8 23:23:00	14
NACC3	capitalOrders		8/19/2016	20:20:05	2016-19-08	23:21:23	0.973183	Friday	5	19	2016-19-8 23:21:23	15
NACC3	capitalOrders		9/16/2016	20:20:05	2016-16-09	23:20:40	0.972685	Friday	5	19	2016-16-9 23:20:40	35
NACC3	capitalOrders		8/29/2016	20:20:06	2016-29-08	23:21:28	0.973241	Monday	1	19	2016-29-8 23:21:28	21
NACC3	capitalOrders		8/25/2016	20:21:01	2016-25-08	23:23:28	0.97463	Thursday	4	19	2016-25-8 23:23:28	19
NACC3	capitalOrders		9/6/2016	20:21:01	2016-06-09	23:23:00	0.974306	Tuesday	2	19	2016-09-06 23:23	27
NACC3	capitalOrders		9/8/2016	20:21:01	2016-08-09	23:22:02	0.973634	Thursday	4	19	2016-09-08 23:22	29
NACC3	capitalOrders		9/19/2016	20:21:01	2016-19-09	23:22:34	0.974005	Monday	1	19	2016-19-9 23:22:34	36
NACC3	capitalOrders		9/23/2016	20:21:02	2016-23-09	23:22:39	0.974063	Friday	5	19	2016-23-9 23:22:39	40
NACC3	capitalOrders		8/10/2016	20:21:03	2016-10-08	23:21:42	0.973403	Wednesday	3	19	2016-08-10 23:21	8
NACC3	capitalOrders		8/2/2016	20:21:05	2016-02-08	23:23:22	0.97456	Tuesday	2	19	2016-08-02 23:23	2
NACC3	capitalOrders		9/7/2016	20:21:05	2016-07-09	23:23:46	0.974838	Wednesday	3	19	2016-09-07 23:23	28
NACC3	capitalOrders		9/22/2016	19:20:06	2016-22-09	22:22:01	0.931956	Thursday	4	19	2016-22-9 22:22:01	39
NACC3	capitalOrders		9/2/2016	19:20:07	2016-02-09	22:21:06	0.931319	Friday	5	19	2016-09-02 22:21	25
NACC3	capitalOrders		8/1/2016	19:21:01	2016-01-08	22:22:47	0.932488	Monday	1	19	2016-08-01 22:22	1
NACC3	capitalOrders		8/31/2016	19:21:01	2016-31-08	22:22:25	0.932234	Wednesday	3	19	2016-31-8 22:22:25	23
NACC3	capitalOrders		9/12/2016	19:21:01	2016-12-09	22:22:02	0.931968	Monday	1	19	2016-09-12 22:22	31
NACC3	capitalOrders		8/12/2016	19:21:02	2016-12-08	22:23:40	0.933102	Friday	5	19	2016-08-12 22:23	10
NACC3	capitalOrders		8/17/2016	20:20:04	2016-17-08	23:22:33	0.973993	Wednesday	3	19	2016-17-8 23:22:33	13
NACC3	capitalOrders		9/13/2016	20:20:04	2016-13-09	23:22:34	0.974005	Tuesday	2	19	2016-13-9 23:22:34	32
NACC3	capitalOrders		9/15/2016	20:20:04	2016-15-09	23:21:59	0.9736	Thursday	4	19	2016-15-9 23:21:59	34
NACC3	capitalOrders		8/23/2016	20:20:05	2016-23-08	23:22:22	0.973866	Tuesday	2	19	2016-23-8 23:22:22	17
NACC3	capitalOrders		8/5/2016	20:20:08	2016-05-08	23:21:52	0.973519	Friday	5	19	2016-08-05 23:21	5
NACC3	capitalOrders		8/11/2016	20:20:11	2016-11-08	23:20:50	0.972801	Thursday	4	19	2016-08-11 23:20	9
NACC3	capitalOrders		8/24/2016	20:21:02	2016-24-08	23:22:38	0.974051	Wednesday	3	19	2016-24-8 23:22:38	18
NACC3	capitalOrders		9/16/2016	20:21:02	2016-16-09	23:22:41	0.974086	Friday	5	19	2016-16-9 23:22:41	35
NACC3	capitalOrders		8/18/2016	20:21:03	2016-18-08	23:23:00	0.974306	Thursday	4	19	2016-18-8 23:23:00	14
NACC3	capitalOrders		9/1/2016	20:21:03	2016-01-09	23:22:46	0.974144	Thursday	4	19	2016-09-01 23:22	24
NACC3	capitalOrders		9/22/2016	19:21:01	2016-22-09	22:22:02	0.931968	Thursday	4	19	2016-22-9 22:22:02	39
NACC3	capitalOrders		9/2/2016	19:21:02	2016-02-09	22:23:06	0.932708	Friday	5	19	2016-09-02 22:23	25
NACC3	capitalOrders		9/12/2016	20:20:03	2016-12-09	23:22:05	0.973669	Monday	1	19	2016-09-12 23:22	31
NACC3	capitalOrders		8/31/2016	20:20:04	2016-31-08	23:22:27	0.973924	Wednesday	3	19	2016-31-8 23:22:27	23
NACC3	capitalOrders		8/1/2016	20:21:01	2016-01-08	23:22:21	0.973854	Monday	1	19	2016-08-01 23:22	1
NACC3	capitalOrders		8/5/2016	20:21:01	2016-05-08	23:21:52	0.973519	Friday	5	19	2016-08-05 23:21	5
NACC3	capitalOrders		8/17/2016	20:21:01	2016-17-08	23:22:34	0.974005	Wednesday	3	19	2016-17-8 23:22:34	13
NACC3	capitalOrders		8/23/2016	20:21:02	2016-23-08	23:22:22	0.973866	Tuesday	2	19	2016-23-8 23:22:22	17
NACC3	capitalOrders		9/15/2016	20:21:02	2016-15-09	23:21:59	0.9736	Thursday	4	19	2016-15-9 23:21:59	34
NACC3	capitalOrders		8/11/2016	20:21:03	2016-11-08	23:22:50	0.97419	Thursday	4	19	2016-08-11 23:22	9
NACC3	capitalOrders		9/13/2016	20:21:03	2016-13-09	23:22:34	0.974005	Tuesday	2	19	2016-13-9 23:22:34	32
NACC3	capitalOrders		8/12/2016	20:38:48	2016-12-08	23:39:44	0.985926	Friday	5	19	2016-08-12 23:39	10
NACC3	capitalOrders		9/12/2016	20:21:01	2016-12-09	23:22:06	0.973681	Monday	1	19	2016-09-12 23:22	31
NACC3	capitalOrders		9/22/2016	20:21:01	2016-22-09	23:22:06	0.973681	Thursday	4	19	2016-22-9 23:22:06	39
NACC3	capitalOrders		8/31/2016	20:21:02	2016-31-08	23:22:27	0.973924	Wednesday	3	19	2016-31-8 23:22:27	23
NACC3	capitalOrders		8/12/2016	20:38:47	2016-12-08	23:39:45	0.985938	Friday	5	19	2016-08-12 23:39	10
NACC3	NACC320170131212005.csv.20170201002115906		2/1/2017	0:20:05	2017-01-02	0:21:15	0.014757	Wednesday	3	19	2017-02-01 00:21	42
NACC3	NACC320170131222124.csv.20170201012319500		2/1/2017	1:21:24	2017-01-02	1:23:19	0.057859	Wednesday	3	19	2017-02-01 01:23	42
NACC3	NACC320170131232004.csv.20170201022124164		2/1/2017	2:20:04	2017-01-02	2:21:24	0.098194	Wednesday	3	19	2017-02-01 02:21	42
NACC3	NACC320170201002004.csv.20170201032127852		2/1/2017	3:20:04	2017-01-02	3:21:27	0.139896	Wednesday	3	19	2017-02-01 03:21	42
NACC3	NACC320170201002102.csv.20170201032328328		2/1/2017	3:21:02	2017-01-02	3:23:28	0.141296	Wednesday	3	19	2017-02-01 03:23	42
NACC3	NACC320170201012102.csv.20170201042131006		2/1/2017	4:21:02	2017-01-02	4:21:31	0.181609	Wednesday	3	19	2017-02-01 04:21	42
NACC3	NACC320170201042010.csv.20170201072144923._ADS		2/1/2017	7:20:10	2017-01-02	7:21:44	0.306759	Wednesday	3	19	2017-02-01 07:21	42
NACC3	NACC320170201042010.csv.20170201072144923		2/1/2017	7:20:10	2017-01-02	7:21:44	0.306759	Wednesday	3	19	2017-02-01 07:21	42
NACC3	NACC320170201042104.csv.20170201072345424		2/1/2017	7:21:04	2017-01-02	7:23:45	0.30816	Wednesday	3	19	2017-02-01 07:23	42
NACC3	NACC320170201062007.csv.20170201092150873		2/1/2017	9:20:07	2017-01-02	9:21:50	0.390162	Wednesday	3	19	2017-02-01 09:21	42
NACC3	NACC320170201062102.csv.20170201092351244		2/1/2017	9:21:02	2017-01-02	9:23:51	0.391563	Wednesday	3	19	2017-02-01 09:23	42
NACC3	NACC320170201082003.csv.20170201112135281		2/1/2017	11:20:03	2017-01-02	11:21:35	0.473322	Wednesday	3	19	2017-02-01 11:21	42
NACC3	NACC320170201082101.csv.20170201112136366		2/1/2017	11:21:01	2017-01-02	11:21:36	0.473333	Wednesday	3	19	2017-02-01 11:21	42
NACC3	NACC320170201092102.csv.20170201122344060		2/1/2017	12:21:02	2017-01-02	12:23:44	0.516481	Wednesday	3	19	2017-02-01 12:23	42
NACC3	NACC320170201102003.csv.20170201132149357		2/1/2017	13:20:03	2017-01-02	13:21:49	0.556817	Wednesday	3	19	2017-02-01 13:21	42
NACC3	NACC320170201102102.csv.20170201132149646		2/1/2017	13:21:02	2017-01-02	13:21:49	0.556817	Wednesday	3	19	2017-02-01 13:21	42
NACC3	NACC320170201172004.csv.20170201202223871		2/1/2017	20:20:04	2017-01-02	20:22:23	0.848877	Wednesday	3	19	2017-02-01 20:22	42
NACC3	NACC320170201172102.csv.20170201202224244		2/1/2017	20:21:02	2017-01-02	20:22:24	0.848889	Wednesday	3	19	2017-02-01 20:22	42
NACC3	NACC320170201182005.csv.20170201212227694		2/1/2017	21:20:05	2017-01-02	21:22:27	0.89059	Wednesday	3	19	2017-02-01 21:22	42
NACC3	NACC320170201182102.csv.20170201212227930		2/1/2017	21:21:02	2017-01-02	21:22:27	0.89059	Wednesday	3	19	2017-02-01 21:22	42
NACC3	NACC320170201192005.csv.20170201222230808		2/1/2017	22:20:05	2017-01-02	22:22:30	0.932292	Wednesday	3	19	2017-02-01 22:22	42
NACC3	NACC320170201192102.csv.20170201222231145		2/1/2017	22:21:02	2017-01-02	22:22:31	0.932303	Wednesday	3	19	2017-02-01 22:22	42
NACC3	NACC320170201202006.csv.20170201232203613		2/1/2017	23:20:06	2017-01-02	23:22:03	0.973646	Wednesday	3	19	2017-02-01 23:22	42
NACC3	NACC320170201212007.csv.20170202002207751		2/2/2017	0:20:07	2017-02-02	0:22:07	0.015359	Thursday	4	19	2017-02-02 00:22	43
NACC3	NACC320170201212101.csv.20170202002208034		2/2/2017	0:21:01	2017-02-02	0:22:08	0.01537	Thursday	4	19	2017-02-02 00:22	43
NACC3	NACC320170201222007.csv.20170202012211453		2/2/2017	1:20:07	2017-02-02	1:22:11	0.057072	Thursday	4	19	2017-02-02 01:22	43
NACC3	NACC320170201222103.csv.20170202012211810		2/2/2017	1:21:03	2017-02-02	1:22:11	0.057072	Thursday	4	19	2017-02-02 01:22	43
NACC3	NACC320170202002006.csv.20170202032217639		2/2/2017	3:20:06	2017-02-02	3:22:17	0.140475	Thursday	4	19	2017-02-02 03:22	43
NACC3	NACC320170202002102.csv.20170202032218136		2/2/2017	3:21:02	2017-02-02	3:22:18	0.140486	Thursday	4	19	2017-02-02 03:22	43
NACC3	NACC320170202042003.csv.20170202072035017		2/2/2017	7:20:03	2017-02-02	7:20:35	0.305961	Thursday	4	19	2017-02-02 07:20	43
NACC3	NACC320170202042101.csv.20170202072235458		2/2/2017	7:21:01	2017-02-02	7:22:35	0.30735	Thursday	4	19	2017-02-02 07:22	43
NACC3	NACC320170202052005.csv.20170202082037504		2/2/2017	8:20:05	2017-02-02	8:20:37	0.34765	Thursday	4	19	2017-02-02 08:20	43
NACC3	NACC320170202052101.csv.20170202082237816		2/2/2017	8:21:01	2017-02-02	8:22:37	0.349039	Thursday	4	19	2017-02-02 08:22	43
NACC3	NACC320170202062006.csv.20170202092240669		2/2/2017	9:20:06	2017-02-02	9:22:40	0.390741	Thursday	4	19	2017-02-02 09:22	43
NACC3	NACC320170202062101.csv.20170202092240933		2/2/2017	9:21:01	2017-02-02	9:22:40	0.390741	Thursday	4	19	2017-02-02 09:22	43
NACC3	NACC320170202072102.csv.20170202102245926		2/2/2017	10:21:02	2017-02-02	10:22:45	0.432465	Thursday	4	19	2017-02-02 10:22	43
NACC3	NACC320170202082002.csv.20170202112049745		2/2/2017	11:20:02	2017-02-02	11:20:49	0.472789	Thursday	4	19	2017-02-02 11:20	43
NACC3	NACC320170202082102.csv.20170202112250848		2/2/2017	11:21:02	2017-02-02	11:22:50	0.47419	Thursday	4	19	2017-02-02 11:22	43
NACC3	NACC320170202092002.csv.20170202122225480		2/2/2017	12:20:02	2017-02-02	12:22:25	0.515567	Thursday	4	19	2017-02-02 12:22	43
NACC3	NACC320170202092103.csv.20170202122225864		2/2/2017	12:21:03	2017-02-02	12:22:25	0.515567	Thursday	4	19	2017-02-02 12:22	43
NACC3	NACC320170202102002.csv.20170202132229570		2/2/2017	13:20:02	2017-02-02	13:22:29	0.55728	Thursday	4	19	2017-02-02 13:22	43
NACC3	NACC320170202172003.csv.20170202202117605		2/2/2017	20:20:03	2017-02-02	20:21:17	0.848113	Thursday	4	19	2017-02-02 20:21	43
NACC3	NACC320170202172102.csv.20170202202317973		2/2/2017	20:21:02	2017-02-02	20:23:17	0.849502	Thursday	4	19	2017-02-02 20:23	43
NACC3	NACC320170202182007.csv.20170202212121827		2/2/2017	21:20:07	2017-02-02	21:21:21	0.889826	Thursday	4	19	2017-02-02 21:21	43
NACC3	NACC320170202182102.csv.20170202212322281		2/2/2017	21:21:02	2017-02-02	21:23:22	0.891227	Thursday	4	19	2017-02-02 21:23	43
NACC3	NACC320170202202003.csv.20170202232128930		2/2/2017	23:20:03	2017-02-02	23:21:28	0.973241	Thursday	4	19	2017-02-02 23:21	43
NACC3	NACC320170202202101.csv.20170202232329320		2/2/2017	23:21:01	2017-02-02	23:23:29	0.974641	Thursday	4	19	2017-02-02 23:23	43
NACC3	NACC320170202212101.csv.20170203002332162		2/3/2017	0:21:01	2017-03-02	0:23:32	0.016343	Friday	5	19	2017-02-03 00:23	44
NACC3	NACC320170202222002.csv.20170203012135550		2/3/2017	1:20:02	2017-03-02	1:21:35	0.056655	Friday	5	19	2017-02-03 01:21	44
NACC3	NACC320170202222102.csv.20170203012335952		2/3/2017	1:21:02	2017-03-02	1:23:35	0.058044	Friday	5	19	2017-02-03 01:23	44
NACC3	NACC320170202232014.csv.20170203022138807		2/3/2017	2:20:14	2017-03-02	2:21:38	0.098356	Friday	5	19	2017-02-03 02:21	44
NACC3	NACC320170202232104.csv.20170203022339184		2/3/2017	2:21:04	2017-03-02	2:23:39	0.099757	Friday	5	19	2017-02-03 02:23	44
NACC3	NACC320170203002019.csv.20170203032144365		2/3/2017	3:20:19	2017-03-02	3:21:44	0.140093	Friday	5	19	2017-02-03 03:21	44
NACC3	NACC320170203002137.csv.20170203032344774		2/3/2017	3:21:37	2017-03-02	3:23:44	0.141481	Friday	5	19	2017-02-03 03:23	44
NACC3	NACC320170203042005.csv.20170203072133741		2/3/2017	7:20:05	2017-03-02	7:21:33	0.306632	Friday	5	19	2017-02-03 07:21	44
NACC3	NACC320170203042102.csv.20170203072134026		2/3/2017	7:21:02	2017-03-02	7:21:34	0.306644	Friday	5	19	2017-02-03 07:21	44
NACC3	NACC320170203052005.csv.20170203082135830		2/3/2017	8:20:05	2017-03-02	8:21:35	0.348322	Friday	5	19	2017-02-03 08:21	44
NACC3	NACC320170203052102.csv.20170203082336199		2/3/2017	8:21:02	2017-03-02	8:23:36	0.349722	Friday	5	19	2017-02-03 08:23	44
NACC3	NACC320170203072006.csv.20170203102148159		2/3/2017	10:20:06	2017-03-02	10:21:48	0.431806	Friday	5	19	2017-02-03 10:21	44
NACC3	NACC320170203072101.csv.20170203102348482		2/3/2017	10:21:01	2017-03-02	10:23:48	0.433194	Friday	5	19	2017-02-03 10:23	44
NACC3	NACC320170203082102.csv.20170203112203588		2/3/2017	11:21:02	2017-03-02	11:22:03	0.473646	Friday	5	19	2017-02-03 11:22	44
NACC3	NACC320170203092003.csv.20170203122207567		2/3/2017	12:20:03	2017-03-02	12:22:07	0.515359	Friday	5	19	2017-02-03 12:22	44
NACC3	NACC320170203092102.csv.20170203122207981		2/3/2017	12:21:02	2017-03-02	12:22:07	0.515359	Friday	5	19	2017-02-03 12:22	44
NACC3	NACC320170203102003.csv.20170203132210970		2/3/2017	13:20:03	2017-03-02	13:22:10	0.55706	Friday	5	19	2017-02-03 13:22	44
NACC3	NACC320170203102102.csv.20170203132211278		2/3/2017	13:21:02	2017-03-02	13:22:11	0.557072	Friday	5	19	2017-02-03 13:22	44
NACC3	NACC320170203172003.csv.20170203202239999		2/3/2017	20:20:03	2017-03-02	20:22:39	0.849063	Friday	5	19	2017-02-03 20:22	44
NACC3	NACC320170203172102.csv.20170203202240230		2/3/2017	20:21:02	2017-03-02	20:22:40	0.849074	Friday	5	19	2017-02-03 20:22	44
NACC3	NACC320170203182004.csv.20170203212045425		2/3/2017	21:20:04	2017-03-02	21:20:45	0.88941	Friday	5	19	2017-02-03 21:20	44
NACC3	NACC320170203192006.csv.20170203222048504		2/3/2017	22:20:06	2017-03-02	22:20:48	0.931111	Friday	5	19	2017-02-03 22:20	44
NACC3	NACC320170203192101.csv.20170203222249011		2/3/2017	22:21:01	2017-03-02	22:22:49	0.932512	Friday	5	19	2017-02-03 22:22	44
NACC3	NACC320170203202101.csv.20170203232223969		2/3/2017	23:21:01	2017-03-02	23:22:23	0.973877	Friday	5	19	2017-02-03 23:22	44
NACC3	NACC320170205212102.csv.20170206002153339		2/6/2017	0:21:02	2017-06-02	0:21:53	0.015197	Monday	1	19	2017-02-06 00:21	45
NACC3	NACC320170205222002.csv.20170206012155598		2/6/2017	1:20:02	2017-06-02	1:21:55	0.056887	Monday	1	19	2017-02-06 01:21	45
NACC3	NACC320170205232006.csv.20170206022158878		2/6/2017	2:20:06	2017-06-02	2:21:58	0.098588	Monday	1	19	2017-02-06 02:21	45
NACC3	NACC320170205232101.csv.20170206022159099		2/6/2017	2:21:01	2017-06-02	2:21:59	0.0986	Monday	1	19	2017-02-06 02:21	45
NACC3	NACC320170206002101.csv.20170206032202022		2/6/2017	3:21:01	2017-06-02	3:22:02	0.140301	Monday	1	19	2017-02-06 03:22	45
NACC3	NACC320170206012003.csv.20170206042205048		2/6/2017	4:20:03	2017-06-02	4:22:05	0.182002	Monday	1	19	2017-02-06 04:22	45
NACC3	NACC320170206012102.csv.20170206042205354		2/6/2017	4:21:02	2017-06-02	4:22:05	0.182002	Monday	1	19	2017-02-06 04:22	45
NACC3	NACC320170206042017.csv.20170206072216418		2/6/2017	7:20:17	2017-06-02	7:22:16	0.30713	Monday	1	19	2017-02-06 07:22	45
NACC3	NACC320170206042126.csv.20170206072417154		2/6/2017	7:21:26	2017-06-02	7:24:17	0.30853	Monday	1	19	2017-02-06 07:24	45
NACC3	NACC320170206062003.csv.20170206092223675		2/6/2017	9:20:03	2017-06-02	9:22:23	0.390544	Monday	1	19	2017-02-06 09:22	45
NACC3	NACC320170206062102.csv.20170206092223932		2/6/2017	9:21:02	2017-06-02	9:22:23	0.390544	Monday	1	19	2017-02-06 09:22	45
NACC3	NACC320170206072005.csv.20170206102158490		2/6/2017	10:20:05	2017-06-02	10:21:58	0.431921	Monday	1	19	2017-02-06 10:21	45
NACC3	NACC320170206072102.csv.20170206102358863		2/6/2017	10:21:02	2017-06-02	10:23:58	0.43331	Monday	1	19	2017-02-06 10:23	45
NACC3	NACC320170206082006.csv.20170206112203545		2/6/2017	11:20:06	2017-06-02	11:22:03	0.473646	Monday	1	19	2017-02-06 11:22	45
NACC3	NACC320170206082102.csv.20170206112404523		2/6/2017	11:21:02	2017-06-02	11:24:04	0.475046	Monday	1	19	2017-02-06 11:24	45
NACC3	NACC320170206092007.csv.20170206122207753		2/6/2017	12:20:07	2017-06-02	12:22:07	0.515359	Monday	1	19	2017-02-06 12:22	45
NACC3	NACC320170206092102.csv.20170206122208142		2/6/2017	12:21:02	2017-06-02	12:22:08	0.51537	Monday	1	19	2017-02-06 12:22	45
NACC3	NACC320170206102102.csv.20170206132212740		2/6/2017	13:21:02	2017-06-02	13:22:12	0.557083	Monday	1	19	2017-02-06 13:22	45
NACC3	NACC320170206172003.csv.20170206202242410		2/6/2017	20:20:03	2017-06-02	20:22:42	0.849097	Monday	1	19	2017-02-06 20:22	45
NACC3	NACC320170206172102.csv.20170206202242765		2/6/2017	20:21:02	2017-06-02	20:22:42	0.849097	Monday	1	19	2017-02-06 20:22	45
NACC3	NACC320170206182102.csv.20170206212216553		2/6/2017	21:21:02	2017-06-02	21:22:16	0.890463	Monday	1	19	2017-02-06 21:22	45
NACC3	NACC320170206192004.csv.20170206222219486		2/6/2017	22:20:04	2017-06-02	22:22:19	0.932164	Monday	1	19	2017-02-06 22:22	45
NACC3	NACC320170206192105.csv.20170206222219910		2/6/2017	22:21:05	2017-06-02	22:22:19	0.932164	Monday	1	19	2017-02-06 22:22	45
NACC3	NACC320170206202005.csv.20170206232224857._ADS		2/6/2017	23:20:05	2017-06-02	23:22:24	0.973889	Monday	1	19	2017-02-06 23:22	45
NACC3	NACC320170206202005.csv.20170206232224857		2/6/2017	23:20:05	2017-06-02	23:22:24	0.973889	Monday	1	19	2017-02-06 23:22	45
NACC3	NACC320170206212005.csv.20170207002229018		2/7/2017	0:20:05	2017-07-02	0:22:29	0.015613	Tuesday	2	19	2017-02-07 00:22	46
NACC3	NACC320170206212102.csv.20170207002229170		2/7/2017	0:21:02	2017-07-02	0:22:29	0.015613	Tuesday	2	19	2017-02-07 00:22	46
NACC3	NACC320170206222101.csv.20170207012231602		2/7/2017	1:21:01	2017-07-02	1:22:31	0.057303	Tuesday	2	19	2017-02-07 01:22	46
NACC3	NACC320170206232004.csv.20170207022234910		2/7/2017	2:20:04	2017-07-02	2:22:34	0.099005	Tuesday	2	19	2017-02-07 02:22	46
NACC3	NACC320170206232102.csv.20170207022235146		2/7/2017	2:21:02	2017-07-02	2:22:35	0.099016	Tuesday	2	19	2017-02-07 02:22	46
NACC3	NACC320170207002111.csv.20170207032239841		2/7/2017	3:21:11	2017-07-02	3:22:39	0.140729	Tuesday	2	19	2017-02-07 03:22	46
NACC3	NACC320170207012003.csv.20170207042243150		2/7/2017	4:20:03	2017-07-02	4:22:43	0.182442	Tuesday	2	19	2017-02-07 04:22	46
NACC3	NACC320170207042015.csv.20170207072256577		2/7/2017	7:20:15	2017-07-02	7:22:56	0.307593	Tuesday	2	19	2017-02-07 07:22	46
NACC3	NACC320170207042113.csv.20170207072256970		2/7/2017	7:21:13	2017-07-02	7:22:56	0.307593	Tuesday	2	19	2017-02-07 07:22	46
NACC3	NACC320170207062002.csv.20170207092232285		2/7/2017	9:20:02	2017-07-02	9:22:32	0.390648	Tuesday	2	19	2017-02-07 09:22	46
NACC3	NACC320170207062102.csv.20170207092232578		2/7/2017	9:21:02	2017-07-02	9:22:32	0.390648	Tuesday	2	19	2017-02-07 09:22	46
NACC3	NACC320170207072007.csv.20170207102236543		2/7/2017	10:20:07	2017-07-02	10:22:36	0.432361	Tuesday	2	19	2017-02-07 10:22	46
NACC3	NACC320170207072102.csv.20170207102236822		2/7/2017	10:21:02	2017-07-02	10:22:36	0.432361	Tuesday	2	19	2017-02-07 10:22	46
NACC3	NACC320170207082102.csv.20170207112248111		2/7/2017	11:21:02	2017-07-02	11:22:48	0.474167	Tuesday	2	19	2017-02-07 11:22	46
NACC3	NACC320170207092004.csv.20170207122056243		2/7/2017	12:20:04	2017-07-02	12:20:56	0.514537	Tuesday	2	19	2017-02-07 12:20	46
NACC3	NACC320170207092102.csv.20170207122256697		2/7/2017	12:21:02	2017-07-02	12:22:56	0.515926	Tuesday	2	19	2017-02-07 12:22	46
NACC3	NACC320170207102004.csv.20170207132100360		2/7/2017	13:20:04	2017-07-02	13:21:00	0.55625	Tuesday	2	19	2017-02-07 13:21	46
NACC3	NACC320170207102102.csv.20170207132300767		2/7/2017	13:21:02	2017-07-02	13:23:00	0.557639	Tuesday	2	19	2017-02-07 13:23	46
NACC3	NACC320170207172004.csv.20170207202129194		2/7/2017	20:20:04	2017-07-02	20:21:29	0.848252	Tuesday	2	19	2017-02-07 20:21	46
NACC3	NACC320170207172102.csv.20170207202329518		2/7/2017	20:21:02	2017-07-02	20:23:29	0.849641	Tuesday	2	19	2017-02-07 20:23	46
NACC3	NACC320170207182004.csv.20170207212134474		2/7/2017	21:20:04	2017-07-02	21:21:34	0.889977	Tuesday	2	19	2017-02-07 21:21	46
NACC3	NACC320170207192101.csv.20170207222338213		2/7/2017	22:21:01	2017-07-02	22:23:38	0.933079	Tuesday	2	19	2017-02-07 22:23	46
NACC3	NACC320170207202002.csv.20170207232142022		2/7/2017	23:20:02	2017-07-02	23:21:42	0.973403	Tuesday	2	19	2017-02-07 23:21	46
NACC3	NACC320170207202102.csv.20170207232342448		2/7/2017	23:21:02	2017-07-02	23:23:42	0.974792	Tuesday	2	19	2017-02-07 23:23	46
NACC3	NACC320170207212017.csv.20170208002345611		2/8/2017	0:20:17	2017-08-02	0:23:45	0.016493	Wednesday	3	19	2017-02-08 00:23	47
NACC3	NACC320170207212130.csv.20170208002345978		2/8/2017	0:21:30	2017-08-02	0:23:45	0.016493	Wednesday	3	19	2017-02-08 00:23	47
NACC3	NACC320170207232008.csv.20170208022121215		2/8/2017	2:20:08	2017-08-02	2:21:21	0.09816	Wednesday	3	19	2017-02-08 02:21	47
NACC3	NACC320170207232101.csv.20170208022321649		2/8/2017	2:21:01	2017-08-02	2:23:21	0.099549	Wednesday	3	19	2017-02-08 02:23	47
NACC3	NACC320170208002102.csv.20170208032124613		2/8/2017	3:21:02	2017-08-02	3:21:24	0.139861	Wednesday	3	19	2017-02-08 03:21	47
NACC3	NACC320170208012027.csv.20170208042127705		2/8/2017	4:20:27	2017-08-02	4:21:27	0.181563	Wednesday	3	19	2017-02-08 04:21	47
NACC3	NACC320170208012113.csv.20170208042328000		2/8/2017	4:21:13	2017-08-02	4:23:28	0.182963	Wednesday	3	19	2017-02-08 04:23	47
NACC3	NACC320170208042020.csv.20170208072141757		2/8/2017	7:20:20	2017-08-02	7:21:41	0.306725	Wednesday	3	19	2017-02-08 07:21	47
NACC3	NACC320170208042117.csv.20170208072342158		2/8/2017	7:21:17	2017-08-02	7:23:42	0.308125	Wednesday	3	19	2017-02-08 07:23	47
NACC3	NACC320170208062006.csv.20170208092148874		2/8/2017	9:20:06	2017-08-02	9:21:48	0.390139	Wednesday	3	19	2017-02-08 09:21	47
NACC3	NACC320170208062102.csv.20170208092149437		2/8/2017	9:21:02	2017-08-02	9:21:49	0.39015	Wednesday	3	19	2017-02-08 09:21	47
NACC3	NACC320170208082004.csv.20170208112206485		2/8/2017	11:20:04	2017-08-02	11:22:06	0.473681	Wednesday	3	19	2017-02-08 11:22	47
NACC3	NACC320170208082102.csv.20170208112207106		2/8/2017	11:21:02	2017-08-02	11:22:07	0.473692	Wednesday	3	19	2017-02-08 11:22	47
NACC3	NACC320170208092006.csv.20170208122216676		2/8/2017	12:20:06	2017-08-02	12:22:16	0.515463	Wednesday	3	19	2017-02-08 12:22	47
NACC3	NACC320170208092102.csv.20170208122217063		2/8/2017	12:21:02	2017-08-02	12:22:17	0.515475	Wednesday	3	19	2017-02-08 12:22	47
NACC3	NACC320170208102102.csv.20170208132221093		2/8/2017	13:21:02	2017-08-02	13:22:21	0.557188	Wednesday	3	19	2017-02-08 13:22	47
NACC3	NACC320170208172008.csv.20170208202251622		2/8/2017	20:20:08	2017-08-02	20:22:51	0.849201	Wednesday	3	19	2017-02-08 20:22	47
NACC3	NACC320170208172102.csv.20170208202251917		2/8/2017	20:21:02	2017-08-02	20:22:51	0.849201	Wednesday	3	19	2017-02-08 20:22	47
NACC3	NACC320170208192004.csv.20170208222258961		2/8/2017	22:20:04	2017-08-02	22:22:58	0.932616	Wednesday	3	19	2017-02-08 22:22	47
NACC3	NACC320170208192103.csv.20170208222259276		2/8/2017	22:21:03	2017-08-02	22:22:59	0.932627	Wednesday	3	19	2017-02-08 22:22	47
NACC3	NACC320170208212015.csv.20170209002105693		2/9/2017	0:20:15	2017-09-02	0:21:05	0.014641	Thursday	4	19	2017-02-09 00:21	48
NACC3	NACC320170208212109.csv.20170209002307047		2/9/2017	0:21:09	2017-09-02	0:23:07	0.016053	Thursday	4	19	2017-02-09 00:23	48
NACC3	NACC320170208222041.csv.20170209012310556		2/9/2017	1:20:41	2017-09-02	1:23:10	0.057755	Thursday	4	19	2017-02-09 01:23	48
NACC3	NACC320170208222113.csv.20170209012310855		2/9/2017	1:21:13	2017-09-02	1:23:10	0.057755	Thursday	4	19	2017-02-09 01:23	48
NACC3	NACC320170209002002.csv.20170209032047665		2/9/2017	3:20:02	2017-09-02	3:20:47	0.139433	Thursday	4	19	2017-02-09 03:20	48
NACC3	NACC320170209002102.csv.20170209032248184		2/9/2017	3:21:02	2017-09-02	3:22:48	0.140833	Thursday	4	19	2017-02-09 03:22	48
NACC3	NACC320170209012005.csv.20170209042251314		2/9/2017	4:20:05	2017-09-02	4:22:51	0.182535	Thursday	4	19	2017-02-09 04:22	48
NACC3	NACC320170209042002.csv.20170209072102276		2/9/2017	7:20:02	2017-09-02	7:21:02	0.306273	Thursday	4	19	2017-02-09 07:21	48
NACC3	NACC320170209042102.csv.20170209072302789		2/9/2017	7:21:02	2017-09-02	7:23:02	0.307662	Thursday	4	19	2017-02-09 07:23	48
NACC3	NACC320170209052007.csv.20170209082104523		2/9/2017	8:20:07	2017-09-02	8:21:04	0.347963	Thursday	4	19	2017-02-09 08:21	48
NACC3	NACC320170209052101.csv.20170209082305025		2/9/2017	8:21:01	2017-09-02	8:23:05	0.349363	Thursday	4	19	2017-02-09 08:23	48
NACC3	NACC320170209062102.csv.20170209092309192		2/9/2017	9:21:02	2017-09-02	9:23:09	0.391076	Thursday	4	19	2017-02-09 09:23	48
NACC3	NACC320170209072001.csv.20170209102115199		2/9/2017	10:20:01	2017-09-02	10:21:15	0.431424	Thursday	4	19	2017-02-09 10:21	48
NACC3	NACC320170209072102.csv.20170209102315512		2/9/2017	10:21:02	2017-09-02	10:23:15	0.432813	Thursday	4	19	2017-02-09 10:23	48
NACC3	NACC320170209082003.csv.20170209112124813._ADS		2/9/2017	11:20:03	2017-09-02	11:21:24	0.473194	Thursday	4	19	2017-02-09 11:21	48
NACC3	NACC320170209082003.csv.20170209112124813		2/9/2017	11:20:03	2017-09-02	11:21:24	0.473194	Thursday	4	19	2017-02-09 11:21	48
NACC3	NACC320170209092006.csv.20170209122144651		2/9/2017	12:20:06	2017-09-02	12:21:44	0.515093	Thursday	4	19	2017-02-09 12:21	48
NACC3	NACC320170209092102.csv.20170209122344940._ADS		2/9/2017	12:21:02	2017-09-02	12:23:44	0.516481	Thursday	4	19	2017-02-09 12:23	48
NACC3	NACC320170209092102.csv.20170209122344940		2/9/2017	12:21:02	2017-09-02	12:23:44	0.516481	Thursday	4	19	2017-02-09 12:23	48
NACC3	NACC320170209102102.csv.20170209132149034		2/9/2017	13:21:02	2017-09-02	13:21:49	0.556817	Thursday	4	19	2017-02-09 13:21	48
NACC3	NACC320170209172003.csv.20170209202218155		2/9/2017	20:20:03	2017-09-02	20:22:18	0.848819	Thursday	4	19	2017-02-09 20:22	48
NACC3	NACC320170209172102.csv.20170209202218423		2/9/2017	20:21:02	2017-09-02	20:22:18	0.848819	Thursday	4	19	2017-02-09 20:22	48
NACC3	NACC320170209182007.csv.20170209212153230		2/9/2017	21:20:07	2017-09-02	21:21:53	0.890197	Thursday	4	19	2017-02-09 21:21	48
NACC3	NACC320170209182102.csv.20170209212353676		2/9/2017	21:21:02	2017-09-02	21:23:53	0.891586	Thursday	4	19	2017-02-09 21:23	48
NACC3	NACC320170209192102.csv.20170209222156868		2/9/2017	22:21:02	2017-09-02	22:21:56	0.931898	Thursday	4	19	2017-02-09 22:21	48
NACC3	NACC320170209202007.csv.20170209232200475		2/9/2017	23:20:07	2017-09-02	23:22:00	0.973611	Thursday	4	19	2017-02-09 23:22	48
NACC3	NACC320170209212013.csv.20170210002203480		2/10/2017	0:20:13	2017-10-02	0:22:03	0.015313	Friday	5	19	2017-02-10 00:22	49
NACC3	NACC320170209212110.csv.20170210002403865		2/10/2017	0:21:10	2017-10-02	0:24:03	0.016701	Friday	5	19	2017-02-10 00:24	49
NACC3	NACC320170209232002.csv.20170210022210606		2/10/2017	2:20:02	2017-10-02	2:22:10	0.098727	Friday	5	19	2017-02-10 02:22	49
NACC3	NACC320170209232101.csv.20170210022211013		2/10/2017	2:21:01	2017-10-02	2:22:11	0.098738	Friday	5	19	2017-02-10 02:22	49
NACC3	NACC320170210002002.csv.20170210032216132		2/10/2017	3:20:02	2017-10-02	3:22:16	0.140463	Friday	5	19	2017-02-10 03:22	49
NACC3	NACC320170210002104.csv.20170210032416434		2/10/2017	3:21:04	2017-10-02	3:24:16	0.141852	Friday	5	19	2017-02-10 03:24	49
NACC3	NACC320170210012003.csv.20170210042218530		2/10/2017	4:20:03	2017-10-02	4:22:18	0.182153	Friday	5	19	2017-02-10 04:22	49
NACC3	NACC320170210042005.csv.20170210072232768		2/10/2017	7:20:05	2017-10-02	7:22:32	0.307315	Friday	5	19	2017-02-10 07:22	49
NACC3	NACC320170210042102.csv.20170210072233080		2/10/2017	7:21:02	2017-10-02	7:22:33	0.307326	Friday	5	19	2017-02-10 07:22	49
NACC3	NACC320170210062001.csv.20170210092208391		2/10/2017	9:20:01	2017-10-02	9:22:08	0.39037	Friday	5	19	2017-02-10 09:22	49
NACC3	NACC320170210062101.csv.20170210092208742		2/10/2017	9:21:01	2017-10-02	9:22:08	0.39037	Friday	5	19	2017-02-10 09:22	49
NACC3	NACC320170210072006.csv.20170210102212506		2/10/2017	10:20:06	2017-10-02	10:22:12	0.432083	Friday	5	19	2017-02-10 10:22	49
NACC3	NACC320170210072101.csv.20170210102212850		2/10/2017	10:21:01	2017-10-02	10:22:12	0.432083	Friday	5	19	2017-02-10 10:22	49
NACC3	NACC320170210082102.csv.20170210112326663		2/10/2017	11:21:02	2017-10-02	11:23:26	0.474606	Friday	5	19	2017-02-10 11:23	49
NACC3	NACC320170210092002.csv.20170210122107174		2/10/2017	12:20:02	2017-10-02	12:21:07	0.514664	Friday	5	19	2017-02-10 12:21	49
NACC3	NACC320170210092103.csv.20170210122307552		2/10/2017	12:21:03	2017-10-02	12:23:07	0.516053	Friday	5	19	2017-02-10 12:23	49
NACC3	NACC320170210102003.csv.20170210132111540		2/10/2017	13:20:03	2017-10-02	13:21:11	0.556377	Friday	5	19	2017-02-10 13:21	49
NACC3	NACC320170210102102.csv.20170210132312020		2/10/2017	13:21:02	2017-10-02	13:23:12	0.557778	Friday	5	19	2017-02-10 13:23	49
NACC3	NACC320170210172007.csv.20170210202139709		2/10/2017	20:20:07	2017-10-02	20:21:39	0.848368	Friday	5	19	2017-02-10 20:21	49
NACC3	NACC320170210172101.csv.20170210202340324		2/10/2017	20:21:01	2017-10-02	20:23:40	0.849769	Friday	5	19	2017-02-10 20:23	49
NACC3	NACC320170210182102.csv.20170210212344334		2/10/2017	21:21:02	2017-10-02	21:23:44	0.891481	Friday	5	19	2017-02-10 21:23	49
NACC3	NACC320170210192002.csv.20170210222147025		2/10/2017	22:20:02	2017-10-02	22:21:47	0.931794	Friday	5	19	2017-02-10 22:21	49
NACC3	NACC320170210192102.csv.20170210222347733		2/10/2017	22:21:02	2017-10-02	22:23:47	0.933183	Friday	5	19	2017-02-10 22:23	49
NACC3	NACC320170210202002.csv.20170210232151087		2/10/2017	23:20:02	2017-10-02	23:21:51	0.973507	Friday	5	19	2017-02-10 23:21	49
NACC3	NACC320170212212002.csv.20170213002023679		2/13/2017	0:20:02	2017-13-02	0:20:23	0.014155	Monday	1	19	2017-13-2 0:20:23	50
NACC3	NACC320170212212102.csv.20170213002224036		2/13/2017	0:21:02	2017-13-02	0:22:24	0.015556	Monday	1	19	2017-13-2 0:22:24	50
NACC3	NACC320170212222005.csv.20170213012226700		2/13/2017	1:20:05	2017-13-02	1:22:26	0.057245	Monday	1	19	2017-13-2 1:22:26	50
NACC3	NACC320170212222102.csv.20170213012226897		2/13/2017	1:21:02	2017-13-02	1:22:26	0.057245	Monday	1	19	2017-13-2 1:22:26	50
NACC3	NACC320170213002006.csv.20170213032033788		2/13/2017	3:20:06	2017-13-02	3:20:33	0.139271	Monday	1	19	2017-13-2 3:20:33	50
NACC3	NACC320170213002101.csv.20170213032234071		2/13/2017	3:21:01	2017-13-02	3:22:34	0.140671	Monday	1	19	2017-13-2 3:22:34	50
NACC3	NACC320170213012006.csv.20170213042235430		2/13/2017	4:20:06	2017-13-02	4:22:35	0.18235	Monday	1	19	2017-13-2 4:22:35	50
NACC3	NACC320170213012102.csv.20170213042235780		2/13/2017	4:21:02	2017-13-02	4:22:35	0.18235	Monday	1	19	2017-13-2 4:22:35	50
NACC3	NACC320170213042025.csv.20170213072246816		2/13/2017	7:20:25	2017-13-02	7:22:46	0.307477	Monday	1	19	2017-13-2 7:22:46	50
NACC3	NACC320170213042121.csv.20170213072247180		2/13/2017	7:21:21	2017-13-02	7:22:47	0.307488	Monday	1	19	2017-13-2 7:22:47	50
NACC3	NACC320170213062001.csv.20170213092052553		2/13/2017	9:20:01	2017-13-02	9:20:52	0.389491	Monday	1	19	2017-13-2 9:20:52	50
NACC3	NACC320170213062102.csv.20170213092252914		2/13/2017	9:21:02	2017-13-02	9:22:52	0.39088	Monday	1	19	2017-13-2 9:22:52	50
NACC3	NACC320170213072005.csv.20170213102257064		2/13/2017	10:20:05	2017-13-02	10:22:57	0.432604	Monday	1	19	2017-13-2 10:22:57	50
NACC3	NACC320170213082102.csv.20170213112258234		2/13/2017	11:21:02	2017-13-02	11:22:58	0.474282	Monday	1	19	2017-13-2 11:22:58	50
NACC3	NACC320170213092003.csv.20170213122103596		2/13/2017	12:20:03	2017-13-02	12:21:03	0.514618	Monday	1	19	2017-13-2 12:21:03	50
NACC3	NACC320170213092102.csv.20170213122304038		2/13/2017	12:21:02	2017-13-02	12:23:04	0.516019	Monday	1	19	2017-13-2 12:23:04	50
NACC3	NACC320170213102102.csv.20170213132310133		2/13/2017	13:21:02	2017-13-02	13:23:10	0.557755	Monday	1	19	2017-13-2 13:23:10	50
NACC3	NACC320170213172007.csv.20170213202134492		2/13/2017	20:20:07	2017-13-02	20:21:34	0.84831	Monday	1	19	2017-13-2 20:21:34	50
NACC3	NACC320170213172102.csv.20170213202134750		2/13/2017	20:21:02	2017-13-02	20:21:34	0.84831	Monday	1	19	2017-13-2 20:21:34	50
NACC3	NACC320170213182102.csv.20170213212138606		2/13/2017	21:21:02	2017-13-02	21:21:38	0.890023	Monday	1	19	2017-13-2 21:21:38	50
NACC3	NACC320170213192009.csv.20170213222141159		2/13/2017	22:20:09	2017-13-02	22:21:41	0.931725	Monday	1	19	2017-13-2 22:21:41	50
NACC3	NACC320170213202102.csv.20170213232344038		2/13/2017	23:21:02	2017-13-02	23:23:44	0.974815	Monday	1	19	2017-13-2 23:23:44	50
NACC3	NACC320170213212001.csv.20170214002146779		2/14/2017	0:20:01	2017-14-02	0:21:46	0.015116	Tuesday	2	19	2017-14-2 0:21:46	51
NACC3	NACC320170213222002.csv.20170214012149360		2/14/2017	1:20:02	2017-14-02	1:21:49	0.056817	Tuesday	2	19	2017-14-2 1:21:49	51
NACC3	NACC320170213222101.csv.20170214012149813		2/14/2017	1:21:01	2017-14-02	1:21:49	0.056817	Tuesday	2	19	2017-14-2 1:21:49	51
NACC3	NACC320170213232002.csv.20170214022152615		2/14/2017	2:20:02	2017-14-02	2:21:52	0.098519	Tuesday	2	19	2017-14-2 2:21:52	51
NACC3	NACC320170213232101.csv.20170214022353190		2/14/2017	2:21:01	2017-14-02	2:23:53	0.099919	Tuesday	2	19	2017-14-2 2:23:53	51
NACC3	NACC320170214002005.csv.20170214032156026		2/14/2017	3:20:05	2017-14-02	3:21:56	0.140231	Tuesday	2	19	2017-14-2 3:21:56	51
NACC3	NACC320170214002101.csv.20170214032156409		2/14/2017	3:21:01	2017-14-02	3:21:56	0.140231	Tuesday	2	19	2017-14-2 3:21:56	51
NACC3	NACC320170214012006.csv.20170214042159347		2/14/2017	4:20:06	2017-14-02	4:21:59	0.181933	Tuesday	2	19	2017-14-2 4:21:59	51
NACC3	NACC320170214012101.csv.20170214042159511		2/14/2017	4:21:01	2017-14-02	4:21:59	0.181933	Tuesday	2	19	2017-14-2 4:21:59	51
NACC3	NACC320170214042144.csv.20170214072342197		2/14/2017	7:21:44	2017-14-02	7:23:42	0.308125	Tuesday	2	19	2017-14-2 7:23:42	51
NACC3	NACC320170214042326.csv.20170214072542681		2/14/2017	7:23:26	2017-14-02	7:25:42	0.309514	Tuesday	2	19	2017-14-2 7:25:42	51
NACC3	NACC320170214062002.csv.20170214092147728		2/14/2017	9:20:02	2017-14-02	9:21:47	0.390127	Tuesday	2	19	2017-14-2 9:21:47	51
NACC3	NACC320170214062102.csv.20170214092148023		2/14/2017	9:21:02	2017-14-02	9:21:48	0.390139	Tuesday	2	19	2017-14-2 9:21:48	51
NACC3	NACC320170214072006.csv.20170214102203582		2/14/2017	10:20:06	2017-14-02	10:22:03	0.431979	Tuesday	2	19	2017-14-2 10:22:03	51
NACC3	NACC320170214072102.csv.20170214102203909		2/14/2017	10:21:02	2017-14-02	10:22:03	0.431979	Tuesday	2	19	2017-14-2 10:22:03	51
NACC3	NACC320170214092006.csv.20170214122213596		2/14/2017	12:20:06	2017-14-02	12:22:13	0.515428	Tuesday	2	19	2017-14-2 12:22:13	51
NACC3	NACC320170214092102.csv.20170214122213945		2/14/2017	12:21:02	2017-14-02	12:22:13	0.515428	Tuesday	2	19	2017-14-2 12:22:13	51
NACC3	NACC320170214102102.csv.20170214132218655		2/14/2017	13:21:02	2017-14-02	13:22:18	0.557153	Tuesday	2	19	2017-14-2 13:22:18	51
NACC3	NACC320170214172006.csv.20170214202215333		2/14/2017	20:20:06	2017-14-02	20:22:15	0.848785	Tuesday	2	19	2017-14-2 20:22:15	51
NACC3	NACC320170214172102.csv.20170214202215677		2/14/2017	20:21:02	2017-14-02	20:22:15	0.848785	Tuesday	2	19	2017-14-2 20:22:15	51
NACC3	NACC320170214192003.csv.20170214222224312		2/14/2017	22:20:03	2017-14-02	22:22:24	0.932222	Tuesday	2	19	2017-14-2 22:22:24	51
NACC3	NACC320170214192101.csv.20170214222224626		2/14/2017	22:21:01	2017-14-02	22:22:24	0.932222	Tuesday	2	19	2017-14-2 22:22:24	51
NACC3	NACC320170214202010.csv.20170214232227257		2/14/2017	23:20:10	2017-14-02	23:22:27	0.973924	Tuesday	2	19	2017-14-2 23:22:27	51
NACC3	NACC320170214202101.csv.20170214232227687		2/14/2017	23:21:01	2017-14-02	23:22:27	0.973924	Tuesday	2	19	2017-14-2 23:22:27	51
NACC3	NACC320170214212010.csv.20170215002231064		2/15/2017	0:20:10	2017-15-02	0:22:31	0.015637	Wednesday	3	19	2017-15-2 0:22:31	52
NACC3	NACC320170214212103.csv.20170215002231196		2/15/2017	0:21:03	2017-15-02	0:22:31	0.015637	Wednesday	3	19	2017-15-2 0:22:31	52
NACC3	NACC320170214222105.csv.20170215012234647		2/15/2017	1:21:05	2017-15-02	1:22:34	0.057338	Wednesday	3	19	2017-15-2 1:22:34	52
NACC3	NACC320170214232002.csv.20170215022039326		2/15/2017	2:20:02	2017-15-02	2:20:39	0.097674	Wednesday	3	19	2017-15-2 2:20:39	52
NACC3	NACC320170215002005.csv.20170215032242562		2/15/2017	3:20:05	2017-15-02	3:22:42	0.140764	Wednesday	3	19	2017-15-2 3:22:42	52
NACC3	NACC320170215002102.csv.20170215032242696		2/15/2017	3:21:02	2017-15-02	3:22:42	0.140764	Wednesday	3	19	2017-15-2 3:22:42	52
NACC3	NACC320170215012101.csv.20170215042245432		2/15/2017	4:21:01	2017-15-02	4:22:45	0.182465	Wednesday	3	19	2017-15-2 4:22:45	52
NACC3	NACC320170215042007.csv.20170215072058513		2/15/2017	7:20:07	2017-15-02	7:20:58	0.306227	Wednesday	3	19	2017-15-2 7:20:58	52
NACC3	NACC320170215042117.csv.20170215072258856		2/15/2017	7:21:17	2017-15-02	7:22:58	0.307616	Wednesday	3	19	2017-15-2 7:22:58	52
NACC3	NACC320170215062002.csv.20170215092107112		2/15/2017	9:20:02	2017-15-02	9:21:07	0.389664	Wednesday	3	19	2017-15-2 9:21:07	52
NACC3	NACC320170215062102.csv.20170215092308119		2/15/2017	9:21:02	2017-15-02	9:23:08	0.391065	Wednesday	3	19	2017-15-2 9:23:08	52
NACC3	NACC320170215072002.csv.20170215102113136		2/15/2017	10:20:02	2017-15-02	10:21:13	0.4314	Wednesday	3	19	2017-15-2 10:21:13	52
NACC3	NACC320170215082003.csv.20170215112323672		2/15/2017	11:20:03	2017-15-02	11:23:23	0.474572	Wednesday	3	19	2017-15-2 11:23:23	52
NACC3	NACC320170215082102.csv.20170215112325040._ADS		2/15/2017	11:21:02	2017-15-02	11:23:25	0.474595	Wednesday	3	19	2017-15-2 11:23:25	52
NACC3	NACC320170215082102.csv.20170215112325040		2/15/2017	11:21:02	2017-15-02	11:23:25	0.474595	Wednesday	3	19	2017-15-2 11:23:25	52
NACC3	NACC320170215092007.csv.20170215122136814		2/15/2017	12:20:07	2017-15-02	12:21:36	0.515	Wednesday	3	19	2017-15-2 12:21:36	52
NACC3	NACC320170215092102.csv.20170215122337213		2/15/2017	12:21:02	2017-15-02	12:23:37	0.5164	Wednesday	3	19	2017-15-2 12:23:37	52
NACC3	NACC320170215102102.csv.20170215132311094		2/15/2017	13:21:02	2017-15-02	13:23:11	0.557766	Wednesday	3	19	2017-15-2 13:23:11	52
NACC3	NACC320170215172003.csv.20170215202210437		2/15/2017	20:20:03	2017-15-02	20:22:10	0.848727	Wednesday	3	19	2017-15-2 20:22:10	52
NACC3	NACC320170215172102.csv.20170215202210828		2/15/2017	20:21:02	2017-15-02	20:22:10	0.848727	Wednesday	3	19	2017-15-2 20:22:10	52
NACC3	NACC320170215182006.csv.20170215212215624		2/15/2017	21:20:06	2017-15-02	21:22:15	0.890451	Wednesday	3	19	2017-15-2 21:22:15	52
NACC3	NACC320170215182102.csv.20170215212416237		2/15/2017	21:21:02	2017-15-02	21:24:16	0.891852	Wednesday	3	19	2017-15-2 21:24:16	52
NACC3	NACC320170215202004.csv.20170215232150061		2/15/2017	23:20:04	2017-15-02	23:21:50	0.973495	Wednesday	3	19	2017-15-2 23:21:50	52
NACC3	NACC320170215202101.csv.20170215232150413		2/15/2017	23:21:01	2017-15-02	23:21:50	0.973495	Wednesday	3	19	2017-15-2 23:21:50	52
NACC3	NACC320170215212105.csv.20170216002354972		2/16/2017	0:21:05	2017-16-02	0:23:54	0.016597	Thursday	4	19	2017-16-2 0:23:54	53
NACC3	NACC320170215222010.csv.20170216012158323		2/16/2017	1:20:10	2017-16-02	1:21:58	0.056921	Thursday	4	19	2017-16-2 1:21:58	53
NACC3	NACC320170215222114.csv.20170216012158626		2/16/2017	1:21:14	2017-16-02	1:21:58	0.056921	Thursday	4	19	2017-16-2 1:21:58	53
NACC3	NACC320170216002002.csv.20170216032210032		2/16/2017	3:20:02	2017-16-02	3:22:10	0.140394	Thursday	4	19	2017-16-2 3:22:10	53
NACC3	NACC320170216002147.csv.20170216032410630		2/16/2017	3:21:47	2017-16-02	3:24:10	0.141782	Thursday	4	19	2017-16-2 3:24:10	53
NACC3	NACC320170216012007.csv.20170216042213582		2/16/2017	4:20:07	2017-16-02	4:22:13	0.182095	Thursday	4	19	2017-16-2 4:22:13	53
NACC3	NACC320170216042002.csv.20170216072225259		2/16/2017	7:20:02	2017-16-02	7:22:25	0.307234	Thursday	4	19	2017-16-2 7:22:25	53
NACC3	NACC320170216042102.csv.20170216072225602		2/16/2017	7:21:02	2017-16-02	7:22:25	0.307234	Thursday	4	19	2017-16-2 7:22:25	53
NACC3	NACC320170216052007.csv.20170216082227631		2/16/2017	8:20:07	2017-16-02	8:22:27	0.348924	Thursday	4	19	2017-16-2 8:22:27	53
NACC3	NACC320170216052102.csv.20170216082227923		2/16/2017	8:21:02	2017-16-02	8:22:27	0.348924	Thursday	4	19	2017-16-2 8:22:27	53
NACC3	NACC320170216072005.csv.20170216102237267		2/16/2017	10:20:05	2017-16-02	10:22:37	0.432373	Thursday	4	19	2017-16-2 10:22:37	53
NACC3	NACC320170216072101.csv.20170216102237555		2/16/2017	10:21:01	2017-16-02	10:22:37	0.432373	Thursday	4	19	2017-16-2 10:22:37	53
NACC3	NACC320170216082102.csv.20170216112246049		2/16/2017	11:21:02	2017-16-02	11:22:46	0.474144	Thursday	4	19	2017-16-2 11:22:46	53
NACC3	NACC320170216092002.csv.20170216122253385		2/16/2017	12:20:02	2017-16-02	12:22:53	0.515891	Thursday	4	19	2017-16-2 12:22:53	53
NACC3	NACC320170216092102.csv.20170216122253760		2/16/2017	12:21:02	2017-16-02	12:22:53	0.515891	Thursday	4	19	2017-16-2 12:22:53	53
NACC3	NACC320170216102002.csv.20170216132056663		2/16/2017	13:20:02	2017-16-02	13:20:56	0.556204	Thursday	4	19	2017-16-2 13:20:56	53
NACC3	NACC320170216102102.csv.20170216132257033		2/16/2017	13:21:02	2017-16-02	13:22:57	0.557604	Thursday	4	19	2017-16-2 13:22:57	53
NACC3	NACC320170216172006.csv.20170216202056075		2/16/2017	20:20:06	2017-16-02	20:20:56	0.84787	Thursday	4	19	2017-16-2 20:20:56	53
NACC3	NACC320170216172102.csv.20170216202256509		2/16/2017	20:21:02	2017-16-02	20:22:56	0.849259	Thursday	4	19	2017-16-2 20:22:56	53
NACC3	NACC320170216192007.csv.20170216222107051		2/16/2017	22:20:07	2017-16-02	22:21:07	0.931331	Thursday	4	19	2017-16-2 22:21:07	53
NACC3	NACC320170216192102.csv.20170216222307571		2/16/2017	22:21:02	2017-16-02	22:23:07	0.93272	Thursday	4	19	2017-16-2 22:23:07	53
NACC3	NACC320170216202102.csv.20170216232310468		2/16/2017	23:21:02	2017-16-02	23:23:10	0.974421	Thursday	4	19	2017-16-2 23:23:10	53
NACC3	NACC320170216212014.csv.20170217002115897		2/17/2017	0:20:14	2017-17-02	0:21:15	0.014757	Friday	5	19	2017-17-2 0:21:15	54
NACC3	NACC320170216222107.csv.20170217012322269		2/17/2017	1:21:07	2017-17-02	1:23:22	0.057894	Friday	5	19	2017-17-2 1:23:22	54
NACC3	NACC320170216232003.csv.20170217022126919		2/17/2017	2:20:03	2017-17-02	2:21:26	0.098218	Friday	5	19	2017-17-2 2:21:26	54
NACC3	NACC320170217002004.csv.20170217032138468		2/17/2017	3:20:04	2017-17-02	3:21:38	0.140023	Friday	5	19	2017-17-2 3:21:38	54
NACC3	NACC320170217002102.csv.20170217032338806		2/17/2017	3:21:02	2017-17-02	3:23:38	0.141412	Friday	5	19	2017-17-2 3:23:38	54
NACC3	NACC320170217012008.csv.20170217042112276		2/17/2017	4:20:08	2017-17-02	4:21:12	0.181389	Friday	5	19	2017-17-2 4:21:12	54
NACC3	NACC320170217012102.csv.20170217042312680		2/17/2017	4:21:02	2017-17-02	4:23:12	0.182778	Friday	5	19	2017-17-2 4:23:12	54
NACC3	NACC320170217042002.csv.20170217072124487		2/17/2017	7:20:02	2017-17-02	7:21:24	0.306528	Friday	5	19	2017-17-2 7:21:24	54
NACC3	NACC320170217042102.csv.20170217072324828._ADS		2/17/2017	7:21:02	2017-17-02	7:23:24	0.307917	Friday	5	19	2017-17-2 7:23:24	54
NACC3	NACC320170217042102.csv.20170217072324828		2/17/2017	7:21:02	2017-17-02	7:23:24	0.307917	Friday	5	19	2017-17-2 7:23:24	54
NACC3	NACC320170217052002.csv.20170217082126494		2/17/2017	8:20:02	2017-17-02	8:21:26	0.348218	Friday	5	19	2017-17-2 8:21:26	54
NACC3	NACC320170217062002.csv.20170217092130943		2/17/2017	9:20:02	2017-17-02	9:21:30	0.389931	Friday	5	19	2017-17-2 9:21:30	54
NACC3	NACC320170217062103.csv.20170217092331336		2/17/2017	9:21:03	2017-17-02	9:23:31	0.391331	Friday	5	19	2017-17-2 9:23:31	54
NACC3	NACC320170217072002.csv.20170217102140099		2/17/2017	10:20:02	2017-17-02	10:21:40	0.431713	Friday	5	19	2017-17-2 10:21:40	54
NACC3	NACC320170217082005.csv.20170217112200324		2/17/2017	11:20:05	2017-17-02	11:22:00	0.473611	Friday	5	19	2017-17-2 11:22:00	54
NACC3	NACC320170217082101.csv.20170217112401364		2/17/2017	11:21:01	2017-17-02	11:24:01	0.475012	Friday	5	19	2017-17-2 11:24:01	54
NACC3	NACC320170217092102.csv.20170217122207888		2/17/2017	12:21:02	2017-17-02	12:22:07	0.515359	Friday	5	19	2017-17-2 12:22:07	54
NACC3	NACC320170217102002.csv.20170217132210834		2/17/2017	13:20:02	2017-17-02	13:22:10	0.55706	Friday	5	19	2017-17-2 13:22:10	54
NACC3	NACC320170217102102.csv.20170217132211257		2/17/2017	13:21:02	2017-17-02	13:22:11	0.557072	Friday	5	19	2017-17-2 13:22:11	54
NACC3	NACC320170217172014.csv.20170217202210505		2/17/2017	20:20:14	2017-17-02	20:22:10	0.848727	Friday	5	19	2017-17-2 20:22:10	54
NACC3	NACC320170217172101.csv.20170217202210894		2/17/2017	20:21:01	2017-17-02	20:22:10	0.848727	Friday	5	19	2017-17-2 20:22:10	54
NACC3	NACC320170217182101.csv.20170217212219381		2/17/2017	21:21:01	2017-17-02	21:22:19	0.890498	Friday	5	19	2017-17-2 21:22:19	54
NACC3	NACC320170217192007.csv.20170217222222944		2/17/2017	22:20:07	2017-17-02	22:22:22	0.932199	Friday	5	19	2017-17-2 22:22:22	54
NACC3	NACC320170217192101.csv.20170217222223411		2/17/2017	22:21:01	2017-17-02	22:22:23	0.932211	Friday	5	19	2017-17-2 22:22:23	54
NACC3	NACC320170217202101.csv.20170217232225939		2/17/2017	23:21:01	2017-17-02	23:22:25	0.9739	Friday	5	19	2017-17-2 23:22:25	54
NACC3	NACC320170219222004.csv.20170220012123059		2/20/2017	1:20:04	2017-20-02	1:21:23	0.056516	Monday	1	19	2017-20-2 1:21:23	55
NACC3	NACC320170219222102.csv.20170220012323407		2/20/2017	1:21:02	2017-20-02	1:23:23	0.057905	Monday	1	19	2017-20-2 1:23:23	55
NACC3	NACC320170220002002.csv.20170220032131250		2/20/2017	3:20:02	2017-20-02	3:21:31	0.139942	Monday	1	19	2017-20-2 3:21:31	55
NACC3	NACC320170220002101.csv.20170220032331585		2/20/2017	3:21:01	2017-20-02	3:23:31	0.141331	Monday	1	19	2017-20-2 3:23:31	55
NACC3	NACC320170220012007.csv.20170220042134537		2/20/2017	4:20:07	2017-20-02	4:21:34	0.181644	Monday	1	19	2017-20-2 4:21:34	55
NACC3	NACC320170220012102.csv.20170220042334900		2/20/2017	4:21:02	2017-20-02	4:23:34	0.183032	Monday	1	19	2017-20-2 4:23:34	55
NACC3	NACC320170220042007.csv.20170220072148577		2/20/2017	7:20:07	2017-20-02	7:21:48	0.306806	Monday	1	19	2017-20-2 7:21:48	55
NACC3	NACC320170220042118.csv.20170220072349034		2/20/2017	7:21:18	2017-20-02	7:23:49	0.308206	Monday	1	19	2017-20-2 7:23:49	55
NACC3	NACC320170220062001.csv.20170220092124889._ADS		2/20/2017	9:20:01	2017-20-02	9:21:24	0.389861	Monday	1	19	2017-20-2 9:21:24	55
NACC3	NACC320170220062001.csv.20170220092124889		2/20/2017	9:20:01	2017-20-02	9:21:24	0.389861	Monday	1	19	2017-20-2 9:21:24	55
NACC3	NACC320170220062102.csv.20170220092325410		2/20/2017	9:21:02	2017-20-02	9:23:25	0.391262	Monday	1	19	2017-20-2 9:23:25	55
NACC3	NACC320170220072003.csv.20170220102128374		2/20/2017	10:20:03	2017-20-02	10:21:28	0.431574	Monday	1	19	2017-20-2 10:21:28	55
NACC3	NACC320170220082003.csv.20170220112155464		2/20/2017	11:20:03	2017-20-02	11:21:55	0.473553	Monday	1	19	2017-20-2 11:21:55	55
NACC3	NACC320170220082102.csv.20170220112356423		2/20/2017	11:21:02	2017-20-02	11:23:56	0.474954	Monday	1	19	2017-20-2 11:23:56	55
NACC3	NACC320170220092005.csv.20170220122137521		2/20/2017	12:20:05	2017-20-02	12:21:37	0.515012	Monday	1	19	2017-20-2 12:21:37	55
NACC3	NACC320170220092102.csv.20170220122337929		2/20/2017	12:21:02	2017-20-02	12:23:37	0.5164	Monday	1	19	2017-20-2 12:23:37	55
NACC3	NACC320170220102102.csv.20170220132142427		2/20/2017	13:21:02	2017-20-02	13:21:42	0.556736	Monday	1	19	2017-20-2 13:21:42	55
NACC3	NACC320170220172005.csv.20170220202205825		2/20/2017	20:20:05	2017-20-02	20:22:05	0.848669	Monday	1	19	2017-20-2 20:22:05	55
NACC3	NACC320170220172102.csv.20170220202206216		2/20/2017	20:21:02	2017-20-02	20:22:06	0.848681	Monday	1	19	2017-20-2 20:22:06	55
NACC3	NACC320170220192004.csv.20170220222214123		2/20/2017	22:20:04	2017-20-02	22:22:14	0.932106	Monday	1	19	2017-20-2 22:22:14	55
NACC3	NACC320170220192101.csv.20170220222214473		2/20/2017	22:21:01	2017-20-02	22:22:14	0.932106	Monday	1	19	2017-20-2 22:22:14	55
NACC3	NACC320170220202102.csv.20170220232218584		2/20/2017	23:21:02	2017-20-02	23:22:18	0.973819	Monday	1	19	2017-20-2 23:22:18	55
NACC3	NACC320170220212004.csv.20170221002151395		2/21/2017	0:20:04	2017-21-02	0:21:51	0.015174	Tuesday	2	19	2017-21-2 0:21:51	56
NACC3	NACC320170220212102.csv.20170221002351604		2/21/2017	0:21:02	2017-21-02	0:23:51	0.016563	Tuesday	2	19	2017-21-2 0:23:51	56
NACC3	NACC320170220222006.csv.20170221012200629		2/21/2017	1:20:06	2017-21-02	1:22:00	0.056944	Tuesday	2	19	2017-21-2 1:22:00	56
NACC3	NACC320170220222104.csv.20170221012201195		2/21/2017	1:21:04	2017-21-02	1:22:01	0.056956	Tuesday	2	19	2017-21-2 1:22:01	56
NACC3	NACC320170221002001.csv.20170221032206337		2/21/2017	3:20:01	2017-21-02	3:22:06	0.140347	Tuesday	2	19	2017-21-2 3:22:06	56
NACC3	NACC320170221002102.csv.20170221032206950		2/21/2017	3:21:02	2017-21-02	3:22:06	0.140347	Tuesday	2	19	2017-21-2 3:22:06	56
NACC3	NACC320170221012004.csv.20170221042209163		2/21/2017	4:20:04	2017-21-02	4:22:09	0.182049	Tuesday	2	19	2017-21-2 4:22:09	56
NACC3	NACC320170221012102.csv.20170221042209519		2/21/2017	4:21:02	2017-21-02	4:22:09	0.182049	Tuesday	2	19	2017-21-2 4:22:09	56
NACC3	NACC320170221042010.csv.20170221072225381		2/21/2017	7:20:10	2017-21-02	7:22:25	0.307234	Tuesday	2	19	2017-21-2 7:22:25	56
NACC3	NACC320170221042119.csv.20170221072225813		2/21/2017	7:21:19	2017-21-02	7:22:25	0.307234	Tuesday	2	19	2017-21-2 7:22:25	56
NACC3	NACC320170221062002.csv.20170221092232461		2/21/2017	9:20:02	2017-21-02	9:22:32	0.390648	Tuesday	2	19	2017-21-2 9:22:32	56
NACC3	NACC320170221062102.csv.20170221092232784		2/21/2017	9:21:02	2017-21-02	9:22:32	0.390648	Tuesday	2	19	2017-21-2 9:22:32	56
NACC3	NACC320170221072003.csv.20170221102207709		2/21/2017	10:20:03	2017-21-02	10:22:07	0.432025	Tuesday	2	19	2017-21-2 10:22:07	56
NACC3	NACC320170221082004.csv.20170221112226440		2/21/2017	11:20:04	2017-21-02	11:22:26	0.473912	Tuesday	2	19	2017-21-2 11:22:26	56
NACC3	NACC320170221082102.csv.20170221112227335		2/21/2017	11:21:02	2017-21-02	11:22:27	0.473924	Tuesday	2	19	2017-21-2 11:22:27	56
NACC3	NACC320170221092102.csv.20170221122234836		2/21/2017	12:21:02	2017-21-02	12:22:34	0.515671	Tuesday	2	19	2017-21-2 12:22:34	56
NACC3	NACC320170221102005.csv.20170221132038072		2/21/2017	13:20:05	2017-21-02	13:20:38	0.555995	Tuesday	2	19	2017-21-2 13:20:38	56
NACC3	NACC320170221102102.csv.20170221132238445		2/21/2017	13:21:02	2017-21-02	13:22:38	0.557384	Tuesday	2	19	2017-21-2 13:22:38	56
NACC3	NACC320170221172002.csv.20170221202109109		2/21/2017	20:20:02	2017-21-02	20:21:09	0.848021	Tuesday	2	19	2017-21-2 20:21:09	56
NACC3	NACC320170221172102.csv.20170221202309423		2/21/2017	20:21:02	2017-21-02	20:23:09	0.84941	Tuesday	2	19	2017-21-2 20:23:09	56
NACC3	NACC320170221182004.csv.20170221212245559		2/21/2017	21:20:04	2017-21-02	21:22:45	0.890799	Tuesday	2	19	2017-21-2 21:22:45	56
NACC3	NACC320170221192101.csv.20170221222249015		2/21/2017	22:21:01	2017-21-02	22:22:49	0.932512	Tuesday	2	19	2017-21-2 22:22:49	56
NACC3	NACC320170221202004.csv.20170221232051506		2/21/2017	23:20:04	2017-21-02	23:20:51	0.972813	Tuesday	2	19	2017-21-2 23:20:51	56
NACC3	NACC320170221202102.csv.20170221232251911		2/21/2017	23:21:02	2017-21-02	23:22:51	0.974201	Tuesday	2	19	2017-21-2 23:22:51	56
NACC3	NACC320170221212008.csv.20170222002054895		2/22/2017	0:20:08	2017-22-02	0:20:54	0.014514	Wednesday	3	19	2017-22-2 0:20:54	57
NACC3	NACC320170221212103.csv.20170222002255430		2/22/2017	0:21:03	2017-22-02	0:22:55	0.015914	Wednesday	3	19	2017-22-2 0:22:55	57
NACC3	NACC320170221232003.csv.20170222022301079		2/22/2017	2:20:03	2017-22-02	2:23:01	0.099317	Wednesday	3	19	2017-22-2 2:23:01	57
NACC3	NACC320170221232101.csv.20170222022301453		2/22/2017	2:21:01	2017-22-02	2:23:01	0.099317	Wednesday	3	19	2017-22-2 2:23:01	57
NACC3	NACC320170222002003.csv.20170222032105085		2/22/2017	3:20:03	2017-22-02	3:21:05	0.139641	Wednesday	3	19	2017-22-2 3:21:05	57
NACC3	NACC320170222002102.csv.20170222032305458		2/22/2017	3:21:02	2017-22-02	3:23:05	0.14103	Wednesday	3	19	2017-22-2 3:23:05	57
NACC3	NACC320170222012105.csv.20170222042309153		2/22/2017	4:21:05	2017-22-02	4:23:09	0.182743	Wednesday	3	19	2017-22-2 4:23:09	57
NACC3	NACC320170222042012.csv.20170222072123439		2/22/2017	7:20:12	2017-22-02	7:21:23	0.306516	Wednesday	3	19	2017-22-2 7:21:23	57
NACC3	NACC320170222042107.csv.20170222072323873		2/22/2017	7:21:07	2017-22-02	7:23:23	0.307905	Wednesday	3	19	2017-22-2 7:23:23	57
NACC3	NACC320170222062004.csv.20170222092129557		2/22/2017	9:20:04	2017-22-02	9:21:29	0.389919	Wednesday	3	19	2017-22-2 9:21:29	57
NACC3	NACC320170222062102.csv.20170222092300060		2/22/2017	9:21:02	2017-22-02	9:23:00	0.390972	Wednesday	3	19	2017-22-2 9:23:00	57
NACC3	NACC320170222072004.csv.20170222102104526		2/22/2017	10:20:04	2017-22-02	10:21:04	0.431296	Wednesday	3	19	2017-22-2 10:21:04	57
NACC3	NACC320170222072102.csv.20170222102304947._ADS		2/22/2017	10:21:02	2017-22-02	10:23:04	0.432685	Wednesday	3	19	2017-22-2 10:23:04	57
NACC3	NACC320170222072102.csv.20170222102304947		2/22/2017	10:21:02	2017-22-02	10:23:04	0.432685	Wednesday	3	19	2017-22-2 10:23:04	57
NACC3	NACC320170222082007.csv.20170222112134172		2/22/2017	11:20:07	2017-22-02	11:21:34	0.47331	Wednesday	3	19	2017-22-2 11:21:34	57
NACC3	NACC320170222092102.csv.20170222122342615		2/22/2017	12:21:02	2017-22-02	12:23:42	0.516458	Wednesday	3	19	2017-22-2 12:23:42	57
NACC3	NACC320170222102002.csv.20170222132145713		2/22/2017	13:20:02	2017-22-02	13:21:45	0.556771	Wednesday	3	19	2017-22-2 13:21:45	57
NACC3	NACC320170222102102.csv.20170222132316177		2/22/2017	13:21:02	2017-22-02	13:23:16	0.557824	Wednesday	3	19	2017-22-2 13:23:16	57
NACC3	NACC320170222172003.csv.20170222202145856		2/22/2017	20:20:03	2017-22-02	20:21:45	0.848438	Wednesday	3	19	2017-22-2 20:21:45	57
NACC3	NACC320170222172102.csv.20170222202146206		2/22/2017	20:21:02	2017-22-02	20:21:46	0.848449	Wednesday	3	19	2017-22-2 20:21:46	57
NACC3	NACC320170222182004.csv.20170222212150401		2/22/2017	21:20:04	2017-22-02	21:21:50	0.890162	Wednesday	3	19	2017-22-2 21:21:50	57
NACC3	NACC320170222182102.csv.20170222212150757		2/22/2017	21:21:02	2017-22-02	21:21:50	0.890162	Wednesday	3	19	2017-22-2 21:21:50	57
NACC3	NACC320170222202002.csv.20170222232155571		2/22/2017	23:20:02	2017-22-02	23:21:55	0.973553	Wednesday	3	19	2017-22-2 23:21:55	57
NACC3	NACC320170222202102.csv.20170222232356169		2/22/2017	23:21:02	2017-22-02	23:23:56	0.974954	Wednesday	3	19	2017-22-2 23:23:56	57
NACC3	NACC320170222212004.csv.20170223002159634		2/23/2017	0:20:04	2017-23-02	0:21:59	0.015266	Thursday	4	19	2017-23-2 0:21:59	58
NACC3	NACC320170222222029.csv.20170223012201135		2/23/2017	1:20:29	2017-23-02	1:22:01	0.056956	Thursday	4	19	2017-23-2 1:22:01	58
NACC3	NACC320170222222126.csv.20170223012401481		2/23/2017	1:21:26	2017-23-02	1:24:01	0.058345	Thursday	4	19	2017-23-2 1:24:01	58
NACC3	NACC320170223002020.csv.20170223032208938		2/23/2017	3:20:20	2017-23-02	3:22:08	0.14037	Thursday	4	19	2017-23-2 3:22:08	58
NACC3	NACC320170223002119.csv.20170223032209147		2/23/2017	3:21:19	2017-23-02	3:22:09	0.140382	Thursday	4	19	2017-23-2 3:22:09	58
NACC3	NACC320170223042004.csv.20170223072156668		2/23/2017	7:20:04	2017-23-02	7:21:56	0.306898	Thursday	4	19	2017-23-2 7:21:56	58
NACC3	NACC320170223042102.csv.20170223072157002		2/23/2017	7:21:02	2017-23-02	7:21:57	0.30691	Thursday	4	19	2017-23-2 7:21:57	58
NACC3	NACC320170223052005.csv.20170223082229233		2/23/2017	8:20:05	2017-23-02	8:22:29	0.348947	Thursday	4	19	2017-23-2 8:22:29	58
NACC3	NACC320170223062103.csv.20170223092203917		2/23/2017	9:21:03	2017-23-02	9:22:03	0.390313	Thursday	4	19	2017-23-2 9:22:03	58
NACC3	NACC320170223072008.csv.20170223102208620		2/23/2017	10:20:08	2017-23-02	10:22:08	0.432037	Thursday	4	19	2017-23-2 10:22:08	58
NACC3	NACC320170223082101.csv.20170223112222734		2/23/2017	11:21:01	2017-23-02	11:22:22	0.473866	Thursday	4	19	2017-23-2 11:22:22	58
NACC3	NACC320170223092005.csv.20170223122229676		2/23/2017	12:20:05	2017-23-02	12:22:29	0.515613	Thursday	4	19	2017-23-2 12:22:29	58
NACC3	NACC320170223092102.csv.20170223122230047		2/23/2017	12:21:02	2017-23-02	12:22:30	0.515625	Thursday	4	19	2017-23-2 12:22:30	58
NACC3	NACC320170223102102.csv.20170223132233468		2/23/2017	13:21:02	2017-23-02	13:22:33	0.557326	Thursday	4	19	2017-23-2 13:22:33	58
NACC3	NACC320170223172003.csv.20170223202100114		2/23/2017	20:20:03	2017-23-02	20:21:00	0.847917	Thursday	4	19	2017-23-2 20:21:00	58
NACC3	NACC320170223172102.csv.20170223202300494		2/23/2017	20:21:02	2017-23-02	20:23:00	0.849306	Thursday	4	19	2017-23-2 20:23:00	58
NACC3	NACC320170223192006.csv.20170223222106846		2/23/2017	22:20:06	2017-23-02	22:21:06	0.931319	Thursday	4	19	2017-23-2 22:21:06	58
NACC3	NACC320170223192102.csv.20170223222307370		2/23/2017	22:21:02	2017-23-02	22:23:07	0.93272	Thursday	4	19	2017-23-2 22:23:07	58
NACC3	NACC320170223202006.csv.20170223232309697		2/23/2017	23:20:06	2017-23-02	23:23:09	0.97441	Thursday	4	19	2017-23-2 23:23:09	58
NACC3	NACC320170223202102.csv.20170223232310147		2/23/2017	23:21:02	2017-23-02	23:23:10	0.974421	Thursday	4	19	2017-23-2 23:23:10	58
NACC3	NACC320170223212104.csv.20170224002314464		2/24/2017	0:21:04	2017-24-02	0:23:14	0.016134	Friday	5	19	2017-24-2 0:23:14	59
NACC3	NACC320170223222004.csv.20170224012116980		2/24/2017	1:20:04	2017-24-02	1:21:16	0.056435	Friday	5	19	2017-24-2 1:21:16	59
NACC3	NACC320170223222105.csv.20170224012317377		2/24/2017	1:21:05	2017-24-02	1:23:17	0.057836	Friday	5	19	2017-24-2 1:23:17	59
NACC3	NACC320170223232005.csv.20170224022320065		2/24/2017	2:20:05	2017-24-02	2:23:20	0.099537	Friday	5	19	2017-24-2 2:23:20	59
NACC3	NACC320170224002004.csv.20170224032300689		2/24/2017	3:20:04	2017-24-02	3:23:00	0.140972	Friday	5	19	2017-24-2 3:23:00	59
NACC3	NACC320170224002102.csv.20170224032300892		2/24/2017	3:21:02	2017-24-02	3:23:00	0.140972	Friday	5	19	2017-24-2 3:23:00	59
NACC3	NACC320170224012004.csv.20170224042305343		2/24/2017	4:20:04	2017-24-02	4:23:05	0.182697	Friday	5	19	2017-24-2 4:23:05	59
NACC3	NACC320170224012102.csv.20170224042305485		2/24/2017	4:21:02	2017-24-02	4:23:05	0.182697	Friday	5	19	2017-24-2 4:23:05	59
NACC3	NACC320170224042004.csv.20170224072117215		2/24/2017	7:20:04	2017-24-02	7:21:17	0.306447	Friday	5	19	2017-24-2 7:21:17	59
NACC3	NACC320170224042102.csv.20170224072317677		2/24/2017	7:21:02	2017-24-02	7:23:17	0.307836	Friday	5	19	2017-24-2 7:23:17	59
NACC3	NACC320170224052008.csv.20170224082119941		2/24/2017	8:20:08	2017-24-02	8:21:19	0.348137	Friday	5	19	2017-24-2 8:21:19	59
NACC3	NACC320170224062102.csv.20170224092324552		2/24/2017	9:21:02	2017-24-02	9:23:24	0.39125	Friday	5	19	2017-24-2 9:23:24	59
NACC3	NACC320170224072005.csv.20170224102159602		2/24/2017	10:20:05	2017-24-02	10:21:59	0.431933	Friday	5	19	2017-24-2 10:21:59	59
NACC3	NACC320170224072101.csv.20170224102159855		2/24/2017	10:21:01	2017-24-02	10:21:59	0.431933	Friday	5	19	2017-24-2 10:21:59	59
NACC3	NACC320170224082102.csv.20170224112421124		2/24/2017	11:21:02	2017-24-02	11:24:21	0.475243	Friday	5	19	2017-24-2 11:24:21	59
NACC3	NACC320170224092005.csv.20170224122234428		2/24/2017	12:20:05	2017-24-02	12:22:34	0.515671	Friday	5	19	2017-24-2 12:22:34	59
NACC3	NACC320170224092102.csv.20170224122234706		2/24/2017	12:21:02	2017-24-02	12:22:34	0.515671	Friday	5	19	2017-24-2 12:22:34	59
NACC3	NACC320170224102006.csv.20170224132238620		2/24/2017	13:20:06	2017-24-02	13:22:38	0.557384	Friday	5	19	2017-24-2 13:22:38	59
NACC3	NACC320170224102102.csv.20170224132238963		2/24/2017	13:21:02	2017-24-02	13:22:38	0.557384	Friday	5	19	2017-24-2 13:22:38	59
NACC3	NACC320170224172005.csv.20170224202307024		2/24/2017	20:20:05	2017-24-02	20:23:07	0.849387	Friday	5	19	2017-24-2 20:23:07	59
NACC3	NACC320170224172102.csv.20170224202307414		2/24/2017	20:21:02	2017-24-02	20:23:07	0.849387	Friday	5	19	2017-24-2 20:23:07	59
NACC3	NACC320170224192005.csv.20170224222246072		2/24/2017	22:20:05	2017-24-02	22:22:46	0.932477	Friday	5	19	2017-24-2 22:22:46	59
NACC3	NACC320170224192101.csv.20170224222246512		2/24/2017	22:21:01	2017-24-02	22:22:46	0.932477	Friday	5	19	2017-24-2 22:22:46	59
NACC3	NACC320170224202005.csv.20170224232249107		2/24/2017	23:20:05	2017-24-02	23:22:49	0.974178	Friday	5	19	2017-24-2 23:22:49	59
NACC3	NACC320170224202101.csv.20170224232249566		2/24/2017	23:21:01	2017-24-02	23:22:49	0.974178	Friday	5	19	2017-24-2 23:22:49	59
NACC3	NACC320170226222005.csv.20170227012108775		2/27/2017	1:20:05	2017-27-02	1:21:08	0.056343	Monday	1	19	2017-27-2 1:21:08	60
NACC3	NACC320170226222101.csv.20170227012309113		2/27/2017	1:21:01	2017-27-02	1:23:09	0.057743	Monday	1	19	2017-27-2 1:23:09	60
NACC3	NACC320170226232102.csv.20170227022313868		2/27/2017	2:21:02	2017-27-02	2:23:13	0.099456	Monday	1	19	2017-27-2 2:23:13	60
NACC3	NACC320170227002006.csv.20170227032119609		2/27/2017	3:20:06	2017-27-02	3:21:19	0.139803	Monday	1	19	2017-27-2 3:21:19	60
NACC3	NACC320170227002102.csv.20170227032320185		2/27/2017	3:21:02	2017-27-02	3:23:20	0.141204	Monday	1	19	2017-27-2 3:23:20	60
NACC3	NACC320170227012102.csv.20170227042323901		2/27/2017	4:21:02	2017-27-02	4:23:23	0.182905	Monday	1	19	2017-27-2 4:23:23	60
NACC3	NACC320170227042012.csv.20170227072136615		2/27/2017	7:20:12	2017-27-02	7:21:36	0.306667	Monday	1	19	2017-27-2 7:21:36	60
NACC3	NACC320170227042120.csv.20170227072337351		2/27/2017	7:21:20	2017-27-02	7:23:37	0.308067	Monday	1	19	2017-27-2 7:23:37	60
NACC3	NACC320170227062003.csv.20170227092143833		2/27/2017	9:20:03	2017-27-02	9:21:43	0.390081	Monday	1	19	2017-27-2 9:21:43	60
NACC3	NACC320170227062102.csv.20170227092344320		2/27/2017	9:21:02	2017-27-02	9:23:44	0.391481	Monday	1	19	2017-27-2 9:23:44	60
NACC3	NACC320170227082004.csv.20170227112150799		2/27/2017	11:20:04	2017-27-02	11:21:50	0.473495	Monday	1	19	2017-27-2 11:21:50	60
NACC3	NACC320170227082101.csv.20170227112351985		2/27/2017	11:21:01	2017-27-02	11:23:51	0.474896	Monday	1	19	2017-27-2 11:23:51	60
NACC3	NACC320170227092102.csv.20170227122202365		2/27/2017	12:21:02	2017-27-02	12:22:02	0.515301	Monday	1	19	2017-27-2 12:22:02	60
NACC3	NACC320170227102002.csv.20170227132207638		2/27/2017	13:20:02	2017-27-02	13:22:07	0.557025	Monday	1	19	2017-27-2 13:22:07	60
NACC3	NACC320170227172003.csv.20170227202203602		2/27/2017	20:20:03	2017-27-02	20:22:03	0.848646	Monday	1	19	2017-27-2 20:22:03	60
NACC3	NACC320170227172103.csv.20170227202203992		2/27/2017	20:21:03	2017-27-02	20:22:03	0.848646	Monday	1	19	2017-27-2 20:22:03	60
NACC3	NACC320170227182005.csv.20170227212211565		2/27/2017	21:20:05	2017-27-02	21:22:11	0.890405	Monday	1	19	2017-27-2 21:22:11	60
NACC3	NACC320170227192101.csv.20170227222214667		2/27/2017	22:21:01	2017-27-02	22:22:14	0.932106	Monday	1	19	2017-27-2 22:22:14	60
NACC3	NACC320170227202002.csv.20170227232217721		2/27/2017	23:20:02	2017-27-02	23:22:17	0.973808	Monday	1	19	2017-27-2 23:22:17	60
NACC3	NACC320170227202102.csv.20170227232217984		2/27/2017	23:21:02	2017-27-02	23:22:17	0.973808	Monday	1	19	2017-27-2 23:22:17	60
NACC3	NACC320170227212004.csv.20170228002221757		2/28/2017	0:20:04	2017-28-02	0:22:21	0.015521	Tuesday	2	19	2017-28-2 0:22:21	61
NACC3	NACC320170227212105.csv.20170228002222097		2/28/2017	0:21:05	2017-28-02	0:22:22	0.015532	Tuesday	2	19	2017-28-2 0:22:22	61
NACC3	NACC320170227222006.csv.20170228012224431		2/28/2017	1:20:06	2017-28-02	1:22:24	0.057222	Tuesday	2	19	2017-28-2 1:22:24	61
NACC3	NACC320170227232008.csv.20170228022228198		2/28/2017	2:20:08	2017-28-02	2:22:28	0.098935	Tuesday	2	19	2017-28-2 2:22:28	61
NACC3	NACC320170227232114.csv.20170228022428506		2/28/2017	2:21:14	2017-28-02	2:24:28	0.100324	Tuesday	2	19	2017-28-2 2:24:28	61
NACC3	NACC320170228012018.csv.20170228042239010		2/28/2017	4:20:18	2017-28-02	4:22:39	0.182396	Tuesday	2	19	2017-28-2 4:22:39	61
NACC3	NACC320170228012111.csv.20170228042239369		2/28/2017	4:21:11	2017-28-02	4:22:39	0.182396	Tuesday	2	19	2017-28-2 4:22:39	61
NACC3	NACC320170228042019.csv.20170228072222310		2/28/2017	7:20:19	2017-28-02	7:22:22	0.307199	Tuesday	2	19	2017-28-2 7:22:22	61
NACC3	NACC320170228042114.csv.20170228072222652		2/28/2017	7:21:14	2017-28-02	7:22:22	0.307199	Tuesday	2	19	2017-28-2 7:22:22	61
NACC3	NACC320170228062005.csv.20170228092629066		2/28/2017	9:20:05	2017-28-02	9:26:29	0.393391	Tuesday	2	19	2017-28-2 9:26:29	61
NACC3	NACC320170228062101.csv.20170228092629409		2/28/2017	9:21:01	2017-28-02	9:26:29	0.393391	Tuesday	2	19	2017-28-2 9:26:29	61
NACC3	NACC320170228072005.csv.20170228102234548		2/28/2017	10:20:05	2017-28-02	10:22:34	0.432338	Tuesday	2	19	2017-28-2 10:22:34	61
NACC3	NACC320170228072101.csv.20170228102234903		2/28/2017	10:21:01	2017-28-02	10:22:34	0.432338	Tuesday	2	19	2017-28-2 10:22:34	61
NACC3	NACC320170228082101.csv.20170228112344177		2/28/2017	11:21:01	2017-28-02	11:23:44	0.474815	Tuesday	2	19	2017-28-2 11:23:44	61
NACC3	NACC320170228092007.csv.20170228122157181		2/28/2017	12:20:07	2017-28-02	12:21:57	0.515243	Tuesday	2	19	2017-28-2 12:21:57	61
NACC3	NACC320170228092102.csv.20170228122357759		2/28/2017	12:21:02	2017-28-02	12:23:57	0.516632	Tuesday	2	19	2017-28-2 12:23:57	61
NACC3	NACC320170228102102.csv.20170228132132672		2/28/2017	13:21:02	2017-28-02	13:21:32	0.55662	Tuesday	2	19	2017-28-2 13:21:32	61
NACC3	NACC320170228172008.csv.20170228202202465		2/28/2017	20:20:08	2017-28-02	20:22:02	0.848634	Tuesday	2	19	2017-28-2 20:22:02	61
NACC3	NACC320170228172102.csv.20170228202202719		2/28/2017	20:21:02	2017-28-02	20:22:02	0.848634	Tuesday	2	19	2017-28-2 20:22:02	61
NACC3	NACC320170228192003.csv.20170228222211222		2/28/2017	22:20:03	2017-28-02	22:22:11	0.932072	Tuesday	2	19	2017-28-2 22:22:11	61
NACC3	NACC320170228192101.csv.20170228222212000		2/28/2017	22:21:01	2017-28-02	22:22:12	0.932083	Tuesday	2	19	2017-28-2 22:22:12	61
NACC3	NACC320170228202017.csv.20170228232215038		2/28/2017	23:20:17	2017-28-02	23:22:15	0.973785	Tuesday	2	19	2017-28-2 23:22:15	61
NACC3	NACC320170228202111.csv.20170228232215431		2/28/2017	23:21:11	2017-28-02	23:22:15	0.973785	Tuesday	2	19	2017-28-2 23:22:15	61
NACC3	NACC320170228222009.csv.20170301012221331		3/1/2017	1:20:09	2017-01-03	1:22:21	0.057188	Wednesday	3	19	2017-03-01 01:22	62
NACC3	NACC320170228222101.csv.20170301012221642		3/1/2017	1:21:01	2017-01-03	1:22:21	0.057188	Wednesday	3	19	2017-03-01 01:22	62
NACC3	NACC320170228232122.csv.20170301022225504		3/1/2017	2:21:22	2017-01-03	2:22:25	0.0989	Wednesday	3	19	2017-03-01 02:22	62
NACC3	NACC320170301002002.csv.20170301032228760		3/1/2017	3:20:02	2017-01-03	3:22:28	0.140602	Wednesday	3	19	2017-03-01 03:22	62
NACC3	NACC320170301012007.csv.20170301042204663		3/1/2017	4:20:07	2017-01-03	4:22:04	0.181991	Wednesday	3	19	2017-03-01 04:22	62
NACC3	NACC320170301012102.csv.20170301042204821		3/1/2017	4:21:02	2017-01-03	4:22:04	0.181991	Wednesday	3	19	2017-03-01 04:22	62
NACC3	NACC320170301042001.csv.20170301072220539		3/1/2017	7:20:01	2017-01-03	7:22:20	0.307176	Wednesday	3	19	2017-03-01 07:22	62
NACC3	NACC320170301042101.csv.20170301072220932		3/1/2017	7:21:01	2017-01-03	7:22:20	0.307176	Wednesday	3	19	2017-03-01 07:22	62
NACC3	NACC320170301052002.csv.20170301082223264		3/1/2017	8:20:02	2017-01-03	8:22:23	0.348877	Wednesday	3	19	2017-03-01 08:22	62
NACC3	NACC320170301052101.csv.20170301082223540		3/1/2017	8:21:01	2017-01-03	8:22:23	0.348877	Wednesday	3	19	2017-03-01 08:22	62
NACC3	NACC320170301062004.csv.20170301092226874		3/1/2017	9:20:04	2017-01-03	9:22:26	0.390579	Wednesday	3	19	2017-03-01 09:22	62
NACC3	NACC320170301062102.csv.20170301092227302		3/1/2017	9:21:02	2017-01-03	9:22:27	0.39059	Wednesday	3	19	2017-03-01 09:22	62
NACC3	NACC320170301072005.csv.20170301102233379		3/1/2017	10:20:05	2017-01-03	10:22:33	0.432326	Wednesday	3	19	2017-03-01 10:22	62
NACC3	NACC320170301072102.csv.20170301102233665		3/1/2017	10:21:02	2017-01-03	10:22:33	0.432326	Wednesday	3	19	2017-03-01 10:22	62
NACC3	NACC320170301092003.csv.20170301122255635		3/1/2017	12:20:03	2017-01-03	12:22:55	0.515914	Wednesday	3	19	2017-03-01 12:22	62
NACC3	NACC320170301092102.csv.20170301122256074		3/1/2017	12:21:02	2017-01-03	12:22:56	0.515926	Wednesday	3	19	2017-03-01 12:22	62
NACC3	NACC320170301102005.csv.20170301132301955		3/1/2017	13:20:05	2017-01-03	13:23:01	0.55765	Wednesday	3	19	2017-03-01 13:23	62
NACC3	NACC320170301102102.csv.20170301132302199		3/1/2017	13:21:02	2017-01-03	13:23:02	0.557662	Wednesday	3	19	2017-03-01 13:23	62
NACC3	NACC320170301172003.csv.20170301202104437		3/1/2017	20:20:03	2017-01-03	20:21:04	0.847963	Wednesday	3	19	2017-03-01 20:21	62
NACC3	NACC320170301172102.csv.20170301202304872		3/1/2017	20:21:02	2017-01-03	20:23:04	0.849352	Wednesday	3	19	2017-03-01 20:23	62
NACC3	NACC320170301182004.csv.20170301212109021		3/1/2017	21:20:04	2017-01-03	21:21:09	0.889688	Wednesday	3	19	2017-03-01 21:21	62
NACC3	NACC320170301192005.csv.20170301222311516		3/1/2017	22:20:05	2017-01-03	22:23:11	0.932766	Wednesday	3	19	2017-03-01 22:23	62
NACC3	NACC320170301192101.csv.20170301222311882		3/1/2017	22:21:01	2017-01-03	22:23:11	0.932766	Wednesday	3	19	2017-03-01 22:23	62
NACC3	NACC320170301202012.csv.20170301232114270		3/1/2017	23:20:12	2017-01-03	23:21:14	0.973079	Wednesday	3	19	2017-03-01 23:21	62
NACC3	NACC320170301202101.csv.20170301232314839		3/1/2017	23:21:01	2017-01-03	23:23:14	0.974468	Wednesday	3	19	2017-03-01 23:23	62
NACC3	NACC320170301212104.csv.20170302002518898		3/2/2017	0:21:04	2017-02-03	0:25:18	0.017569	Thursday	4	19	2017-03-02 00:25	63
NACC3	NACC320170301222006.csv.20170302012121833		3/2/2017	1:20:06	2017-02-03	1:21:21	0.056493	Thursday	4	19	2017-03-02 01:21	63
NACC3	NACC320170301232102.csv.20170302022326710		3/2/2017	2:21:02	2017-02-03	2:23:26	0.099606	Thursday	4	19	2017-03-02 02:23	63
NACC3	NACC320170302002007.csv.20170302032134101		3/2/2017	3:20:07	2017-02-03	3:21:34	0.139977	Thursday	4	19	2017-03-02 03:21	63
NACC3	NACC320170302012028.csv.20170302042138666		3/2/2017	4:20:28	2017-02-03	4:21:38	0.18169	Thursday	4	19	2017-03-02 04:21	63
NACC3	NACC320170302012138.csv.20170302042339997		3/2/2017	4:21:38	2017-02-03	4:23:39	0.18309	Thursday	4	19	2017-03-02 04:23	63
NACC3	NACC320170302042004.csv.20170302072124362		3/2/2017	7:20:04	2017-02-03	7:21:24	0.306528	Thursday	4	19	2017-03-02 07:21	63
NACC3	NACC320170302042102.csv.20170302072324869		3/2/2017	7:21:02	2017-02-03	7:23:24	0.307917	Thursday	4	19	2017-03-02 07:23	63
NACC3	NACC320170302052004.csv.20170302082127060		3/2/2017	8:20:04	2017-02-03	8:21:27	0.348229	Thursday	4	19	2017-03-02 08:21	63
NACC3	NACC320170302062004.csv.20170302092203036		3/2/2017	9:20:04	2017-02-03	9:22:03	0.390313	Thursday	4	19	2017-03-02 09:22	63
NACC3	NACC320170302062101.csv.20170302092403247		3/2/2017	9:21:01	2017-02-03	9:24:03	0.391701	Thursday	4	19	2017-03-02 09:24	63
NACC3	NACC320170302072101.csv.20170302102409702		3/2/2017	10:21:01	2017-02-03	10:24:09	0.433438	Thursday	4	19	2017-03-02 10:24	63
NACC3	NACC320170302082004.csv.20170302112212206		3/2/2017	11:20:04	2017-02-03	11:22:12	0.47375	Thursday	4	19	2017-03-02 11:22	63
NACC3	NACC320170302082101.csv.20170302112413968		3/2/2017	11:21:01	2017-02-03	11:24:13	0.47515	Thursday	4	19	2017-03-02 11:24	63
NACC3	NACC320170302092007.csv.20170302122157373		3/2/2017	12:20:07	2017-02-03	12:21:57	0.515243	Thursday	4	19	2017-03-02 12:21	63
NACC3	NACC320170302092102.csv.20170302122157686		3/2/2017	12:21:02	2017-02-03	12:21:57	0.515243	Thursday	4	19	2017-03-02 12:21	63
NACC3	NACC320170302172007.csv.20170302202233632		3/2/2017	20:20:07	2017-02-03	20:22:33	0.848993	Thursday	4	19	2017-03-02 20:22	63
NACC3	NACC320170302172104.csv.20170302202233909		3/2/2017	20:21:04	2017-02-03	20:22:33	0.848993	Thursday	4	19	2017-03-02 20:22	63
NACC3	NACC320170302192003.csv.20170302222246605		3/2/2017	22:20:03	2017-02-03	22:22:46	0.932477	Thursday	4	19	2017-03-02 22:22	63
NACC3	NACC320170302192102.csv.20170302222247019		3/2/2017	22:21:02	2017-02-03	22:22:47	0.932488	Thursday	4	19	2017-03-02 22:22	63
NACC3	NACC320170302202106.csv.20170302232250140		3/2/2017	23:21:06	2017-02-03	23:22:50	0.97419	Thursday	4	19	2017-03-02 23:22	63
NACC3	NACC320170302212006.csv.20170303002254335		3/3/2017	0:20:06	2017-03-03	0:22:54	0.015903	Friday	5	19	2017-03-03 00:22	64
NACC3	NACC320170302222014.csv.20170303012258459		3/3/2017	1:20:14	2017-03-03	1:22:58	0.057616	Friday	5	19	2017-03-03 01:22	64
NACC3	NACC320170302222104.csv.20170303012258754		3/3/2017	1:21:04	2017-03-03	1:22:58	0.057616	Friday	5	19	2017-03-03 01:22	64
NACC3	NACC320170302232103.csv.20170303022303513		3/3/2017	2:21:03	2017-03-03	2:23:03	0.09934	Friday	5	19	2017-03-03 02:23	64
NACC3	NACC320170303002004.csv.20170303032042872		3/3/2017	3:20:04	2017-03-03	3:20:42	0.139375	Friday	5	19	2017-03-03 03:20	64
NACC3	NACC320170303002103.csv.20170303032243372		3/3/2017	3:21:03	2017-03-03	3:22:43	0.140775	Friday	5	19	2017-03-03 03:22	64
NACC3	NACC320170303012102.csv.20170303042248005		3/3/2017	4:21:02	2017-03-03	4:22:48	0.1825	Friday	5	19	2017-03-03 04:22	64
NACC3	NACC320170303042007.csv.20170303072304596		3/3/2017	7:20:07	2017-03-03	7:23:04	0.307685	Friday	5	19	2017-03-03 07:23	64
NACC3	NACC320170303042102.csv.20170303072304938		3/3/2017	7:21:02	2017-03-03	7:23:04	0.307685	Friday	5	19	2017-03-03 07:23	64
NACC3	NACC320170303052102.csv.20170303082306780		3/3/2017	8:21:02	2017-03-03	8:23:06	0.349375	Friday	5	19	2017-03-03 08:23	64
NACC3	NACC320170303062002.csv.20170303092110422		3/3/2017	9:20:02	2017-03-03	9:21:10	0.389699	Friday	5	19	2017-03-03 09:21	64
NACC3	NACC320170303072005.csv.20170303102116929		3/3/2017	10:20:05	2017-03-03	10:21:16	0.431435	Friday	5	19	2017-03-03 10:21	64
NACC3	NACC320170303072101.csv.20170303102317485		3/3/2017	10:21:01	2017-03-03	10:23:17	0.432836	Friday	5	19	2017-03-03 10:23	64
NACC3	NACC320170303082102.csv.20170303112329460		3/3/2017	11:21:02	2017-03-03	11:23:29	0.474641	Friday	5	19	2017-03-03 11:23	64
NACC3	NACC320170303092002.csv.20170303122139586		3/3/2017	12:20:02	2017-03-03	12:21:39	0.515035	Friday	5	19	2017-03-03 12:21	64
NACC3	NACC320170303102004.csv.20170303132144747		3/3/2017	13:20:04	2017-03-03	13:21:44	0.556759	Friday	5	19	2017-03-03 13:21	64
NACC3	NACC320170303102102.csv.20170303132345047._ADS		3/3/2017	13:21:02	2017-03-03	13:23:45	0.55816	Friday	5	19	2017-03-03 13:23	64
NACC3	NACC320170303102102.csv.20170303132345047		3/3/2017	13:21:02	2017-03-03	13:23:45	0.55816	Friday	5	19	2017-03-03 13:23	64
NACC3	NACC320170303172003.csv.20170303202221999		3/3/2017	20:20:03	2017-03-03	20:22:21	0.848854	Friday	5	19	2017-03-03 20:22	64
NACC3	NACC320170303172105.csv.20170303202222337		3/3/2017	20:21:05	2017-03-03	20:22:22	0.848866	Friday	5	19	2017-03-03 20:22	64
NACC3	NACC320170303182003.csv.20170303212227641		3/3/2017	21:20:03	2017-03-03	21:22:27	0.89059	Friday	5	19	2017-03-03 21:22	64
NACC3	NACC320170303192102.csv.20170303222201492		3/3/2017	22:21:02	2017-03-03	22:22:01	0.931956	Friday	5	19	2017-03-03 22:22	64
NACC3	NACC320170303202005.csv.20170303232205655		3/3/2017	23:20:05	2017-03-03	23:22:05	0.973669	Friday	5	19	2017-03-03 23:22	64
NACC3	NACC320170305212101.csv.20170306002331996		3/6/2017	0:21:01	2017-06-03	0:23:31	0.016331	Monday	1	19	2017-03-06 00:23	65
NACC3	NACC320170305222005.csv.20170306012133924		3/6/2017	1:20:05	2017-06-03	1:21:33	0.056632	Monday	1	19	2017-03-06 01:21	65
NACC3	NACC320170305222102.csv.20170306012334403		3/6/2017	1:21:02	2017-06-03	1:23:34	0.058032	Monday	1	19	2017-03-06 01:23	65
NACC3	NACC320170306002007.csv.20170306032143231		3/6/2017	3:20:07	2017-06-03	3:21:43	0.140081	Monday	1	19	2017-03-06 03:21	65
NACC3	NACC320170306002104.csv.20170306032343624		3/6/2017	3:21:04	2017-06-03	3:23:43	0.14147	Monday	1	19	2017-03-06 03:23	65
NACC3	NACC320170306042014.csv.20170306072159110		3/6/2017	7:20:14	2017-06-03	7:21:59	0.306933	Monday	1	19	2017-03-06 07:21	65
NACC3	NACC320170306042121.csv.20170306072359456		3/6/2017	7:21:21	2017-06-03	7:23:59	0.308322	Monday	1	19	2017-03-06 07:23	65
NACC3	NACC320170306062004.csv.20170306092134251		3/6/2017	9:20:04	2017-06-03	9:21:34	0.389977	Monday	1	19	2017-03-06 09:21	65
NACC3	NACC320170306062102.csv.20170306092334544		3/6/2017	9:21:02	2017-06-03	9:23:34	0.391366	Monday	1	19	2017-03-06 09:23	65
NACC3	NACC320170306072102.csv.20170306102338495		3/6/2017	10:21:02	2017-06-03	10:23:38	0.433079	Monday	1	19	2017-03-06 10:23	65
NACC3	NACC320170306082004.csv.20170306112202888		3/6/2017	11:20:04	2017-06-03	11:22:02	0.473634	Monday	1	19	2017-03-06 11:22	65
NACC3	NACC320170306082102.csv.20170306112403957		3/6/2017	11:21:02	2017-06-03	11:24:03	0.475035	Monday	1	19	2017-03-06 11:24	65
NACC3	NACC320170306102004.csv.20170306132211707		3/6/2017	13:20:04	2017-06-03	13:22:11	0.557072	Monday	1	19	2017-03-06 13:22	65
NACC3	NACC320170306102101.csv.20170306132212112		3/6/2017	13:21:01	2017-06-03	13:22:12	0.557083	Monday	1	19	2017-03-06 13:22	65
NACC3	NACC320170306172005.csv.20170306202210423		3/6/2017	20:20:05	2017-06-03	20:22:10	0.848727	Monday	1	19	2017-03-06 20:22	65
NACC3	NACC320170306172102.csv.20170306202210731		3/6/2017	20:21:02	2017-06-03	20:22:10	0.848727	Monday	1	19	2017-03-06 20:22	65
NACC3	NACC320170306182102.csv.20170306212215883		3/6/2017	21:21:02	2017-06-03	21:22:15	0.890451	Monday	1	19	2017-03-06 21:22	65
NACC3	NACC320170306192007.csv.20170306222220105		3/6/2017	22:20:07	2017-06-03	22:22:20	0.932176	Monday	1	19	2017-03-06 22:22	65
NACC3	NACC320170306192102.csv.20170306222220451		3/6/2017	22:21:02	2017-06-03	22:22:20	0.932176	Monday	1	19	2017-03-06 22:22	65

