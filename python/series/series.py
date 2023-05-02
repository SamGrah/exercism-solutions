def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    all_slices = []
    start = 0
    end = length - 1
    while end < len(series):
        slice = series[start:end + 1]
        all_slices.append(slice)
        start += 1
        end += 1
    return all_slices
