# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22  from IndexEnum

@author: Barry Martin Dancis
                          Modification History
2021-02-22 Generate keys and labels from data frame column names
2021-02-22 Create funtion getDataFrameEnum from input enum Name and columns
2021-02-25 Change display to label. Barry Martin Dancis
2021-03-04 Replace concat w/ join and change to use printSectionHead. Barry Martin Dancis
                                To Do
2021-02-?? Fix handling of duplicate keys (date = 0, low = 1)

"""
#=======================================================================
from enum            import Enum, IntEnum, auto
from libdefinitions  import *

DEBUGMODULE = True
DEBUGMODULE = False
#=======================================================================
__all__ = ['DataFrameEnum', 'getDataFrameEnum', 'printenum', 'printenummember']

class DataFrameEnum(Enum):
  def __init__(self, value):
    # Correct for zero-based Dataframes using one-based enum values
    self.key = value - 1
    # print (self.name)
    # Assumes spaces in dataframe column names were replaced with underbars
    #   to create enum names
    # label restores the space to the name for labelling and indexing of
    #   dataframes
    self.label = self.name.replace(ASCII.UNDERBAR, ASCII.SPACE)

  @classmethod
  def size(cls):
    return len([function.value for function in cls])
  @classmethod
  def values(cls):
    return [function.value for function in cls]
  @classmethod
  def names(cls):
    return [function.name for function in cls]
  @classmethod
  def keys(cls):
    return [function.key for function in cls]
  @classmethod
  def labels(cls):
    return [function.label for function in cls]

#------------------------------------------------------------------------------
def getDataFrameEnum(df_name, df_columns):
  print (type(df_columns))
  enumstring = ' '.join([name.replace(' ','_') for name in df_columns])
  # print ('data frame enum names: ', enumstring)
  return DataFrameEnum(df_name, enumstring)
# end getDataFrameEnum
#------------------------------------------------------------------------------
def printenum (nextEnum):
  printSectionHead(nextEnum.__name__)
  print ("Enum values <%s>" % (nextEnum.values()))
  print ("Enum names <%s>" % (nextEnum.names()))
  print ("Enum labels <%s>" % (nextEnum.labels()))
  print ("Enum keys <%s>" % (nextEnum.keys()))
  print ("Enum size <%s>" % (nextEnum.size()))
#------------------------------------------------------------------------------
def printenummember (member):
  printSectionHead(member.name)
  print ("Enum value <%s>" % (member.value))
  print ("Enum name <%s>" % (member.name))
  print ("Enum label <%s>" % (member.label))
  print ("Enum key <%s>" % (member.key))
#------------------------------------------------------------------------------

if __name__ == '__main__':

  names = ['Date', 'High', 'Low', 'Close', 'Adj Close', 'Daily Gain', 'Percent Change']
  dfEnum = getDataFrameEnum('DataFrame', names)

  printenum(dfEnum)
  printenummember(dfEnum.Close)
  printenummember(dfEnum.Adj_Close)
  # printenum(TestEnum2)