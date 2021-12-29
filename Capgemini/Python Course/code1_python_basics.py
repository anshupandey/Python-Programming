# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:11:40 2021

@author: anshu
"""

print("Hello World")

x = 5
y = 6
z = x + y
print(z)

print("hey hi",x,y,z) # printing something
# i am a one line comment in python

x = "hello world from python"
y = 'hello world from python'
z = """ hi i am a part of 
multiline string
thanks
"""

print(x,y,z)

"""
i am a multiline string not assigned to variable
can be thought of as a multiline comment as well
"""

print(x)
x = 5
print(x)


#######################################

x = 5
x = 5; y = 6
x,y,z = "hi",2.5,45
print(x,y,z)
##################################################

# =============================================================================
# Four important pillars
# 
# 1. Data Types/structure
#     - Primitive Data types - integer, string, float, boolean, complex
#     - non primitive data types - list, tuple, dictionary and set
# 2. Control Flow
#     - if else
#     - for loop
#     - while loop
# 3. Functions
#     - Built-in functions
#     - user defined functions
# 4. Object oriented programming
#     - Class and creating objects
#     - inheritance
#     
# =============================================================================


# Data Types
## Primitive Data types
# integer
x = 5
print(x)
type(x)

# float
y = 2.5
type(y)
print(y)

# string
m = "hello world"
print(m)
type(m)

# Boolean - True, False
k = True
print(k)
type(k)

# complex - we use j to represent complex part
w = 5 + 4j
print(w)
type(w)

# Non primitive data types 

# =============================================================================
# Lists
#     - used to store collection of values, support repeatation of values
#     - accommodate values of different data types
#     - mutable object - modifiable
#     - can be created using square/upper bracket = []
# =============================================================================

x = [45,20,'hii','hello',2.5,12,True]
print(x)
type(x)

# getting the total number of values in a list
len(x)

# indexing - accessing the elements by their position
# in python indexing starts with 0 and goes from left to right
# leftmost = 0th element, rightmost = (n-1)th element (total n elements)
print(x[0])
print(x[3])
print(x[6])
print(x[20]) # this will throw error

# python also supports negative indexing 
# starts with -1 and goes from right to left
# rightmost element = -1st element
print(x[-1])
print(x[-3])

# slicing - accessing a sublist from a list
# mylist [lb:ub]
# lb = lowerbound, ub = uppperbound, from lb to ub-1
print(x[1:4]) # we will get [x[1],x[2],x[3]]
print(x[2:7])
print(x[2:20]) # no errors for specying higher ub

# slicing with step = lb:ub:step
print(x[1:7:2]) # x[1],x[3],x[5]

######################## Modify a list
print(x)
# change 0th value to 10
x[0] = 10
print(x)

# insert an element at the end of the list
x.append(60)
print(x)
# insert an element in between the list - 2nd position
x.insert(2,'python')
print(x)

# remove an element by value
x.remove('hii')
print(x)
# remove an element by position
x.pop(3)
print(x)

######################################################

# =============================================================================
# Tuple 
#     - a collection of values, supports repeatation of values
#     - supports values of different data types 
#     - immutable - not modifiable 
#     - can be created using parenthesis, small/lower brackets = ()
#     
# =============================================================================

y = (45,23,2.5,'hii',False,True,12)
print(y)
type(y)

len(y)

# indexing - rules are same as list
print(y[0])
print(y[3])
print(y[-1])
print(y[-2])

# slicing
print(y[1:4])
print(y[2:5])

# tuples are immutable
y[0] = 10 # this will throw error

#################################################################

# =============================================================================
# dictionary
#     - a collection of key:value pairs,
#     - only immutable objects can be used as keys, anything works for value
#     - keys are unique and values can repeat
#     - dictionary is mutable - modifiable
#     - can be created using flower/middle/curly brackets = {}
#     
# =============================================================================

w = {'name':'Anshu','Age':45,'Cities':['Delhi','Dubai','Kulalalumpur']}
print(w)
type(w)

len(w)

# indexing - values can be accessed by passig keys
print(w['name'])
print(w['Cities'])
print(w['Age'])

# modification
w['laptop'] = "hp" # adding a new key value pair
w['Age'] = 42 # modyfing existing key value pair
w.pop('name') # removing a key value pair
print(w)

print(w.keys())
print(w.values())

w['Cities'].append("Jakarta")
print(w['Cities'])

##############################################################

# =============================================================================
# Set
#     - collection of values, does not support repeatation
#     - supports elements of multiple data types
#     - unordered - you can not do indexing
#     - mainly used for set theory operations, union, intersection etc
#     - can be defined using curly/middle/flower brackets= {}
#     
# =============================================================================

m = {7,5,4,5,6,6,5,2}
print(m)
type(m)
len(m)

print(m[0]) # this will throw error

n = {4,2,5,5,3,1}
print(n)

# set theory operations
m.union(n)
n.intersection(m)

# set is mutable
m.add(12)
print(m)
m.remove(5) # to remove a specific value from set
print(m)
m.pop() # remove any value randomly
print(m)
m.add(1)
m.add(5)
print(m)

m.clear() # clearing the set
print(m)


print(n)
n.discard(3)
print(n)

print(n)
n.remove(10)
n.discard(10)


#############################################################

