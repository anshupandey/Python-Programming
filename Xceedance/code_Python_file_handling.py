# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:08:21 2021

@author: anshu
"""

# OS native files = txt/csv/tsv/json

# Writing data to a new file
data = """ Hi
My name is Anshu, I hope you are doing good.
How can I help you today. Thank you for calling"""

file = open("mydata.txt",'w')# w = write mode
file.write(data)
file.close()

# appending data to an existing file

data = """
Hy thanks for connecting
Thank you for calling today.
"""
file = open("mydata.txt",'a')# a = append mode
file.write(data)
file.close()


# reading data from a file

file = open('mydata.txt','r')
data = file.read() # reading whole content of file as one string
file.close()

print(data)

# reading each line sepearately

file = open('mydata.txt','r')
data = file.readlines() # a list of strings, each string = one line
file.close()

for line in data:print(line)
