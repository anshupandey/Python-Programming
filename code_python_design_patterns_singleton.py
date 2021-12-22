# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:37:43 2021

@author: anshu
"""


# =============================================================================
# Singleton - used to restrict number of objects which can be created from a class to 1
# -used to fix that only one object can be created from the class
# 
# =============================================================================


class mysingleton:
    __myinstance = "anshu"
    
    def __init__(self):
        if mysingleton.__myinstance== "anshu":
            mysingleton.__myinstance = self
        else:
            raise Exception(" this class is a singleton class")
            
    
    @staticmethod
    def getInstance():
        if mysingleton.__myinstance=='anshu':
            # this will happen when no objects are instantiated
            mysingleton()
        return mysingleton.__myinstance
    
    
k = mysingleton()
id(k)
m = mysingleton() # this will throw error

w = mysingleton.getInstance()
id(w)
