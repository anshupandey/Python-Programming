# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:10:12 2022

@author: admin
"""

# staticmethod and class method

# =============================================================================
# Staticmethod 
#     - no idea about class/instance, 
#     - can not access class attributes 
#     - does not accpet self argument, 
#     - accessible by the isntance 
#     
# =============================================================================
    

class employee: 

    age = 45
    def __init__(self,name):
        self.name = name
        
    @staticmethod 
    def validate_age(age):
        if age>18:
            return "Valid"
        else:
            return "Invalid"
        
e = employee("Anshu")        
e.validate_age(78)

##############################################

# =============================================================================
# Classmethod:
#     - bound to class, but not to instance 
#     can be used to create object with different approach 
#     
# =============================================================================


class employee: 

    age = 45
    def __init__(self,name):
        self.name = name
        
    @classmethod 
    def ex_employee(cls,name,city):
        print("employee created with name ",name)
        cls.city = city
        cls.country = "Nepal"
        return cls(name)

e1 = employee("John")
e1.age 

e2 = employee.ex_employee("Anshu", "Delhi")
# employee("Anshu") 
e2.country
e2.city 
