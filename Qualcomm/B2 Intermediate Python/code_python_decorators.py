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
