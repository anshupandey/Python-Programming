# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:08:41 2021

@author: anshu
"""


# Regular Expression in python

# \d = any one number between 0 to 9
# [0-9] = any number between 0 to 9
# a-z - anything between smallcase a to smallcase z
# A-Z


import re

data = "my address is A58, Flank Street, 36545 what is your?"

# informatin extraction - data mining
pattern = "\d\d\d\d\d"
re.findall(pattern,data)

pattern = '[0-9]{5}'
re.findall(pattern,data)

# information masking
re.sub(pattern,"*****",data)

# text cleaning
re.sub(pattern,"",data)

data = "my age is -45 your age is 23 and what his?"

pattern = "-[0-9]{2}"
re.findall(pattern,data)

################################################
##################################################

data = """ My birthday is 30-02-1990 and your birthday is 
 15-12-1985 and his brithday is 12-5-1987 and his friend's 
birthday is 12/05/1996 when is your bday?
please drop me an email to anshu@mycompaby.com and also keep
my boss badboss_mycompany@abc_company.com in cc thanks in advance.
"""
print(data)
# dd-mm-yyyy
pattern = "[0-9]{2}-[0-9]{2}-[0-9]{4}"
re.findall(pattern,data)

# variable size
pattern = "[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
re.findall(pattern,data)

# adding more options to slash
pattern = "[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
pattern = pattern + "|[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"

re.findall(pattern,data)

# Extracting emails
pattern = "[a-zA-Z0-9._]+@[a-zA-Z0-9._]+"
re.findall(pattern,data)
