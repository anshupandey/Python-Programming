# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:51:45 2021

@author: Nitu
"""
# Regular Expressions

import re

# information extraction
# text/information hiding
# text cleaning

data = "my mobile number is 9898123476 and his mobile number is 7812345678 what is yours?"

pattern = "[0-9]{10}"

re.findall(pattern,data)

re.sub(pattern,"*********",data)

re.sub(pattern,"",data)
##################################################################
data = """ my birhday is on 12-11-2021 and your birthday is on 31-02-1999 and his
birthday is 12-6-2020 and his friend's birthday is on 12/5/1998 please drop me
an email at anshu@mycompany.com and also keep john123@mkglobal.com 
you may wanna add manager@mkglobal.com in cc. Thank you.
"""

pattern = '[0-9]{2}-[0-9]{2}-[0-9]{4}'
re.findall(pattern,data)

pattern = '[0-9]{1,2}-[0-9]{1,2}-[0-9]{2,4}'
re.findall(pattern,data)

pattern = '[0-9]{1,2}-[0-9]{1,2}-[0-9]{2,4}|[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}'
re.findall(pattern,data)


pattern = "[a-zA-Z0-9._]+@[a-zA-Z0-9._]+"
re.findall(pattern,data)

data = "my bday is 14 Feb 2021 and what is yours?"
pattern = "[0-9]{2} [a-z]{3} [0-9]{4}"
re.findall(pattern,data.lower())



#######################################################

data = "my mobile number is 9876541230 and what is yours?"

pattern = '[0-9]{10}'

re.search(pattern,data)

re.search("mobile",data)

# \w = any alphanumeric word character = [a-zA-Z0-9_]
# \W = non word character = [^a-zA-Z0-9_]
    
# \d = anything which is decimal digit
# \D = anything which is not decimal digit

# \s = for whitespace
# \S = anything which is not whitespace
data = "9878787878 thank you"
print(re.match("[0-9]{10}",data))

# any number of repition less than or equal to 10
print(re.match("[0-9]{,10}",data))

data = "my name is name and your name is name"
data.count('name')

data = "my mobile number is 98765  and address is MUM76754 thank you"
re.findall("[0-9]{5}",data)
re.findall("\s[0-9]{5}",data)

data = """ my birhday is on 12-11-2021 and your birthday is on 31-02-1999 and his
birthday is 12-6-2020 and his friend's birthday is on 12/5/1998 please drop me
an email at anshu.pandey_123@mycompany.com and also keep john123@mkglobal.com 
you may wanna add manager@mkglobal.com in cc. Thank you.
"""
pattern = "[a-zA-Z0-9._]+@[a-zA-Z0-9._]+"
re.findall(pattern,data)

pattern = "[\w\.]+@[\w\.]+"
re.findall(pattern,data)
pt = "[\w\.]+@[\w]+[\.]+[\w]{2,4}"
re.findall(pt,data)

##################################################################
# Grouping - regular expressions
# () - can be used to create a group
# <> - create a named group
# + - used for repition - 1 or more time

data = "my nameeeeeee is anshu and your namenamename is John"
pt1 = 'name+'
re.findall(pt1,data)

pt2 = '(name)+'
re.findall(pt2,data)

data = "please drop us an email at manager@mkglobal.com thank you"
pattern = "[\w\.]+@[\w\.]+"
re.findall(pattern,data)

pattern = "([\w\.]+)@([\w\.]+)"
match = re.search(pattern,data)
match.group()
print("the user name is ",match.group(1))
print("the domain name is ",match.group(2))

pattern = "(?P<username>[\w\.]+)@(?P<host>[\w\.]+)"
match = re.search(pattern,data)
match.group()
match.group("username")
match.group("host")
