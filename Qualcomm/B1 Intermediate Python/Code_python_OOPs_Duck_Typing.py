# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:02:28 2022

@author: admin
"""

# =============================================================================
# Dock Typing
#     - related to dynamic typing in programming 
#     - Type of the object is less important than that of methods it has
# =============================================================================


x = 5
x + 3
type(x)
x + "Hi"

x + 3
# is equivalent to 
x.__add__(3)

m = [4,2,5,8,3]
len(m)
m.__len__()

#################################

class employee:
    age = 45 
    Nationality = "Indian"
    
    def __init__(self,name):
        self.name = name 
        
    def __str__(self):
        return self.name 
    
    def __len__(self):
        return self.age
    
    def __add__(self,value):
        return self.age + float(value)
    
    def __sub__(self,value):
        return self.age + float(value)
    
    def __mul__(self,value):
        return self.age * float(value)
    
    def __truediv__(self,value):
        return self.age/float(value)
    
    def __pow__(self,value):
        return self.age ** float(value)
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return True 
    
    def __or__(self,value):
        return True or value

e = employee("Anshu")    

e+5 
e-6 
e*3
e/2
str(e) 
len(e) 
int(e)
bool(e)
e**3  
e|True 



##############################################################


class employee:
    age = 45 
    Nationality = "Indian"
    
    def __init__(self,name):
        self.name = name 
        
    def __lt__(self,value):
        return self.age<value
    
    def __gt__(self,value):
        return self.age>value
    
    def __le__(self,value):
        return self.age<=value
    
    def __ge__(self,value):
        return self.age>=value
    
    def __eq__(self,value):
        return self.age==value
    
    def __ne__(self,value):
        return self.age!=value
    
    def __getitem__(self,index):
        return self.name[index]



e = employee('James Carter')
e[0]
e[1]
e[2]

e.age
e<=45
e>25
e==12
e!=40
################################################

5+6
"hi " + "Bye"
