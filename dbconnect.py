import MySQLdb
import pandas as pd
import numpy as np
from pandas.io import sql
db = MySQLdb.connect(host = "localhost",
					 user = "root",
					 passwd = "Msatyam13$")
con = db.cursor()
con.execute("USE python")
data = pd.read_csv("/root/daily.csv",header = 0)
data.fillna(0,inplace=True)
data['account'] = data['total_sale'] + data['beg_reg_bills'] + data['beg_change'] + data['beg_bag_bills'] + data['beg_bag_change'] + data['tacos_pay'] - data['end_reg_bills'] - data['end_change'] - data['end_bag_bills'] - data['end_bag_change'] - data['Salary'] - data['tickets_pay'] - data['Void_bills_amount'] - data['lottery_pay'] - data['credit_card'] - data['other_pays'] - data['total_Drop']
data['overall'] = np.sum(data['account'])


sql.write_frame(data, con=db, name='sales', if_exists='replace', flavor='mysql')



