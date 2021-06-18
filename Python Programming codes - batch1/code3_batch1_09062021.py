# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:19:12 2021

@author: Nitu
"""

## break, continue and pass

### brek - used to stop execution of the loop / interuppt the loop when a certain conditio is true

x = 5
while x<20:
    x = x + 2
    print(x)


x = 5
while True:
    x = x+2
    print(x)
    if x==21:
        break


### Continue - to skip the set of code after continue in that iteration, when a certain condition is met

x = 5
while x<20:
    x = x + 2
    if x==15:
        continue
    print(x)
    
### pass - to skip the loop/condition/function without any job/task
for i in range(5):
    pass
    


################################################################################
'''
A Guessing Game

Phase 1

1. declare a variable ans = 5
2. write code to ask user to guess a number between 0 to 9
3. compare the guess with answer
    4. if guess is equal to answer - say user has won the jackpot
    else say try again.
5. the user should get only 3 trials to guess a number


Phase 2

1. if the user makes a guess outside range of 0 to 9 - ask to guesss again, the attempt 
should not be counted from inappropriate guess.
2. if the user wins the game in one or two attempt only, user should not get further
chances
'''

#phase 1

ans = 5
for i in range(3):
    guess = int(input("Enter a number between 0 to 9"))
    if guess == ans:
        print("you won the jackpot")
    else:
        print("Try Again")

#Phase 2

ans = 5
attempt = 0
while attempt<3:
    guess = int(input("Enter a number between 0 to 9: "))
    if guess<0 or guess>9:
        print("enter a valid number between 0 to 9")
        continue        
    attempt = attempt + 1
    if guess == ans:
        print("you won the jackpot")
        break
    else:
        if attempt<3:
            print("Try Again")
        else:
            print("You lost the game")








"""
1. define the answer
2. start for 3 attempts
    3. get the guess from user
    4. check the validity if valid
        5. compare with answer, if correct
            6. user won, exit the loop
        7. else - say try again
    8. else - ask for valid input
9. end the loop, increment counter, say you lost

"""







    
    
    