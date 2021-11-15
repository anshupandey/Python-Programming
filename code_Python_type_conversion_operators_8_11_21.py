# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:33:41 2021

@author: anshu
"""

# Type conversion - convert object of one data type to other
# implicit
x = 4
x = x/1
print(x)

x = True
x = 5*x
print(x)



# explicit
# Primitive
x = 45

# int to string
y = str(x)
print(y,type(y))

# int to float
y = float(x)
print(y,type(y))

# int to boolean
y = bool(x)
print(y,type(y))

x=0
y = bool(x)
print(y,type(y))

m = True
k = str(m)
print(k,type(k))

# bool to int
k = int(m)
print(k,type(k))

# non Primitive

x = [4,5,6,3.5,'hi',4,5]
print(x,type(x))

y = tuple(x)
print(y,type(y))

z = set(x)
print(z,type(z))

k = {4,7,8,5,6}
m = list(k)
print(m,type(m))

q = [['name','Anshu'],['age',39]]
w = dict(q)
print(w,type(w))

w.items()

###############################################################

# arithmetic operators
print(5+6)
print(5-6)
print(5*6)
print(5/6)

print(5**3) # ** is used for exponent

# string
x = "hello "
y = "bye"
print(x+y)
print(x*3)

# list, tuple
x = [4,2,6]
y = [8,5,3]
print(x+y)
print(x*3)

# logical operators
True and True
True or False
not True

x = 6
x>5 and x<12
x<5 or x<12
not x>20

x = [4,5]
y = [4,5]
x==y and x==y

# Membership operators
# in, not in
# iterables - string, list, tuple, set, dictionary

h = "My name is anshu"
print('anshu' in h)

m = [7,8,5,6,3]
print(8 in m)
print(12 in m)

print(5 not in m)
print(25 not in m)

# identity operators
# is, is not

# immutable - int,string,float, bool, complex, tuple
# mutable - list, dict, set
x = 5
id(x)
m = 5
id(m)
print(x==m) # comparison of values 
print(x is m) # comparison of identity

#####################################
m = [4,2,3]
id(m)
n = [4,2,3]
id(n)
print(m==n)
print(m is n)

k = m
id(k)
id(m)
print(k==m)
print(k is m)


##############################################################
###############################################################
# input function
# write a code to ask use enter two number and add them, show result

x = input('Enter the first number ')
print(x,type(x))
y = input("Enter the second number ")
z = int(x)+int(y)
print(z)

#############################################################
# Write code to create BMI caclculator

# =============================================================================
# Ask user
#     - enter weight in KG
#     - enter height in CMs
#     
# - convert the height from CMS to meters, use the below formula
#     BMI = w/(h*h)
#     in the above formula height should be in meters, print(bmi)
#     
#     Testing
#     w = 60, h = 150, bmi= 26.66666
# =============================================================================

w = int(input("Enter the weight in KG "))
h = int(input("Enter the height in CMs "))
h = h/100
bmi = w/(h*h)
print("your bmi is ",bmi)
