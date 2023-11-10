import random
x = 0
while x < 10:
    x += 1
    door = ["goat","goat","car"]


    choice = input("Door 1, 2 or 3? ")
    otherDoor = 0
    goatDoor = 0

    random.shuffle(door)

    if choice == "1":
        if door[1] == "goat":
            otherDoor = 3 
            goatDoor = 2
        elif door[2] == "goat":
            otherDoor = 2
            goatDoor = 3  
    elif choice == "2":
        if door[0] == "goat":
            otherDoor = 3
            goatDoor = 1
        elif door[2] == "goat":
            otherDoor = 1
            goatDoor = 3
    elif choice == "3":
        if door[0] == "goat":
            otherDoor = 2
            goatDoor = 1
        elif door[1] == "goat":
            otherDoor = 1
            goatDoor = 2


    switch = input("There is a goat behind door " + str(goatDoor) +
                " switch to door " + str(otherDoor) + "? (y/n) ")

    if switch == "y":
        choice = otherDoor

    if door[int(choice)-1] == "car":
        print("You won a car!")
    else:
        print("You won a goat!")

input("Press enter to exit.")