# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:23:26 2021

@author: Nitu
"""
# regular Expression
# information extraction, hiding, text cleaning

import re

data = "My mobile number is 9876863686 and your number is 8764539576 thank you."

pattern = "[0-9]{10}"

re.findall(pattern,data)

re.sub(pattern,"*********",data)

re.sub(pattern,"",data)
