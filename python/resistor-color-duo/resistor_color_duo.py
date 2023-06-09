color_codes = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}

def value(colors):
    tens_color = color_codes[colors[0]]
    ones_color = color_codes[colors[1]]
    return int(tens_color + ones_color)
