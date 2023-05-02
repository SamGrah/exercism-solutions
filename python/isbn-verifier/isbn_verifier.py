def is_valid(isbn):
    isbn_digits = isbn.replace('-', '')
    if len(isbn_digits) != 10:
        return False

    multiple = 1
    sum = 0
    for digit in isbn_digits:
        if digit == 'X':
            if multiple == 10:
                digit = '10'
            else:
                return False
        try:
           digit_value = int(digit)
        except:
            return False
        sum += multiple * digit_value
        multiple += 1

    return sum % 11 == 0
