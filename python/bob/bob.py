from distutils.command.clean import clean


def response(hey_bob):
    cleaned_msg = hey_bob.strip()
    if len(cleaned_msg) == 0:
        return 'Fine. Be that way!'

    is_question = cleaned_msg[-1] == "?"
    is_yell = cleaned_msg == cleaned_msg.upper()
    has_letter = cleaned_msg.islower() or cleaned_msg.isupper()

    if is_question and is_yell and has_letter:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return 'Sure.'
    if is_yell and has_letter:
        return 'Whoa, chill out!'
    return 'Whatever.'
