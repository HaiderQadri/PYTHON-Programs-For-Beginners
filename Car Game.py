condition = ""
started = False
while True:
    condition = input("> ").lower()
    if condition == "start":
        if started:
            print("Hey, Car is already started")
        else:
            started = True
        print("Car is started...")
    elif condition == "stop":
        if not started:
           print("Car is already stopped!")
        else:
            started = True
            print("Car stopped...")
    elif condition == "help":
        print('''
              start - to start the car
              stop - to stop the car
              quit - to quit
              ''')
    elif condition == "quit":
        break
    else:
        print("Sorry I don't understand that!")

