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

import sys
sys.path.append(r'/Users/nealkuperman/Python_Scripts/Stock_analysis/git_Project/Lib')


#=======================================================================
from enum            import auto#, Enum, IntEnum

from dataframeenum   import *
from libdefinitions  import ASCII, printSectionHeader, concat
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
# User-defined Column Titles
DailyGainTitle     = "Daily Gain"
PercentChangeTitle = "Percent Change"
fig = ''

#------------------------------------------------------------------------------
def import_stock_data(ticker_symbol, source, query_start, query_end):
    df = web.DataReader(ticker_symbol, source, query_start, query_end)
    df.reset_index(level=0, inplace=True) # create new column and move Date
                                          # index to column "Date"
    df.insert(0,"stock",str(ticker_symbol))
    return df
# end import_stock_data
#------------------------------------------------------------------------------

"""
Code how to get a list of current prices given an input list of instruments.

Stocks, bonds, futures, options, bitcoins are all examples of instruments

You would like a function whose input is a list of symbols, the output is a list of current or closing prices

Similar to calling Yahoo with “NFLX”to get NFLX prices

"""

class stock_query ():
    ticker_symbol = ""
    data_source = ""
    query_start = dt.datetime.now()
    query_end = dt.datetime.now()
    
    def __init__(self, next_stock, next_source, next_query_start, next_query_end = dt.datetime.now()):
        self.ticker_symbol = next_stock
        self.data_source = next_source
        self.query_start = next_query_start
        self.query_end = next_query_end
 
x = stock_query("NFLX","yahoo",(2020,1,1))
y = stock_query("NFLX","yahoo",(2020,1,1))
#------------------------------------------------------------------------------
def import_stocks(stocks):
    
    stocks_df = pd.DataFrame()
    length = len(stocks)
    
    # make sure all of the input lists are the same length
    if any(len(lst) != length for lst in [sources, query_starts, query_ends]):
        return("your lists have different lengths")
    
    stocks_df 
    
    for i in range(0,len(stocks)):
        print(i)
        single_stock = import_stock_data(stocks[i], sources[i], query_starts[i],query_ends[i])
        single_stock.columns = [str(stocks[i]) + "_" + str(col) for col in single_stock.columns]
        print(single_stock)
        stocks_df = pd.concat([stocks_df,single_stock],axis = 1)
        
    return stocks_df

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

    for i in range(plotCounts):
      printSectionHeader ('i<%s> x<%s> y<%s>' % \
                          (i, x_axis_display, column_names[i]))
      axs[i].plot(df[x_axis_display],df[column_names[i]],plot_colors[i])
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
def plot_price(df,x_axis_display,y_axis_display):
    plt.plot (df[x_axis_display], df[y_axis_display])
    plt.xlabel (x_axis_display)
    plt.ylabel (y_axis_display)
    plt.title (df.name)
    plt.show()
    plt.close
#end plot_prices
#==============================================================================

"""
1. create CSV of my allocations and read into python
2. place to store all of the stocks I am tracking - stores all data about stocks 
"""
def load_csv(full_file_name):
    dataFrame = pd.read_csv(full_file_name)
    return dataFrame

#==============================================================================

"""
3. store what are the ones that I own and how much do I own
"""
def import_stocks_i_hold(df):
    stock_data = pd.DataFrame()
    
    for i in range(0,len(df.index)):
        ticker = str(df.loc[i,"Symbol"])
        if df.loc[i,"Holding_Type"] == "stock":
            stocks = [stock_data,import_stock_data(ticker, \
                                                   "yahoo", \
                                                   dt.datetime(2000,1,1), \
                                                   dt.datetime.now())]
            
            stock_data = pd.concat(stocks,ignore_index=True)
            
    return stock_data

#==============================================================================

def get_today_close(df):
    df["today_close"] = ""
    
    for i in range(0,len(df.index)):
        ticker = str(df.loc[i,"Symbol"])
        if df.loc[i,"Holding_Type"] == "stock":
            stock = import_stock_data(ticker, \
                                          "yahoo", \
                                              dt.datetime(2021,1,1), \
                                                  dt.datetime.now())
            today_close = stock["Close"].iloc[-1]
            df.loc[i,"today_close"] = today_close
    return df

"""
4. relationship between 2 and 3 so that item 3 can get prices from item 1
5. allocation schemes 
    1. in general fund balance tab
        1. for a given scheme what is the allocation? 
6. my current allocation
7. how does my allocation compare to what the scheme allocation says it should be
    1. how much change is necessary to get from current allocation to scheme allocation
8. summary 
    1. add up everything that i have in different places and how much do i have? 
9. keep track of changes 
"""

                



if __name__ == '__main__':
    action = "test graphing"
    action = "load data"
    # action = "test new function"
  
    if action == "test graphing":
  
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
          plt.close
        
          #end Finance module

    elif action == "load data":
        Holdings = load_csv("/Users/nealkuperman/Python_Scripts/Financial_holdings.csv")
        Trackings = load_csv("/Users/nealkuperman/Python_Scripts/Financial_trackings.csv")
        alocation_schema = ""
        my_stocks = import_stocks_i_hold(Holdings)
        Holdings = get_today_close(Holdings)