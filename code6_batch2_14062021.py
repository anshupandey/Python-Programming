# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:08:38 2021

@author: Nitu
"""

class employee:
    name = ""
    salary = 10000
    eid = 110011007


print(employee)

e1 = employee()
e2 = employee()

e1
e2

print(e1.name,e1.salary,e1.eid)
print(e2.name,e2.salary,e2.eid)

e1.name = "anshu"
e1.salary = 5000
e2.name = "Vinay"
e2.salary = 500000

print(e1.name,e1.salary,e1.eid)
print(e2.name,e2.salary,e2.eid)

e1.eid = "gjtu78i8t"

#################################################################


class employee:
    name = ""
    salary = 10000
    eid = 110011007
    
    def joining(self):
        print("you have joined the company, comgratulations")
        print(self.name,self.eid)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal

e1 = employee()
# e1 is an object if class employee
# e1 can be also be called as an instance of the class employee
e1.name = "Anshu"
e1.salary
e1.joining()
e1.get_salary(23,1200)


###################################################################

class employee:
    """
    this class can be used to create objects of type employee
    with attributes like salary and eid
    """
    salary = 10000
    eid = 110011007
    
    def __init__(self,name):
        self.name = name
        print("Employee got created")
    
    def joining(self):
        """
        this function simply print the joining message

        Returns
        -------
        None.

        """
        print("you have joined the company, comgratulations")
        print(self.name,self.eid)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal

help(employee)
help(employee.joining)
e1 = employee("Anshu")

e1.name = "Anshu Pandey"

e2 = employee("Marco")
e2.joining()




############################################################
# inheritance
class employee:
    salary = 10000
    eid = 110011007
    
    def __init__(self,name):
        self.name = name
        print("Employee got created")
    
    def joining(self):
        print("you have joined the company, comgratulations")
        print(self.name,self.eid)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal


class manager(employee):
    desk_number = 123
    def __init__(self,name):
        self.name = name
        print("Manager got created")
        

e1 = employee("ANshu")

m = manager("Vinay")
print(m.salary,m.eid)
print(m.desk_number,m.name)

##########################################################
# Data Hiding
class employee:
    salary = 10000
    _eid = 110011007
    __address = "Mumbai"
    def __init__(self,name):
        self.name = name
        print("Employee got created")
    
    def joining(self):
        print("you have joined the company, comgratulations")
        print(self.name,self.eid)
        print(self.__address)
        
    def get_salary(self,days,perday):
        sal = days*perday
        return sal

class manager(employee):
    desk_number = 123
    def __init__(self,name):
        self.name = name
        print("Manager got created")
    
    def test(self):
        print(self.salary,self._eid,self.__address)

e1 = employee("Anshu")
e1.salary
e1._eid
e1.__address

m1 = manager("Anshu")
m1.salary
m1._eid
m1.test()
