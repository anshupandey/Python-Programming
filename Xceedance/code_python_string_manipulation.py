# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:07:07 2021

@author: anshu
"""

# working with strings in python

x = "I love python programming quite a lot"

# string to list of characters

y = list(x)
print(y)

# string to list of words
y = x.split(' ')
print(y)

x.capitalize()
x.upper()
x.lower()
x.count('p')
x.strip()

# list to string
mylist = ['hey','hi','how','are','you','doing']

y = "_".join(mylist)
print(y)

y = " ".join(mylist)
print(y)
