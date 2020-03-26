from sea import Sea
from ship import Ship
from command import Command

print("Welcome to BattleShips Game!\n")
print("Commands information:\n")
print(
    "place: place ship to sea. example place v,1,3\nshow ships: show ships on the sea.\nexit battleships: exit the game\n")

# create commands for battleships game
commands = Command()

# create sea size of 5x5
seaOfGame = Sea()

isFinished = False

# loop continue when isFinished equal to false
while isFinished == False:
    command = input()
    # show ships command for show all ships on the sea
    if command == commands.command[0]:
        seaOfGame.showShips()
    # exit battleships command for exit game
    elif command == commands.command[1]:
        isFinished = True
    # size 2 for split " ", and size 3 for split of first split's for "," example that place v,1,3
    elif len(command.split(" ")) == 2 and len(command.split(" ")[1].split(",")) == 3:
        # first element command name
        commandName = command.split(" ")[0]
        # second element position type
        commandPlacePositionType = command.split(" ")[1].split(",")[0]
        # third element start poisiton x
        startPositionX = command.split(" ")[1].split(",")[1]
        # last element start poisiton y
        startPositionY = command.split(" ")[1].split(",")[2]

        # control first element place
        if commandName == commands.command[2]:
            # control second element v:vertical or horizontal
            if commandPlacePositionType == "v" or commandPlacePositionType == "h":
                # control for x and y coordinates true like 0,1,2,3,4, not 00,01 etc..
                if len(startPositionX) == 1 and len(startPositionY) == 1:
                    # control for x and y coordinates true size (5x5)
                    if int(startPositionX) < 5 or int(startPositionY) < 5:
                        # create a ship
                        shipOnSea = Ship(commandPlacePositionType, int(startPositionX), int(startPositionY))
                        # add ship to sea
                        existShip = seaOfGame.addShip(shipOnSea)
                        if existShip == True:
                            print("Ship is not placed! Because there is a ship these coordinates.\n")
                    else:
                        print("Ship is not placed! At least one position for this ship is invalid.\n")
                else:
                    print("Ship is not placed! At least one position for this ship is invalid.\n")
            else:
                print("Ship is not placed! Please write true position type h:horizontal, v:vertical\n")
        else:
            print("Please write true command!!!\n")
    else:
        print("Please write true command!!!\n")