# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:41:42 2021

@author: Nitu
"""

def myfun(x):
    return x.upper()

myfun("hii")
m = myfun
m("hi")
#################################################################
# defining a function inside other function
def addhello(x):
    def myfun(x):
        return x.upper()
    output = myfun(x)
    return output + " hello"

addhello("hii")
#################################################################
# passing a function as argument to other function

def myfun(x):
    return x.upper()

def addhello(fun):
    x = "hii"
    return fun(x)

addhello(myfun)

###################################################################
# decorators

def deco(fun):
    def wrapper():
        f = fun()
        f = f.upper()
        return f
    return wrapper


def greet():
    return "hello everyone"

decorate = deco(greet)
decorate()


###############################################################
@deco
def greet():
    return "hello everyone"

greet()
