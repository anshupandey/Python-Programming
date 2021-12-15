# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:45:51 2021

@author: anshu

create a file - qualcomm.py in the same directory


class myclass:
    def snapdragon():
        print("i am a method of the class my class from the module qualcomm")
        
    def myfun(a,b):
        return a + b

"""


# =============================================================================
# Monkey Patching - dynamically modifying the behaviour of the code
# - applied on class/modules
# 
# 
# =============================================================================

import sys
sys.path.append("D:\python\DEC2021\Qualcomm_intermediate_b1")


import qualcomm as qc

k = qc.myclass()
k.myfun(4,5)

k.snapdragon()


def monkey(self):
    print("this is a monkey function which does something")

# monkey patching - modifying the default behaviour of the class
qc.myclass.snapdragon = monkey 

h = qc.myclass()
h.snapdragon()

################################################

def myfun3(self,a,b,c):
    return a + b+ c

qc.myclass.newfun = myfun3 

w = qc.myclass()
w.snapdragon()
w.newfun(4,2,3)
