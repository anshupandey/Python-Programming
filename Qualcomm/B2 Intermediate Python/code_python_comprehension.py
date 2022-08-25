# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:43:10 2022

@author: admin
"""

# comprehension

# List comprehension

temp = [25,26,23,25,28,29,32,35,24,25,26,28,29]

g25 = []

for i in temp:
    if i>25: 
        g25.append(i)
        
print(g25)

# comprehension approach
g26 = [i for i in temp if i>26]
print(g26)

#####################################################


# =============================================================================
# template 1 
# 
# [f(x) for x in mylist]
# 
# template 2 
# [f(x) for x in mylist if condition ]
# 
# template 3 
# [f(x) if condition else g(x) for x in mylist]
# =============================================================================

data = [7,5,4,2,6,3,2,5,8,9,5,4,2]

# template 1
# get square of all values
sq = [i**2 for i in data]
print(sq)

# template 2
# get even numbers
ev = [i for i in data if i%2==0]
print(ev)

# template 3
# get square of even numbers and cube of odd numbers
nd = [i**2 if i%2==0 else i**3 for i in data]
print(nd)

# nested comprehension
data = [[4,5,6],[3,2,4,8],[6,8,7,1],[6,1]]

d1 = [i**2 for sublist in data for i in sublist]
print(d1)

d2 = [[i**2 if i%2==0 else i**3 for i in sublist] for sublist in data]
print(d2)

m = [7,5,3,2,5,4,5]

out = [[i,j] for i in m for j in m if i+j==12]
out
d2 = [[i for i in sublist if i > 1] for sublist in data]


##########################################################


# =============================================================================
# # Dictionary Comprehension
# 
# template 1
# 
# {k:f(v) for k,v in mydict.items()}
# 
# 
# template 2 
# 
# {k:f(v) for k,v in mydict.items() if condition}
# 
# template 3
# 
# {k:f(v) if condition else g(v) for k,v in mydict.items()}
# 
# 
# =============================================================================


data = {"Anshu":45,"Kartik":12,"Aashish":32,"Krish":22}

# template 1
# get age in months
mdata = {k:v*12 for k,v in data.items()}
print(mdata)

# template 2
# get data for users with age>30
g30 = {k:v for k,v in data.items() if v>30}
print(g30)

# template 3
# increase age by 5 for age<30 otherwise by 10
ndata = {k:v+5 if v<30 else v+10 for k,v in data.items()}
print(ndata)

######################################################

# Set Comprehension


# =============================================================================
# template 1 
# 
# {f(x) for x in set}
# 
# template 2 
# {f(x) for x in set if condition }
# 
# template 3 
# {f(x) if condition else g(x) for x in set}
# =============================================================================


myset = {4,5,2,3,6,5,8,7}

# template 1
nset = {i**2 for i in myset}
print(nset)

# template 2
mset = {i**2 for i in myset if i%2==0}
print(mset)

# template 3
oset = {i**2 if i%2==0 else i**3 for i in myset}
print(oset)
