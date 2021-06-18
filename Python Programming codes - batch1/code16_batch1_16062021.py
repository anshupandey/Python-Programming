# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:42:19 2021

@author: Nitu
"""
# Exception Handling - Try and Except
a = [5,6,8]
a[3]
a['hi']

try:
    print(a[1])
    print(a[3])
except IndexError:
    print("An error occurred")
################################################### 
try:
    print(a[1])
    print(a[3])
    print(a['hi'])
except (IndexError,TypeError):
    print("An error occurred")
#####################################################    
try:
    print(a[1])
    print(a[2])
except IndexError:
    print("An error occurred")
else:
    print(a)
#####################################################
#####################################################    
try:
    print(a[1])
    print(a[3])
except IndexError:
    print("An error occurred")
else:
    print(a)


###########################################################
a = 5
import sys

try:
    b = a/0
except BaseException as ex:
    print(str(ex))
    extype,exvalue,extraceback = sys.exc_info()
    print(extype.__name__)
    print(exvalue)
else:
    print("code worked out")

####################################################################

import traceback

try:
    b = a/0
except BaseException as ex:
    extype,exvalue,extraceback = sys.exc_info()
    extb = traceback.extract_tb(extraceback)
    print(list(extb))    
else:
    print("code worked out")
finally:
    print("i will always be executed")
    
    
########################################################

age = int(input("Enter your age: "))
if age<0:
    raise Exception("Age value can not be negative")
else:
    print("your age is ",age)


######################################################
def cm2m(height):
    assert (height>0),"Height can not be negaitve"
    return height/100

cm2m(100)
cm2m(5)
cm2m(-10)

b = 8
del b
