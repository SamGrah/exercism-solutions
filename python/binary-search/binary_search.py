def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while low <= high and len(search_list):
        mid = low + (high - low) // 2

        if search_list[mid] == value:
            return mid
        elif low == high:
            break

        if search_list[mid] < value:
            if low == mid: mid += 1
            low = mid
        else:
            high = mid

    raise ValueError("value not in array")
