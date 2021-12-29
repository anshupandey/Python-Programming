# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:07:42 2021

@author: anshu
"""

# File Handling

# write data to a new file

data = """Hi
How are you doing today?
I hope you are doing good today
Stay healthy stay fit
"""
file = open("mydata.txt",mode='w') # w = write
file.write(data)
file.close()


# append data to an existing file
data = """
Hey thanks, thank you for contacting.
I am doing good today.
"""

file = open("mydata.txt",mode='a')#a=append
file.write(data)
file.close()

# read data from a file

# reading the content as a single string

file = open('mydata.txt',mode='r') # r =read
data = file.read()
file.close()

print(type(data))
print(data)

# reading each line and returning list of lines

file = open("mydata.txt",mode='r')
data= file.readlines()
file.close()

print(type(data))
print(data)

###############################
file = open("mydata.txt",mode='r')
data= file.readline()
print(data)
file.close()



############################################
#############################################
# list comprehension
mylist = [5,4,2,3,6,8]

sqlist = [k**2 for k in mylist]
type(sqlist)
print(sqlist)

# tuple comprehension - generator
sqgen = (k**2 for k in mylist)
type(sqgen)
next(sqgen)

###############################################

# Data ingestion pipeline using generators

file = r"D:\AI\data\datasets-1\Bank_churn_modelling.csv"

data_lines= (line for line in open(file))
type(data_lines)
#next(data_lines)
data = (line.strip().split(',') for line in data_lines)
#next(data)

col_names = next(data)
col_names

data = (dict(zip(col_names,row)) for row in data)


next(data)

