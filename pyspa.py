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


import pandas as pd
%matplotlib inline
import matplotlib.pyplot as pyplot
from pandas import ExcelWriter
import numpy as np 
from scipy.stats import norm
import xlrd
import matplotlib.pyplot as plt
import datetime as dt

#xl_train=pd.ExcelFile('H:\Python27\\Sec_Transport_Data_Consolidated_AR.xlsx')
xl_train=pd.ExcelFile('H:\Python27\\Sec_Transport_Data_Consolidated_AR.rev1.xlsx',)

xl_train.sheet_names
print (xl_train.sheet_names)

df_train=xl_train.parse('All_Client_without_outlier')
print (df_train.head())

#df_train_csv = pd.read_csv(r'H:\Python27\\Sec_Transport_Data_Consolidated_AR_CSV.csv')

df_train.info()

#newDF.to_csv("H:\Python27\App-Dep-df_model_cumsum_1000.csv")

#writer=pd.ExcelWriter('Sec_Transport_Data_Consolidated_AR.xlsx', engine='xlsxwriter')
#df_train.to_excel(writer, sheet_name='data2')
#writer.save()

#df_miss.info()


min=df_train['SS_DATE'].min()
max=df_train['SS_DATE'].max()
print ("start date",min)
print ("end date", max)

# min=df_miss['SS_DATE'].min()
# max=df_miss['SS_DATE'].max()


#df_train['newtime'] = pd.to_datetime(df_train['Update_Time'],format = '%H:%M:%S')

df_train.head(5)

df_train.info()

df_trail = df_train[['Client_Identifier', 'Date_Identifier', 'SS_TIME_VALUE']].reset_index().rename(columns={'index': 'row_id'})

df_train['SS_DATE'].describe()

df_train['SS_TIME_VALUE'].describe()

df_train['dummy'] = np.ones(df_train.shape[0])

df_train['Client_Order_No']=df_train.groupby(['SS_DATE', 'Client_Identifier'])['dummy'].cumsum()

df_train.drop(['dummy'], axis =1, inplace = True)

df_train

df_train.to_csv("H:\H drive files\Documents\FOK Projects\GM\Secured_Transport_all_clients\df_train_all_clients.csv")

# df_train[df_train['Client_Identifier']==1]

X=df_train['SS_TIME_VALUE']
plt.hist(X)



df_train['labels'] = pd.cut(df_train['SS_TIME_VALUE'], [0,0.025,0.05,0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525,0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1], labels = [1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,38,39, 40], include_lowest=True, right=False )

df_train.head()

df_train.info()

df_train[df_train['labels']==37]



df_train.to_csv("H:\H drive files\Documents\FOK Projects\GM\Secured_Transport_all_clients\df_train_all_clients.csv")

writer=pd.ExcelWriter('NAV_train_data.xlsx', engine='xlsxwriter')
df_train.to_excel(writer, sheet_name='NAV-train_data')
writer.save()

min=df_train['SS Time (EST)'].min()
max=df_train['SS Time (EST)'].max()
print ("start time",min)
print ("end time", max)

# min=df_miss['Update_Time'].min()
# max=df_miss['Update_Time'].max()


min_time=df_train['SS_TIME_VALUE'].min().round(6)
max_time=df_train['SS_TIME_VALUE'].max().round(6)
print ("start time",min_time)
print ("end time", max_time)

#len(df_train)

#df_train.info()

#(df_train['Update_Time'].groupby(df_train['AddDate'])).count()

#df_train.info()

ts = df_train.DATETIME 
#print(type(ts))
ts1 = pd.Series(1, index = ts)
print (ts1.head())

df_train.boxplot('SS_TIME_VALUE', by='weekday', figsize=(10, 8))

df_train.boxplot('SS_TIME_VALUE', by='Client_Identifier', figsize=(10, 8))



df_train

df_train.to_csv("H:\H drive files\Documents\FOK Projects\GM\Secured_Transport_all_clients\df_train_all_clients.csv")

