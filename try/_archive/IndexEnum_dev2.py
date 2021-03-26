# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:13:40 2021

@author: Barry
                          Modification History
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

                          To Do
2021-02-?? Fix use of values to include generated index instead of default auto

"""
#=======================================================================
from enum            import Enum, IntEnum, auto
from LibDefinitions  import ASCII, printSectionHeader
#=======================================================================
class Constants:
  FirstKey = 0
  NextKey = FirstKey

  @classmethod
  def nextkey(cls, key):
    if isinstance(key,int): # use __Nextkey__
      cls.NextKey = key
      print("1.cls next key: %s" % cls.NextKey)
    else: #Not an int. used saved value
      print("2.cls next key: %s" % cls.NextKey)
      key = cls.NextKey
    print("3.cls next key: %s" % cls.NextKey)
    cls.NextKey  += 1
    print("4.cls next key: %s" % cls.NextKey)
    return key

class IndexEnum(Constants, Enum):

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
  __NextKey__ = 0
  Date       = (5, "Date Text")
  High       = ('auto', "High Text")

  def __init__(self, key, display):
    self.key = self.nextkey (key)
    self.display = display

class TestEnum2(IndexEnum):
  # Date       = (0, "Date Text")
  # High       = ('auto', "High Text")
  Low        = (0, "Low Text")
  Open       = (auto(), "Open Text")
  Close      = (5, "Close Text")
  Volume     = (auto(), "Volume Text")

  def __init__(self, key, display):
    self.key = Constants.nextkey (key)
    self.display = display

printenum(TestEnum)
printenum(TestEnum2)