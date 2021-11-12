# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:43:53 2021

@author: anshu
"""

# Decorators

# in python functions are first class objects
# =============================================================================
# Functions
#     - instance of an object type
#     - we can store a function in a variable
#     - we can pass a function as input to other function
#     - we can have nested functions
#     - a function can return another function as op
#     
# =============================================================================
m = "hello from python"
m.upper()

def myfun(data):
    return data.upper()

myfun("hey hi")

# a fuction can be stored in a variable
x = myfun
x('hey hi')
############################################
def getupper(data):
    data = data + "Bye!!"
    return data.upper()
def getlower(data):
    return data.lower()

def sayhello(fun):
    x = "Hey Hello, how are you today"
    x = x + " | now next "
    op = fun(x)
    return op

sayhello(getupper)
sayhello(getlower)

##############################################
# a function can be defined inside another fun,
# a function can return another function

def create_greetings(a):
    def make_upper(b):
        c = a + " " + b
        return c.upper()
    return make_upper

# first call to the parent function
# it return another function
op = create_greetings("hi")
# op is now equivalent to make_upper
# again calling output of parent function
op("hello")
###############################################

# =============================================================================
# Decorators
#      - used to modify behaviour of any class or fun
# =============================================================================


def mydecorator(fun):
    # fun is a function which is to be decorated
    # now we will write a wrapper function
    def innerfun():
        # this function is modifying the output of
        # any other function passed to
        # myedecorator
        op = fun()
        return op.upper()
    return innerfun


def greet():
    return "Hey Good Morning"

greet()

@mydecorator
def greet():
    return "Hey Good morning"

greet()


######################################
def greet():
    return "Hey Good Morning"

greet2 = mydecorator(greet)

greet()
greet2()
#######################################

def decoratorfun(newfun):
    # - some operation
    def wrapperfun(arg):
        # some operations  - 
        op = newfun()
        # some modifications on op
        return op
    return wrapperfun

