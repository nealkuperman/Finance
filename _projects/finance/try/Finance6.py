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
                          To Do
2021-??-?? Rename percent_change and put in LibDefinitions or SupportWebReaer
2021-??-?? Create separate plot_price routine - separate visual outputs,
             add graph title (with stock name) and axis titles
"""
#=======================================================================
from enum            import auto#, Enum, IntEnum
from indexenum       import IndexEnum, printenum
from LibDefinitions  import ASCII, printSectionHeader
#=======================================================================

# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt
from get_all_tickers import get_tickers as gt
import pandas as pd
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web # (https://pandas-datareader.readthedocs.io)

#Library Constants
DEBUGMODULE = True
#Finance Table Constants
""" Replace constants with Enum name and value """
class YahooEnum(IndexEnum):
  Date           = 0
  High           = ('auto')
  Low            = ('auto')
  Open           = ('auto')
  Close          = ('auto')
  Volume         = ('auto')
  Adj_Close      = ('auto', "Adj Close")
  # Additional Columns
  Daily_Gain     = ('auto', "Daily Gain")
  Percent_Change = ('auto', "Percent Change")
y=YahooEnum

#------------------------------------------------------------------------------
def import_stock_data(stock, source, query_start, query_end):
    df = web.DataReader(stock, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date
                                          # index to column "Date"
    return df
# end import_stock_data
#------------------------------------------------------------------------------
def ADD_Daily_Gain(df, col):
    df[col.Daily_Gain.name] = ""
    df.loc[:,col.Daily_Gain.name] = df.iloc[0:,col.Close.key] - \
                                    df.iloc[0:,col.Close.key].shift(1)
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
def ADD_percent_change(df, col):
    df[col.Percent_Change.name] = ""
    df.loc[:,col.Percent_Change.name] \
      = percent_change (df.iloc[0:,col.Close.key].shift(1),\
                        df.iloc[0:,col.Close.key])
# end ADD_percent_change
#------------------------------------------------------------------------------
def plot_prices(df,date_text,column_names):
    fig, axs = plt.subplots(len(column_names))
    for i in range(len(column_names)):
        axs[i].plot(df[date_text],df[column_names[i]])
    plt.show()
#end plot_prices
#------------------------------------------------------------------------------
#==============================================================================
if __name__ == '__main__':
  start_year = 2000
  date = (start_year,1,1)

  NFLX = import_stock_data('NFLX','yahoo', dt.datetime(*date), dt.datetime.now())
  ADD_Daily_Gain(NFLX, y)
  ADD_percent_change(NFLX, y)

  plot_prices(NFLX, \
              'Date',\
              [y.Daily_Gain.name,y.Percent_Change.name,'Close'])
  # print(repr(NFLX),type(NFLX))
  print (NFLX.columns)
  y =IndexEnum('Yahoo', *NFLX.columns)
  printenum(y)