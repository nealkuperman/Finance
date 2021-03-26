# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:13:57 2021

@author: Barry
                          Modification History
2021-02-05 Created class constants to store value of nextkey. Barry Martin Dancis
2021-02-05 Added def nextkey to calculate value of next key. Barry Martin Dancis
2021-02-05 Added compression defs for keys, values, names and displays. Barry Martin Dancis
2021-02-05 Added def size to TestEnum. Barry Martin Dancis
2021-02-06 Created global def printenum to print compression output of TestEnum. Barry Martin Dancis
"""

#=======================================================================
from enum            import Enum, IntEnum, auto
from LibDefinitions  import ASCII, printSectionHeader
#=======================================================================
debugModule=False
debugModule=True
LINELENGTH = 60

class constants:
  FirstKey = 0
  NextKey = FirstKey

class TestEnum(Enum):
  Date       = (     5, "Date Text")
  High       = ('auto', "High Text")

  # def __new__(self, nextkey, display): # if it works replace self w/ cls
  def __init__(self, key, display):
    # print ("%s type key is <%s>" % (display, type(nextkey)))
    self.key     = self.nextkey (key,constants)
    self.display = display

  @classmethod
  def nextkey(cls, key, constants):
    if isinstance(key,int): # use __Nextkey__
      constants.NextKey = key
      print("1.constants next key: %s" % constants.NextKey)
    else: #Not an int. used saved value
      print("2.constants next key: %s" % constants.NextKey)
      key = constants.NextKey
    print("3.constants next key: %s" % constants.NextKey)
    constants.NextKey  += 1
    print("4.constants next key: %s" % constants.NextKey)
    return key
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


  # High       = (auto(), "High Text")
  # Low        = (auto(), "Low Text")
  # Open       = (auto(), "Open Text")
  # Close      = (5, "Close Text")
  # Volume     = (auto(), "Volume Text")
def printenum (nextEnum):
  printSectionHeader(nextEnum.__name__)
  print ("Enum values <%s>" % (nextEnum.values()))
  print ("Enum names <%s>" % (nextEnum.names()))
  print ("Enum displays <%s>" % (nextEnum.displays()))
  print ("Enum keys <%s>" % (nextEnum.keys()))
  print ("Enum size <%s>" % (nextEnum.size()))
printenum(TestEnum)