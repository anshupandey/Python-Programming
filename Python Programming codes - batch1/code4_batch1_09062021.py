# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:35:24 2021

@author: Nitu
"""
# Functions in python

## Built in functions

x = [4,5,6,2,8]
sum(x)
min(x)
max(x)
print(x)
len(x)
type(x)
sorted(x)
dir(x)
round(2.345343534,2)
help(sorted)

## User defined functions
def myfun():
    print("Hey hi from myfun")
    return None

def myfun2(a,b):
    c = a+b
    return c


myfun()

myfun2(4,9)

##################################
# making an input argument accept  a defualt value
def myfun2(a,b=1):
    c = a+b
    return c

myfun2(6,5)
myfun2(5)

# *arg = make a function accept variable number of arguments
def myfun(a,*b):
    # a will be a single value
    # b will be taken as a tuple
    print(a,type(a))
    print(b,type(b))
    return None

myfun(3)
myfun(3,4)
myfun(3,4,5,2,3,5,9)

def myfun(a,*b):
    c = a
    for i in b:
        c = c + i
    return c

myfun(4)
myfun(4,3)
myfun(4,5,2,3,5,6)

# **kwarg = make a function accept variable number of 
# keyword arguments

def myfun(a,**b):
    # a will be a single value
    # b will be taken as a tuple
    print(a,type(a))
    print(b,type(b))
    return None


myfun(4,name="anshu",salary=10000,laptop=["hp",'lenovo'])

def myfun(age,**b):
    if 'name' in b.keys():
        print("Hey %s Welcome"%b['name'])
    if 'w' in b.keys() and 'h' in b.keys():
        w = b['w']
        h = b['h']
        h = h/100
        bmi = w/(h*h)
        print("Hey your bmi is ",bmi)
    print("you are age is ",age)
    return None

myfun(24)
myfun(24,name="Anshu")
myfun(24,name="Anshu",w=60,h=150)

#################################################
def myfun(a,b):
    "this function can be used to add two numbers or concatenate two strings"
    c = a+b
    return c


help(myfun)
myfun.__doc__


def myfun(a,b):
    """
    THis function can be used to add two numbers
    Parameters
    ----------
    a : Integer/float
        it can be any number - integer or float.
    b : Integer/float
        it can be any number - integer or float.

    Returns
    -------
    c : float
        it will addition to two input args.

    """
    c = a+b
    return float(c)

x = "Hello world"
y = list(x) # string to list
print(y,type(y))
z = "_".join(y)
print(z)
z = "".join(y)
print(z)
#########################################################
# Task 1

# Write code which accepts a number from user and returns the reverse of it.
# For example

# reverse_number(852) will return 258
# reverse_number(6242) will return 2426
# reverse_number(81) will return 18
#######################################################

def reverse_number(x):
    x = str(x)
    y = reversed(x) # reversed function outputs a generator obj
    y = "".join(y)
    return int(y)

reverse_number(2345)
reverse_number(6242)

def reverse_number(x):
    return int("".join(reversed(str(x))))

reverse_number(2345)

# ####################################################
# Task 2
# Write code to generate the fibiniocci series.
# Create a function fib(length) which generates fibiniocci series of a specific lenght. For example

# fib(5) will return [0,1,1,2,3]
# fib(8) will return [0,1,1,2,3,5,8,13]
# fib(10) will return [0,1,1,2,3,5,8,13,21,34]
# you can use [0,1] as known initial values
#####################################################

def fib(n):
    c = [0,1]
    for i in range(n-2):c.append(c[-1]+c[-2])
    return c

fib(3)
fib(8)
fib(12)

###########################################################

x = "Hello World from Python"

print(x,type(x))

print(x[0])
print(x[2])
print(x[-5])
print(x[2:11])

for i in x: print(i)
#strings are immutable
x[0] = "W"

x.upper()
x.lower()
x.split()
x.count('o')


################################################
x = "hello"
y = "hello"
id(x)
id(y)

x = [4,5,6]
y = [4,5,6]
id(x)
id(y)

a = 6
def myfun():
    b = 12
    print(a,b)
    return None

print(a) 
print(b)
myfun()
##################################################
## call by value
k = 'hi'
def test(k):
    k = 'hello'
    print("Inside the function ",k)
    return None

test(k)
print("Outside the function ",k)

## call by object reference
mylist = [4,5,6]
def test(mylist):
    mylist.append(7)
    print("Inside function ",mylist)
    return None
test(mylist)
print("outside function ",mylist)




#########################################################################

#generators = a type of iterators which can be iterated only once

def myfun1():
    x = 9
    return x,x+1,x+2

k = myfun1()
for i in k:print(i)

print(k,type(k))
###############################
def myfun1():
    x = 9
    yield x
    yield x+1
    yield x+2
    
k = myfun1()
for i in k:print(i)

print(type(k))

k = myfun1()
next(k)
next(k)
next(k)

m = iter("hello")
next(m)

