# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:25:16 2021

@author: anshu
"""

# builtin functions

x = [8,4,5,6]

print(x)
type(x)
len(x)

sum(x)
max(x)
min(x)
sorted(x)
sorted(x,reverse=True)

round(2.465644684,2)
list(reversed(x))


help(sorted)

######### user defined functions

def myfun():
    print("Python is amazing and awesome")
    print("python is easy and simple")
    return None


myfun()


def myfun2(a,b):
    c = a + b
    return c

myfun2(4,9)

#del myfun 


# documentation string
def myfun2(a,b):
    "this function is used to add two numbers"
    c = a + b
    return c

help(myfun2)

# creating multiline string - triple quotes
x = """hi i am a string
i am a multiline strign """
print(x,type(x))

def myfun2(a,b):
    """
    Parameters
    ----------
    a : a number - int/float
        the first number to add
    b : int/float
        second number to add.

    Returns
    -------
    c : int/float
    Examples - 
    >> myfun2(4,6)
    10
    >> myfun2(7,-3)
    4
    """
    c = a + b
    return c

help(myfun2)

##############################################################

def myfun(a,b):
    c = a + b
    return c

myfun(7,6)
myfun(7)

# by defining a default value for an argument, we can make it optional
def myfun(a,b=6):
    c = a + b
    return c

myfun(7,3)
myfun(5)

##### making a function accept variable number of arguments
# *arg

def myfun(a,*b):
    print(a,type(a))
    print(b,type(b))
    return None

myfun(5)
myfun(4,3)
myfun(7,6,5,6,3)

def myfun(a,*b):
    c = a + sum(b)
    return c

myfun(5)
myfun(4,3)
myfun(7,6,5,6,3)

##############################################################

# keyword arguments

def mypy(name,salary):
    print('hi %s your salary is %d'%(name,salary))
    return salary + 100


mypy(salary=500,name='john')

# variable number of keyword arguments
# **arg

def mypy(name,**b):
    print(name,type(name))
    print(b,type(b))
    return None


mypy(name="anshu")
mypy(name="anshu",salary=500)
mypy(name="anshu",salary=500,age=25)

###############################################
name = "Anshu"
age = 25
print("hi ",name," your age is ",age)
print("Hi %s your age is %d "%(name,age))

# f string
print(f"Hi {name} your age is {age}")


##############################################################
# global v/s local variable

x = 5 # is a global variable
def myfun(a,b):
    output = a+b # here output is a local variable
    output = output + x
    return output

myfun(4,5)
print(output) # as output is a local variable, we will get error


# In python an input argument is always pass by reference

def myfun(mylist):
    print(mylist)
    mylist[0] = 25
    print(mylist)
    return None

mm = [45,56,23,12,78]
myfun(mm)

print(mm)

# link of pass by reference gets broken if you try to overwrite the object

def myfun(mylist):
    print(mylist)
    mylist = [25,65,23]
    print(mylist)
    return None

mm = [45,56,23,12,78]
myfun(mm)
print(mm)
print(mm)

