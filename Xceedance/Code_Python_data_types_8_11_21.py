# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:43:52 2021

@author: anshu
"""

print("Hello from Python")

x = 5
y = 6
y = 2.5
z = "Hello everyone"

print(x+y, z , x*y)

# i am a single line comment in python


# =============================================================================
# Four important pillars of any language
# 1. Data types
#     - primitive data types - integer, float, string, complex, boolean
#     - non primitive data types - list, tuple, dictionary, set
# 2. Control flow structure
#     - if else
#     - for loop
#     - while loop
# 3. Functions
#     - built in functions
#     - user defined functions
#     - lambda functions, generators, decorators
#     
# 4. Object oriented programming
#     - creating class 
#     - iheritance
# =============================================================================

# Primitive Data types
# integer, float, string, boolean, complex

x = 5
print(x)
type(x) # get the data type of any python object

y = 2.5
print(y)
type(y)

z = "hi from python"
print(z)
type(z)

k = True
print(k)
type(k)

m = 5 + 9j
print(m)
type(m)

################################################
# Non Primitive Data types

# =============================================================================
# List
#     - a collection of values, values can be of different data types
#     - supports repeatation of values
#     - mutable - modifiable
#     - can be creaated using suqare/upper barckets - []
# =============================================================================
    
x = [4,'hi',12,5.6,True,'hello',45]
print(x)
type(x)
len(x) # check the length of an iterable

## Indexing - accessing the values based on position
# in python indexing always starts with 0 -> left to right direction
print(x[0])
print(x[5])
# python also supports negative indexing
# starts from -1 -> from right to left
print(x[-1])
print(x[-4])

# Slicing - accessing a sublist from a list
# slicing starts from lowerbound upto upperbound-1
print(x)
print(x[2:5])# lowerbound=2, upperbound=5,elements= x[2],x[3],x[4]
print(x[0:4])
# x[0],x[2],x[4]
print(x[0:5:2]) # start = 0, end = 5, jump/step = 2

# modify a list
print(x)
x[0] = 10 # replacce element on 0th position by 10
print(x)

x.append(20) # insert 20 at the end of the list
print(x)
x.insert(2, 'python') # insering 'python' on 2nd position
print(x)
x.remove('hello') # removing helllo from list
print(x)
x.pop(3) # removing element from 3rd position
print(x)
tiny = [45,30] # another list
x.extend(tiny) # extend previous list by insertingvalues from other list
print(x)

##############################################################

# =============================================================================
# Tuple
#     - a collection of values, values can be of different data type
#     - supports repeation of values
#     - immutable - not modifiable
#     - can be defined using round/lower brackets / parenthesis - ()
# =============================================================================
y = (45,23,'hii',True,12.5,65)    
print(y)
type(y)
len(y)

# indexing
print(y[0])
print(y[3])
print(y[-1])    
print(y[-5])    

# slicing 
print(y[2:6])    
print(y[1:4])    

# tuples are immutable - not modifiable
print(y)
y[0] = 30 # this will throw error


#############################################################

# =============================================================================
# dictionary
#     - a collection of key:value pair (similar to JSON)
#     - keys can be any type - immutable, unique(cant repeat)
#     - value can be anything, can repeat
#     - mutable - can be modified
#     - can be created using curly/flower/middle brackets - {}
# =============================================================================
m = {'name':'Anshu','age':42,'salary':452200}
print(m)
type(m)
len(m)

# indexing by using key (no meaning of using position)
print(m['name'])
print(m['age'])

# modify
m['city'] = 'Ahmedabad'
print(m)
m.pop('salary')
print(m)

m.items()
m.keys()
m.values()

#########################################################

# =============================================================================
# Set
#     - a collection of values, can be of different data types
#     - does not support repeatation
#     - does not support indexing
#     - primarily used for set theory operations - union, intersection
#     - mutable - can be modified
#     - can be created using curly/middle/flower brackets - {}
# =============================================================================
a = {4,5,6,5,4,7,3,2,3}
print(a)
type(a)
len(a)

b = {1,5,9,8,4,2,1}
print(b)
type(b)
len(b)

a.union(b)
a.intersection(b)

print(a)
a.add(45)
print(a)
a.remove(6)
print(a)
