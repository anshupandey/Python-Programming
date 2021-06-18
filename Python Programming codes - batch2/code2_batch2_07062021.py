# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:09:58 2021

@author: Nitu
"""
"""
Write a code to accept two numbers from user, add both and print result
"""

x = input("Enter the first number ")
y = input("Enter the second number ")
z = int(x) + int(y)
print(z)

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

w = input("Enter your wight in KG ")
h = input("Enter your height in CMs ")
h = int(h)/100
bmi = int(w)/(h*h)
print("Your BMI is ",bmi)
print("your bmi is "+str(bmi))
print("Hi %s your bmi is %.4f and your weight is %d"%("Anshu",bmi,int(w)))


# Control Flow in Python
## if else statement

if bmi<25:
    print("You are underweight")
    print("You should join some IT job and sit and relax")
    print("make some foodie friends")
    print("Dominos is calling you....")

if (bmi<25):
    print("You are underweight")
    print("You should join some IT job and sit and relax")
    print("make some foodie friends")
    print("Dominos is calling you....")
elif bmi>=25 and bmi<30:
    print("You are fit")
    print("stay healthy, stay happy")
else:
    print("you are overweight")
    print("Are you an instructor?")
    print("Leave IT, and join civil engineering")
    if bmi>40:
        print("you need to take action now, walk everyday, eat less and stay happy")
        
######################################################################

# for loop - when you know the exact count of repeatation
# while loop - when the exact count of repeatation is not known, condition based repeatation

print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")
print("Python is awesome and easy")


#for loop
for i in range(5):
    print("Python is awesome and easy")


for i in range(5):
    print("Python is awesome and easy",i)

for i in range(6):
    print("Python is awesome and easy",i)

for i in range(3,16):
    print("Python is awesome and easy",i)

for i in range(3,16,2):
    print("Python is awesome and easy",i)

for i in range(3,16,2):
    print("Python is awesome and easy and i is %d"%(i))


temp = [25,26,24,27,27,32,34,26,28,25,24,23,23,25,26,26,32,27,26,25]
for val in temp:
    if val>27:
        print(val)

for val in temp:
    if val>27:print(val)


g27 = []
for val in temp:
    if val>27:
        g27.append(val)

#### list comprehension
g27 = [val for val in temp if val>27]    
print(g27)

g27.sort(reverse=True)

print(g27)

####### While loop

x = 5
while x<20:
    x = x+1
    print(x)
    
x = 5
while x<20:
    print(x)
    x = x+1








