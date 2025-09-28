"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    
    param: number_of_layers: int - number of layers needed to prepare the lasagna.
    :return: int - return the time (in minutes) necessary to complete all layers.
    
    Function that takes the number of layers needed to do the lasagna as
    an argument and returns how many minutes needs to prepare the layers
    of the lasagna based on the `PREPARATION_TIME`.
    """
    
    total = number_of_layers * PREPARATION_TIME
    return total


def elapsed_time_in_minutes(layers, time):
    """Calculate the preparation time in minutes.
    
    param: preparation: int - return value of the function preparation_time_in_minutes
    param: bake: int - return value of the function bake_time_remaining
    :return: int - return the total elapsed time (in minutes) for prepping + baking.
    
    Function that takes the return value of both functions as arguments and 
    returns the total elapsed time in minutes.
    """
    
    bake_time = time
    preparation_time_two = preparation_time_in_minutes(layers)
    elapsed_time = bake_time + preparation_time_two
    return elapsed_time
