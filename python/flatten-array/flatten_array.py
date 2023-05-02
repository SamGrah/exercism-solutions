def flatten(iterable):
    flattened_iterable = []
    for item in iterable:
        if type(item) is list:
            items = flatten(item)
            flattened_iterable = flattened_iterable + items
        elif item != None:
            flattened_iterable.append(item)

    return flattened_iterable
