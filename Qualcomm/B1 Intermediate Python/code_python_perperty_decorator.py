# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:34:34 2022

@author: admin
"""

class employee:
    age = 28 
    def __init__(self,name):
        self.name = name
        print("Employee created with name ",name)
        
e1 = employee("Anshu")  
e1.age     
e1.age = 45 
e1.age
#######################################################

# property
# property(fget,fset,fdel,doc) 

class employee:
    def __init__(self,name,age):
        self.name = name
        print("Employee created with name ",name)
        self._age = age
        
    def _get_age(self):
        print("getting the value for age ")
        return self._age 
    
    def _set_age(self,value):
        if value > 18:
            self._age = value 
        else:
            raise ValueError("Age can not be less than 18 ")
            
    def _del_age(self):
        print("deleted age")
        del self._age 
        
    age = property(fget=_get_age, fset=_set_age, 
                   fdel = _del_age, doc="this is age of employee")
    
                   
        
e = employee("Anshu",25)    

e.age        

e.age = 45        
e.age = 12     

del e.age 

e.age 

e.age.__doc__
e.age
############################################################
############################################################


class employee:
    def __init__(self,name,age):
        self.name = name
        print("Employee created with name ",name)
        self._age = age
        
    @property    
    def age(self):
        """
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        print("getting the value for age ")
        return self._age 
    
    @age.setter
    def age(self,value):
        if value > 18:
            self._age = value 
        else:
            raise ValueError("Age can not be less than 18 ")
            
    @age.deleter
    def age(self):
        print("deleted age")
        del self._age 
        
e = employee("james",22)
e.age 
e.age = 12 
e.age = 45 

del e.age 
help(e)
