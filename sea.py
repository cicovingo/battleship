# sea class for battleships game
class Sea():
    # all of sea points to 0, size 5x5
    def __init__(self):
        self.seas = [[0 for x in range(5)] for y in range(5)]

        # initialize first ship at scenario tab on project document
        self.seas[1][3] = 1
        self.seas[2][3] = 1
        self.seas[3][3] = 1
        # initialize second ship at scenario tab on project document
        self.seas[0][0] = 1
        self.seas[0][1] = 1
        self.seas[0][2] = 1

    # add ship to sea
    def addShip(self, ship):
        # add vertical so increase y
        if ship.position_type == "v":
            # control for existing ship
            if self.seas[ship.position.x][ship.position.y] == 0 and self.seas[ship.position.x][
                ship.position.y + 1] == 0 and self.seas[ship.position.x][ship.position.y + 2] == 0:
                self.seas[ship.position.x][ship.position.y] = 1
                self.seas[ship.position.x][ship.position.y + 1] = 1
                self.seas[ship.position.x][ship.position.y + 2] = 1
                # if no exist ship return false
                return False
            else:
                # if exist ship return true
                return True
        # add vertical so increase x
        elif ship.position_type == "h":
            if self.seas[ship.position.x][ship.position.y] == 0 and self.seas[ship.position.x + 1][
                ship.position.y] == 0 and self.seas[ship.position.x + 2][ship.position.y] == 0:
                self.seas[ship.position.x][ship.position.y] = 1
                self.seas[ship.position.x + 1][ship.position.y] = 1
                self.seas[ship.position.x + 2][ship.position.y] = 1
                # if no exist ship return false
                return False
            else:
                # if exist ship return true
                return True

    # show all ships on the sea
    def showShips(self):
        print("Ships at sea:\n")
        for i in range(5):
            for j in range(5):
                print(self.seas[i][j], end=' ')
            print("\n")