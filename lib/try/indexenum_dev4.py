# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20

@author: Barry Martin Dancis
                          Modification History
2021-02-05 Created class constants to store value of nextkey. Barry Martin Dancis
2021-02-05 Added def nextkey to calculate value of next key. Barry Martin Dancis
2021-02-05 Added compression defs for keys, values, names and displays. Barry Martin Dancis
2021-02-05 Added def size to TestEnum. Barry Martin Dancis
2021-02-06 Created global def printenum to print compression output of TestEnum. Barry Martin Dancis
2021-02-18 Moved def __init__ to IdexEnum from TestEnum, TestEnum2. Barry Martin Dancis
2021-02-18 Renamed TestEnum to IndexEnum. Barry Martin Dancis
2021-02-18 Added Constants to inheritance of IndexEnum. Barry Martin Dancis
2021-02-18 Moved def __init__, key assignments to new subclassess TestEnum, TestEnum2. Barry Martin Dancis
2021-02-18 Moved def __init__ back to IdexEnum from TestEnum, TestEnum2. Barry Martin Dancis
2021-02-19 Renamed class Constants to AutoKey. Barry Martin Dancis
2021-02-19 Added AUTO_KEY text. Barry Martin Dancis
2021-02-20 Added DEBUGMODULE constants. Barry Martin Dancis
2021-02-20 Added test for __main__. Barry Martin Dancis
2021-02-20 Added default arguments for input to __init__
                                To Do
2021-02-?? Fix use of values to include generated index instead of default auto
2021-02-?? Fix handling of duplicate keys (date = 0, low = 1)

"""
#=======================================================================
from enum            import Enum, IntEnum, auto
from LibDefinitions  import ASCII, printSectionHeader

DEBUGMODULE = True
DEBUGMODULE = False
#=======================================================================
class AutoKey:
  AUTO_KEY = 'auto'
  FirstKey = 0
  NextKey = FirstKey

  @classmethod
  def nextkey(cls, key):
    if isinstance(key,int): # use __Nextkey__
      cls.NextKey = key
    else: #Not an int. used saved value
      key = cls.NextKey
    cls.NextKey  += 1
    return key

class IndexEnum(AutoKey, Enum):
  def __init__(self, key=AutoKey.AUTO_KEY, display='none'):
    self.key = self.nextkey (key)
    if display == 'none':
      self.display = self.name
    else:
      self.display = display

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
  def displays(cls):
    return [function.display for function in cls]

def printenum (nextEnum):
  printSectionHeader(nextEnum.__name__)
  print ("Enum values <%s>" % (nextEnum.values()))
  print ("Enum names <%s>" % (nextEnum.names()))
  print ("Enum displays <%s>" % (nextEnum.displays()))

  print ("Enum keys <%s>" % (nextEnum.keys()))
  print ("Enum size <%s>" % (nextEnum.size()))

if __name__ == '__main__':
  class TestEnum(IndexEnum):
    Date       = 5
    High       = (IndexEnum.AUTO_KEY)
    Low        = (8)

  class TestEnum2(IndexEnum):
    Date       = 1
    High       = ('auto')
    Low        = (0)
    Open       = auto()
    Close      = (15)
    Volume     = auto()
    Daily_Gain = (IndexEnum.AUTO_KEY, 'Daily Gain')

  printenum(TestEnum)
  printenum(TestEnum2)