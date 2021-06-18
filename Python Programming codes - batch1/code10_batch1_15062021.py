# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:39:27 2021

@author: Nitu
"""
# file handling

# Reading data from a file

file = open("mydata.txt",'r')
data = file.read()
file.close()

print(data)

######## loading lines in a list
file = open("mydata.txt",'r')
data = file.readlines()
file.close()


print(data)

####################################################################

##### Writing data to a file

data = """ Hi ALl,
hope you are doing good. I am also doing good today.
"""
file= open('yourdata.txt','w')
file.write(data)
file.close()

###################################################################

# data import / export with pandas

import pandas as pd

# two data types
# Dataframe - used to represent tabular 2D data
# series - 1D data

# loading data with pandas
df = pd.read_csv(r"C:\Users\Nitu\Desktop\Python\datasets-1\datasets-1\datawh.csv")
df
#show top 5 rows
df.head()
#show total number of rows and cols
df.shape

# load a json file in tabular fomat
df = pd.read_json(r"C:\Users\Nitu\Desktop\Python\datasets-1\datasets-1\server-metrics.json")
df.shape
df.head()

# normal string
print("Hello \n world")
# raw string
print(r"Hello \n world")


url = "https://raw.githubusercontent.com/anshupandey/xebia_training_data/main/datasets/server-metrics.json"
df = pd.read_json(url)
df.shape
df.head(2)

####################################################################################

url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Gujarat"
df_list = pd.read_html(url)

len(df_list)

df_list[0]
df_list[1]
df_list[3]

## export data with pandas
df = df_list[3]
df.to_excel("coviddata.xlsx")
