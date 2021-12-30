# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:19:13 2021

@author: anshu
"""

# String manipulation

data = "Hello world from python"

data.capitalize()

data.count("l")

data.find("world")

data.islower()

data.isspace()

data.upper()

data.lower()

# string to list of words
data.split(" ")

# string to list of characters
list(data)

# list to string
mylist = ['hey','hi','how','are','you']

data = " ".join(mylist)
print(data)

data = "  hi hello "
data.strip()
