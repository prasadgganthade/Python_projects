"""
It is a where you must guess a number based on clues
"""
import random
import math
# inputs
lower = int(input('Enter lower bound : '))
# input
upper = int(input('Enter upper bound : '))
# generating random between upper and lower bound
x = random.randint(lower,upper)
print("\n\tYou have only",
      round(math.log(upper - lower +1, 2)),
      "Chances to guess integer!!!\n")
count = 0
while count < math.log(upper - lower +1,2):
    count += 1
    # Taking guessing number as a input
    guess = int(input("Guess a number : "))
    # condition
    if x == guess:
        print("Congratulations you dit it in",count, "try")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print('You guessed too high')

if count >= math.log(upper - lower +1,2):
    print("\nThe number is %d"%x)
    print("\tBetter luck next time!!!!!")