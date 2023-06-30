# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:06:14 2022

@author: admin
"""


# create a file
file = open("mydata.txt",'w')
file.write("Hey Hi")
file.close()



########################
# reading data from the file

file = open("mydata.txt",'r')
file.write("hello all")
file.close()

file.closed

##############################################

# using context manager
with open("mydata.txt",'r') as f:
    f.write("hii")
    
f.closed

######################################################


class custom_file:
    def __init__(self,fname,mode):
        self.fname = fname
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.fname,self.mode)
        print("Entered into the context")
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_tracebook):
        self.file.close()
        print("file closed")
        
with custom_file("mydata.txt", "w") as file:
    print("writing some data")
    file.write("SOme data written")
    print("done writing")


with custom_file("mydata.txt", "r") as file:
    print("writing some data")
    file.write("SOme data written")
    print("done writing")
    