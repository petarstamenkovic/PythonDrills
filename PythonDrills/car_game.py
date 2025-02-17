# Simple pyhton drill with input and if branching

is_started = False

while True: 
    command = input("> ").lower()
    if command == 'help':
        print('''
start - starts a car 
stop - stops the car  
quit - quits the program
''')
    elif command == 'start':
        if is_started:
            print('Car is already turned on!')
        else:
            print('Car started, ready to go!')
            is_started = True
    elif command == 'stop':
        if not is_started:
            print('Car is already stopped!')
            is_started = False
        else:
            print('Car stopped.')
    elif command == 'quit':
        print('Goodbye!')
        break
    else: 
        print('I do not understand this command!')