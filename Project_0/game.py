"""Guess the number game"""

import numpy as np

number = np.random.randint(1, 101) # guessing the number
count = 0 # number of attempts

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100:  "))
    
    if predict_number > number:
        print("The nunber should be less!")

    elif predict_number < number:
        print("The nunber should be more!")

    else:
        print(f"You guessed the number! This number = {number}, for {count} attempts")
        break # end of the game, exit the loop