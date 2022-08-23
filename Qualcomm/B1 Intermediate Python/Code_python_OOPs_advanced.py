# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:00:32 2022

@author: admin
"""


class employee:
    country = "India" # class attribute
    salary = 15000 
    
    def __init__(self,name):
        self.name = name # instance attribute
        print("employee class created")
        self.expertise = "Python" # this will be accessible outside method
        year = 2022 # this wont be accessible outside method
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)


e1 = employee("Marco")
e1.onboarding()



# to check whether an attribute exists or not
hasattr(e1, "name")
hasattr(e1, "city")

# to get the value of an attribute
getattr(e1, "name")
getattr(e1, "country")

# to modify the attribute of the class
setattr(e1, "name", "Windy")
setattr(e1, "salary", 20000)
getattr(e1,"name")

# to delete the attribute
hasattr(e1, "name")
getattr(e1, "name")
delattr(e1, "name")
hasattr(e1, "name")
delattr(e1,"salary")

#getattr(e1, "name")
getattr(e1, "salary")

e1.name = "Anshu"
delattr(e1, "name")
setattr(e1, "name", "value")

######################################################


class A:
    x = 5
    y = 6
    k = None
    

w = A()
id(w.x)
id(A.x)
q = A()
id(q.x)

w.x = 8
id(w.x)



w = A()

hasattr(w, "k")
w.k is not None


hasattr(e1, "name")
(e1.name is not None)

getattr(e1, "name")
e1.name

setattr(e1, "name", "Windy")
e1.name = "Windy"

delattr(e1, "name")
#del e1.name

########################################################

class employee:
    country = "India" # class attribute
    salary = 15000 
    
    def __init__(self,name):
        self.name = name # instance attribute
        print("employee class created")
        self.expertise = "Python" # this will be accessible outside method
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)
                
    def __str__(self):
        return f"this is an object for employee {self.name}"
    
    def __add__(self,val):
        return self.name + str(val)


e1 = employee("Marco")
e1.onboarding()


employee.__name__
employee.__dict__
employee.__module__


str(e1)
e1 + 123
e1 + "hey hi"


class ABC:
    # i will code later
    pass

ABC.__dict__
    