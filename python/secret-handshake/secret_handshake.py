def commands(binary_str):
    commands_list = [
       'Reverse the order of the operations in the secret handshake.',
       'jump',
       'close your eyes',
       'double blink',
       'wink'
    ]

    if binary_str[0] == '1':
        indices_order = range(1, 5)
    else:
        indices_order = range(4, 0, -1)

    commands = []
    for idx in indices_order:
        if binary_str[idx] == '1':
            commands.append(commands_list[idx])

    return commands
