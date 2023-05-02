def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    present_chars = set()
    for char in lowercase_sentence:
        if 'a' <= char <= 'z':
            present_chars.add(char)
    return len(present_chars) == 26
