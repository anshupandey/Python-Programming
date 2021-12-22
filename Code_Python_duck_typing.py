# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:42:14 2021

@author: anshu
"""

# =============================================================================
# # Duck Typing
# 
#  - related to dynamic typing in programming languages
#  - type of the object is less important than that of the methods it has
#  
# =============================================================================

x = 5
x + 3

type(x)
x.__add__(3)

m = [4,5,3]
len(m)

len(x)

m.__len__()


class employee:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __len__(self):
        return self.age
        

e1 = employee("Anshu",25)
str(e1)  # it executes e1.__str__()
len(e1) # it executes e1.__len__()

#############################################


class A:
    country = "India"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __add__(self,value):
        return self.age + value
    
    def __sub__(self,value):
        return self.age - value
    
    def __mul__(self,value):
        return self.age*value
    
    def __truediv__(self,value):
        return self.age/value
    
    def __pow__(self,value):
        return self.age**value
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return True
    
    def __or__(self,value):
        return True or value
    
    
k = A("Anshu",20)    

k + 5
k - 5
k*2
k/10
int(k)
bool(k)
k**2

#######################################################

m = 456355
m + 2
m.__add__(45)

len(m) # this will throw error
m[0] # this will throw error


class mint(int):
    
    def __len__(self):
        return len(self.__str__())
    
    def __getitem__(self,index):
        return int(self.__str__()[index])
    
    
k = mint(456135)
type(k)
print(k)
k + 5
k - 2
k*3

len(k)
# indexing
k[0]
k[2]
