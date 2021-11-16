# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:08:27 2021

@author: anshu
"""

# Context Manager

# file handling
# file is a resource

file = open("myfile.txt",mode='w')
file.write("hii how are you")
file.close()


# if there is error before releasing resource
file = open("myfile.txt",mode='r')
file.write("hii how are you")
file.close()

try:
    file = open("myfile.txt",mode='r')
    file.write("hii how are you")
except Exception as e:
    print("error occurred - ",e)
finally:
    file.close()
    
# - amore simple, clearer solution
# with statement - context managers
with open("myfile.txt",mode='w') as f:
    f.write("some data")



################ Understanding context manager

# =============================================================================
# with A() as a:
#     # __enter__() method gets executed
#     # your code goes here ----------
#     # __exit__() method gets executed
#     pass
# =============================================================================

class mycontext:
    def __enter__(self):
        print("Enter method gets executed")
    def __exit__(self,exc_type, exc_value,exc_tb):
        print("Exit method gets executed")


with mycontext() as my:
    print("this a sample code")
    print(" now done, exiting...")
    
    
# Custom context manager

class myfile:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_tb):
        self.file.close()
    

with myfile("myfile.txt",'w') as f:
    f.write("hey hi, how are you")
    

print(f.closed)

#############################################
# creating context manager using decorator function
from contextlib import contextmanager

@contextmanager 
def myfile(file,mode):
    f = open(file,mode)
    yield f
    f.close()

with myfile("mydata.txt",'w') as f:
    f.write("some data written here")

print(f.closed)    

#################################################

# Example of use of context manager

# =============================================================================
# os.scandir - used to iterate over a directory object
# it support context management protocol
# 
# =============================================================================

import os

with os.scandir(".") as entries:
    for en in entries:
        print(en.name, en.stat().st_size)
        
        
########################################
# performing high precision calculations
# =============================================================================
# decimal has an implementation of contextmanager using
# localcontext()
# =============================================================================

from decimal import Decimal, localcontext

with localcontext() as ct:
    ct.prec = 42 # set the precision for calculations
    print(Decimal("1")/Decimal("42"))
    
#######################################################

# speech to text conversion
# conda install pyaudio
# pip install speechrecognition

import speech_recognition as sr
r = sr.Recognizer()    

# to record audio - we need to access microphone

with sr.Microphone(1) as source:
    audio = r.listen(source,phrase_time_limit=10)
    
text = r.recognize_google(audio)
print(text)
