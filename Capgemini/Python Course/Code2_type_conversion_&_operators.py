# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:29:38 2021

@author: anshu
"""

# Type conversion

# Primtive

# converting to int = int()

x = "456"
print(x,type(x))
y = int(x)
print(y,type(y))

m = 12.5
n = int(m)
print(n,type(n))

# converting to string = str()
n = True
m = str(n)
print(m,type(m))
k = 45688
h = str(k)
print(h,type(h))

# converting to float = float()
k= "456.2"
w = float(k)
print(w,type(w))
q = 4785
y = float(q)
print(y,type(y))

# converting to boolean = bool()
k = 45
m = bool(k)
print(m,type(m))
p = 0
q = bool(p)
print(q,type(q))

###############################################

x = 5
print(type(x))
id(x)
x = "hi"
id(x)
print(type(x))

########################################################

# Type conversion - non primitive


# conversion to a list
# tupel to list
x = (4,5,6,2,'hi') # a tuple
y = list(x)
print(y,type(y))

# set to list
m = {4,5,6,7,8,3}
n = list(m)
print(n,type(n))

# dictionary to a list
w = {'name':'Anshu','age':45,'salary':500}
k = list(w.items())
print(k)
print(type(k))


# conversion to tuple
# list to tuple
x = [4,5,6,2,'hi']
y = tuple(x)
print(y,type(y))


# set to tuple
m = {4,5,6,7,8,3}
n = tuple(m)
print(n,type(n))


# dictionary to a list
w = {'name':'Anshu','age':45,'salary':500}
k = tuple(w.items())
print(k)
print(type(k))



# to dictionary
x = [['name','anshu'],['age',45]]
y = dict(x)
print(y,type(y))


# to set
m = [7,4,5,6,2,2,5]
n = set(m)
print(n,type(n))

##################################################################

# Operators in python

# Arithmetic operators

x = 5
y = 6
# addition
x + y
# subtraction
x - y
# multiplication
x * y
# division
x/y

x = 'hi '
y =" bye"
x+y # + concatenates the strings
x *4 # * repeataion of string
m = [4,5,6]
n = [2,4,7]
m+n

# exponent
m = 5
m**2
m**3

####################################################################
# logical operators

a = True
b = False
a and b
a or b
not a
not b

#############################################################

# Memberships Operators - in, not in

m = [7,3,6,5,9]
5 in m
12 in m

6 not in m
12 not in m

'hi' in 'hi from python'
'bye' not in 'hi from python'

################################################################

# identity operators - is, is not 
# to check whether two objects are pointing to same memory location or not
# primitive
a = 5
b = 5
print(a==b)
a is b

# non primitive
a = [4,6,6]
b = [4,6,6]

print(a==b)
a is b
a is not b


#####################################################
w = {'name':'Anshu','Age':45}
'name' in w # looks for keys
45 in w

'name' in w.keys()
45 in w.values()


