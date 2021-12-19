# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:05:42 2021

@author: anshu
"""

w = int(input("Enter the weight in KG "))
h = int(input("Enter the height in CMs "))
h = h/100
bmi = w/(h*h)
print("your bmi is %.2f"%bmi)

# if else

if (bmi<25):
    print("your BMI is low")
    print("You should eat more and work less")

if bmi<25:
    print("your bmi is low")
    print("You should eat more and work less")
elif bmi>=25 and bmi<30:
    print("your BMI is good")
    print("you are fit and fine")
    print("Stay fit, stay happy")
else:
    print("Your BMi is high")
    print("you need to workout more, start running regularly")
    if bmi>40:
        print("Your BMI is very high")
        
######################################################################
# Loop - used to repeat the execution multiple times
# For loop - when the exact count of repeatation is known
# while loop - when condition based repeatation is to be done

print("Hello from Python")

list(range(5))


for i in range(5):
    print("Hello from python")    
    

for i in range(5):
    print("Hello from python",i)    

for i in range(3,20):
    print("Hello from python",i)    

for i in range(3,20,2):
    print("Hello from python",i)    

for i in range(20,3,-2):
    print("Hello from python",i)    

for i in range(-20,-1,2):
    print("Hello from python",i)    

cities = ['del','bom','agra','amd','bangalore','maa']    
for c in cities:
    if len(c)==3:
        print(c)
        
##########################################################################

# =============================================================================
# Guessing Game
#     -  create a variable ans = 5
#     - ask user to guess a number between 0 to 9
#     - compare guess with ans, if equal say- you won the jackpot
#     else say try again
#     - the user should get 3 chances to make a guess
# =============================================================================

ans = 5
for i in range(3):
    guess = int(input('Guess a number between 0 to 9 '))
    if guess==ans:
        print("You won the jackpot")
        break
    else:
        print("Try again")

###################################################################
ans = 5
c = 0
while c<3:
    guess = int(input('Guess a number between 0 to 9 '))
    c = c + 1
    if guess==ans:
        print("You won the jackpot")
        break
    else:
        print("Try again")



# While loop
ans = 5
while True:
    guess = int(input('Guess a number between 0 to 9 '))
    if guess==ans:
        print("You won the jackpot")
        break
    else:
        print("Try again")
###################################################################
x = 5
while x<20:
    x = x + 1
    print("Python is awesome",x)
    
    
##################################################################
################################################################
# break, continue and pass
# break - stops the execution of loop
# continue - skips the below that, and shifts the execution to the begining
#pass - do nothing

ans = 5
while True:
    guess = int(input('Guess a number between 0 to 9 '))
    if guess<0 or guess>10:
        continue
    if guess==ans:
        print("You won the jackpot")
        break
    else:
        print("Try again")
        
# pass

for i in range(5):
    pass

#########################################################################
cities = ['del','bom','agra','amd','bangalore','maa','hyd','Kochi']    


city3 = []
for c in cities:
    if len(c)==3:
        city3.append(c)
print(city3)

# list comprehension
mycity = [c for c in cities if len(c)==3]
print(mycity)

########################################

# =============================================================================
# template 1: [f(x) for x in sequence]
# template 2: [f(x) for x in sequence if condition]
# template 3: [f(x) if condition else g(x) for x in sequence]
# =============================================================================
# template 1
mylist= [2,3,6,5,9]
sqlist = [x**2 for x in mylist]
print(sqlist)


# template 2
sqevenlist = [x**2 for x in mylist if x%2==0]
print(sqevenlist)

# template 3
# for even numbers - get sqaure, odd number get cube
customlist = [x**2 if x%2==0 else x**3 for x in mylist]
print(customlist)

######################################################################
# Dictionary comprehension
# dictionary = {key:value for vars in sequence}
mydic = {"apple":20,"mango":30,'banana':50,'grapes':40,'watermelon':80}

# add price - 10
newdic = {key:value+10 for (key,value) in mydic.items()}
print(newdic)

# adding conditions 
# extracting dictionary of fruits having price more than 50
newdic = {key:value for (key,value) in mydic.items() if value>50}
print(newdic)

# increasing prices for fruits having price less than 50
newdic = {key:(value+10 if value<50 else value) for (key,value) in mydic.items()}
print(newdic)






