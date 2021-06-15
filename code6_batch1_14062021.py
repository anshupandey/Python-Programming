# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:43:28 2021

@author: Nitu
"""

# Object oriented programming

class employee:
    name = ""
    eid = 0
    Salary = 100000
    
    
e1 = employee()
# e1 is an object of type class employee
# e1 is an instance of the class employee

print(employee)
print(e1)
e2 = employee()
print(e2)

print(e1.name,e1.Salary,e1.eid)
print(e2.name,e2.Salary,e2.eid)

e1.name="Anshu"
e1.eid = 1100110077
e1.salary = 10000

e2.name="Ram"
e2.eid = 1100110055
e2.salary = 500000

print(e1.name,e1.Salary,e1.eid,e1.salary)
print(e2.name,e2.Salary,e2.eid,e2.salary)



############################################################

class employee:
    name = ""
    eid = 0
    Salary = 100000
    
    def joining(self):
        print("Congratulations, you have joined the company")
        self.name = "Anshu"
        print(self.name,self.eid,self.Salary)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal

        

e1 = employee()
e1.name
e1.Salary
e1.eid
e1.joining()
e1.get_salary(20, 1000)


class employee:
    """
    this class can be used to create objects of class employee
    it has methods such as joining and get_salary
    you need to pass name of employee while creating the class as argument
    """
    def __init__(self,name):
        self.eid = 100
        self.salary = 200000
        self.name = name
        print("Employee got created!")
        
    def joining(self):
        print("Congratulations, you have joined the company")
        print(self.name)
        print(self.name,self.eid,self.salary)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal
    
e1 = employee("Anshu")
help(employee)

e1.joining()


# Inheritance
class employee:
    """
    this class can be used to create objects of class employee
    it has methods such as joining and get_salary
    you need to pass name of employee while creating the class as argument
    """
    eid = 1233
    salary = 200000
    def __init__(self,name):
        self.name = name
        print("Employee got created!")
        
    def joining(self):
        print("Congratulations, you have joined the company")
        print(self.name)
        print(self.name,self.eid,self.salary)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal

class manager(employee):
    def __init__(self,name):
        self.name = name
        print("Manager got created")
        
    def get_salary(self, days, perday):
        sal = days*perday + 100000
        return sal
    
m = manager("Anshu")
m.eid
m.salary
m.joining()
m.get_salary(20, 5000)

# Data hiding

class employee:
    """
    this class can be used to create objects of class employee
    it has methods such as joining and get_salary
    you need to pass name of employee while creating the class as argument
    """
    eid = 1233
    _salary = 200000
    __address = "Delhi"
    def __init__(self,name):
        self.name = name
        print("Employee got created!")
        
    def joining(self):
        print("Congratulations, you have joined the company")
        print(self.name)
        print(self.name,self.eid,self._salary)
        print(self.__address)
        

class manager(employee):
    def __init__(self,name):
        self.name = name
        print("Manager got created")
        print(self.eid,self._salary,self.__address)
    def get_salary(self, days, perday):
        sal = days*perday + 100000
        return sal
    
e1 = employee("anshu")
e1.eid
e1._salary
e1.__address
e1.joining()

m = manager("john")
