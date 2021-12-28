# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:36:55 2021

@author: anshu
"""

# Object oriented programming

class employee:
    # class arguments
    name = ""
    age = 25
    

# Object - an instance of the class
# create an object of type class employee
e1 = employee()
e1.name, e1.age  = "Anshu", 22

e2 = employee()
id(e1)
id(e2)
e2.name="Jonathan"; e2.age = 35
print(e2.name,e1.name)
###############################################

class employee:
    # class arguments
    name = ""
    age = 25
    
    def myfunction(self):
        print("hi from a method of class employee")
        
    def onboarding(self):
        print(f"Employee {self.name} got onboarded")
        print("Age is ",self.age)
        
    def get_salary(self,exp,multi):
        return exp*multi
        
e1 = employee()
e1.name = "Anshu"
e1.age = 25
e1.myfunction()

e1.onboarding()
e1.get_salary(10, 5000)

#######################################################



class employee:
    # class arguments
    age = 25
    city = ""
    
    def __init__(self,name):
        self.name = name
        print(f"Employee object created with name {self.name}")
            
    def onboarding(self):
        print(f"Employee {self.name} got onboarded")
        print("Age is ",self.age)
        
    def get_salary(self,exp,multi):
        return exp*multi

e1 = employee('Anshu')
e1.onboarding()

#####################################################
# Inheritance

class A:
    def __init__(self,name):
        print("I am class A")

class manager(A,employee):
    team_size = None
    def __init__(self,name):
        super().__init__(name)

m1 = manager("Anshu")
m1.age = 45
m1.city = "London"
m1.onboarding()
