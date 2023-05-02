ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    rotated_letters_map = {}
    for idx in range(0, 26):
       letter = ALPHABET[idx]
       rotated_idx = (idx + key) % 26
       rotated_letters_map[letter] = ALPHABET[rotated_idx]

    rotated_text = ''
    for text_letter in text:
        lower_letter = text_letter.lower()
        rotated_letter = rotated_letters_map.get(lower_letter, text_letter)
        if text_letter.isupper():
            rotated_letter = rotated_letter.upper()
        rotated_text += rotated_letter
    return rotated_text
