# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:10:41 2021

@author: Nitu
"""
# map function

def sqr(x):
    return x**2

mylist = [4,5,6,2,12,3.5,15]

# one approach
for i in mylist:
    print(sqr(i))

# other approach with map function
list(map(sqr,mylist))
###########################################################
###########################################################
def sqr(x,y):
    return (x**2) + y

mylist1 = [4,5,6,2,12,3.5,15]
mylist2 = [6,6,1,9,2,4,1]

# one approach
for i,j in zip(mylist1,mylist2):
    print(sqr(i,j))

# other approach with map function
list(map(sqr,mylist1,mylist2))

help(map)


# lambda functions

def sqr(x):
    return x**2

mylist = [4,5,6,2,12,3.5,15]

# one approach
for i in mylist:
    print(sqr(i))

# other approach with map function

list(map(sqr,mylist))


list(map(lambda x:x**2,mylist))

m = lambda a:a+5
m(4)
