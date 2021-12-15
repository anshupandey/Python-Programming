# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:39:32 2021

@author: anshu
"""

# Duck Typing in python

# relates to Dynamic typing OR dynamic programming
# type of an object has less significance than the methods it has
# type of an object is less improtant than what the object
# can be used for

x = [4,5,3]
len(x)

y = "hello"
len(y)

x.__len__()

m = 5
len(m)

class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name
    
    def __len__(self):
        return self.age
    
    def __add__(self,value):
        return self.age + value
    
e1 = employee("Anshu",25)

str(e1) # this will call __str__()
len(e1) # will trigger e1.__len__()

e1 + 5 # will call e1.__add__(5)

########################################################

class A:
    country = "India" # class attribute
    def __init__(self,name,age,city):
        self.name = name # instance attribute
        self.age = age
        self.city = city
    def __add__(self,value):
        return self.age + value
    
    def __sub__(self,value):
        return self.age - value
    
    def __mul__(self,value):
        return self.age * value
    
    def __truediv__(self,value):
        return self.age/value
    
    def __pow__(self,value):
        return self.age**value
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return True
    
    def __or__(self):
        return True

k = A("anshu",20,"delhi")

k +5
k *2
k-2
k/2
int(k)
bool(k)
k**2

((k+5)*2)/5
###############################################################

m = 45613
len(m) # this will throw error
m[1] # this will also throw error - indexing cant be done


class mint(int):
    
    def __len__(self):
        return len(m.__str__())
    
    def __getitem__(self,index):
        return int(m.__str__()[index])
    
    
k = mint(45612)
print(k)
type(k)
len(k)
k + 5
k[0]
k[2]
