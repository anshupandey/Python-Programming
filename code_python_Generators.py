# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:10:00 2021

@author: anshu
"""


def myfun(a):
    return a+5,a+6,a+7,a+8,a+9

mydata = myfun(6)
type(mydata)
print(mydata)

# Generators - special type of iterators, more memory efficient

def mygen(a):
    yield a+5
    yield a+6
    yield a+7
    yield a+8
    yield a+9
    
gen = mygen(5)
type(gen)
print(gen)

next(gen)
next(gen)
next(gen)
next(gen)

gen = mygen(5)
for v in gen:
    print(v)
    
    
################################################
# creating generators using tuple comprehension
mylist = [4,5,2,3,6,9,8]

#  get square of each value

newdata = (k**2 for k in mylist) # tuple comprehension
type(newdata)
print(newdata)

for v in newdata:
    print(v)
    
newdata = (k**2 for k in mylist)
list(newdata)
    

########################################################
#########################################################

# Map and filter

mylist = [4,5,2,3,6,9,8]

def mycalc(x):
    return x**2 + 2*x + 5

# one approach - comprehension
out = [mycalc(k) for k in mylist]
print(out)

# second approach
out = map(mycalc,mylist)
type(out)
print(out)

for v in out:
    print(v)
    
# filter - used to filter out the values from the iterable

def myfil(x):
    if x%2==0:
        return True
    else:
        return False
    
out = filter(myfil,mylist)
type(out)

for k in out:
    print(k)
    
#########################################################
# creating a list using list comprehension
mylist = [k**2 for k in range(1,10000)]

# creating a generator object using tuple comprehension
mygen = (k**2 for k in range(1,10000))

# Which is more memory efficient

import sys
sys.getsizeof(mylist)
sys.getsizeof(mygen)


# which is more faster

import cProfile
cProfile.run('sum(mylist)')
cProfile.run('sum(mygen)')



#####################################################
#####################################################

file = r"D:\AI\data\datasets-1\Bank_churn_modelling.csv"

data_lines = (line for line in open(file))
data_lines = (line.strip().split(',') for line in data_lines)
col_names = next(data_lines)
data_dict = (dict(zip(col_names,line)) for line in data_lines)

next(data_dict)


############################################
file = r"D:\AI\data\datasets-1\Bank_churn_modelling.csv"

data_lines = (line for line in open(file))
data_lines = (line.strip().split(',') for line in data_lines)
columns = next(data_lines)
data_dict = (dict(zip(columns,line)) for line in data_lines)
male_age = (int(data['Age']) for data in data_dict if data['Gender']=="Male")

sum(male_age)
