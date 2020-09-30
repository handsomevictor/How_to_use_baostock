# -*- coding: utf-8 -*-
import tushare as ts
import baostock as bs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#get all the ticks
pro = ts.pro_api()
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
data.to_csv('result.csv', encoding = 'gbk')

# login
lg = bs.login()

# 获取沪深A股历史K线数据
rs = bs.query_history_k_data_plus("sz.300313",
    "date,code,open,high,low,close",
    start_date='2020-06-01', end_date='2020-09-29',
    frequency="d", adjustflag="3")

# get result
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

# 结果集输出到csv文件
result.to_csv("szzz.csv", index=False)

# 退出系统
bs.logout()

hist_data = pd.read_csv('szzz.csv', names=None, usecols = [0, 1, 2, 3, 4, 5])
hist_data_list1 = hist_data.values.tolist()


# find out everyday closing price
result_time = []
result_close = []

for i in hist_data_list1:
    result_time.append(i[0])
for i in hist_data_list1:
    result_close.append(i[5])

plt.plot(result_time, result_close)





