# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:29:40 2021

@author: anshu
"""
import numpy as np
import matplotlib.pyplot as plt

year=np.arange(2010,2022,1)
print(year)
growth = [12,18,22,24,39,42,45,48,52,56,48,45]

# line plot
plt.plot(year,growth)
plt.show()

loss = [5,4,8,9,12,13,15,18,12,16,20,22]
len(loss)


plt.plot(year,growth)
plt.plot(year,loss)
plt.show()

###Annotations
plt.figure(figsize=(12,5))
plt.plot(year,growth,c='green',label="Profit")
plt.plot(year,loss,c='red',label='Loss')
plt.title("12 year profit loss analysis")
plt.xlabel('Years')
plt.ylabel("percentage of profit and loss")
plt.legend()
plt.show()

# scatter plot
plt.scatter(year,growth)
plt.show()

plt.figure(figsize=(12,5))
plt.scatter(year,growth,c='red')
plt.plot(year,growth,c='green',label="Profit")
plt.show()


# barplot
plt.figure(figsize=(12,5))
plt.bar(year,growth)
plt.show()

colors = ['red' if g<30 else 'green' for g in growth]

plt.figure(figsize=(12,5))
plt.bar(year,growth,color=colors)
plt.show()


# piechart

names = ['DXB','KUL','NYU','DEL','BOM']
vals= [45,56,23,78,42]

plt.pie(vals,labels=names)
plt.show()

# histogram

temperature = [25,24,26,25,24,26,27,28,32,34,32,34,35,36,35,34,38,37]

plt.hist(temperature)
plt.show()


##########################################

# plotly
# go to anaconda prompt
# pip install plotly

import plotly.express as px
import pandas as pd
# load bank_churn.csv
df = pd.read_csv(r"D:\AI\data\datasets-1\Bank_churn_modelling.csv")

df.head()
df.columns

import plotly.io as pio
pio.renderers.default = 'browser'

fig = px.histogram(df,x='Geography')
fig.show()


fig = px.histogram(df,x='Age')
fig.show()