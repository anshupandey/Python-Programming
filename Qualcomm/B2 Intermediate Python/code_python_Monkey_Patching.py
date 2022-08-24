# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:17:48 2022

@author: admin
"""

import qualcomm as qc 

w = qc.myclass()
w.snapdragon()
w.myfun(4,3) 

# =============================================================================
# Monkey Patching
#     - Dynamically modifying behaviour of code 
#     - class / module 
# =============================================================================

def monkey(self):
    print("hey hello good morning")
    
    
qc.myclass.snapdragon = monkey 

m = qc.myclass()
m.snapdragon()


def urfun(self,a,b,c):
    return a+b+c 

qc.myclass.myfun = urfun 

k = qc.myclass()
k.myfun(7,5,3)

#######################################################

m.age = 45 
m.salary = 12

print(m.age, m.salary)


m.abc = monkey 

m.abc(m) 

def monkey2():
    print("hey hello good morning")

m.anshu = monkey2 
m.anshu() 

