BRACKETS_MATCH = {
    '(':')',
    '[':']',
    '{':'}'
}

LEFT_BRACKETS = BRACKETS_MATCH.keys()
RIGHT_BRACKETS = BRACKETS_MATCH.values()

def is_paired(input_string):
    brackets_only = ''
    for char in input_string:
        if char in LEFT_BRACKETS or char in RIGHT_BRACKETS:
            brackets_only += char

    idx = 0
    while idx < len(brackets_only) - 1:
        current_char = brackets_only[idx]
        next_char = brackets_only[idx + 1]
        if BRACKETS_MATCH.get(current_char, '') == next_char:
            brackets_only = brackets_only[:idx] + brackets_only[idx+2:]
            idx = 0
        else:
            idx += 1
    return True if len(brackets_only) == 0 else False
