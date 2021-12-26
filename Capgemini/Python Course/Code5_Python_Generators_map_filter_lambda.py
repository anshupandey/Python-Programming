# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 19:42:10 2021

@author: anshu
"""

# =============================================================================
# # Generators
# 
# - special type of iterators, more memory efficient
# =============================================================================


def myfun(a):
    return a+2,a+3,a+4,a+5,a+6

k = myfun(5)
print(k)

##############################
# Use generators

# create a generator function

def mygen(a):
    yield a+2
    yield a+3
    yield a+4
    yield a+5
    yield a+6
    
w = mygen(5)
type(w)

# generators are iterators which allow us to iterate
# through it and access the values sequenetially

next(w)
next(w)
next(w)

########################################

w = mygen(5)

for i in w:
    print(i)
    
#####################################################


# map & filter

mylist = [4,5,2,3,6,9,8,7]

# create a new list to get square of each value

def mysq(a):
    return a**2

# one approach
out = []
for k in mylist:
    out.append(mysq(k))
print(out)

# more efficient approach
out = map(mysq,mylist)
print(out)
type(out)

next(out)


out = map(mysq,mylist)

for val in out:
    print(val)
    
####################################################

# filter
mylist = [4,5,2,3,6,9,8,7]

def geteven(a):
    if a%2==0:
        return True
    else:
        return False

out = filter(geteven,mylist)

for v in out:
    print(v)
    
#####################################################

# Lambda function = anonymous functions
# functions with no name


# without lambda function
mylist = [4,5,2,3,6,9,8,7]


def mysq(a):
    return a**2

out = map(mysq,mylist)
for v in out:print(v)

## with lambda function - lambda input:f(input)

out = map(lambda a:a**2,mylist)
for v in out:print(v)


k = lambda g:g**2 + 2*g + 5

k(6)



out = map(k,mylist)
for v in out:print(v)