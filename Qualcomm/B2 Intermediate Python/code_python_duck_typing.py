# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:37:09 2022

@author: admin
"""


# =============================================================================
# Duck Typing
#     - related to dynamic typing in programming langauges 
#     - type of an object is less important than the methods defined in it 
#     
# =============================================================================

x = 5
type(x)

x + 5 

x + "hii "

x + 6 
x.__add__(6)

x*3
x.__mul__(3)

x**3 
x.__pow__(3) 

x<6
x.__lt__(6)

m = [4,5,3]
len(m)

m.__len__()

# indexing
m[1]
m.__getitem__(1)

#######################################################

class employee:
    nationality = "Indian"
    age = 40 
    
    def __init__(self,name):
        self.name = name
        
    def __add__(self,val):
        return self.age + val
    
    def __sub__(self,val):
        return self.age - val
    
    def __mul__(self,val):
        return self.age * val
    
    def __truediv__(self,val):
        return self.age / val
    
    def __pow__(self,val):
        return self.age ** val
    
    def __lt__(self,val):
        return self.age < val
    
    def __gt__(self,val):
        return self.age > val
    
    def __le__(self,val):
        return self.age <= val
    
    def __ge__(self,val):
        return self.age >= val
    
    def __eq__(self,val):
        return self.age == val
    
    def __ne__(self,val):
        return self.age != val
    

e = employee("Anshu")

e+5
e-12
e*5 
e/12 
e**2 
e<12 
e>45 
e<=23 
e>=45 
e==55 
e!=12 



class employee:
    nationality = "Indian"
    age = 40 
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.age
    
    def __type__(self):
        return self.nationality 
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self,index):
        return self.name[index]
    
    def __repr__(self):
        return self.name

e = employee("James Carter")

type(e)

print(e)

str(e)
int(e)
len(e)
e[0]
e[1]
