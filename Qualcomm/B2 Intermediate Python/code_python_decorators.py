# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:39:49 2022

@author: admin
"""

# A function can accept another function as input argument

def greet():
    return "Hey hi good morning"

def dayplan(fun):
    print(fun())
    return "Thank you"

dayplan(greet)


# A function can be defined inside another function in python

def dayplan():
    
    def greet():
        print("hhey good morning")
    
    greet()
    return None

dayplan()

# A function can return another function

def dayplan():  
    def greet():
        print("hhey good morning")

    return greet 

out = dayplan()
out()

###########################################################


def mydecorator(fun):
    def wrapper():
        out = fun()
        out = out.upper()
        return out 
    return wrapper 


def greet():
    return "hey good morning"

# approch 1 to use decorator method

fun2 = mydecorator(greet)

fun2() 

# approach 2 to use decorator

@mydecorator 
def greet():
    return "hey good morning"


greet()


#######################################################



def maindecorator(name):    
    def psuedo_decorator(fun):
        def wrapper():
            out = fun()
            out = "Hey "+name+" "+out
            return out 
        return wrapper 
    return psuedo_decorator


@maindecorator("Anshu")
def greet():
    return "good morning"

# the above code is equivalent to 
# greet = maindecorator("Anshu")(greet) = psuedodecorator(greet)

greet()

######################################################

def maindecorator(name):    
    def psuedo_decorator(fun):
        def wrapper(**arg):
            out = fun(arg)
            out = "Hey "+name+" "+out
            if 'city' in arg.keys():
                print("you are from ",arg['city'])
            return out 
        return wrapper 
    return psuedo_decorator


@maindecorator("Anshu")
def greet(a):
    return "good morning"


greet()

@maindecorator("Anshu")
def greet(a,**arg):
    return "good morning"

greet(city='Delhi',country="india")

###############################################################


# Chaining decorators

def decor1(fun):
    def wrapper(a):
        k = fun(a)
        return k**2
    return wrapper 


def decor2(fun):
    def wrapper(a):
        k = fun(a)
        return k*2
    return wrapper 

    
# decor1(decor2(myfun(5)))

@decor1 
@decor2 
def myfun(x):
    return x+3 

myfun(5)

# myfun: 5+3 = 8 => decor2: 8*2 = 16, => decor1: 16**2 = 256

#############################################################
#############################################################


class employee:
    def __init__(self,name):
        self.name = name 
        print("an employee created with name ",self.name)
        
    def __call__(self):
        print("This is an employee object with name ",self.name)
        
e = employee("John")

e()

################################################################

class mydecor:
    def __init__(self,name):
        self.name = name
        
    def __call__(self,fun):
        def wrapper():
            out = fun()
            out = "Hey "+self.name+" "+out
            return out 
        return wrapper
    

@mydecor("Anshu")
def greet():
    return "Good Morning"

greet()
# mydecor("Anshu")(greet)    



###################################################



def decor2(fun):
    print("decor2 is called")
    def wrapper(a):
        k = fun(a)
        return k*2
    return wrapper 


def myfun(x):
    return x+3 

newfun = decor2(myfun)

newfun(6)
    
# decor1(decor2(myfun(5)))

@decor2 
def myfun(x):
    return x+3 

#myfun(5)

dir(decor2)

dir(myfun)

help(decor2)


