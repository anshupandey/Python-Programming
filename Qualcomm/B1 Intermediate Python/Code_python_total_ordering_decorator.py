# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:42:15 2022

@author: admin
"""

from functools import total_ordering 

@total_ordering
class employee:
    age = 45
    
    def __eq__(self,value):
        return self.age==value
    
    def __lt__(self,value):
        return self.age<value
    
    

e = employee()
e<25    
e==45 
e!=25 
e>90 
e<=12 
e>=13 

e.__name__ 

import qualcomm as qc

 
qc.__name__ 


