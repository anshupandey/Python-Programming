# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:15:25 2021

@author: Nitu
"""
x = [3,4,5]
x*3

y = [2,1,6,4]
x+y


# break, continue, pass

x = 7
while x<20:
    print(x)
    x = x+2
    
# break - used to stop execution of loop when a condition is met
x = 7
while True:
    print(x)
    x = x+2    
    if x>20:
        break
    
# continue - to skip the execution of further codes when a condition is met in a 
# certain iteration of the loop
x = 7
while x<20:
    x = x+2    
    if x==15:
        continue
    print(x)

# pass - can be used to skip the execution of a condition/loop/function
for i in range(10):
    pass




# =============================================================================
# Phase 1
# 1. declare a variable ans = 5
# 2. write code to ask user to guess a number between 0 to 9
# 3. compare the guess with answer
#     4. if guess is equal to answer - say user has won the jackpot
#     else say try again.
# 5. the user should get only 3 trials to guess a number
# 
# 
# Phase 2
# 
# 1. if the user makes a guess outside range of 0 to 9 - ask to guesss again, the attempt 
# should not be counted from inappropriate guess.
# 2. if the user wins the game in one or two attempt only, user should not get further
# chances
# 
# =============================================================================

# phase 1
ans = 5
for i in range(3):
    guess = int(input("Guess a number between 0 to 9: "))
    if guess==ans:
        print("You won the jackpot")
    else:
        print("Try Again")

#Phase 2
ans = 5
attempt = 0
while attempt<3:
    guess = int(input("Guess a number between o to 9: "))
    if guess>9 or guess<0:
        continue
    
    if guess==ans:
        print("you won the jackpot")
        break
    else:
        if attempt==2:
            print("You lost the game")
        else:
            print("Try again")
    attempt = attempt + 1










