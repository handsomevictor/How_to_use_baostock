# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd

# login
lg = bs.login()

# return login information
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# retrive A 500 list shares
rs = bs.query_zz500_stocks()
print('query_zz500 error_code:'+rs.error_code)
print('query_zz500  error_msg:'+rs.error_msg)

# print result
zz500_stocks = []
while (rs.error_code == '0') & rs.next():
    
    # get a record and combine them
    zz500_stocks.append(rs.get_row_data())
result = pd.DataFrame(zz500_stocks, columns=rs.fields)

# to csv
result.to_csv("zz500_stocks.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()