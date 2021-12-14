# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:11:35 2021

@author: anshu
"""

# Functions in python

# a function can be stored/accessed as an object
def myfun(a,b):
    c = a + b
    return c

mm = myfun 

mm(4,5)

# a function can accept another function as input

def calc(fun,a=4,b=6):
    m = fun(a,b)
    return m + 5

calc(myfun) # passing a function as input to another fun

# a function can be defined inside another function

def calc(a,b):
    a = a + 2
    def add(x,y):
        return x + y
    out = add(a,b)
    return out

calc(4,3)

# a function can return another function as output

def calc():
    def add(x,y):
        return x + y
    return add

mm = calc()

mm(4,2)

###################################################

# decorator - used to modify a function or a class

# =============================================================================
# Decorators can be created by making a wrapper function accept 
# another function as argument, process by a inner function
#  defined  inside the wrapper function, return inner fun
#  
# =============================================================================
 
 
# =============================================================================
# def wrapper_dec(fun):
#     def inner():
#         out = fun()
#         ## here modify the out object 
#         return out
#     return inner
# 
# =============================================================================

def mydecorator(fun):
    def pretty_text():
        out = fun()
        out = out.upper()
        out = out + "\n Hey Thanks"
        return out
    return pretty_text


def greet():
    return "Hey good morning"

greet()

# decorating greet - method 1

greet2 = mydecorator(greet)

greet()
greet2()

# decorating greet - method 2

@mydecorator
def greet():
    return "Hey good morning"


greet()

#####################################################
#####################################################



# Chaining decorators

def decorator1(fun):
    def wrapper(*arg):
        x = fun(*arg)
        return x*3
    return wrapper

def decorator2(fun):
    def wrapper(*arg):
        x = fun(*arg)
        return x*2
    return wrapper


@decorator1 
@decorator2
def myfun(a):
    return a


myfun(5)

##################################
def myfun(a):
    return a
myfun = decorator2(myfun)


#####################################################

# Scenario - performing checks and validations

def validate(fun):
    def wrapper(a,b):
        "i am a wrapper function"
        print(f"Dividing {a} by {b}")
        if b ==0:
            raise TypeError("can not divide by zero")
        return fun(a,b)
    return wrapper 


@validate
def divide(a,b):
    "I am a divide function used to divide a by b"
    return a/b

divide(4,0)
divide(4,6)


print(divide.__name__)
print(divide.__doc__)

#######################################
import functools

def validate(fun):
    @functools.wraps(fun)
    def wrapper(a,b):
        "i am a wrapper function"
        print(f"Dividing {a} by {b}")
        if b ==0:
            raise TypeError("can not divide by zero")
        return fun(a,b)
    return wrapper 


@validate
def divide(a,b):
    "I am a divide function used to divide a by b"
    return a/b

divide(4,0)
divide(4,6)

print(divide.__name__)
print(divide.__doc__)

########################################################

#############################################################

# Decorators using class

# modify = __call__ method

class mydecorator:
    def __init__(self,fun):
        self.fun = fun
        
    def __call__(self,*arg):
        out = self.fun(*arg)
        out = out.upper()
        return out

@mydecorator
def greet():
    return "hey hi"

greet()