df_train['labels'].astype(int).head()

df_train['labels'].head()

y=df_train['Client_Identifier']
x= df_train['SS_TIME_VALUE']
           
plt.scatter(x,y)

df_train.info()

df_train.sort_values('labels')
x=df_train['labels']
y=df_train['SS_TIME_VALUE']
print (len(x)), print (len(y))
plt.scatter(x, y)


df_train.info()

df_train1=df_train[['MRE_FILE', 'labels','Predicted_Y','Reg_Yellow', 'Reg_Green','Reg_Red']].drop_duplicates()
df_train1.sort_values('labels')
df_train2=df_train1.sort_values('labels')
df_train2.columns.values[1]='SS_ORDER_NUMBER'
df_train2.head()


x=df_train['Client_Identifier']
y=df_train['SS_TIME_VALUE']
plt.scatter(x, y, c='r')

df_train.info()

len(df_train['SS_DATE'].unique())

ts = df_train.DATETIME
#print(type(ts))
ts1 = pd.Series(1, index = ts)
print (ts1.head())

ts2 = ts1.resample('1min', how = 'count')

ts3 = pd.DataFrame(ts2,columns=['Count']).reset_index()

# Splitting Date time into Date and time 
ts3['Time'] = pd.DatetimeIndex(ts3['DATETIME']).time
ts3['Date'] = pd.DatetimeIndex(ts3['DATETIME']).date

ts3.head()



type(ts3['Date'][0])

ts3['Date'] = ts3['Date'].apply(pd.Timestamp)

df_train_dates = df_train['SS_DATE'].unique()

ts3 = ts3[ts3['Date'].isin(df_train_dates)]

set(ts3['Date'])

pd.options.mode.chained_assignment = None  # default='warn'
df2 = ts3[['DATETIME','Date','Time','Count']]
#print(df2.dtypes)

df2['weekday'] = df2['DATETIME'].dt.dayofweek
days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}
df2['week_day'] = df2['weekday'].apply(lambda x: days[x])
df2.head()

df2['Count'].groupby(df2['weekday']).count()

import warnings
warnings.filterwarnings('ignore')

df_model = df2.copy()
#bin_dict = {'00:30:00':1, '01:00:00':2, '01:30:00':3,'02:00:00':4, '02:30:00':5, '03:00:00':6,'03:30:00':7, '04:00:00': 8, '04:30:00':9, '05:00:00':10, '05:30:00':11,'06:00:00':12, '06:30:00':13, '07:00:00':14,'07:30:00':15, '08:00:00': 16,'08:30:00':17, '09:00:00': 18, '09:30:00':19, '10:00:00': 20, '10:30:00':21, '11:00:00': 22, '11:30:00':23, '12:00:00': 24, '12:30:00':25, '13:00:00': 26, '13:30:00':27, '14:00:00': 28, '14:30:00':29, '15:00:00': 30,'15:30:00':31, '16:00:00':32,'16:30:00':33, '17:00:00':34,'17:30:00':35, '18:00:00': 36,'18:30:00':37, '19:00:00': 38,'19:30:00':39, '20:00:00':40,'20:30:00':41, '21:00:00': 42,'21:30:00':43, '22:00:00': 44,'22:30:00':45, '23:00:00': 46,'23:30:00':47, '00:00:00': 48 }

# Extracting Time from date
df_model["Bin"] = df_model["DATETIME"].apply(lambda x: dt.datetime.strftime(x, '%H:%M:%S'))

# for loop to create bins

time = dt.datetime(2017, 2, 23,15, 59, 0)
delta = dt.timedelta(minutes= 1)

bindict={}

for k in range(1,1441):
    newtime = (time + delta)
    bindict[str(newtime.time())] = k
    time = newtime
    k=+1    

# Create bins 

