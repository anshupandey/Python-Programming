# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:57:57 2021

@author: anshu
"""

# =============================================================================
# Pandas has two imp data types
#     - pandas series - 1D data
#     - pandas dataframe - 2D data
# =============================================================================

import pandas as pd

data = {'Name':['Anshu','Amanda','Jenny','Joan','Max','Marco'],
        'Age':[25,24,32,45,46,51],
        "City":['Paris','Rome','Paris','Rome','Brisben','Brisben']}

df = pd.DataFrame(data)
df

type(df)

# access any column
df['Name']
type(df['Name'])

# accessing data by rows
df[2:4]

# filtering
df[df['Age']>40]
df[df['City']=='Rome']

# add a new column
df['Gender'] = ['Male','Female','Female','Male','Male','Male']

df



####################################################################


# Data Import export with pandas
# loading data from a CSV file
df = pd.read_csv(r"D:\AI\data\datasets-1\datawh.csv")
df.shape

# top 5 rows
df.head()


# load data from a JSON file
df = pd.read_json(r"D:\AI\data\datasets-1\server-metrics.json")
df.shape
df.head()


# load data from an excel file
df = pd.read_excel(r"D:\AI\data\datasets-1\Bank_marketing.xlsx")
df.shape
df.head()

# loading data from html webpages
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

df_list = pd.read_html(url)
len(df_list)

df_list[0].shape
df_list[1].shape

df = df_list[0]


# export data
df.to_excel("wolrd_data.xlsx")


######################################################
######################################################


import sqlite3

# create a database or connect to existing database
# create a connection object
conn = sqlite3.connect("mydatabase.db")


# create a table
query = "create table if not exists customers (id numeric primary key, name text, age numeric, city text, gender text);"
conn.execute(query)

# inserting data into the database table
query = "insert into customers values(?,?,?,?,?);"
conn.execute(query,(1,"Anshu",45,"Delhi",'Male'))
conn.execute(query,(2,"Amanda",25,"Berlin",'Female'))
conn.execute(query,(3,"Jenny",35,"Singapore",'Female'))

# fetch data from the database
data = conn.execute("select * from customers;")

for d in data:
    print(d)
    
##############################################

#loading data with pandas

import time
time.clock = time.time 

query = "select * from customers;"
mydf = pd.read_sql_query(query, conn)   
mydf

# write data to a SQL database

df.to_sql("world_pop", conn)

########################################

data = conn.execute("select * from world_pop")
for d in data:
    print(d)
    
    
##################################################

# Data Wrangling and Data Aggregation

df1 = pd.read_csv(r"D:\AI\data\datasets-1\regiment.csv",index_col='index')
df1.shape

df2 = pd.read_csv(r"D:\AI\data\datasets-1\regiment2.csv")
df2.shape

# joining two dataframes using a common column

df = pd.merge(left=df1, right=df2,how='inner',on='name')
df.shape
df


# create a column representing improvement by each soldier during the training
df['improvement'] = df['postTestScore'] - df['preTestScore']
df

# which is the strongest regiment after training

df['postTestScore'].mean()

df.groupby(['regiment'])['postTestScore'].mean()

# which company of which regiment is best after training?

df.groupby(['regiment','company'])['postTestScore'].mean()

# which regument made most improvement during the trianing?

df.groupby(['regiment'])['improvement'].mean()

#############################################
# getting statistical summary of the data
df.describe()

df['preTestScore'].min()
df['preTestScore'].max()
df['preTestScore'].mean()
df['preTestScore'].median()
df['preTestScore'].mode()
df['preTestScore'].var()
df['preTestScore'].std()
