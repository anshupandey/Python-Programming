# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:26:49 2021

@author: anshu
"""

# Comprehension
# a pythonic way of writing code


cities = ['london','luxemberg','leviv','delhi',
          'Rome','lisbon','Jakarta']

mycities = []
for c in cities:
    if c[0]=='l':
        mycities.append(c)

print(mycities)


# list comprehension
# template 2
# [f(x) for x in sequence if condition]
mycities = [c for c in cities if c[0].lower()=='l']
print(mycities)

# template 1
# [f(val) for val in sequence]
mylist = [4,4,5,2,6,3,6,9]

mysq = [k**2 for k in mylist]
print(mysq)


# template 3
# [f(x) if condition else g(x) for x in sequence]

mycities = [c.upper() if c[0]=='l' else c for c in cities ]
print(mycities)




m = "Hello WORLD"
m.lower()
