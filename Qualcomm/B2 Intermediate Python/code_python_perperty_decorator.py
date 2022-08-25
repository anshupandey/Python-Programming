# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:22:15 2022

@author: admin
"""

class employee: 
    def __init__(self,name,age):
        self.age = age 
        self.name = name 
        print("Employee created")
        
    def onboarding():
        print("you are onboarded")
        
        
        
e = employee("anshu",55)

e.age = 45
e.age

m = 45

#####################################################################
#####################################################################


# property(fget, fset, fdel, doc)


class employee: 
    def __init__(self,name,age):
        self._age = age 
        self.name = name 
        print("Employee created")
        
    def onboarding():
        print("you are onboarded")
        
    def _get_age(self):
        print("value of age")
        return self._age
    
    def _set_age(self,value):
        if value >18:
            self._age = value 
        else:
            raise ValueError("age can not be negative")
        
    def _del_age(self):
        print("attribute deleted")
        del self._age
        
    # creating a property
    age = property(fget=_get_age, fset = _set_age, 
                   fdel = _del_age, doc="this is age property")
    
    
ee = employee('Anshu',45)

ee.age
ee.age = 42         
ee.age = 12    
del ee.age
###############################################################

class employee: 
    def __init__(self,name,age):
        self._age = age 
        self.name = name 
        print("Employee created")
        
    def onboarding():
        print("you are onboarded")
    
    @property
    def age(self):
        """
        this is doc for age
        """
        print("value of age")
        return self._age
    
    @age.setter 
    def age(self,value):
        if value >18:
            self._age = value 
        else:
            raise ValueError("age can not be negative")
        
    @age.deleter
    def age(self):
        print("attribute deleted")
        del self._age

kk = employee("Jaseo",36)
kk.age
kk.age = 21 
kk.age = 16 
del kk.age 


