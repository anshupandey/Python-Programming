# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:49:14 2021

@author: Nitu

"""


def myfun(a,b):
    c = a+b
    return c


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
        print(self.eid,self._salary)
    def get_salary(self, days, perday):
        sal = days*perday + 100000
        return sal
    
 