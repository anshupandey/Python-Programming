# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:13:32 2022

@author: admin
"""

# =============================================================================
# Monkey Patching: dynamically modifying behaviour of the object/module 
# 
# =============================================================================

import qualcomm as qc 

w = qc.myclass()

w.snapdragon()
w.myfun(5, 6)




def monkey(self):
    print("I am a monkey function and can be integrated to modify")
    
    
qc.myclass.snapdragon = monkey 

m = qc.myclass()

m.snapdragon()


############################

def urfun(self,a,b,c):
    return a+b+c

qc.myclass.myfun = urfun 

z = qc.myclass() 
z.myfun(4,5,3)

#############################################################

qc.myclass.abc = urfun

s = qc.myclass() 
s.abc(7,5,3)

s.age = 45 
s.salary = 445222 

