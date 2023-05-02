def leap_year(year):
    divides_hundreds = year % 400 == 0
    divides_hundred = year % 100 == 0
    divides_single = year % 4 == 0

    if divides_single:
        return divides_hundreds or not divides_hundred
    else:
        return False
        
