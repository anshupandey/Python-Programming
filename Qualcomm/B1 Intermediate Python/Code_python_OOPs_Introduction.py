# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:37:53 2022

@author: admin
"""

# Python OOPs Introduction


class employee:
    name = ""
    salary = 12000 
    


e1 = employee()
print(e1.name, e1.salary)

e1.name = "Anshu"
e1.salary = 5000
print(e1.name, e1.salary)

e2 = employee()
e2.name = "John"
e2.salary = 4000
print(e2.name, e2.salary)



########################################################
# I am a comment in python

class employee:
    name = ""
    salary = 15000 
    
    def onboarding():
        print("hey welcome to the company")
        

e1 = employee()
print(e1.salary)
e1.name = "Anshu"

e1.onboarding()# this will throw error
# when we try to access a method of class with refrence to an object,
# it always passes the instance of class as input argument to the method.


####################

class employee:
    name = ""
    salary = 15000 
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")



e1 = employee()

e1.name = "Jimmy"

e1.onboarding()

#####################################


class employee:
    name = ""
    salary = 15000 
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)
        
        
e2 = employee()
e2.name = "James"
e2.onboarding()
e2.increment_salary(2000)

############################################################
# Doc String to the class

class employee:
    "This class can be used to create employee objects"
    name = ""
    salary = 15000 
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)

e1 = employee()
help(e1)
print(e1.__doc__)

############################################################

class employee:
    """
    This class can be used to create employee objects
    
    Arguments:
        None
    
    Attributes:
        name: name of employee, to be modified, default ""
        salary: salary of the employee, default 15000
        
    Methods:
        Onboarding(): this method welcomes the employee
            arguments: None
            Return: None
        
        increment_salary(): this method increases the salary of the employee
            arguments: incr: amount of increment
            Returns: None
        
    """
    name = ""
    salary = 15000 
    
    def onboarding(self):
        """
        this method greets user

        Returns
        -------
        None.

        """
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        """
        

        Parameters
        ----------
        incr : int/float
            increment to be made to salary.

        Returns
        -------
        None.

        """
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)


e1 = employee()
print(e1.__doc__)
help(e1)

print(e1.onboarding.__doc__)
help(e1.onboarding)

############################################################


# Constructor


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

##################################################################

# Destructor

class employee:
    country = "India" # class attribute
    salary = 15000 
    
    def __init__(self,name):
        self.name = name # instance attribute
        print("employee class created")
    
    def onboarding(self):
        print("hey welcome to the company")
        print(f" Hey {self.name}, welcome to the team ")
        
    def increment_salary(self,incr):
        self.salary = self.salary + incr 
        print("Your final salary is ",self.salary)
        
        
    def __del__(self):
        print(f"the object got deleted for employee {self.name}")


e1 = employee("Maggy")
e1.salary 
e1.onboarding()

del e1 

