def score(dice, category):
    return category(dice)


def countSides(dice):
    count = {}
    for side in dice:
        count.setdefault(side, 0)
        count[side] += 1
    return count


def digitCount(dice, num):
    count = countSides(dice)
    count.setdefault(num, 0)
    return count[num] * num


def ones(dice):
    return digitCount(dice, 1)


def twos(dice):
    return digitCount(dice, 2)

def threes(dice):
    return digitCount(dice, 3)


def fours(dice):
    return digitCount(dice, 4)


def fives(dice):
    return digitCount(dice, 5)


def sixes(dice):
    return digitCount(dice, 6)


def full_house(dice):
    count = countSides(dice)
    present_sides = list(count)
    if len(present_sides) == 2:
        side1 = int(present_sides[0])
        if side1 == 4 or side1 == 1:
            return 0
        side2 = int(present_sides[1])
        return count[side1] * side1 + count[side2] * side2
    return 0


def four_of_a_kind(dice):
    count = countSides(dice)
    for side in count:
        if count[side] >= 4:
            return side * 4
    return 0


def straight(dice, num):
    count = countSides(dice)
    if len(list(count)) != 5:
        return 0
    count.setdefault(num, 0)
    if count[num] > 0:
        return 0 
    return 30
   
    
def little_straight(dice):
    return straight(dice, 6)


def big_straight(dice):
    return straight(dice, 1)


def choice(dice):
    sum = 0
    for side in dice:
        sum += side
    return sum


def yatch(dice):
    count = countSides(dice)
    for side in count:
       if count[side] == 5:
           return 50
    return 0
# Score categories.
# Change the values as you see fit.
YACHT = yatch 
ONES = ones 
TWOS = twos 
THREES = threes 
FOURS = fours 
FIVES = fives 
SIXES = sixes 
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind 
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice 
