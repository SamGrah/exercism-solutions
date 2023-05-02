def transform(legacy_data):
    data = {}
    for key in legacy_data:
        for letter in legacy_data[key]:
            data[letter.lower()] = int(key)
    return data
