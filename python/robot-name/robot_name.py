from random import randint

CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
generated_names = set()

def generate_new_name():
    name = ''
    while len(name) != 5:
        new_char = str(randint(0, 9))
        if len(name) < 2:
            char_idx = randint(0, len(CHARACTERS) - 1)
            new_char = CHARACTERS[char_idx]
        name += new_char

        if len(name) == 5 and name in generated_names:
            name = ''

    generated_names.add(name)
    return name

        
class Robot:
    def __init__(self):
        self.name = generate_new_name()


    def reset(self):
       self.__init__()
