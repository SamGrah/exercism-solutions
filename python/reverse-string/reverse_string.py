def reverse(text):
    chars = list(text)
    idx1 = 0
    idx2 = len(chars) - 1

    while idx1 < idx2:
        chars[idx1], chars[idx2] = chars[idx2], chars[idx1]
        idx1 += 1
        idx2 -= 1

    return ''.join(chars)