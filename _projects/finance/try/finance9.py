# -*- coding: utf-8 -*-
"""
     !!!!!!!!!!!!!! Put Documentation about Purpose of the file here!!!!!
     Develop structure for this header eg:
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
2021-02-21 Use display name to create new columns. Barry Martin Dancis
2021-02-21 Modify to use dataframeenum. Barry Martin Dancis
2021-02-23 Add ability to plot only 1 graph. Barry Martin Dancis
2021-02-22 Created separate plot_price function. Barry Martin Dancis
2021-02-23 Added labels to title and axes. Barry Martin Dancis
                          To Do
2021-??-?? Rename percent_change and put in LibDefinitions or SupportWebReaer
2021-??-?? rename dataframeenum.py to dataframe.py
2021-??-?? Move add_dataframe_column to dataframe.py

"""
#=======================================================================
from enum            import auto#, Enum, IntEnum

from dataframeenum   import *
from libdefinitions  import ASCII, printSectionHeader, concat
#=======================================================================

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt
from get_all_tickers import get_tickers as gt
# import pandas as pd
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web # (https://pandas-datareader.readthedocs.io)

#Library Constants
DEBUGMODULE = True
#Finance Table Constants
# User-defined Column Titles
DailyGainTitle     = "Daily Gain"
PercentChangeTitle = "Percent Change"
fig = ''

#------------------------------------------------------------------------------
def import_stock_data(stock, source, query_start, query_end):
    df = web.DataReader(stock, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date
                                          # index to column "Date"
    return df
# end import_stock_data
#------------------------------------------------------------------------------
def add_dataframe_column(df, newTitle):
    df[newTitle] = ""
    return getDataFrameEnum(newTitle, df)

# end add_dataframe_column
#------------------------------------------------------------------------------
""" remove newTitle from argument list. If value is not "Daily Gain" then
      calculating the value using Daily_Gain.display will not work """
def ADD_Daily_Gain(df, newTitle=DailyGainTitle):
    col = add_dataframe_column(df, newTitle)
    df.loc[:,col.Daily_Gain.display] = df.iloc[0:,col.Close.key] - \
                                       df.iloc[0:,col.Close.key].shift(1)
    return col
# end ADD_Daily_Gain
#------------------------------------------------------------------------------
""" Added function to calculate percent_change; shorten name and put in Lib??? """
def percent_change(from_value, to_value):
    return 100*((to_value - from_value)/from_value)
# end percent_change
#------------------------------------------------------------------------------
""" Must percent_change use iloc? Can it us loc instead? """
""" What does '0:' signify in iloc[0:, ...]? The row?"""
"""   Why isn't it needed in loc[:, ...]? The row?"""
""" remove newTitle from argument list. If value is not "Percent Change" then
      calculating the value using Percent_Change.display will not work """
def ADD_percent_change(df, newTitle = PercentChangeTitle):
    col = add_dataframe_column(df, newTitle)
    df.loc[:,col.Percent_Change.display] \
                        = percent_change (df.iloc[0:,col.Close.key].shift(1),\
                                          df.iloc[0:,col.Close.key])
    return col
# end ADD_percent_change
#------------------------------------------------------------------------------
""" Change axs to standard pyplot name of axes """
def plot_prices(df,x_axis_display,column_names):
    plot_colors = ('r', 'b', 'g')
    plotCounts =len(column_names)
    fig, axs = plt.subplots(plotCounts)
    plt.suptitle (df.name)

    for i in range(len(column_names)):
      printSectionHeader ('i<%s> x<%s> y<%s>' % \
                          (i, x_axis_display, column_names[i]))
      axs[i].plot(df[x_axis_display],df[column_names[i]], \
                  plot_colors[i % plotCounts])
      axs[i].set(ylabel=column_names[i])
      if i < plotCounts-1:
        axs[i].xaxis.set_ticklabels([])
      # if len(column_names) == 1:
      #   axs.plot(df[x_axis_display],df[column_names[i]],plot_colors[i])
      #   axs.set(ylabel=column_names[i])
      # else:
      #   axs[i].plot(df[x_axis_display],df[column_names[i]],plot_colors[i])
      #   axs[i].set(ylabel=column_names[i])
    axs[plotCounts-1].set(xlabel=x_axis_display)
    axs[plotCounts-1].axis("on")

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
              y.Date.display,\
              [y.Daily_Gain.display, \
              y.Percent_Change.display, \
              y.Close.display])

  plot_prices(NFLX, \
              y.Open.display,\
              [y.Daily_Gain.display, \
              y.Close.display])

  printSectionHeader('using plt.plot')
  plot_price(NFLX, y.Date.display, y.Close.display)

  printSectionHeader('using plt.plot_date')
  plt.plot_date (NFLX[y.Date.display], NFLX[y.Daily_Gain.display])
  plt.show()

  plt.plot(NFLX[y.Date.display], NFLX[y.Close.display], 'r', \
           NFLX[y.Date.display], NFLX[y.Percent_Change.display], 'b', \
           NFLX[y.Date.display], NFLX[y.Daily_Gain.display], 'g', \
          )
  plt.show()

  # fig,axes=plt.subplots(3)
  # axes[0].plot(NFLX[y.Date.display], NFLX[y.Close.display], 'r',)
  # axes[1].plot(NFLX[y.Date.display], NFLX[y.Daily_Gain.display], 'g',)
  # axes[2].plot(NFLX[y.Date.display], NFLX[y.Low.display], 'b',)
  # axes[0].set(ylabel='close', title=NFLX.name)
  # axes[1].set(ylabel='Daily Gain')
  # axes[2].set(xlabel='Year', ylabel='Low')

  # plt.show()
  plt.close

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
""" More tests for plotting """
  # printSectionHeader('prevent failure with axs[1].plot by using 2 subplots')
  # fig, axs = plt.subplots(2)
  # axs[1].plot (NFLX[y.Date.display], NFLX[y.Close.display])
  # plt.show()
  # printSectionHeader('causing failure with axs[1].plot')
  # fig, axs = plt.subplots(1)
  # axs[1].plot (NFLX[y.Date.display], NFLX[y.Close.display])
  # plt.show()