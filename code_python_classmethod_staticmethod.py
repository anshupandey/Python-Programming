# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:41:38 2021

@author: anshu
"""

# Builtin decorators - classmethod, staticmethod


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def onboard(self):
        print(f"{self.name} you got succesfully onboarded")
        
    # creating a static method to validate age
    @staticmethod
    def validate_age(age):
        if age>0:
            return True
        else:
            False
            
            
e1 = employee(name="Anshu",age=25)
e1.name
e1.onboard()

employee.validate_age(23)
e1.validate_age(12)
employee.onboard()

################# class method
# - methods bound to class not the instance
# - they can access class attributes not the instance attributes

class employee:
    country = "India"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def onboard(self):
        print(f"{self.name} you got succesfully onboarded")
        
    # creating a class method
    
    @classmethod 
    def qualcomm(cls,name,city,age=12):
        print(f"Hey {name} your country is {cls.country}")
        print(f"your city is {city}")
        cls.country = "Nepal"
        return cls(name,age)
    
e1 = employee("anshu",12)
e1.country
e1.onboard()

e2 = employee.qualcomm("John", "Delhi")
e2

e3 = employee("jkhk",45)
e3.country = "UAE"

employee.qualcomm("aefee", "eg")

e4 = employee("Jack",12)
e4.country
