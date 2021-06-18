# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:46:52 2021

@author: Nitu
"""

import today

today.myfun(3, 5)

e1 = today.employee("Anshu")
m1 = today.manager("John")

import today as td

td.myfun(5,2)
e2 = td.employee("anshu")

from today import employee

e3 = employee('ANshu')

# package in python
'''
mypack
    __init__.py
    
    mymath
        __init__.py
        urmath.py
    
    myutility
        __init__.py
        today.py
'''

from mypack.mymath import urmath
urmath.addtwo(5, 6)
urmath.multtwo(9, 2)

from mypack.myutility import today
today.myfun(4,2)

import mypack

mypack.myutility.today.myfun(4,5)

#####################################################
#####################################################

'''
random = for random number calculations
os = operating system related operations
time, datetime = data and time operations
urllib2,requests = internet access, request response
re = regular expressions
Flask, Django = web frameworkd development

opepyxl,pandas = import/export data - structured
openCV = work with images
librosa = work with audio files

'''

import os

# get the current working directory
os.getcwd()

# create a new directory
os.mkdir("python dummy codes")

# get list of files/folders in a directory
os.listdir('C:\\Users\\Nitu\\Desktop\\Python')

# getting the number of cores of processor
os.cpu_count()

##################################
'['
import sys

# get the list of system paths
sys.path
# get the list of modules
sys.modules


# add a new path
sys.path.append(r"C:\Users\Nitu\Desktop\Anshu\pythonmodules")

print(sys.path)

import tomorrow
tomorrow.myfun(3, 2)




