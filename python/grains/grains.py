def square(number):
    is_not_number = type(number) is not int
    is_out_of_range = number < 1 or number > 64
    if is_not_number or is_out_of_range:
        raise ValueError('square must be between 1 and 64')
    return total(number)


def total(number = 65):
    total_grains = pow(2, number - 1)
    if number == 65:
        return total_grains - 1
    return total_grains
