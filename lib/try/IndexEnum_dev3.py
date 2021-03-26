# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 18:13:40 2021

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
2021-02-20 Added module DEBUG constants. Barry Martin Dancis
                                To Do
2021-02-?? Fix use of values to include generated index instead of default auto
2021-02-?? Add default arguments for input to __init__

"""
#=======================================================================
from enum            import Enum, IntEnum, auto
from LibDefinitions  import ASCII, printSectionHeader

DEBUG = True
# DEBUG = False
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
  def __init__(self, key, display):
  # def __init__(self, key='none', display='none'):
    self.key     = self.nextkey (key)
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

class TestEnum(IndexEnum):
  Date       = (5, "Date Text")
  High       = (IndexEnum.AUTO_KEY, "High Text")

class TestEnum2(IndexEnum):
  Date       = (0, "Date Text")
  High       = ('auto', "High Text")
  Low        = (0, "Low Text")
  Open       = (auto(), "Open Text")
  Close      = (15, "Close Text")
  Volume     = (auto(), "Volume Text")

if DEBUG:
  printenum(TestEnum)
  printenum(TestEnum2)