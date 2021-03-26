# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:35:14 2021

@author: Barry
"""
delete when ItemEnum is finished
debugModule = True

from LibDefinitions  import ASCII
from LibDefinitions  import printSectionHeader
LINELENGTH = 60
"""===========================================================================
Example 3: Property Decorator.
---------------------------------------------------------------------------"""
""" https://artandlogic.com/2015/01/dynamic-python-method/
def add_description_fn(description):
   fn_name = description + '_values'

   def fn(self):
      print "{0}: {1}".format(self.name, self.descriptions[description])
   setattr(Animal, fn_name, fn)

for description in description_names:
   add_description_fn(description)

cat.color_values()
# => cat: ['red', 'orange']
cat.sound_values()
# => cat: ['purr', 'meow']
"""
""" VBA bdcRecordClass
myFields() As Variant 'Array - Index: Enum,   Value: Field value
myFieldName As Dictionary ' Key:   Enum,      Value: FieldName
myFieldKey As Dictionary  ' Key:   FieldName, Value: Enum
"""
class IndexEnum:
  descriptions = {}
  TextLabel    = {} #input EnumKey, Output TextLabel
  TextKey      = {} #input EnumKey, Output TextKey
  EnumKey      = {} #input TextKey, Output EnumKey
  PropertyName = {} #input EnumKey, Output PropertyName
  # Using @property decorator

  def __init__(self, name, newEnum, newLabel, newProperty):
      self.__name = name + "_"
      self.enum = newEnum
      self.label = newLabel
      self.TextLabel[newEnum]=newLabel
      self.EnumKey[newLabel]=newEnum
      self.PropertyName [newEnum]= newProperty

  @property
  def name_(self):
      return self.__name

s = IndexEnum('PriceName', 3, "Stock Price","Price")
def add_description_fn(textkey):
  fn_name = textkey + '_'
  print ("New function name <%s>" % (fn_name))
  @property
  def get_fn(self):
    return self.EnumKey[textkey]
  getattr(IndexEnum, fn_name, get_fn)

# for description in description_names:
add_description_fn('price')

print ("Label <%s>" % s.Price_)
print ("Property name <%s>" % s.name_)

print ("Name<%s> Enum<%s> Label<%s>" % (s.name_,s.enum,s.label))
print ("__dict__: ", list(s.__dict__))
"""------------------------------------------------------------------------"""
""" https://artandlogic.com/2015/01/dynamic-python-method/
def add_description_fn(description):
   fn_name = description + '_values'

   def fn(self):
      print "{0}: {1}".format(self.name, self.descriptions[description])
   setattr(Animal, fn_name, fn)

for description in description_names:
   add_description_fn(description)

cat.color_values()
# => cat: ['red', 'orange']
cat.sound_values()
# => cat: ['purr', 'meow']
"""