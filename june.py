# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:44:28 2021

@author: Nitu
this module is a generic module
"""

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
        
        
def myfun(a,b):
    return a+b