"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual_minutes):
    """Calculate the bake time remaining.

    Keyword Arguments:
    :elapsed_bake_time -- baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_minutes


def preparation_time_in_minutes(layers):
    """Amount of time it takes to prepare the lasagna for baking

    Args:
        layers (int): number of layers

    Returns:
        int: total number of minutes
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    :param number_of_layers: int - layers in lasagna
    :param elapsed_bake_time: int - number of minutes lasagna has been in oven

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    