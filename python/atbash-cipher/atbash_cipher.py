_alphabet = 'abcdefghijklmnopqrstuvwxyz'
_reversed_alphabet = _alphabet[::-1]
_digits = '1234567890'


def encode(plain_text):
    reverse_letter_map = {}
    for idx, letter in enumerate(_alphabet):
        reverse_letter_map[letter] = _reversed_alphabet[idx]
        reverse_letter_map[letter.upper()] = _reversed_alphabet[idx]

    encoded_words = []
    encoded_text = ''
    for letter in plain_text:
        if letter.lower() in _alphabet:
            encoded_text += reverse_letter_map[letter]
        if letter in _digits:
            encoded_text += letter
        
        if len(encoded_text) == 5:
            encoded_words.append(encoded_text)
            encoded_text = ''
    encoded_words.append(encoded_text)

    return ' '.join(encoded_words).strip()


def decode(ciphered_text):
    return encode(ciphered_text).replace(' ', '')
