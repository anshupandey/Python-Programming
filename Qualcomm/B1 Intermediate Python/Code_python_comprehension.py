# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:06:32 2022

@author: admin
"""

# =============================================================================
# List Comprehension 
# 
#  template 1
# [f(x) for x in mylist]
# 
#  template 2 
#  [f(x) for x in mylist if condition]
#  
#  template 3 
#  [f(x) if condition else g(x) for x in mylist]
# 
# =============================================================================

temp = [24,25,26,27,28,29,23,32,35,34,22,21,20,18]

g25= []
for i in temp:
    if i>25:
        g25.append(i)

print(g25)    
    
# pythonic way: comprehension approach

g26 = [i for i in temp if i>26]
print(g26)

#template 1
m = [4,5,3,6,1,4,7,2,6,9,8,7,4]
# get square of each value in a new list
k = [i**2 for i in m]
print(k)

# template 2
# get the numbers from m
e = [i for i in m if i%2==0]
print(e)

# template 3 
# get square of even numbers, cube of odd numbers
sc = [i**2 if i%2 ==0 else i**3 for i in m]
print(sc)

#####################################################

# =============================================================================
# Dictionary Comprehension 
# 
# template 1
# 
# {k:f(v) for k,v in mydict.items()}
# 
# template 2 
# 
# {k:f(v) for k,v in mydict.items() if condition}
# 
# template 3 
# {k:f(v) if condition else g(v) for k,v in mydict.items()}
# 
# =============================================================================

emp = {"Anshu":45,"Jason":23,"Kartik":11, "Aashish":36}



# template 1
# get age in days

emp2 = {k:v*365 for k,v in emp.items()}
print(emp2)

# template 2
# get data for users with age >30
g30 = {k:v for k,v in emp.items() if v>30}
print(g30)

# template 3
# get incremented age for users with age>30 by 5, rest by 10

nemp = {k:v+5 if v>30 else v+10 for k,v in emp.items()}
nemp

##################################################################

# =============================================================================
# Set Comprehension 
# 
#  template 1
# {f(x) for x in myset}
# 
#  template 2 
#  {f(x) for x in myset if condition}
#  
#  template 3 
#  {f(x) if condition else g(x) for x in myset}
# 
# =============================================================================


#template 1
m = {4,5,3,6,1,4,7,2,6,9,8,7,4}
# get square of each value in a new list
k = {i**2 for i in m}
print(k)

# template 2
# get the numbers from m
e = {i for i in m if i%2==0}
print(e)

# template 3 
# get square of even numbers, cube of odd numbers
sc = {i**2 if i%2 ==0 else i**3 for i in m}
print(sc)


