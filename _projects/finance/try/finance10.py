# -*- coding: utf-8 -*-
"""
     !!!!!!!!!!!!!! Put Documentation about Purpose of the file here!!!!!
     Develop structure for this Head eg:
                          Modification History
2021-01-?? Created. Neal Kuperman
2021-02-15 Added percent_change column and graphing. Neal Kuperman
2021-02-16 Added line breaks for clarity. Barry M Dancis
2021-02-17 Added file doc mod history. Barry M Dancis
2021-02-17 Replaced column constants with YahooEnum class. Barry M Dancis
2021-02-17 Created percent_change function. Barry M Dancis
2021-02-20 Use class IndexEnum to create keys. Barry M Dancis
2021-02-20 Replaced enum.value with enum.key. Barry M Dancis
2021-02-20 Added test for __main__. Barry Martin Dancis
2021-02-21 Use label name to create new columns. Barry Martin Dancis
2021-02-21 Modify to use dataframeenum. Barry Martin Dancis
2021-02-23 Add ability to plot only 1 graph. Barry Martin Dancis
2021-02-22 Created separate plot_price function. Barry Martin Dancis
2021-02-23 Added labels to title and axes. Barry Martin Dancis
2021-02-25 Move percent_change to LibDefinitions. Barry Martin Dancis
2021-02-25 Rename display to label. Barry Martin Dancis
                          To Do
2021-??-?? rename dataframeenum.py to dataframe.py
2021-??-?? Move add_dataframe_column to dataframe.py

"""
#=======================================================================
from enum            import auto#, Enum, IntEnum

from dataframeenum   import *
from libdefinitions  import *

import yfinance as yf
import matplotlib.pyplot as plt
from get_all_tickers import get_tickers as gt
# import pandas as pd
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web # (https://pandas-datareader.readthedocs.io)
#=======================================================================

                               #Library Constants
DEBUGMODULE = True
#Finance Table Constants
                          # User-defined Column Titles
DailyGainLabel     = "Daily Gain"
PercentChangeLabel = "Percent Change"


#------------------------------------------------------------------------------
def import_stock_data(stock, source, query_start, query_end):
    df = web.DataReader(stock, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date
                                          # index to column "Date"
    return df
# end import_stock_data
#------------------------------------------------------------------------------
def add_dataframe_column(col_label, df):
    df[col_label] = ""
    return getDataFrameEnum(col_label, df.columns)
# end add_dataframe_column
#------------------------------------------------------------------------------
def ADD_Daily_Gain(df):
    col = add_dataframe_column(DailyGainLabel, df)
    df.loc[:,col.Daily_Gain.label] = df.iloc[0:,col.Close.key] - \
                                       df.iloc[0:,col.Close.key].shift(1)
    return col
# end ADD_Daily_Gain
#------------------------------------------------------------------------------
def ADD_percent_change(df, newTitle = PercentChangeLabel):
    col = add_dataframe_column(newTitle, df)
    df.loc[:,col.Percent_Change.label] \
                        = percent_change (df.iloc[0:,col.Close.key].shift(1),\
                                          df.iloc[0:,col.Close.key])
    return col
# end ADD_percent_change
#------------------------------------------------------------------------------
def plot_prices(df,x_axis_label,column_names):
    plot_colors = ('r', 'b', 'g')
    plotCounts =len(column_names)
    fig, axes = plt.subplots(plotCounts)
    plt.suptitle (df.name)

    for i in range(plotCounts):
      y_axis_label = column_names[i]
      printSectionHead ('i<%s> x<%s> y<%s>' % \
                        (i, x_axis_label, y_axis_label))
      axes[i].plot(df[x_axis_label],df[y_axis_label], \
                  plot_colors[i % plotCounts])
      axes[i].set(ylabel=y_axis_label)
      if i < plotCounts-1:
        axes[i].xaxis.set_ticklabels([])

    axes[plotCounts-1].set(xlabel=x_axis_label)
    axes[plotCounts-1].axis("on")

    plt.show()
    plt.close
#end plot_prices
#------------------------------------------------------------------------------
def plot_price(df,x_axis_label,y_axis_label):
    plt.plot (df[x_axis_label], df[y_axis_label])
    plt.xlabel (x_axis_label)
    plt.ylabel (y_axis_label)
    plt.title (df.name)
    plt.show()
    plt.close
#end plot_prices
#==============================================================================
if __name__ == '__main__':
  start_year = 2000
  date = (start_year,1,1)
  start_date = dt.datetime(*date)
  end_date = dt.datetime.now()
  NFLX = import_stock_data('NFLX', \
                           'yahoo', \
                           start_date, end_date)
  print (start_date.date())
  print (dt.datetime.now().date())
  NFLX.name = 'Yahoo NFLX: from %s to %s' % (start_date.date(), end_date.date())
  y = getDataFrameEnum ("NFLX", NFLX.columns)
  printenummember (y.Close)
  y = ADD_percent_change(NFLX)
  printenummember (y.Percent_Change)
  y = ADD_Daily_Gain(NFLX)
  printenummember (y.Daily_Gain)

  plot_prices(NFLX, \
              y.Date.label,\
              [y.Daily_Gain.label, \
              y.Percent_Change.label, \
              y.Close.label])

  plot_prices(NFLX, \
              y.Open.label,\
              [y.Daily_Gain.label, \
              y.Close.label])

  printSectionHead('using plt.plot')
  plot_price(NFLX, y.Date.label, y.Close.label)

  printSectionHead('using plt.plot_date')
  plt.plot_date (NFLX[y.Date.label], NFLX[y.Daily_Gain.label])
  plt.show()
  plt.close()

  printSectionHead('Multiple curves per plot')
  plt.plot(NFLX[y.Date.label], NFLX[y.Close.label], 'r', \
            NFLX[y.Date.label], NFLX[y.Percent_Change.label], 'b', \
            NFLX[y.Date.label], NFLX[y.Daily_Gain.label], 'g', \
          )
  plt.show()
  plt.close()

 #end Finance module
""" Get data directly from yf instead of from reader """
# import yfinance as yf

# #define the ticker symbol
# tickerSymbol = 'MSFT'

# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)

# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# #see your data
# tickerDf