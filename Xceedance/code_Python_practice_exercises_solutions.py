# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:49:13 2021

@author: anshu
"""

# Python practice exercises

# Task 1

# =============================================================================
# Given two lists
# 
# listone = [3,6,9,12,15,18,21]
# listtwo = [5,10,15,20,25,30,35]
# 
# create a third list by picking an odd index element from
# listone and even index element from listtwo

# listthree = [5,6,15,12,25,18,35]
# =============================================================================


listone = [3,6,9,12,15,18,21]
listtwo = [5,10,15,20,25,30,35]

listthree = []
for i in range(len(listone)):
    if i%2==0:
        listthree.append(listtwo[i])
    else:
        listthree.append(listone[i])

print(listthree)


# Task 2

# =============================================================================
# Given a list
# 
# mylist = [12,56,45,89,78.5,56.99,12.785,12,56,45]
# 
# Find
#     - remove duplicates and convert it to a tuple
#     - get the mean of the list using python builtin function
#     (do not use any python module)
#     - Use list comprehension to create another list 
#     having square of each element
# =============================================================================

mylist = [12,56,45,89,78.5,56.99,12.785,12,56,45]

# remove duplicates and convert it to a tuple
mytuple = tuple(set(mylist))
print(mytuple)

# get the mean of the list using python builtin function
#     (do not use any python module)

mean = sum(mylist)/len(mylist)
print(mean)

# Use list comprehension to create another list 
#     having square of each element

sqlist = [k**2 for k in mylist]
print(sqlist)

# Task 3

# =============================================================================
# Given below list, count the occurrence of each element
# create a dictionary having element as key and count as value 
# mylist = [12,45,23,56,45,12,23,89,45,23,56,12,45,12,56]
# =============================================================================


# solution 1
list1= [12,45,23,56,45,12,23,89,45,23,56,12,45,12,56]
print ([ [l, list1.count(l)] for l in set(list1)])
print (dict( (l, list1.count(l) ) for l in set(list1)))
#################################################
# solution 2
x={}
mylist = [12,45,23,56,45,12,23,89,45,23,56,12,45,12,56]
for i in set(mylist):
    x[i]=mylist.count(i)

print(x)

# solution 3
mylist = [12,45,23,56,45,12,23,89,45,23,56,12,45,12,56]
mydic = {k:mylist.count(k) for k in set(mylist)}
print(mydic)

# Task 4

# =============================================================================
# Write a code for sentiment analysis
# positive = ['good','amazing','awesome','happy','excited','love']
# negative = ['bad','poor','worst','sad','unhappy','dull']
# 1. Ask user to enter any text
# 2. convert text into list of words
# 3. check the count of positive words from the list in the document
# 4. check the count of negative words from the list in the document
# 5. print both positive and negative words, print overall sentiment
# 
# test = "I am happy to code in python today. Python is exciting and i love it."
# =============================================================================

# solution 1
test = "I am happy to code in python today. Python is exciting and i love it."
positive = ['good','amazing','awesome','happy','excited','love']
negative = ['bad','poor','worst','sad','unhappy','dull']


text=test.split(' ')
print(type(text))
pos=0
neg=0
for i in text:
    if i in positive:
        pos=pos+1
    elif i in negative:
        neg=neg+1

print ("Positive words",pos)
print ("Negative words",neg)

if pos>neg:
    print("Overall sentiment - Positive")
elif pos<neg:
    print("Overall sentiment - Negative")
else:
    print("Overall sentiment - Neutral")
    
##############################################################################

# Task 5

# =============================================================================
# Write a function in python which can accept a number and return reverse of that
# number.
# for example - :
#          reverse_num(45879) should return 97854
#          reverse_num(129) should return 921
# =============================================================================

# solution 1
num = input("Enter a number")
print(str(num)[::-1])

# solution 2
def reverse_num(x):
    y = list(reversed(list(str(x))))
    return int("".join(y))


reverse_num(468)
reverse_num(78958)
