# Integer(floor) division
#print 4//3
print 'a' in 'sdfsdfsdfaasdf'
print '%s %s' % ('hello', 'man')
print '%(x)s %(y)s' % {'x':'hello', 'y':'man'}
import string
xytemplate = string.Template('$x $y')
print xytemplate.substitute({'x':'hello', 'y':'man'})
print xytemplate.substitute(dict(x='hello', y='man'))
# list comprehension - creates list
aList = [x for x in range(5)]
print aList
# list generation - creates generator - uses ()
aList = (x for x in range(5))
print aList
print aList.next()
print aList.next()
listuple1 = list('abcd')
lis
listuple2 = list('efgh')
listuple2.append(l1)
print 'Append: %s' % listuple2
listuple2 = list('efgh')
listuple2.extend(l1)
print 'Extend: %s' % listuple2
# Tuple
tuple0 = ()
print 'tuple0 %s: %s' % (type(tuple0), tuple0)
tuple1 = (0)
print 'tuple1 %s: %s' % (type(tuple1), tuple1)
tuple2 = (0,)
print 'tuple2 %s: %s' % (type(tuple2), tuple2)
# Dictionary
d1 = {'a':1,'c':3}
d2 = dict(b=2,d=4)
d3 = dict(zip(list('ef'),[5,6]))
print 'd1: %s' % d1
print 'd2: %s' % d2
print 'd3: %s' % d3
d1.update(d2)
print 'd1 + d2: %s' % d1
dict = {}
for i,word in enumerate(('Now', 'is', 'the', 'time')):
    dict[i] = word
print dict
alist = ['Now', 'is', 'the', 'time']
print alist
alist.reverse()
print alist
print alist.reverse() # Invalid operation in print context - returns none


#              Files
#infile = open ('filename', 'r')
#allLines = infile.readlines
#for line in allLines:
#for line in infile: # More efficient - infile is an iterator
#             Loops
#for, while
#    continue - next iteration
#    pass  - do nothing - go to next statement
#    break - leave closest loop
#    else - execute at after last interation unless break encountered
#           Yield
#In functions only
#Inside a loop only
#returns the value of an expression
#First call to function, starts at top and exists from yield
#Next call starts after yield and continues from there within the interator
#  Imports
# All directories on path to import must contain the file __init__.py. It can be
#   an empty file.
# Files in PYTHONPATH or in dot directory path,
#    eg import dir1.dir2.mod loads dir1/dir2/mod.py
# Also: from mod import * - import all items in namespace
#          Decorators
#  Functions returning functions
#@staticmethod
#def fun1
#function staticmethod returns function fun1
#@classmethod
#def fun2

