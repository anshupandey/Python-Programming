# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:15:09 2021

@author: anshu
"""

# Comprehension
# - one liner - pythonic way of writing codes

vals = [4,5,2,6,3,9]
#############################################################
############################################################
# create another list with square of each value from vals

sqvals = []
for v in vals:
    sqvals.append(v**2)
  
print(sqvals)
# List Comprehension

# template 1 
# [g(x) for x in sequence]

sqv = [v**2 for v in vals]
print(sqv)

##################################################3
#################################################
# create another list with square of each even value from vals

evensq = []
for v in vals:
    if v%2==0:
        evensq.append(v**2)
        
print(evensq)

# template 2
# [g(x) for x in sequence if condition]

evensquare = [v**2 for v in vals if v%2==0]
print(evensquare)

# template 3

# [g(x) if condition else h(x) for x in sequence]

mylist = [v**2 if v%2==0 else v for v in vals]
print(mylist)

###########################################################
# Dictionary

mydic = {"apple":24,"banana":26,"mango":30,"grapes":65,
         "water-melon":68,"orange":75}

# increase price of each fruit by 5

mydic.items()
# template 1
# {key:g(val) for (key,val) in dictionary.items()}

mydic2 = {key:val+5 for (key,val) in mydic.items()}
print(mydic2)

# template 2

# {k:v for (k,v) in dictionary.items() if condition}
# increase the price of items having existing price below 50

mydic2 = {key:val+5 for (key,val) in mydic.items() if val<50}
print(mydic2)


# template 3
# {k:(g(v) if condition else h(v)) for (k,v) in dictionary.items()}

mydic2 = {k:(v+5 if v>50 else v+10) for (k,v) in mydic.items()}
print(mydic2)

###########################################

### Set comprehension

mylist = [4,5,2,6,5,2,4,5,2,3,9,8,7]

myset = {v**2 for v in mylist}
print(myset)

myset = {v**2 for v in mylist if v%2==0}
print(myset)

myset = {v**2 if v%2==0 else v**3 for v in mylist}
print(myset)
##########################################################

# nested comprehension
# nested if

mylist = [k for k in range(50) if k%2==0 if k%5==0]
print(mylist)

mylist = [[4,5],[3,6],[2,8],[4,8],[1,4]]
# getting the transpose
mylist2 = [val for sublist in mylist for val in sublist]

mylist2
