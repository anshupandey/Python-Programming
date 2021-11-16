# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:26:31 2021

@author: anshu
"""

# =============================================================================
# Pandas
#     - Data Import / Export
#     - Data Cleaning
#     - Data Aggregation, wrangling, manipulation, filtering
#     - statistical analysis
#     
# pandas internally uses dictionary to process data
# 
# Pandas mainly has two data types- 
#     1. Pandas Series - 1D data
#     2. Pandas Dataframe - 2D tabular data
# =============================================================================


import pandas as pd

data = {"Name":['Anshu','Dipesh','Saurabh','Punit','Deepa',"Jahnvi"],
        "Age":[25,35,24,22,36,39],
        "Gender":['M','M','M','M','F','F']}

df = pd.DataFrame(data)
df

df.head() # to access top n rows, by default top 5 rows
df.head(2)

df.tail() # to access bottom n rows
df.tail(2)

df['City'] = ['Dubai','London','Dubai','Dubai','London','Delhi']

df


#############################################
type(df)

# accessing a specific column
df.Age
df['Age'] # more recommended

type(df.Age)

# accessing more than one columns
df[['Name','City','Age']]

# to access specific rows
df[2:6]

df[2:6]['Name']
df[2:6][['Name','Age']]
