def meets_traingle_equality(sides):
   valid_side_c = sides[0] + sides[1] >= sides[2]
   valid_side_b = sides[0] + sides[2] >= sides[1]
   valid_side_a = sides[1] + sides[2] >= sides[0]
   return valid_side_a and valid_side_b and valid_side_c


def equilateral(sides):
    if sides[0] == 0 or not meets_traingle_equality(sides):
        return False
    return sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    if not meets_traingle_equality(sides):
        return False
    return sides[0] == sides[1] or \
            sides[1] == sides[2] or \
            sides[0] == sides[2]


def scalene(sides):
    if not meets_traingle_equality(sides):
        return False
    return sides[0] != sides[1] and \
            sides[0] != sides[2] and \
            sides[1] != sides[2]
