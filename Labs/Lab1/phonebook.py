dict = {}
while True:
    command = input()
    command = command.split()
    if (command[0] == 'quit'):
        exit()
    elif (command[0] == 'add'):
        dict[command[1]] = int(command[2])
    elif (command[0] == 'remove'):
        if command[1] in dict:
            dict.pop(command[1])
    elif (command[0] == 'edit'):
        if command[1] in dict:
            dict[command[1]] = int(command[2])
    print(dict)
