# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:13:57 2021

@author: Barry
"""

"""======================================================================="""
from enum            import Enum, IntEnum, auto
from LibDefinitions  import ASCII, printSectionHeader
# from IndexEnum_dev   import IndexEnum
from IndexEnum       import IndexEnum
from matplotlib      import style
from get_all_tickers import get_tickers as gt
import yfinance               as yf
import matplotlib.pyplot      as plt
import pandas                 as pd
import datetime               as dt
import pandas_datareader.data as web
"""======================================================================="""
debugModule=False
debugModule=True
LINELENGTH = 60
StartYear = 2000
StartDate = (StartYear,1,1)

class YahooIndexEnum(IndexEnum):
  FirstEnum = 5
  Fields = (('Date',),
            ('High',),
            ("Low",),
            ('Open',),
            ('Close',),
            ('Volume',),
            ('Adj_Close','Adj Close'),
            ('Daily_Gain','Daily Gain'))

  def __init__(self, EnumerationName):
    self.name = EnumerationName
    self.addEnums(self.FirstEnum, self.Fields)
    if debugModule:
      printSectionHeader (self.name + " Dictionary")
      print ("Dictionary:", list(IndexEnum.__dict__))


def NewInstancePlot (date):
  printSectionHeader("Testing NewClassPlot")
  query_start = dt.datetime(*date)
  query_end = dt.datetime.now()

  df = web.DataReader("NFLX", 'yahoo', query_start, query_end)

  df.reset_index(level=0, inplace=True) # create new column and move Date index
                                        # to column "Date"
  print("df columns: " , df.columns)

  Y=YahooIndexEnum
  print ('IndexEnum Dictionary',list(IndexEnum.__dict__))
  print ('Y Dictionary',list(Y.__dict__))
  print ('YahooIndexEnum Dictionary',list(YahooIndexEnum.__dict__))
  print ("enum <%s>" % (Y.Daily_Gain))
  print ("name <%s>" % (Y.Daily_Gainname))
  print ("Label <%s>" % (Y.Daily_Gainlabel))

  df[Y.Daily_Gainname] = ""
  df.iloc[:,Y.Daily_Gain] = df.iloc[0:,Y.Close]-df.iloc[0:,Y.Close].shift(1)

  printSectionHeader("Plotting Closing Prices",60,ASCII.SECTIONHEADERCHAR.value)
  fig, axs = plt.subplots(2)
  axs[0].plot(df[Y.Datename],df[Y.Daily_Gainname])
  axs[1].plot(df[Y.Datename],df[Y.Closename])
  plt.show()

def ImportStockPrices(StartDate):
  printSectionHeader("Importing Stock Prices",60,ASCII.SECTIONHEADERCHAR.value)
  # # IMPORT using pandas_datareader (https://pandas-datareader.readthedocs.io)
  query_start = dt.datetime(*StartDate)
  query_end = dt.datetime.now()

  df = web.DataReader("NFLX",
                      'yahoo', query_start, query_end)
  df.reset_index(level=0, inplace=True) # create new column and move Date index
                                        # to column "Date"

printSectionHeader("Processing Stock Prices",60,ASCII.SESSIONHEADERCHAR.value)
ImportStockPrices(StartDate)
NewInstancePlot(StartDate)

"""======================================================================="""

def TestNewClassPlot ():
  printSectionHeader("Testing NewClassPlot")
  query_start = dt.datetime(*date)
  query_end = dt.datetime.now()

  df = web.DataReader("NFLX", 'yahoo', query_start, query_end)

  df.reset_index(level=0, inplace=True) # create new column and move Date index
                                        # to column "Date"
  print("df columns: " , df.columns)

  df[Y.Daily_Gainname] = ""
  df.loc[:,Y.Daily_Gainname] = df.iloc[0:,Y.Close]-df.iloc[0:,Y.Close].shift(1)
  print("df columns: " , df.columns)

  printSectionHeader("Plotting Closing Prices",60,ASCII.SECTIONHEADERCHAR.value)
  fig, axs = plt.subplots(2)
  axs[0].plot(df[Y.Datename],df[Y.Daily_Gainname])
  axs[1].plot(df[Y.Datename],df[Y.Closename])
  plt.show()
# TestNewClassPlot()

def TestNealPlot():
  printSectionHeader("Testing Neal PLot")
  query_start = dt.datetime(*date)
  query_end = dt.datetime.now()

  df = web.DataReader("NFLX", 'yahoo', query_start, query_end)

  df.reset_index(level=0, inplace=True) # create new column and move Date index
                                        # to column "Date"

  df["Daily_Gain"] = ""
  df.loc[:,"Daily_Gain"] = df.iloc[0:,close_]-df.iloc[0:,close_].shift(1)

  print(df.columns)

  # # Plot the close prices
  fig, axs = plt.subplots(2)
  axs[0].plot(df["Date"],df["Daily_Gain"])
  axs[1].plot(df["Date"],df["Close"])
  plt.show()
TestNealPlot()