df_model = df_model.replace({"Bin": bindict}).sort_values(['Date'])
pd.options.mode.chained_assignment = None  # default='warn'
df_model['Bin'] = df_model['Bin'].convert_objects(convert_numeric=True)

#df_model['Bin'] = pd.to_numeric(df_model['Bin'])

df_model = df_model[df_model['Bin'] < 1441]

df_model.sort_values('Bin').head()




len(df_model[df_model['Bin']==231])

df_model=df_model[df_model.weekday <5]

df_model['Count'].groupby(df_model['weekday']).sum()

len(df_model)

len(df_model[df_model['Bin']==231])

df_model.sort_values('Bin').head()
len(df_model)

# Create cumulative values

df_model2 = df_model.copy().sort_values('DATETIME')

df_model2['cumsum'] = df_model2.groupby(['Date'])['Count'].apply(lambda x: x.cumsum())
#df_model2.sort_values(['Date','Time'])
df_model3=df_model2[df_model2['Bin']==1440]
#df_model3
df_model2.sort_values('DATETIME').head()


df_train['Temp_DateTime'] = df_train['DATETIME'].apply(lambda x: x.replace(second = 0))
df_model2 = df_model2.merge(df_train[['Temp_DateTime', 'Client_Identifier', 'Date_Identifier']], how = 'left', left_on = 'DATETIME', right_on = 'Temp_DateTime')
df_model2.drop(['Temp_DateTime'], axis = 1, inplace = True)
df_model2

df_model2=df_model2.drop_duplicates()
df_model2.head()

df_model2['cumsumpct'] = df_model2.groupby(['Date'])['cumsum'].apply(lambda x: x / float(x.max()))
df_model2.head()

df_model2.to_csv("H:\H drive files\Documents\FOK Projects\GM\Secured_Transport_all_clients\df_model2_cumsumpct.csv")

#df_model2=pd.DataFrame(df_model2)

df_model2.info()

df_model2=df_model2.sort_values('Bin')
df_model2

df_model_client19=df_model2[df_model2['Client_Identifier']==19]
df_model_client19.sort_values('Bin')

len(df_model2)

# CLIENT # 4 ANALYSIS

df_model_client4=df_model2[df_model2['Client_Identifier']==4]
df_model_client4_noduplicates=df_model_client4.drop_duplicates()
df_model_client4_noduplicates.head()

len(df_model_client4_noduplicates['Date'])

df_model_client4_noduplicates['cumsumpct'] = df_model_client4_noduplicates.groupby(['Date'])['cumsum'].apply(lambda x: x / float(x.max()))
df_model_client4_noduplicates.head()

# cumsum chart: Is File Volume really a continuous varaiable? 

df_model_client4_noduplicates=df_model_client4_noduplicates.sort_values('Bin')
x1=df_model_client4_noduplicates['Bin']
y1=df_model_client4_noduplicates['cumsum']

plt.figure(figsize=(20,5))

plt.scatter(x1,y1, color='blue')

# File Volume is not continuous so we cannot use regression for predicting file receipt time. 

# Using DBSCAN CLUSTERING technique to find time bins to be modeled for file receipt time thresholds 

from sklearn.cluster import DBSCAN
from sklearn import metrics

data=df_model_client4_noduplicates[['Bin','Date_Identifier']]
data=data.as_matrix().astype("float32", copy=False)

db = DBSCAN(eps=30, min_samples=50).fit(data)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

data_dummy = df_model_client4_noduplicates[['Bin','Date_Identifier']]

print(labels)

data_dummy['cluster_labels'] = db.labels_

data_dummy.sort_values('Bin').head()

data_clusters_info=pd.DataFrame(data_dummy['Bin'].groupby(data_dummy['cluster_labels']).unique())
data_clusters_info.reset_index()


data_clusters_info.rename(columns = {0: 'Bin'},inplace = True)
data_clusters_info.reset_index()

import matplotlib.pyplot as plt
    
plt.figure(figsize=(20,10))

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = data[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = data[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)
    
plt.show()
