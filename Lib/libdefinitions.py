# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:13:57 2021

@author: Barry
                          Modification History
2021-02-22 Removed ENUM superclass from ASCII. Barry Martin Dancis
2021-02-22 Added function concat. Barry Martin Dancis
                              To Do
2021-02-16 Fix concat in function in class ASCII. Barry M Dancis
"""
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
  LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  ALPHANUMERICS = LETTERS + DIGITS
  SECTIONHEADERCHAR = HYPHEN
  SESSIONHEADERCHAR = EQUAL
  PERIOD = "."
  SEMICOLON = ";"
  SINGLEQUOTE = "'"
  SLASH = "/"
  SPACE = " "
  UNDERBAR = "_"
    

  def concat (self, strings, separator=' '):
    concatstring = str(strings[0])
    for nextstring in strings[1:]:
      if not isinstance(nextstring,str):
        nextstring = str(nextstring)
      print ('in Class: Type of next string: %s' % type(nextstring))
      print ('in Class: Type of str(next string): %s' % type(str(nextstring)))
      concatstring = concatstring + separator + nextstring
    return (concatstring)


DEFAULTLINEWIDTH = 60
def concat (strings, separator=' '):
  concatstring = str(strings[0])
  for nextstring in strings[1:]:
    if not isinstance(nextstring,str):
      nextstring = str(nextstring)
    concatstring = concatstring + separator + nextstring
  return (concatstring)


def printSectionHeader (SectionName="",
                        LineWidth=DEFAULTLINEWIDTH,
                        HeaderChar=ASCII.SECTIONHEADERCHAR):

  print (LineWidth * HeaderChar)
  print (SectionName.center(LineWidth,HeaderChar))

if __name__ == '__main__':
  debugModule = False
  # debugModule = True
  def Test_printSectionHeader():
    if not debugModule:
      return
    printSectionHeader("Testing printSectionHeder")
    printSectionHeader("Section Heder")
    printSectionHeader("Section Heder",60)
    printSectionHeader("Session Heder",60,ASCII.SESSIONHEADERCHAR.value)
    printSectionHeader("Session Heder",60,ASCII.SECTIONHEADERCHAR.value)
    # printSectionHeader("Session Heder",,ASCII.SECTIONHEADERCHAR.value)
  Test_printSectionHeader()

  names = ['Date', 'High', 'Low', 'Adj Close', 'Daily Gain', '% Change']
  # names = [0,2,5,4,22,3,66,99]
  print (concat([name.replace(' ','_') for name in names],' '))
  print (names)
  print (type(concat(names,'ZZZZZ')), ASCII.DIGITS)