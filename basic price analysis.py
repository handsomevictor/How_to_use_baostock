# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import math
import numpy as np
import sklearn.preprocessing

# get data of AAPL
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 9, 28)
df = web.DataReader("AAPL", 'yahoo', start, end)
df.tail()
df.to_csv('newone.csv')

# moving average
close_px = df['Adj Close']
mavg = close_px.rolling(window = 120).mean()

# graph of moving average using plt
# adjusting the size
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')
close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()


rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')

# add others
dfcomp = web.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],'yahoo',start=start,end=end)['Adj Close']

# find mutual influence, basic correlation ratio
retscomp = dfcomp.pct_change()
corr = retscomp.corr()

# find profit distribution
plt.scatter(retscomp.AAPL, retscomp.GE)
plt.xlabel('Returns AAPL')
plt.ylabel('Returns GE')

# scatter matrix
pd.plotting.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10))

# useless KDE graph and dot matrix
plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)

# return rate and risk
plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(label,xy = (x, y), xytext = (20, -20),
       textcoords = 'offset points', ha = 'right', va = 'bottom',
       bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
       arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

# 特征工程
dfreg = df.loc[:,['Adj Close','Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0


# 预处理和交叉验证
# it's copied!!!!!!!!!!!!!!!!!!!
# Drop missing value
dfreg.fillna(value=-99999, inplace=True)
# We want to separate 1 percent of the data to forecast
forecast_out = int(math.ceil(0.01 * len(dfreg)))
# Separating the label here, we want to predict the AdjClose
forecast_col = 'Adj Close'
dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
X = np.array(dfreg.drop(['label'], 1))
# Scale the X so that everyone can have the same distribution for linear regression
X = sklearn.preprocessing.scale(X)
# Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
# Separate label and identify it as y
y = np.array(dfreg['label'])
y = y[:-forecast_out]

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 简单线性分析和二次判别分析
# Linear regression
clfreg = LinearRegression(n_jobs=-1)
clfreg.fit(X_train, y_train)
# Quadratic Regression 2
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, y_train)
# Quadratic Regression 3
clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
clfpoly3.fit(X_train, y_train)







