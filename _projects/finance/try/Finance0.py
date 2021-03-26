# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:06:11 2021

@author: Barry
"""

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt
from get_all_tickers import get_tickers as gt
import pandas as pd
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web

date_ = 0
high_ = date_ + 1
low_ = high_ + 1
open_ = low_ + 1
close_ = open_ + 1
volume_ = close_ + 1
adj_close_ = volume_ + 1
date_ = adj_close_ + 1

# # IMPORT using pandas_datareader (https://pandas-datareader.readthedocs.io)
date = (2015,1,1)
query_start = dt.datetime(*date)
query_end = dt.datetime.now()

df = web.DataReader("NFLX", 'yahoo', query_start, query_end)

df.reset_index(level=0, inplace=True) # create new column and move Date index
                                      # to column "Date"

df["daily_gain"] = ""
df.loc[:,"daily_gain"] = df.iloc[0:,close_]-df.iloc[0:,close_].shift(1)

print(df.columns)

# # Plot the close prices
fig, axs = plt.subplots(2)
axs[0].plot(df["Date"],df["daily_gain"])
axs[1].plot(df["Date"],df["Close"])
plt.show()

fig, axs = plt.subplots(1)
axs[0].plot(df["Date"],df["daily_gain"])
plt.show()