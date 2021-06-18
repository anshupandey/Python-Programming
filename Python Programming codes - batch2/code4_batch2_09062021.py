# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:36:47 2021

@author: Nitu
"""
# Functions in Python

# Builtin functions

x = [4,5,6,6,2]

print(x)
type(x)
len(x)
sum(x)
min(x)
max(x)
sorted(x)
dir(x)
help(sorted)

round(3.12223434,2)
list(reversed("Bombay"))

#######################################################

# User defined functions
def myfun():
    print("I am myfun function")
    print("hey hi")
    return None

myfun()

def myfun2(a,b):
    c = a + b
    return c

myfun2(4,6)
myfun2(23,11)


#####################################################
myfun2(8,9)
myfun2(3) # error

def myfun2(a,b=6):
    c = a + b
    return c

myfun2(3,9)
myfun2(4)

#####################################################
# *arg = a way of making a function accept variable number
# of arguments
def myfun(a,*b):
    print(a,type(a))
    print(b,type(b))
    return None

myfun(7)
myfun(8,2)
myfun(4,5,6,2,3,4,5)

def myfun(a,*b):
    c = a
    for i in b:
        c = c+i
    return c

myfun(7)
myfun(3,8)
myfun(2,3,4,9,2)

# **kwarg = making a function accept variable number of 
# keyword arguments

def myfun(a,**b):
    print(a,type(a))
    print(b,type(b))
    return None

myfun(4,name="anshu",month='June',Age=20)

def myfun(age,**b):
    print('You age is ',age)
    if 'name' in b.keys():
        print("Hey %s have a good day"%b['name'])
    if 'w' in b.keys() and 'h' in b.keys():
        w = b['w']
        h = b['h']
        h = h/100
        bmi = w/(h*h)
        print("your bmi is %.2f"%bmi)
    return None


myfun(24)
myfun(24,name="anshu")
myfun(24,name="Anshu",w=60,h=150)


#####################################################
def myfun2(a,b=6):
    "this function can be used to add two numbers or concatenate two strings"
    c = a + b
    return c

help(myfun2)
myfun2.__doc__

def myfun2(a,b=6):
    """
    this function can be used to add 2 numbers

    Parameters
    ----------
    a : integer/float
        this is the first numeric to be added
    b : integer/float
        this is another numeric argument The default is 6.

    Returns
    -------
    c : float/integer
        for two integers as input, output will be integer else float
    """
    c = a + b
    return c

help(myfun2)
print(myfun2.__doc__)


#######################################################

## string manipulation

k = "Hello world from Python"
print(k,type(k))

print(k[0])
print(k[3])
print(k[3:12])

k.find('world')
k.upper()
k.lower()
k.split()

m = list(k) # string to list conversion
print(m)

b = "_".join(m)
print(b)

b = "".join(m)
print(b)
k[0] = "m"
k.count('o')

########################################################

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
    y = reversed(x)
    y = list(y)
    y = "".join(y)
    return int(y)

reverse_number(34857)
reverse_number(234)

def reverse_number(x):
    return int("".join(list(reversed(str(x)))))

reverse_number(345)

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
fib(4)
fib(9)

#######################################################

# global v.s local variables

del k



m = 9 # global variable
def myfun():
    k = 78 # local variable
    print(m,k)
    return None

myfun()
print(m)
print(k)
print(w)

m = 9
def myfun():
    k = 78 # local variable
    
    global z
    z = 89
    print(m,k)
    return None

myfun()
print(z)

#######################################################

# Mutable - list, dictionary, set
# Immutable - string,int,float,bool,complex,tuple


x = "hello"
y = "hello"

id(x)
id(y)

x = [4,5,6]
y = [4,5,6]

id(x)
id(y)

# call by value
q = "hey"
def test(q):
    q = "hiii"
    print("Inside the function ",q)
    return None

test(q)
print("outside the function ",q)

# call by object reference

d = [4,5,6]
def test(d):
    d.append(12)
    print("Inside the function ",d)
    return None
test(d)
print("outside the function ",d)

