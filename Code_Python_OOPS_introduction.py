# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:38:50 2021

@author: anshu
"""

# Basics of Object oriented programming

# a class is a blueprint of an object
class employee:
    name = ""
    salary = 45000
    
    
# creating an object of type class
# creating an instance of class

e1 = employee()
e1.name, e1.salary = "anshu",20000
e2 = employee()
e2.name,e2.salary = "John", 60000

print(e1.name)
print(e2.name,e2.salary)
################################################################


class employee:
    name = ""
    salary = 45000
    
    def onboarding():
        print("Hello, you are successfully onboarded")
        
e1 = employee()
e1.name = "Anshu"
print(e1.name,e1.salary)

e1.onboarding()

###################

class employee:
    name = ""
    salary = 45000
    
    def onboarding(self):
        print("Hello, you are successfully onboarded")
        print(f"your name is {self.name} and salary is {self.salary}")
        
    def promote(self,newsalary):
        self.salary = newsalary
        print("you are promoted with new salary ",self.salary)
        
e1 = employee()
e1.name = "Anshu"
print(e1.name,e1.salary)

e1.onboarding()

e1.promote(12000)


####################################################



class employee:
    # class attributes
    country = "India"
    salary = 45000
    
    def __init__(self,name,age):
        # instance attribute
        self.name = name
        print("an object of type class employee created")
    
    def onboarding(self):
        self.x = 5
        print(self.x)
        print("Hello, you are successfully onboarded")
        print(f"your name is {self.name} and salary is {self.salary}")
        
    def promote(self,newsalary):
        print(self.x)
        print(self.salary)
        salary = 12
        print(salary,self.salary)
        self.salary = newsalary
        print("you are promoted with new salary ",self.salary)

e1 = employee(name="Anshu",age=45)

print(e1.country,e1.name)

e1.onboarding()

e1.promote(60000)

#########################################################

class employee:
    country = "India"
    salary = 45000
    
    def __init__(self,name):
        self.name = name
        print("object created")
        print(f"Employee name {self.name}")
    
    def onboarding(self):
        print("Hello, you are successfully onboarded")
        print(f"your name is {self.name} and salary is {self.salary}")
        
    def promote(self,newsalary):
        self.salary = newsalary
        print("you are promoted with new salary ",self.salary)
        
e1 = employee(name="Anshu")

e1.promote(450000)
# builtin fucntions in python for custom objects

# hasattr - to check if an attribute exists or not
hasattr(e1, 'name')
hasattr(e1, 'age')

# getattr - to access the attribute of an object
getattr(e1, 'name')
getattr(e1, 'country')

# setattr - to set the value of an attribute
# if in case the attrubute does nt exist, it will get created
setattr(e1, 'name', "John")
setattr(e1, "age", 45)
hasattr(e1, 'age')

# delattr = used to delete an attribute
delattr(e1, 'name')
hasattr(e1, 'name')

##################################################################
##################################################################

class employee:
    """ This class is used to create an object of type employee
    while creating the object the input argument - name of employee has to be passed.
    
    >>> e1 = employee(name="john")
    object created
    Employee name john
    """
    country = "India"
    salary = 45000
    
    def __init__(self,name):
        self.name = name
        print("object created")
        print(f"Employee name {self.name}")
    
    def onboarding(self):
        print("Hello, you are successfully onboarded")
        print(f"your name is {self.name} and salary is {self.salary}")
        
    def promote(self,newsalary):
        self.salary = newsalary
        print("you are promoted with new salary ",self.salary)


e1 = employee(name="ANshu")

print(e1.__doc__) # accessing documentation string

employee.__name__ # to access name of class
employee.__module__ # name of .py file in which class is written
employee.__dict__

print(employee)
print(e1)

##########################################################

class employee:
    """ This class is used to create an object of type employee
    while creating the object the input argument - name of employee has to be passed.
    
    >>> e1 = employee(name="john")
    object created
    Employee name john
    """
    country = "India"
    salary = 45000
    
    def __init__(self,name):
        self.name = name
        print("object created")
        print(f"Employee name {self.name}")
    
    def onboarding(self):
        print("Hello, you are successfully onboarded")
        print(f"your name is {self.name} and salary is {self.salary}")
        
    def promote(self,newsalary):
        self.salary = newsalary
        print("you are promoted with new salary ",self.salary)
        
    def __str__(self):
        return f"this is an object of class employee for {self.name}"
    
    def __del__(self):
        "this is the destructor method"
        print(f"the object is deleted for employee {self.name}")


e1 = employee(name='Anshu')
print(e1)


del e1
