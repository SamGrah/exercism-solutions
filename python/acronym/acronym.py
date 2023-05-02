ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

def abbreviate(words):
    filtered_words = ''
    for char in words:
        if char == '-': 
           char = ' '
        if char.lower() in ALPHABET:
           filtered_words += char

    filtered_words_arr = filtered_words.split(' ')
    acroynm = ''
    for word in filtered_words_arr:
        acroynm += word[0].upper() if word else ''
    return acroynm
