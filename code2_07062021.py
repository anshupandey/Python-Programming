# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:04:23 2021

@author: Nitu
"""

"""
Task 1 
BMI Calculator
- Write code to ask user
	- Enter the weight in KG
	- Enter the hieght in CMs

- convert the height from CMs to meter
- Use following formula to calculate BMI
	bmi = w/(h*h)  
where h is in meters
= print the bmi value
****************************************
testing
w = 60, h = 150
bmi = 26.6666666666666666

"""

w = input("Enter the weight in KG ")
h = input("Enter the height in CMs ")
h = int(h)/100
bmi = int(w)/(h*h)

print("Your BMI is ",bmi)
print("Your BMI is "+str(bmi))
print("Hi %s your bmi is %.2f"%("Anshu",bmi))

# Control Flow - if else

if bmi<25:
    print("Your BMI is low you need to join IT")
    print("Make foddie friends")
    
if (bmi<25):
    print("Your BMi is low, you should join IT")
    print("Make more foodie friends")
elif bmi>=25 and bmi<30:
    print("You are fit, you should join modelling")
    print("Try out being foodie once.")
    print("Stay healthy, stay happy")
else:
    print("You are overweight.")
    print("you should join civil engineering")
    if bmi>40:
        print("you need to take proper diet and do exercise, its important")

## for loop
# for loop - when the exact count of repeatation is known
# while loop - when the exact count of repeatation is not known

print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")



for i in range(5):
    print("python is awesome and easy")

for i in range(5):
    print("python is awesome and easy",i)

for i in range(3,15):
    print("python is awesome and easy",i)

for i in range(3,15,2):
    print("python is awesome and easy",i)


temp = [25,26,26,27,282,52,26,27,28,32,32,39,26,27,26,24,23,23,29]
for val in temp:
    if val>27:
        print(val)

for val in temp:
    if val>27:print(val)


# list comprehension
g27 = [val for val in temp if val>27]
print(g27)


## While loop

x = 7
while x<20:
    print(x)
    x = x + 1
    
    
print(x)