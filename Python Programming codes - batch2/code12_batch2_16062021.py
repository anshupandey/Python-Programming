# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:28:12 2021

@author: Nitu
"""

a=[3,4,5]
a[2]
a[3]

try:
    print(a[2])
    print(a[3])
except IndexError:
    print("Invalid Index")
#######################################################################
a['hi']

try:
    print(a[2])
    print(a[3])
    print(a['hii'])
except (IndexError,TypeError):
    print("Invalid Index")
#########################################################################
try:
    print(a[2])
except (IndexError,TypeError):
    print("Invalid Index")
else:
    print("none of mentioned errors observed")
    
####################### how to get list of all exceptions
print(dir(locals()['__builtins__']))

#####################################################################
a = 5
a/0
try:
    b = a/0
except BaseException as ex:
    print(str(ex))
else:
    print("code worked out")    
####################################################################
import sys
try:
    b = a/0
except BaseException as ex:
    print(str(ex))
    extype,exvalue,extrace = sys.exc_info()
    print(extype.__name__)
    print(exvalue)
else:
    print("code worked out")
##################################################################
import traceback
try:
    b = a/0
except BaseException as ex:
    extype,exvalue,extrace = sys.exc_info()
    extrace = traceback.extract_tb(extrace)
    print(extrace)
    print(extype.__name__)
else:
    print("code worked out")

##################################################################
# rasing a custom exception

age = int(input("Enter your age: "))
if age<0:
    raise Exception("Age can not be a negative value")
else:
    print("your age is ",age)
    
##################################################################

# raise a custom error = AssertionError

def cm2m(height):
    assert (height>0),"Height can not be negative"
    hm =height/100
    return hm

cm2m(100)
cm2m(203234)
cm2m(-10)
