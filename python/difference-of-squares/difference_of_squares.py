def square_of_sum(number):
    numbers = range(1, number + 1)
    numbers_sum = sum(num for num in numbers)
    return pow(numbers_sum, 2)

def sum_of_squares(number):
    numbers = range(1, number + 1)
    return sum(pow(num, 2) for num in numbers)

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
