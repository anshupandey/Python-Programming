# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:03:00 2021

@author: Nitu
"""

# reading data from a file

file = open("mydata.txt",'r')
data = file.read()
file.close()
print(data)


file = open("mydata.txt",'r')
data = file.readlines()
file.close()
print(data)

# write data to a file
data = """ My name is John, I am an engineer. I love cricket. 
I am going for a tour today.
"""

file = open("newdata.txt",'w')
file.write(data)
file.close()


######################################
newd = "Today it is Tuesday"
file = open("newdata.txt",'a')
file.write(newd)
file.close()
############################################
file = open("mydata.txt",'r')
data = file.readlines()
file.close()
len(data)

data.insert(3,"Hi my name is Max. \n")

file = open("mydata.txt",'w')
file.write(" ".join(data))
file.close()

m = ['anshu','works','for','abc']
'_'.join(m)
' '.join(m)

with open("mydata.txt",'w') as file:
    data = file.read()

###################################################################
###############################################################


import pandas as pd

# 1. pandas series - 1D data
# 2. pandas dataframe - 2D data

df = pd.read_csv(r"C:\Users\Nitu\Desktop\Python\datasets-1\datasets-1\datawh.csv")
df
df.shape # to get the total number of rows and columns
df.head() # this shows top five rows of the dataframe

df.columns

# load a JSON file
df = pd.read_json(r"C:\Users\Nitu\Desktop\Python\datasets-1\datasets-1\server-metrics.json")
df.shape
df.head()

df.info()

import numpy as np
df['Accepted'] = np.float32(df['Accepted'])


#############################################################
url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Gujarat"
df_list = pd.read_html(url)

len(df_list)

df_list[0]
df_list[1]
df_list[2]
df_list[3]

df = df_list[3]

######## export data
df.to_excel("covid19dataset.xlsx")

df.to_excel("covid19dataset.xlsx",sheet_name="table3")

df.to_excel("covid19dataset.xlsx")

