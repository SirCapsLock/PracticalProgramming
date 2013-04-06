'''
Created on Mar 28, 2013

@author: Kiks
'''

import random

# a <= N <= b
randomNumber = random.randint(1,10)

print("Pssssssttttttt.....the answer is " + str(randomNumber))

while True:
    userNumber = int(raw_input("Please enter a number between 1 and 10, inclusive")) 
    if userNumber == randomNumber:
        print("CONGRATS! You win! ^_^")
        break

print("Done!")

