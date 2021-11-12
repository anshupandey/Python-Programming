# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:07:05 2021

@author: anshu
"""

file = open("myfile.txt",'r')
file.write("hi how are you")
file.close()


# Error handling

try:
    file = open("myfile.txt","w")
    file.write("hi how are you")
except Exception as e:
    print("Error occured - ",e)
finally:
    file.close()
    print("file close successfully")
    
    
# with error
try:
    file = open("myfile.txt","r")
    file.write("hi how are you")
except Exception as e:
    print("Error occured - ",e)
finally:
    file.close()
    print("file close successfully")
    
##########################################
# error information extraction

import traceback

try:
    file = open("myfile.txt","r")
    file.write("hi how are you")
except Exception as e:
    print("Error occured - ",e)
    info = traceback.format_exc()
    print(info)
finally:
    file.close()
    print("file close successfully")


import sys

try:
    file = open("myfile.txt","r")
    file.write("hi how are you")
except Exception as e:
    print("Error occured - ",e)
    errotType,errorObj,errorinfo = sys.exc_info()
    print("'Error type is ",errotType)
    print("line number ",errorinfo.tb_lineno)
finally:
    file.close()
    print("file close successfully")


# Exception Handling - logical exceptions

# assert method
# assert success_condition, error_text

age = int(input("Enter your age in years "))
assert age>0, "Negative value of age not allowed"
print("you have sucessfully registered")

# raise
age = int(input("Enter your age in years "))
if age<18:
    raise("you are not eligible to vote")
print("You can vote")
