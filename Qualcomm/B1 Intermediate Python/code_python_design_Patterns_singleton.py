# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:19:36 2022

@author: admin
"""

# =============================================================================
# Singleton
#     - a way to fix that only one object can be created from a class
#     
# =============================================================================


class myclass:
    __ins = "jacob"
    
    def __init__(self):
        if myclass.__ins=="jacob":
            myclass.__ins = self
        else:
            raise Exception("This is a singleton class")
            
    @staticmethod 
    def get_instance():
        if myclass.__ins=="jacob":
            myclass()
        return myclass.__ins
        


k = myclass()        
type(k)

m = myclass()

id(k)


w = k.get_instance()
id(w)
