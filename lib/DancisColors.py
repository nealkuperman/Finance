# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:13:57 2021

@author: Barry
                          Modification History
2021-02-22 Removed ENUM superclass from ASCII. Barry Martin Dancis
2021-02-22 Added function concat. Barry Martin Dancis
2021-02-25 Added function percent_change. Barry Martin Dancis
                              To Do
2021-02-16 Fix concat in function
"""
__all__ = ['ASCII', 'percent_change']

DEFAULTLINEWIDTH = 60

class ASCII (enum):
  _ClassVariable_ = 'class global var'
  NOSTRING = "" # class global var
  BANG = "!"
  BAR = "|"
  def methodname(self):  # class method name
    print (self.__name__)
    localvar0 = self._ClassVariable_
    localvar1 = 3
    localvar2 = "zz" # class method local var
#------------------------------------------------------------------------------
def percent_change(from_value, to_value):
    return 100*((to_value - from_value)/from_value)
# end percent_change
#------------------------------------------------------------------------------
if __name__ == '__main__':
  asciiInstance = ASCII # class instance
  debugModule = False
  # debugModule = True
  names = ['Date', 'High', 'Low', 'Daily Gain', '% Change']
  # names = [0,2,5,4,22,3,66,99]
  print (' '.join([name.replace(' ','_') for name in names]))
  print (names)