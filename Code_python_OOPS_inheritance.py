# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:27:51 2021

@author: anshu
"""

class employee:
    country = "India"
    age = 24
    
    def __init__(self,name):
        self.name = name
        print(f"Employee created with name {self.name}")
        
        
    def onboarding(self):
        print(f"onboarded successfully {self.name}")
        
        
class manager(employee):
    team_size = 2
    age = 52
    
    def __init__(self, name):
        # to access parent class member - super keyword
        super(manager, self).__init__(name)
        print("Age from child class ",self.age)
        print("age from parent class ",super(manager,self).age)
        print("accessing attributed inherited from parent ",self.country)
        
    
    def promote(self,newsalary):
        self.salary = newsalary
        print("Manager promoted with salary ",self.salary)
    
        
        
e1 = employee(name="Anshu")
e1.country
e1.onboarding()

m1 = manager(name="anshu")
m1.country
m1.name
m1.onboarding()
m1.promote(450000)
m1.age
e1.age

#################################
issubclass(manager, employee) # to check whether a class is a subclass of another one
issubclass(employee,manager)

isinstance(e1,employee)
isinstance(m1,employee)
isinstance(e1,manager)


############################################################
##########################################################


class employee:
    country = "India"
    age = 24
    x = 5
    _y = 6
    __z = 12
    
    def __init__(self,name):
        self.name = name
        print(f"Employee created with name {self.name}")
        
        
class manager(employee):
    team_size = 2
    age = 52
    
    def __init__(self, name):
        # to access parent class member - super keyword
        super(manager, self).__init__(name)
        print("Age from child class ",self.age)
        print("age from parent class ",super(manager,self).age)
        print("accessing attributed inherited from parent ",self.country)
    
    def trail(self):
        print(self.x)
        print(self._y)
        print(self.__z)
    
e1 = employee(name="Anshu")
e1.x
e1._y
e1.__z # will give error

m1 = manager(name="john")
m1.trail()

m1._y