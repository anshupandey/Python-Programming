# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:41:51 2021

@author: Nitu
"""

import june

june.myfun(3,4)

e1 = june.employee("Anshu")
m1 = june.manager("Max")

import june as jn

jn.myfun(4,8)
e = jn.employee("Cherry")

jn.__doc__
jn.__file__
jn.__name__
jn.__package__




'''
folder: urpackage
    file: __init__.py
    folder: mymath
        file: __init__.py
        urmath.py
        
    folder: myutility
        file: __init__.py
        june.py
'''


from urpackage.mymath import urmath
urmath.addtwo(4, 4)

urmath.multtwo(6, 2)

######################################

from urpackage.myutility import june
june.myfun(3, 8)


import urpackage

urpackage.mymath.urmath.addtwo(3, 4)

######################################################
######################################################

import os
import pandas as pd
# =============================================================================
# random = for random number generation and calculations
# os = all operating system related processes
# sys = system related operations
# time, datetime = date and time operations
# urllib2, requests = internet access, request response
# 
# re = regular expressions
# Flask, Django = web frameworks
# 
# pandas, pymysql, openpyxl = data handling, cleanng, import export, aggregation
# 
# =============================================================================

# OS
import os

# get the current working directory
os.getcwd()

## create a new directory
os.mkdir("Batch2")

# get the list of files/folders in a directry
os.listdir('C:\\Users\\Nitu\\Desktop\\Python')

# getting the number of cores in the cpu
os.cpu_count()

#############################################################

import sys

# get the list of system paths
print(sys.path)

# get the list of modules
print(sys.modules)

# how to access a module saved on different location
# we can add that addresss as python system path
# we have a file with name july.py on C:\Users\Nitu\Desktop\Anshu\pythonmodules

sys.path.append(r"C:\Users\Nitu\Desktop\Anshu\pythonmodules")

import july
july.myfun(4,5)
