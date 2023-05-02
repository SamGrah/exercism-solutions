ALLOWED_CHARS = "1234567890abcdefghijklmnopqrstuvwxyz'" 
def count_words(sentence):
    filtered_word = '' 
    word_count = {}
    for char in sentence.lower():
        if char in ALLOWED_CHARS:
            filtered_word += char 
        elif filtered_word != '':
            cleaned_word = filtered_word.strip("'")
            if filtered_word != '':
                word_count.setdefault(cleaned_word, 0)
                word_count[cleaned_word] += 1
            filtered_word = ''
    if filtered_word != '':
        cleaned_word = filtered_word.strip("'")
        if filtered_word != '':
            word_count.setdefault(cleaned_word, 0)
            word_count[cleaned_word] += 1
    return word_count
