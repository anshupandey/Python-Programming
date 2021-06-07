# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:01:21 2021

@author: Nitu
"""

print("Hello World")
print("Hi from Python")


x = 10
y = 5.4
z = "hiiiii"
print(x,y,z)

# i am comment
# is used to write single line comment in python
'''
I am part of a multiline string, which can be used as multiline comment
 I am also in same multiline comment
'''
"""
Python Programming Fundamentals

-- Operators in python

1. Data Types
    - Primitive Data Types - integer, float, string, boolean, complex
    - Non primitive data types - list, tuple, dictionary, sets
    
    
2. Control Flow
    - if else
    - for loop
    - while loop
    
3. Functions
    - Builtin functions
    - User defined functions
    
4. Object oriented programming
"""

# Operators in Python

## Assignment Operator - "="
x = 5
y = 6

## comparison operators 
z = 6
z==y # to compare whether z is equal to y or not
z<y # to check whether z is less than y or not
z>y # to check whether z is greater than y or not
z<=y # to check whether z is less than or equal to y
z>=y # to check whether z is greater than or euqal to y

## mathematical operators
x + y  # addition
x - y # subtraction
x * y # multiplication
x / y # division
x**y # exponent



# Data Types in Python
## Primitive data types
### integers
x = 6
print(x)
type(x)
print(type(x))

### float
y = 5.4
print(y)
type(y)

### string
z = "hi from python"
print(z)
type(z)

### boolean
k = True
print(k)
type(k)

### complex
m = 45 + 6j
print(m)
type(m)

# data type conversions
x = 12
y = float(x) # converting integer to float
y = str(x) # converting to string
z = "456"
m = int(z) # converting to integer
m = float(z) # converting to float
k = 0
k = bool(k) # converting to boolean
print(k)
x = "hiiii"
int(x) # this will generate error - ValueError - as hii cannot be converted to int


## Non prmitive Data Types
### List
"""
List
    - used to store multiple values, of different data types
    - support repeatation of values
    - can be customized
    - can be defined using [] - square brackets / big brackets
"""
x = [12,2.5,'hii','hello',456]
print(x)
type(x)
len(x) # to check the length of an iterable - list
#### indexing a list
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])

#### slicing - accessing a list from a list
print(x[0:3]) # access values - x[0], x[1], x[2], will not consider x[3]
print(x[2:4])
print(x[2:6])
print(x[3:]) # slice it from x[3] till end of the list
print(x[:4]) # slice it from begining of list till x[3]

#### customization of list
print(x)
x[0] = 20 # replacing the 0th value by 20
print(x)
x.append('python') # appending a value at the end of list
print(x)
x.insert(3,500) # to insert a vaalue on a specific position
print(x)
x.remove(20) # to remove a value from the list
print(x)
x.pop(3) # remove the value from index=3
print(x)

