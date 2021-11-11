# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:41:15 2021

@author: anshu
"""

# Global v/s local variable

name = "John" # this is a global variable
# a global variable is accessible inside the function
def myfun(age):
    print("Hi %s your name is %d"%(name,age))
    salary = 1000 # this is a local variable
    # a local variable is accessible only inside the func
    print("hi %s your salary is %d"%(name,salary))
    return None

myfun(45)

print(salary)# will get error as salary is a local var

#######################################################
# Global variables can be modified - pass by reference
# only mutable objects can be modified
x = [4,2,3]

def myfun():
    print(x)
    x.append(45)
    print(x)
    return None

# x is a global variable, it accessible to the function
# as it is mutable, it is modifiable inside the function
myfun()
print(x) # x is modified by the function myfun
######################################################
# a global variable can not be assigned with a new value
# inside a function
# the moment we do assignment, pass by reference gets
# disconnected, and it becomes a local variable

x = [4,2,3]

def myfun():
    x = [7,8,9]
    x.append(12)
    print(x)
    return None

# x is a global variable, it accessible to the function
myfun()
print(x) # global variable x is not affected by assignment
# inside the function
##########################################################3
#############################################################
# global keyword in python

x = 45
y = 12

def myfun():
    global x,y
    x = bool(x)
    y = "hi from python"
    return None

print(x,y)
myfun()
print(x,y)


###########################################################

# Recursive function
# process of defning something which repeats itself.


# Write a code which accepts a number and returns its 
# factorial
# 5! = 5*4*3*2*1

def factorial(n):
    """
    This function is a recursive function, can be used to
    Calculate factorial
    """
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))

factorial(5)
factorial(9)


#########################################################

# write recursive algorithm to find the maximum value
# in a squence(list).

mylist = [4,8,7,6,3,5,2]

mylist.pop() # remove from last / position
mylist.remove(4) # remove by value
del mylist[0] # remove/delete by position


def get_max(lis):
    if len(lis)==1:
        return lis[0]
    if lis[0]<=lis[1]:
        del lis[0]
    else:
        del lis[1]
    return get_max(lis)

mylist = [4,8,7,6,3,5,2]
get_max(mylist)

