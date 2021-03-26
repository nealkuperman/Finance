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

class Yahoo(Enum):
  Date = 0
  High = Date + 1
  Low = High + 1
  Open = Low + 1
  Close = Open + 1
  Volume = Close + 1
  Adj_Close = Volume + 1
  daily_gain = Adj_Close + 1
y=Yahoo

# class YahooIndexEnum(IndexEnum):
#   FirstEnum = 5
#   Field = (('Date',),
#             ('High',),
#             ("Low",),
#             ('Open',),
#             ('Close',),
#             ('Volume',),
#             ('Adj_Close',),
#             ('Daily_Gain',)

#   def __init__(self, EnumerationName):
#     self.name = EnumerationName
#     self.addEnums(self.FirstEnum, self.Fields)
#     if debugModule:
#       printSectionHeader (self.name + " Dictionary")
#       print ("Dictionary:", list(IndexEnum.__dict__))

date_ = 0
high_ = date_ + 1
low_ = high_ + 1
open_ = low_ + 1
close_ = open_ + 1
volume_ = close_ + 1
adj_close_ = volume_ + 1
daily_gain_ = adj_close_ + 1

# # IMPORT using pandas_datareader (https://pandas-datareader.readthedocs.io)
date = (2015,1,1)
query_start = dt.datetime(*date)
query_end = dt.datetime.now()

df = web.DataReader("NFLX", 'yahoo', query_start, query_end)

df.reset_index(level=0, inplace=True) # create new column and move Date index
                                      # to column "Date"

df[y.daily_gain.name] = ""
df.loc[:,y.daily_gain.name] = df.iloc[0:,y.Close.value] - \
                              df.iloc[0:,y.Close.value].shift(1)

print(df.columns)

# # Plot the close prices
fig, axs = plt.subplots(3)
axs[0].plot(df["Date"],df["daily_gain"])
axs[1].plot(df["Date"],df['Close'])
# axs[2].plot(df["Date"],df["Adj Close"])
plt.show()