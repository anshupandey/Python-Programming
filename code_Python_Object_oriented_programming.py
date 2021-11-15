# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:05:57 2021

@author: anshu
"""

# Object oriented programming
# =============================================================================
# class
#     - template of an object
#     - can be created using class keyword
#     - can accommodate another class, functions, attributes
#     
# =============================================================================
    

class employee:
    name = ""
    age = 25
    salary = 1000
    
    
e1 = employee()
e2 = employee()

e1.age = 45
e1.name = "Anshu"; e1.salary = 50000
e2.name, e2.age, e2.salary = "Abhi",36,40000

print(e1.name,e1.age,e2.salary)


#####################################################

# government exam - UPSC

# name, age, salary, city, address = attributes of an applicant
# can be created using variables

# processes = filling application, updating application, confirming - 
# - functions and methods

# form - template which everyone will follow where they can add
# attributes and perform processes
# form - class

################################################################

# how to add methods to the class
# - function inside a class is called as a method
class employee:
    name = ''
    age = 25
    salary = 20000
    
    def onboarding():
        print("Employee onboarded successfully")

e1 = employee()        

e1.name = "Anshu"
e1.age = 45
print(e1.name, e1.age)        
# e1 is an object of type class employee
# e1 is an instance of the class employee

e1.onboarding() # this will throw error
# whenever you call a method of the class with refrence to the
# object of type that class.
# the object(instance of class) always passes reference of the
# class as an input argument to the method
        
    
class employee:
    name = ''
    age = 25
    salary = 20000
    
    def onboarding(self):
        print("Employee onboarded successfully")
        print(self.name, "got onboarded successfully")
        print(self.myfun(7,8))
        
    def myfun(self,a,b):
        c = a + b
        return c

e1 = employee()        

e1.name = "Anshu"
e1.age = 45
print(e1.name, e1.age)        
e1.onboarding()

e1.myfun(4,5)

#################################################################

# Constructors - default method of the class
# - primarily used to instantiate an object


class employee:
    # creating a class variable
    salary = 50000
    # defining the constructor method
    def __init__(self,name):
        # create an instance variable
        self.name= name
        self.age = 25
        print("Employee creation started...")
        
    def onboarding(self):
        print(self.name, "got onboarded successfully")
        
    # defining a destructor
    def __del__(self):
        print("the object deleted, destructor called")
        


e1 = employee("Anshu")
e1.onboarding()
e1.name
e2 = employee("Adam")

del e2
########################################################
## Inheritance


class A:
    x = 5
    y = 6
    def myfun(self):
        print(self.x + self.y)
        print(" i am a method of classs A")
        
    def myfun2(self,a,b):
        return a + b
    
m = A()
m.x    
m.y
m.myfun()

class B(A):
    z = 12
    y = 10
    
    def myfun3(self,a,*b):
        A.myfun(self)
        return a + sum(b)
    
    
n = B()
n.x
n.z
n.y
n.myfun()
n.myfun3(5,7,8,3,5)

