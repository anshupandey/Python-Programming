# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:03:01 2021

@author: Nitu
"""

# map function

def sqr(x):
    return x**2

mylist = [3,5,7,8,1,12,5,24,5.5]

# one possible approach
for i in mylist:
    print(sqr(i))
    
# other approach to iterate using map function
list(map(sqr,mylist))

########################################################
def sqr(x,y):
    return x**2 + y**2

mylist1 = [3,5,7,8,1,12,5,24,5.5]
mylist2 = [7,8,5,24,5,4,21,9,4]

list(map(sqr,mylist1,mylist))

#################################################################

# Lambda functions - anonymous functions

def sqr(x):
    return x**2

mylist = [3,5,7,8,1,12,5,24,5.5]

list(map(sqr,mylist))


list(map(lambda x:x**2, mylist))


m = lambda x,y:x+y+5
m(3,4)


