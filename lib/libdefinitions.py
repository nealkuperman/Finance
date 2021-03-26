# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:13:57 2021

@author: Barry
                          Modification History
2021-02-22 Removed ENUM superclass from ASCII. Barry Martin Dancis
2021-02-22 Added function concat. Barry Martin Dancis
2021-02-25 Added function percent_change. Barry Martin Dancis
2021-03-04 Replace concat with system method join. Barry Martin Dancis
2021-03-04 Replace concat with system method join. Barry Martin Dancis
                              To Do
2021-02-16 Fix concat in functi# -*- coding: utf-8 -*-
"""

__all__ = ['ASCII', 'percent_change', 'printSectionHead']

DEFAULTLINEWIDTH = 60

class ASCII ():
  NOSTRING = ""
  BANG = "!"
  BAR = "|"
  COMMA = ","
  COLON = ":"
  CLOSESQUAREBRACKET = "]"
  DOLLARSIGN = "$"
  DOUBLEQUOTE = '\"'
  EQUAL = "="
  GREATERTHAN = ">"
  HYPHEN = "-"
  DIGITS = "0123456789"
  LESSTHAN = "<"
  LOWERCASEALPHAS = "abcdefghijklmnopqrstuvwxyz"
  UPPERCASEALPHAS = LOWERCASEALPHAS.upper()
  ALPHAS = LOWERCASEALPHAS + UPPERCASEALPHAS
  ALPHANUMERICS = ALPHAS + DIGITS
  SECTIONHEADCHAR = HYPHEN
  SESSIONHEADCHAR = EQUAL
  PERIOD = "."
  SEMICOLON = ";"
  SINGLEQUOTE = "'"
  SLASH = "/"
  SPACE = " "
  UNDERBAR = "_"
#------------------------------------------------------------------------------
def percent_change(from_value, to_value):
    return 100*((to_value - from_value)/from_value)
# end percent_change
#------------------------------------------------------------------------------
def printSectionHead (SectionName="",
                      LineWidth=DEFAULTLINEWIDTH,
                      HEADCHAR=ASCII.SECTIONHEADCHAR,
                      includetopline=True):
   if includetopline:
     print (LineWidth * HEADCHAR)
   print (SectionName.center(LineWidth,HEADCHAR))
#------------------------------------------------------------------------------
if __name__ == '__main__':
  debugModule = False
  debugModule = True
  def Test_printSectionHead():
    if not debugModule:
      return
    printSectionHead("Testing printSectionHead",60,ASCII.SESSIONHEADCHAR)
    printSectionHead("No top Line", includetopline=False)
    printSectionHead("Section Head",60)
    printSectionHead("SeSSion Head",60,ASCII.SESSIONHEADCHAR)
    printSectionHead("SeCTion Head",60,ASCII.SECTIONHEADCHAR)
  Test_printSectionHead()

  names = ['Date', 'High', 'Low', 'Adj Close', 'Daily Gain', '% Change']
  # names = [0,2,5,4,22,3,66,99]
  print (ASCII.SPACE.join([str(name).replace(' ','_') for name in names]))

  print (type('#'.join(names)))
  print (type('ZZZZZ'.join(names)), ASCII.DIGITS)

