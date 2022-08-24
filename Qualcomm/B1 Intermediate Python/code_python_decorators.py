# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:34:31 2022

@author: admin
"""

# A function can accept another function as input argument

def greet():
    print("Hey Good morning")
    

def day_schedule(fun):
    fun()
    print("Here is your day schedule")
    return None


day_schedule(greet)


# A function can be defined inside another function

def day_schedule(fun):
    fun()
    print("Here is your day schedule")
    
    def end_of_day():
        print("I hope your day was amazing")
        
    end_of_day()
    return None


day_schedule(greet)

# A function can return another function 


def day_schedule(fun):
    fun()
    print("Here is your day schedule")
    
    def end_of_day():
        print("I hope your day was amazing")
        return "hey hi"
        
    return end_of_day


eod = day_schedule(greet)
eod()


###############################################################


# a decorator will accept a function to be decorated
def mydecorator(fun):
    def modify():
        out = fun()
        out = out.upper()
        return out
    return modify 


# approach 1 to use decorator

def greet():
    return "hey good morning"

newgreet = mydecorator(greet)
newgreet()


# approach 2 to use decorator

@mydecorator
def greet():
    return "hey good morning"

greet()

###########################################################


def maindecorator(name):
    def mydecorator(fun):
        def modify():
            out = fun()
            out = "Hey "+name+" "+out
            return out
        return modify 
    return mydecorator 



@maindecorator("Anshu")
def greet():
    return "hey good morning"


greet()

#########################################################


class employee:
    def __init__(self,name):
        self.name = name
        print(f"An employee object created with name {self.name}")
    
    def __call__(self):
        print(f"This is an object of type employee for {self.name}")
        
e = employee("Jason")
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
    
            
@mydecor("Anshu") # mydecor("Anshu")(greet)
def greet():
    return "good morning"

greet()

################################################################


def decor1(fun):
    def wrapper(x):
        y = fun(x)
        return y**2
    return wrapper 

def decor2(fun):
    def wrapper(x):
        y = fun(x)
        return y*2
    return wrapper 
    

@decor1 
@decor2 
def myfun(a):
    return a+5


myfun(3)

# 3+5 = 8, decor2: 8*2 = 16, decor1: 16**2 = 256

#################################################################