command = ""
started = False
while True:
    command  = input('>').lower()
    if command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('Car is started')
    elif command == 'stop':
        if not started:
         print('car is already stopped')
        else:
            started = False
            print('Car stopped') 
    elif command == 'help':
        print('''
Start = To start the car
Stop = To stop the car 
Quit = To quit the game''')
    elif command == 'quit':
       break
    else:
        print('Enter the right command')