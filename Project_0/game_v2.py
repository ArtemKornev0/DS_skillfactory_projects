"""Guess the number game
   the computer itself makes a guess and guesses the number
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): A hidden number. Defaults to 1.

    Returns:
        int:  Number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        if number == predict_number:
            break # exit the loop, if you guessed right
    return(count)

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = [] # list of number of attempts
    np.random.seed(1) # we fix the seed for reproducibility
    random_array = np.random.randint(1,101,size=(1000)) # made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number)) # made a list of attempts
        
    score = int(np.mean(count_ls)) # we find the average number of attempts

    print(f'Your algorithme guesses the number for {score} attepmtes')
    
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
