VERSES = [ "twelve Drummers Drumming, ", 
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, ",
            "and a Partridge in a Pear Tree."
        ]

DAYS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return [recite_one(start_verse)]

    verses = []
    for idx in range(start_verse, end_verse + 1):
        verses.append(recite_one(idx))
    return verses

def recite_one(from_verse):
    idx = from_verse - 1
    intro = f'On the {DAYS[idx]} day of Christmas my true love gave to me: '
    if from_verse == 1:
        return intro + 'a Partridge in a Pear Tree.'
    verses_to_sing = VERSES[len(VERSES) - idx - 1:]
    verses_to_sing = [intro] + verses_to_sing
    return ''.join(verses_to_sing)
