# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:03:13 2021

@author: anshu
"""

# python Modules and packages


# =============================================================================
# Package
# # =============================================================================
# #         Module - a .py file   
# #         # ================================================================
# #         #      Class
# #         #       # ========================================================
# #         #       #     Attributes (variables) & functions (methods)
# #         #       # ========================================================
# #         #       functions and variables
# #         # ================================================================
# # 
# # =============================================================================
# 
# =============================================================================


import november

november.myfun(5, 6)

k = november.A()

k.func1(4,5,8,7,52,3)

k.func2()

k.x

###################################

import november as nv
nv.myfun(4,3)

#####################################################################

import mypack

from mypack import nove
from mypack import oct

mypack.nove.myfun(7, 6)
mypack.oct.octfun(8, 9)

##############################################################################



import math

math.sqrt(625)
math.cos(0)
math.log10(50000)
math.pow(8, 3)


import time

time.ctime()

# adding delays in the code
print("hey hii")
time.sleep(5)
print("Bye")

import os

os.getcwd() # to get the current working directory
os.chdir('D:\\python\\xceed') # set the current working directory

# get the list of files in a folder

files = os.listdir('D:\\python\\xceed')
for file in files:print(file)

# os.path
# to get the basename of a file
out = os.path.basename(r"D:\python\xceed\code_Python_Object_oriented_programming.py")
out

# to get the directory name
out = os.path.dirname(r"D:\python\xceed\code_Python_Object_oriented_programming.py")
out


# check whether the path exists or not
os.path.isdir(r"D:\python\xceed")

import sys

sys.path

# add any directory to system path

sys.path.append(r"D:\python\xceed")

sys.getwindowsversion()

################################################################

print("Hi \new world")
print("Hi \\new world")
print(r"Hi \new world")
