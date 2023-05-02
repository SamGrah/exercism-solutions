def is_isogram(string):
    char_counts = {}

    for char in string.lower():
        if 'a' > char  or char > 'z':
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1:
            return False
    return True
