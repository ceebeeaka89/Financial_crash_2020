
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()
import seaborn as sns

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2023, 1, 1)


BTC = data.get_data_yahoo("BTC-USD", start, end)
SNP = data.get_data_yahoo("DJI", start, end)
FTSE = data.get_data_yahoo("^FTSE", start, end)
GLD = data.get_data_yahoo("GC=F", start, end)
Eur = data.get_data_yahoo("EURUSD=X", start, end)
CL = data.get_data_yahoo("CL", start, end)

df = data.get_data_yahoo(['BTC-USD', 'DJI', '^FTSE', 'GC=F', 'EURUSD=X', 'CL=F'], start, end)
tickers = ['BTC', 'Dow Jones', 'FTSE', 'GOLD', 'EUR', 'OIL']

eco_price = pd.concat([BTC, SNP, FTSE, GLD, Eur, CL],axis=1,keys=tickers)
eco_price.columns.names = ['Econ Ticker','Stock Info']
eco_price.head()

#max close price for each bank
for tick in tickers:
    (tick,eco_price[tick]['Close'].max())

returns = pd.DataFrame()

for tick in tickers:
    returns[tick+' Return'] = eco_price[tick]['Close'].pct_change()
    returns.head()

#sns.pairplot(returns[1:])

returns.idxmin()
returns.idxmax()
#riskiest of stock calculation
print(returns.std())
returns.head()
#postcovidrisk?
returns.loc['20-01-01':'2022-12-31'].std()
#seaborn for top performances pre COVID pre-crash
sns.displot(returns.loc['2020-01-01':'2020-12-31']['Dow Jones Return'],color='green', bins=8)
#seaborn for top performances post COVID pre-crash
sns.displot(returns.loc['2021-01-01':'2022-12-31']['Dow Jones Return'],color='red', bins=8)
#plt.show()
#lineplot of econo entiretime

for tick in tickers:
    eco_price[tick]['Close'].plot(label=tick, figsize=(12,4))
plt.legend()
#plt.show()
#moving-averages for economies

plt.figure(figsize=(12,4))
BTC['Close'].loc['2020-01-01':'2021-01-01'].rolling(window=30).mean().plot(label='30 day MA')
BTC['Close'].loc['2020-01-01':'2021-01-01'].plot(label='BTC Close')
plt.legend()
#plt.show()
#correlation between
#sns.heatmap(eco_price.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

close_corr = eco_price.xs(key='Close',axis=1,level='Stock Info').corr()
