# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:09:00 2022

@author: admin
"""

class employee:
    country = "India" # class attribute
    salary = 15000 
    
    def __init__(self,name):
        self.name = name # instance attribute
        print("employee class created")
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)
        

class manager(employee):
    team_size = 2 
    
    def __init__(self,name):
        self.name = name
        print(f"A manager with name {self.name} created")
        
    def get_details(self):
        print("name : ",self.name)
        print("Salary : ",self.salary)
        print("Team Size : ",self.team_size)
        

m = manager("Jason")
m.get_details()
m.team_size
m.country

#####################################################################

class manager(employee):
    team_size = 2 
    
    def __init__(self,name):
        employee.__init__(self,name)
        print(f"A manager created with name {self.name}")
        
    def get_details(self):
        print("name : ",self.name)
        print("Salary : ",self.salary)
        print("Team Size : ",self.team_size)
        
m = manager("Jason")
m.get_details()

####################################################################


class manager(employee):
    team_size = 2 
    
    def __init__(self,name):
        super(manager,self).__init__(name)
        print(f"A manager created with name {self.name}")
        
    def get_details(self):
        print("name : ",self.name)
        print("Salary : ",self.salary)
        print("Team Size : ",self.team_size)
        
m = manager("Jason")
m.get_details()

####################################################################
#####################################################################
e = employee("Anshu")

issubclass(employee, manager)
issubclass(manager, employee)

isinstance(e, employee)
isinstance(m, employee)
isinstance(e, manager)
isinstance(m, manager)

#####################################################################

class A:
    x = 45 # public access
    _w = 25 # protected
    __z = 12 # private to class A
    
    def __greet(self):
        print("Hey Good Morning")
    
    def fun(self):
        self.__greet()
        print(self.x,self._w,self.__z)
        

class B(A):
    p = 12 
    __d = 45 # private to class B
    
    def getdata(self):
        print(self.x,self._w)
        
    def getpvt(self):
        print(self.__z)
    
m = A()
m._w
m.x        
m.__z        
m.__greet()    
m.fun()

n = B()
n.getdata()
n.getpvt()
m.













