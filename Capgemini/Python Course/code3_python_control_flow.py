# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:01:38 2021

@author: anshu
"""

# input - accept input by the user via prompt
# - it always converts any data to string format


x = input("Enter your name ")
print(x,type(x))

x = input("Enter your Age ")
print(x,type(x))

# write a code to ask user enter two numbers and add them
a = input("Enter the first number ")
b = input('Enter the second number ')
c = int(a) + int(b)
print(c)


# =============================================================================
# Task
# - write code to create a bmi calculator
#     - askuser to enter the weight in KG
#     - enter the height in CMs
#     write code to 
#     - convert the height from CMs to meters
#     Use below formula with weight in KG and height in meters
#     bmi = w/(h*h)
#     print(bmi)
#  ##################################################
#  w = 60, h = 150, bmi = 26.66666666
# =============================================================================


w = input("Enter weight in KG ")
h = input("Enter heigh in CMs ")
h = float(h)/100
bmi = float(w)/(h*h)

print(bmi)

print("Your bmi is ",bmi)

# f string
name = "Anshu"; age = 45
k = f"hey hi {name}, your age is {age}"
print(k)

print(f"hi your bmi is {bmi}")
print(f"hi your bmi is {bmi:.2f}")


###################################################################


w = input("Enter weight in KG ")
h = input("Enter heigh in CMs ")
h = float(h)/100
bmi = float(w)/(h*h)
print(bmi)

if (bmi<25):
    print("your bmi is low")
    print("you need to gain more weight, you should eat more ")
    print("Work less, eat more")
    
    
    
##############################################

w = input("Enter weight in KG ")
h = input("Enter heigh in CMs ")
h = float(h)/100
bmi = float(w)/(h*h)
print(bmi)

if bmi<25:
    print("your bmi is low")
    print("you need to gain more weight, you should eat more ")
    print("Work less, eat more")
elif bmi>=25 and bmi<30:
    print("you are fit, your bmi is good")
    print("stay healthy stay fit")
else:
    print("you are overweight, your bmi is high like Anshu")
    print("You need to workout more, walk more, eat less")
    print("may be you should leave it, join civil engineering")
    if bmi>40:
        print("you need to take health serious and work on weight loss")


#################################################################

# loop - used to repeat execution of a set of instructions

# =============================================================================
# for loop - when the exact of count of repeatation is known
# while loop - when we need to perform condition based repeatation
# =============================================================================



print("hello from python, good morning")
print("hello from python, good morning")
print("hello from python, good morning")
print("hello from python, good morning")
print("hello from python, good morning")


for i in range(5):
    print("hello from python, good morning")

# range(start,stop,step)
for anshu in range(5):
    print('python is awesome')
    
for i in range(5):
    print("Python is easy ",i)
    
for i in range(3,20):
    print("Python is easy ",i)
    
for i in range(3,20,2):
    print("Python is easy ",i)
    
for i in range(20,5,-2):
    print("Python is easy ",i)
    
mydata = ['DEL','NYU','DXB','KUL','BOM','MAA','BLR']

for c in mydata:
    print(c)
    
for c in mydata:
    if c[0]=='D':
        print(c)
        
#############################################################
x = 5
while x<10:
    print('Python is easy and awesome',x)
    x = x + 1

#############################################################

# =============================================================================
# Task
# Write code for
#                 A Guessing game
#     - create a variable ans = 5
#     - ask user to guess a number between 0 to 9
#     - compare guess with ans, if equal, say "you won the jackpot"
#     - else say try again
#     - User should get 3 attempts to make a guess.
# =============================================================================
options = set(range(10))
ans = options.pop()
for i in range(3):
    ui = int(input("guess a number between 0 to 9: "))
    if ui==ans:
        print("you won the jackpot")
        break
    else:
        print("try again")

####################################


options = set(range(10))
ans = options.pop()
while True:
    ui = int(input("guess a number between 0 to 9: "))
    if ui==ans:
        print("you won the jackpot")
        break
    else:
        print("try again")
        
#########################################################
# continue
ans = 5
while True:
    ui = int(input("guess a number between 0 to 9: "))
    if ui not in range(10):
        print("Enter a valid number")
        continue    
    if ui==ans:
        print("you won the jackpot")
        break
    else:
        print("try again")

#############################################################
# pass

for i in range(5):
    # no code
    # will add later
    pass
    
    
