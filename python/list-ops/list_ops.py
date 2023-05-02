def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    all_elements = []
    for list in lists:
        all_elements.extend(list)
    return all_elements


def filter(function, list):
    filtered_elements = []
    for element in list:
        if function(element):
            filtered_elements.append(element)
    return filtered_elements


def length(list):
    count = 0
    for element in list:
        count += 1
    return count


def map(function, list):
    transformed_elements = []
    for element in list:
        result = function(element)
        transformed_elements.append(result)
    return transformed_elements


def foldl(function, list, initial):
    acc = initial
    for element in list:
        acc = function(acc, element)
    return acc


def foldr(function, list, initial):
    if len(list) == 0:
        return initial

    acc = list[0]
    for idx in range(1, len(list)):
        acc = function(acc, list[idx])
    return function(acc, initial)


def reverse(list):
    reversed_elements = []
    idx = len(list) - 1
    while idx >= 0:
        reversed_elements.append(list[idx])
        idx -= 1
    return reversed_elements
