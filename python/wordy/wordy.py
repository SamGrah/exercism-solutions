operators = ['plus', 'minus', 'multiplied', 'divided']

def answer(question):
    words = question.split(' ')
    words[-1] = words[-1][:-1]
    
    sum = None 
    idx = 3
    num_operators = 0
    while idx < len(words):
        operation = words[idx]
        if operation not in operators:
            raise ValueError('unknown operation')
       
        num_operators += 1 
        try:
            if not sum:
                sum = int(words[idx - 1])
            sum = int(words[idx + 1])
        except:
            raise ValueError('syntax error')
        
        idx += 2 

    if num_operators == 0:
        raise ValueError('syntax error')
    if len(words) != 3 + num_operators * 2:
        raise ValueError('syntax error')