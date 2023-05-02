def is_armstrong_number(number):
    number_str = str(number)
    number_of_digits = len(number_str)
    digits = list(str(number))
    sum = 0
    for digit in digits:
        sum += pow(int(digit), number_of_digits)
    return sum == number
