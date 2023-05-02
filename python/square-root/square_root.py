def square_root(number):
    lower_bound = 0
    upper_bound = number
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2

        product = mid**2
        if product == number:
            return mid
        elif product > number:
            upper_bound = mid
        else:
            lower_bound = mid + 1
    return number
