"""A program for guessing a hidden number
   for the minimum number of attempts.
   The number is set by the computer, in the range from 1 to 100.
   The result is estimated by the average number of attempts
   at 1000 checks.
"""


import numpy as np


def binary_search(number: int=1) -> int:
    """Binary search method in the range from 1 to 100.

    Args:
        number(int, optional): The guessed number. By default: 1.

    Returns:
        int: Number of attempts.
    """
    
    
    # Setting initial values:
    # for the counter of the number of guessing attempts: count,
    # for the left and right borders of the search area: 
    # left_edge and right_edge. 
    
    count = 0 
    left_edge = 1 
    rigt_edge = 100 
    
    # An infinite loop with an exit condition when guessing 
    # a given number.
    # At each iteration, a counter for the number of attempts
    # guessing increases by 1.
    # The middle is chosen as the assumed number 
    # of the current search area (integer from division 
    # by 2 of the sum of the boundaries).
    # If the specified number is greater than the expected one - 
    # the left border becomes the next number after the expected one.
    # If less - the right boundary becomes 
    # the number preceding the assumed one.
    # Otherwise, that is, when the assumed and given numbers 
    # are equal the cycle is interrupted.
    
    while True:
        count += 1
        predict_number = (left_edge + rigt_edge) // 2 
        if number > predict_number:
            left_edge = predict_number + 1 
        elif number < predict_number:
            rigt_edge = predict_number - 1 
        else:
            break  
        if count > 20:
            print('Exceeded the allowed number of iterations')
            break
    return count


def average_attempt(number_guesser) -> int:
    """Average number of guessing attempts per 1000 approaches.

    Args:
        number_guesser([type]): Guessing function.

    Returns:
        int: Average number of attempts.
    """
    
    
    # Creating a random_array - a list of random integers
    # of 1000 elements.
    # In this case, the seed() seed function is used to store
    # a random method for generating the same of random numbers
    # when executing code multiple times on one or different computers.
    # Creating the list of attempts by the number of guessing attempts
    # for each random number out of 1000.
    
    attempts_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1,101,size=(1000)) 
    
    # Loop to calculate the number of guessing attempts for each
    # out of 1000 random numbers.
    # The binary_search function is used for guessing.
              
    for number in random_array:
        attempts_ls.append(number_guesser(number)) 
    
    # Calculation of the average value of the number 
    # of guessing attempts.
    # It is the nearest integer that is determined 
    # - the round() function.
    
    return round(np.mean(attempts_ls)) 


# RUN
if __name__ == "__main__":
    average = average_attempt(binary_search)
    print(f"Average number of guessing attempts: {average}")