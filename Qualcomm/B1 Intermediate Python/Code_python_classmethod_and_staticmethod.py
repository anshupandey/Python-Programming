# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:49:24 2022

@author: admin
"""

# =============================================================================
# static method
#     - methods not bound to class / instance 
#     - cannot access either class attributes or instance attributes 
#     - can used to implement functionalities for aggregation/validations 
# =============================================================================


class employee:
    salary = 45000
    
    def __init__(self,name):
        self.name = name 
        
    # creating a staticmethod 
    
    @staticmethod 
    def validate_age(age):
        if age>18:
            return "valid"
        else:
            return "invalid"
        

e = employee("Jessy")
e.validate_age(45)    

def monkey():
    return "hi"

e.validate_age = monkey     
e.validate_age()

##########################################################

# =============================================================================
# class method
#     - methods bound to class only, not instance 
#     - they are used to create different ways to instantiate the object 
# 
# =============================================================================



class employee:
    age = 25
    def __init__(self,name):
        self.name = name 
        self.city = "Delhi"
        print("An employee created")
        
        
    def onboarding(self):
        print('welcome to the team')
        
        
    @classmethod 
    def manager(cls,name,team_size,unit):
        cls.team_size=team_size 
        cls.bunit = unit 
        cls.orig = True
        print("Employee Type : Manager")
        return cls(name) # employee(name)
    

        
    
    
e = employee("Anshu")    

e.age 

hasattr(e,"orig")
getattr(e,"orig")


m = employee.manager("John",24,"Sales")
type(m)
m.age

dir(m)
hasattr(m,"orig")

hasattr(e,"orig")
dir(e)

