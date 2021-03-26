# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt
from get_all_tickers import get_tickers as gt
import pandas as pd
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web # (https://pandas-datareader.readthedocs.io)

#Library Constants

#Finance Table Constants
date_ = 0
high_ = date_ + 1
low_ = high_ + 1
open_ = low_ + 1
close_ = open_ + 1
volume_ = close_ + 1
adj_close_ = volume_ + 1
date_ = adj_close_ + 1

start_year = 2018

date = (start_year,1,1)

#------------------------------------------------------------------------------
def import_stock_data(stock, source, query_start, query_end):
    df = web.DataReader(stock, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date index
                                          # to column "Date"
    return df
# end import_stock_data
#------------------------------------------------------------------------------
def daily_gain(df):
    df["daily_gain"] = ""
    df.loc[:,"daily_gain"] = df.iloc[0:,close_]-df.iloc[0:,close_].shift(1)
# end daily_gain
#------------------------------------------------------------------------------
def percent_change(df):
    df["percent_change"] = ""
    df.loc[:,"percent_change"] = 100*(df.iloc[0:,close_]-df.iloc[0:,close_].shift(1))/df.iloc[0:,close_].shift(1)


#------------------------------------------------------------------------------
def plot_prices(df,date_text,column_names):
    fig, axs = plt.subplots(len(column_names))
    for i in range(len(column_names)):
        axs[i].plot(df[date_text],df[column_names[i]])
    plt.show()
#end plot_prices
#------------------------------------------------------------------------------




#==============================================================================



NFLX = import_stock_data('NFLX','yahoo', dt.datetime(*date), dt.datetime.now())
daily_gain(NFLX)
percent_change(NFLX)
plot_prices(NFLX,"Date",["daily_gain","Close"])