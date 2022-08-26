# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:22:32 2022

@author: admin
"""

m = [4,5,6,3]

for i in m: print(i)

################################

def myt(a):
    return a+3,a+4,a+5,a+6,a+7

k = myt(3)
type(k)
print(k)

for i in k:print(i)

###########################################

# generator

def kyt(a):
    print("hey hi")
    yield a+3
    
    yield a+4
    yield a+5
    yield a+6
    yield a+7
    
w = kyt(3)

type(w)

print(next(w))
next(w)
next(w)
next(w)
next(w)
next(w)
########################

w = kyt(2)

for i in w:print(i)

###################################################
#####################################################


m = [7,5,4,2,6,3,6,9,3]

mygen = (i**2 for i in m)
type(mygen)

for i in mygen: print(i)

#######################################################
w = kyt(2)
list(w)
list(w)
w = kyt(2)
next(w)
next(w)
list(w)

########################################################


file=r"C:\Users\admin\Desktop\Bank_churn_modelling.csv"

mydata = (line for line in open(file,'r').readlines())
type(mydata)

mydata = (line.strip().split(',') for line in mydata)

# access the column names
colnames  = next(mydata)
colnames

mydict = (dict(zip(colnames,line)) for line in mydata)

age_data = (int(cust['Age']) for cust in mydict)
sum(age_data)

##########################################

import sys
sys.getsizeof(age_data)

#################################################

file=r"C:\Users\admin\Desktop\Bank_churn_modelling.csv"

mydata = (line for line in open(file,'r').readlines())
mydata = (line.strip().split(',') for line in mydata)
colnames  = next(mydata)
mydata = (dict(zip(colnames,line)) for line in mydata)

mydata = (int(cust['Age']) for cust in mydata)
sum(mydata)

sys.getsizeof(mydata)

######################################################

ndata = [line for line in open(file,'r').readlines()]
sum([int(line.strip().split(',')[6]) for line in ndata[1:]])
sys.getsizeof(ndata)

##########################################################

# map

m= [7,8,5,9,6,3,3,2,3,6,4]

def mfun(a):
    return a**2

mm = map(mfun,m)
type(mm)

for i in mm:print(i)

# filter

m= [7,8,5,9,6,3,3,2,3,6,4]

def geteven(a):
    if a%2==0:
        return True

ff = filter(geteven,m)
type(ff)

for i in ff: print(i)

# reversed

m= [7,8,5,9,6,3,3,2,3,6,4]

rr = reversed(m)
type(rr)
for i in rr: print(i)
