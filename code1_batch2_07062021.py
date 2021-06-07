# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:29:44 2021

@author: Nitu
"""

print("Hello WOrld")

# i am a single line comment
"""
I am a part of multiline commment
I am also the part of multiline comment
"""


x = 8
y = 7.8
z = "Hello World"

print(x+y,z)

"""
Python Programming

- Operators in Python

Four important pillars
    - Data Types
        - primitive data types - integer, float, string, boolean, complex
        - Non primitive data types - list tuple, dictionary, set
    - COntrol Flow
        - if else
        - for loop
        - while loop
    - FUnctions
        - built in functions
        - user defined functions
    - Object oriented programming
"""
# operators in python
## Assignment operator
x = 5 # here 5 is assigned to x

## comparison operator 
x = 5
y = 6
x==y # to compare whether x is equal to y or not
x<y # to check whether x is less than y or not

x>y # to check whether x is greater than y or not
x<=y # to check whether x is less or equal to y or not
x>=y # to check whether x is greater or equal to y or not
x!=y # to check whether x is not equall to y or not

## mathematical operators
x+y
x-y
x*y
x/y
x**5


# Data types in Python
## Primitve data types

### integers
x = 8
print(x)
type(x)

### float
y = 3.4
print(y)
type(y)

### string
k = 'hi from python'
print(k)
type(k)

### boolean
m = True
print(m)
type(m)

### complex
m = 45 + 8j
print(m)
type(m)

### Non Primitve Data types
#### List
"""
List 
    - used to store a collection of values, values can be of different data types
    - it supports repeatation of values
    - lists are customizable/mutable
    - can be defined using [] - square brackets / upper brackets
"""

x = [23,2.5,'hi','hello',12]
print(x)
type(x)
len(x) # used to check length of an iterable - list

#### indexing
print(x[0])
print(x[3])
print(x[-1])
print(x[-3])

#### slicing - accessing more than 1 value in the form of a list from a list
print(x[1:4]) # getting x[1],x[2],x[3]
print(x[0:5])
print(x[3:6])
print(x[2:]) # getting values from x[2] till end of list
print(x[:4]) # getting values from begining of list till x[3]

#### customization
print(x)
x[0] = 33
print(x)
x.append('python') # append a new value at the end of the list
print(x)
x.insert(3,'hey')  # insert the value "hey" on 3rd position in the list
print(x)
x.remove('hi') # remove "hi" from the list
print(x)
x.pop(3) # remove the value from 3rd position in the list
print(x)

##############

### Tuple
"""
Tuple 
    - used to store a collection of values, values can be of different data types
    - it supports repeatation of values
    - tuples are not-customizable/immutable
    - can be defined using () - parenthesis / lower brackets
"""

y = (12,25,5.9,'hey','hii','python',50)
print(y)
type(y)
len(y)

#### indexing
print(y[0])
print(y[2])
print(y[-1])
print(y[-4])

#### slicing
print(y[2:5])
print(y[1:3])

#### tuples are immutable
y[0] = 30 # this will generate error as tuples are immutable


### Dictionary
"""
Dictionary
    - used to store a collection of key:value pair
    - keys can not repeat, values can repeat
    - it is customization/mutable
    - can be defined using {} - curly brackets / flower brackets / middle brackets
"""

w = {"Name":"Anshu","Age":21,"Salary":"Low","laptop":"Hp"}

print(w)
type(w)
len(w)

#### indexing
print(w['Name'])
print(w['Age'])

#### dictionary is customizable
w["Age"] = 39

w["Country"]="India" # adding a new key:value pair
print(w)

w.pop("Salary") # remove a key:value pair
print(w)

w.keys()

w = {"Name":["Anshu","John","Marco"],"Age":[25,35,45]}
print(w)
print(w["Name"])
print(w['Age'])
print(w["Name"][1])

### set
"""
Set
    - a collection of values, values can be of different data type
    - does not support repeatation of values
    - unordered data type - you can not do indexing
    - widely used for set theory operations such as union and intersection
    - can be defined using {} - curly brackets / flower brackets / middle brackets
"""

m = {3,4,4,3,2,7,8,12,9}
n = {5,6,7,2,3}

print(m)
type(m)
len(m)

m.union(n)
m.intersection(n)

#######################################

x = 12
y = float(x)
print(y,type(y))
m = str(x)
print(m,type(m))
k = 0
k = bool(k)
print(k,type(k))
m = "234"
m = int(m)
print(m,type(m))


m = "hi"
m = int(m) # this will generate a valueError

#########################
x = [4,5,6,12,3,4]
y = tuple(x)
print(y,type(y))

m = (3,4,5,6,6,7)
n = list(m)
print(n,type(n))
k = set(y)
print(k,type(k))

m = [["abc",123],['def',456],['xyz',789]]
k = dict(m)
print(k)
print(type(k))


x = "hii "
y = "hello"
x+y
