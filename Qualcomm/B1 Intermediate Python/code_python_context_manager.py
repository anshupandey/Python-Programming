# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:32:19 2022

@author: admin
"""

# Context Managers

# create a file
file = open("mydata.txt",'w')
file.write("Some data written here, thanks")
file.close()

file.closed

#################################################

file = open('mydata.txt','r')
file.write("some data written here")
file.close()

file.closed

type(file)

#########################################

with open("mydata.txt",'r') as file:
    file.write("some data here")
    
file.closed

#########################################################
# Custom Context Manager

class freader:
    def __init__(self,fname,mode):
        self.fname = fname
        self.mode = mode
        
    def __enter__(self):
        print("Entered the context manager")
        self.file = open(self.fname,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_msg,exc_traceback):
        print('Exiting the context manager')
        self.file.close()


with freader("mydata.txt",'w') as f:
    print("start entering data")
    f.write("some data goes here thanks")
    print("done writing data")
    
with freader("mydata.txt",'r') as f:
    print("start entering data")
    f.write("some data goes here thanks")
    print("done writing data")