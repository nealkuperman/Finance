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
                          To Do
2021-??-?? Rename percent_change and put in LibDefinitions or SupportWebReaer
2021-??-?? Create separate plot_price routine - separate visual outputs,
             add graph title (with stock name) and axis titles
             
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
# User-defined Columns Titles
DailyGainTitle     = "Daily Gain"
PercentChangeTitle = "Percent Change"

#------------------------------------------------------------------------------
def import_stock_data(stock, source, query_start, query_end):
    df = web.DataReader(stock, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date
                                          # index to column "Date"
    return df
# end import_stock_data
#------------------------------------------------------------------------------
def getDataFrameEnum(df, dataframename):
  rawnames = df.columns
  enumstring = concat([name.replace(' ','_') for name in rawnames],' ')
  print ('data frame enum names: ', enumstring)
  return DataFrameEnum(dataframename, enumstring)

# end ADD_Daily_Gain
#------------------------------------------------------------------------------
def add_dataframe_column(df, newTitle):
    df[newTitle] = ""
    return getDataFrameEnum(df, newTitle)

# end add_dataframe_column
#------------------------------------------------------------------------------
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
""" is %change only for Close? Input Target Col,Source Col? """
""" Must percent_change use iloc? Can it us loc instead? """
""" What does '0:' signify in iloc[0:, ...]? The row?"""
"""   Why isn't it needed in loc[:, ...]? The row?"""
def ADD_percent_change(df, newTitle = PercentChangeTitle):
    col = add_dataframe_column(df, newTitle)
    df.loc[:,col.Percent_Change.display] \
                        = percent_change (df.iloc[0:,col.Close.key].shift(1),\
                                          df.iloc[0:,col.Close.key])
    return col
# end ADD_percent_change
#------------------------------------------------------------------------------
def plot_prices(df,date_text,column_names):
    fig, axs = plt.subplots(len(column_names))
    for i in range(len(column_names)):
        printSectionHeader ('i<%s> x<%s> y<%s>' % \
                            (i, date_text, column_names[i]))
        if len(column_names)  == 1:
          axs.plot(df[date_text],df[column_names[i]])
        else:
          axs[i].plot(df[date_text],df[column_names[i]])
    plt.show()
#end plot_prices
#------------------------------------------------------------------------------
def plot_price(df,x_axis,y_axis):
    fig, axs = plt.subplots(1)
    i=0
    printSectionHeader ('i<%s> x<%s> y<%s>' % \
                        (i, x_axis, y_axis))
    axs.plot(df[x_axis],df[y_axis])
    plt.show()
#end plot_prices
#==============================================================================
if __name__ == '__main__':
  start_year = 2000
  date = (start_year,1,1)

  NFLX = import_stock_data('NFLX', \
                           'yahoo', \
                            dt.datetime(*date), dt.datetime.now())

  y = getDataFrameEnum (NFLX,"NFLX")
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

  plot_prices(NFLX, y.Date.display, [y.Close.display])
  plot_price(NFLX, y.Date.display, y.Close.display)
  printSectionHeader('using plt.plot')
  plt.plot (NFLX[y.Date.display], NFLX[y.Daily_Gain.display])
  plt.show()
  printSectionHeader('prevent failure with axs[1].plot by using 2 subplots')
  fig, axs = plt.subplots(2)
  axs[1].plot (NFLX[y.Date.display], NFLX[y.Close.display])
  plt.show()
  printSectionHeader('causing failure with axs[1].plot')
  fig, axs = plt.subplots(1)
  axs[1].plot (NFLX[y.Date.display], NFLX[y.Close.display])
  plt.show()

 #end Finance module