# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息

print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# ------------------------------------------------------------------------
# 基本用法之日线
'''
rs = bs.query_history_k_data_plus("sh.300064",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,\
        tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2018-09-20', end_date='2019-10-09', 
    frequency="w", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
'''

'''
# 基本用法之更小刻度的线
rs = bs.query_history_k_data_plus("sz.300064",
    "date,code,time,open,high,low,close,volume,amount,adjustflag",
    start_date='2020-10-09', end_date='2020-10-09', 
    frequency="5", adjustflag="3")

print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
'''

# ------------------------------------------------------------------------
# 画基本图
'''
#### 打印结果集 ####
data_list = []

while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####`

# result.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
print(result)
print(result['close'])

k = list(result['close'])
k = list(map(float, k))

plt.plot(range(0, len(k)), k)
plt.ylim(int(k[0]) * 0.7, int(k[0]) * 1.3)
'''

# ------------------------------------------------------------------------
# 查询2015年除权除息信息
'''
rs_list = []
rs_dividend_2015 = bs.query_dividend_data(code="sh.600000", year="2015", yearType="report")
while (rs_dividend_2015.error_code == '0') & rs_dividend_2015.next():
    rs_list.append(rs_dividend_2015.get_row_data())
    
rs_dividend_2016 = bs.query_dividend_data(code="sh.600000", year="2016", yearType="report")
while (rs_dividend_2016.error_code == '0') & rs_dividend_2016.next():
    rs_list.append(rs_dividend_2016.get_row_data())

# 注意的是这个数据输出结果可能不是dataframe,需要再用pd.Dataframe(rs)来转换一下
'''

# ------------------------------------------------------------------------
# 查询季频估值指标盈利能力
'''
profit_list = []
rs_profit = bs.query_profit_data(code="sh.600030", year=2017, quarter=2)
while (rs_profit.error_code == '0') & rs_profit.next():
    profit_list.append(rs_profit.get_row_data())
result_profit = pd.DataFrame(profit_list, columns=rs_profit.fields)

result_profit.to_csv("66data.csv", encoding="gbk", index=False)
print(result_profit)
'''

# ------------------------------------------------------------------------
# 季频营运能力
'''
operation_list = []
rs_operation = bs.query_operation_data(code="sh.600030", year=2017, quarter=2)
while (rs_operation.error_code == '0') & rs_operation.next():
    operation_list.append(rs_operation.get_row_data())
result_operation = pd.DataFrame(operation_list, columns=rs_operation.fields)

print(result_operation)
result_operation.to_csv("66data.csv", encoding="gbk", index=False)
'''

# ------------------------------------------------------------------------
# 季频成长能力
'''
growth_list = []
rs_growth = bs.query_growth_data(code="sh.600030", year=2017, quarter=2)
while (rs_growth.error_code == '0') & rs_growth.next():
    growth_list.append(rs_growth.get_row_data())
result_growth = pd.DataFrame(growth_list, columns=rs_growth.fields)


print(result_growth)
result_growth.to_csv("66data.csv", encoding="gbk", index=False)

'''

# ------------------------------------------------------------------------
# 季频偿债能力
'''
balance_list = []
rs_balance = bs.query_balance_data(code="sh.600000", year=2017, quarter=2)
while (rs_balance.error_code == '0') & rs_balance.next():
    balance_list.append(rs_balance.get_row_data())
result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)

print(result_balance)
result_balance.to_csv("66data.csv", encoding="gbk", index=False)
'''

# ------------------------------------------------------------------------
# 季频现金流量
'''
cash_flow_list = []
rs_cash_flow = bs.query_cash_flow_data(code="sh.600030", year=2017, quarter=2)
while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
    cash_flow_list.append(rs_cash_flow.get_row_data())
    
result_cash_flow = pd.DataFrame(cash_flow_list, columns=rs_cash_flow.fields)

result_cash_flow.to_csv("66data.csv", encoding="gbk", index=False)
print(result_cash_flow)

'''

# ------------------------------------------------------------------------
# 季频杜邦指数
'''
dupont_list = []
rs_dupont = bs.query_dupont_data(code="sh.600000", year=2017, quarter=2)
while (rs_dupont.error_code == '0') & rs_dupont.next():
    dupont_list.append(rs_dupont.get_row_data())
result_profit = pd.DataFrame(dupont_list, columns=rs_dupont.fields)

result_profit.to_csv("66data.csv", encoding="gbk", index=False)
print(result_profit)
'''

# ------------------------------------------------------------------------
# 交易日当天是否是交易日查询
'''
#### 获取交易日信息 ####
rs = bs.query_trade_dates(start_date="2001-01-01", end_date="2020-10-08")
print('query_trade_dates respond error_code:'+rs.error_code)
print('query_trade_dates respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
    
result = pd.DataFrame(data_list, columns=rs.fields)

result.to_csv("66data.csv", encoding="gbk", index=False)
print(result)
'''

# ------------------------------------------------------------------------
# 证券代码查询
'''
#### 获取证券信息 ####
# 直接返回的是全部的ticker对应的关键词！注意是全部的
rs = bs.query_all_stock(day="2020-06-30")
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(result)
result.to_csv("66data.csv", encoding="gbk", index=False)
'''

# ------------------------------------------------------------------------
# 证券基本资料，上市时间，退市时间
'''
rs = bs.query_stock_basic(code="sh.600030")
# rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
print('query_stock_basic respond error_code:'+rs.error_code)
print('query_stock_basic respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

result.to_csv("66data.csv", encoding="gbk", index=False)
print(result)
'''

# ------------------------------------------------------------------------
# 下载某一天的全部股票数据的所有数据！是全部的！会运行大概好几分钟
'''
def download_data(date):
    bs.login()

    # 获取指定日期的指数、股票数据
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    for code in stock_df["code"]:
        print("Downloading :" + code)
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    bs.logout()
    data_df.to_csv("66data.csv", encoding="gbk", index=False) #记得改地址
    print(data_df)


if __name__ == '__main__':
    # 获取指定日期全部股票的日K线数据
    download_data("2020-10-09")
'''



# 宏观经济数据













bs.logout()




















