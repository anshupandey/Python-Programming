# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:06:31 2021

@author: anshu
"""

# Iterators = objects over which we can iterate
# an interator object is initialized with iter() method
# it uses next() method for iteration

x = [4,5,36,9,6]
y = iter(x)
next(y)
next(y)
next(y)
next(y)
next(y)
next(y)

# iterable objects = list, tuple, dictionary, string
# a special type of iterables are generators

# =============================================================================
# Generators
#     - special type of iterators
#     - more memory and compute efficient than list and others
#     - very useful for sequential calculations and data processing
#     - generators can be created using generator functions
#     -  generators function use yield inplace of return
# =============================================================================


def myfun(a,b):
    return a+2,a+3,a+4,a+5,a+6,a+b

op = myfun(4,9)
type(op)
print(op)

# writing a generator function
def mygen(a,b):
    yield a+2
    yield a+3
    yield a+4
    yield a+5
    yield a+b

gen = mygen(4,9)
print(gen,type(gen))
next(gen)

###################################################
for i in op:print(i)
gen = mygen(4,9)
for i in gen:print(i)
########################


#########################################################
# other approach of creating generator obj from an interator

# tuple comprehension -> generator
mylist = [7,8,5,6,9,2,3]
mytup = (c**3 for c in mylist)
type(mytup)


####################################################
# Map

def myfun(x):
    return x**3 + x**2 + 10

mylist = [5,4,8,7,9,6,3,2,1]

myop = map(myfun,mylist)
type(myop) # ouput of map fun = map object - generator in nature

for i in myop:print(i)

myop = map(myfun,mylist)
print(list(myop))

#######################################################
#######################################################

# filter - reduced/smaller/filtered iterable based on a func

mylist = [5,4,8,7,9,6,3,2,1]

# create which return true for even and false for odd

def myfun(a):
    if a%2==0:
        return True
    
fop = filter(myfun,mylist)
type(fop) # filter object - generator
list(fop)

############################################
# lambda function - anonymous fuction
# the functions which do not have any name
# for simpler logics, it is recommended to use lambda function

def myfun(x):
    return x**3 + x**2 + 10

y = lambda x:x**3 + x**2 + 10
y(2)
myfun(2)




mylist = [5,4,8,7,9,6,3,2,1]
myop = map(myfun,mylist)
list(myop)

##### with lambda function
myop = map(lambda a:a**3 + a**2 + 10, mylist)
list(myop)



fop = filter(lambda k:True if (k%2==0) else None, mylist)
list(fop)

m = lambda s:s**2
m(5)
