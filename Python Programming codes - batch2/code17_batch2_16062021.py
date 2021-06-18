# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:46:10 2021

@author: Nitu
"""
## Decorators in python

# You can assign a function to a variable

def myfun(x):
    return x.upper()

myfun("hiiii")
k = myfun
k("hii")

# a function can be defined inside other function
def addhello(x):
    def myfun(x):
        return x.upper()
    op = myfun(x)
    return op + " hello"

addhello("hii")
## a function can be an input argument to another function

def myfun(x):
    return x.upper()

# here the function addhello is expecting another fun as input arg
def addhello(fun):
    x = "hii"
    op = fun(x)
    return op

addhello(myfun)

##################################################################
# Decorators in Python

def sample_decorator(fun):
    def wrapper():
        f = fun()
        f = f.upper()
        return f
    return wrapper

def greet():
    return "hello everyone"

# use decorator to modify capability of the greet function without modifying greet
decorate = sample_decorator(greet)
decorate()

# a better way to use decorator

@sample_decorator
def greet():
    return "hello everyone"


greet()
