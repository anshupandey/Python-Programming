# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:51:20 2022

@author: admin

"""

import sys

# Generators
# - a special iterators which are more memory efficient 
# than standard iterable objects

m = [4,5,3,6]
print(m)
for i in m: print(i)

def mfun(a):
    return a+5,a+6,a+7,a+8,a+9

m = mfun(3)
print(m)
sys.getsizeof(mfun)
sys.getsizeof(m)
###########################################


def gfun(a):
    yield a+5
    yield a+6
    yield a+7
    yield a+8
    yield a+9
    
m = gfun(6)

sys.getsizeof(m)

type(m)

sys.getsizeof(next(m))
next(m)
next(m)
next(m)
next(m)

m = gfun(9)
for i in m:print(i)




kk = gfun(8)
next(kk)

###########################################################
#############################################################


m = [4,5,3,5,6]
k = (i**2 for i in m)
type(k)

next(k)
#############################################################
###############################################################



# building a data pipeline with generators

file = r"C:\Users\admin\Desktop\Bank_churn_modelling.csv"
dlines = (line for line in open(file,'r'))
dlist = (line.strip().split(",") for line in dlines)
colnames = next(dlist)

ddict = (dict(zip(colnames,lines)) for lines in dlist)

# get sum of age for all customers
age = (int(cust['Age']) for cust in ddict)

sum(age)

#################################################################

#map

m = [7,5,4,2,6,9,3]

def myfun(x):
    return x**2

out = map(myfun,m)
type(out)

for i in out:print(i)

#################################
def myfun(x,y):
    return x+y

list(map(myfun,m,m))






# filter

m = [7,5,4,2,6,9,3]

def geteven(x):
    if x%2==0:
        return True

out2 = filter(geteven,m)
for i in out2:print(i)

# reversed
k = reversed(m)
for i in k:print(i)
