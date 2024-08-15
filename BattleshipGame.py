class Player:

    def __init__(self, name):
        self.name = name;

    def __str__(self):
        return self.name;

class Ship:

    def __init__(self):
        self.ships = {"cruiser" : 2, "destructor" : 3, "aircraftCarrier" : 5}


class InputHandler:

    def orientationCheck(self, index, column, row, tiles):
        g = Game();
        board = g.board;
        while True:
            try:
                i = input("Vertical (v) / Horizontal (h): ").lower() 
                if i == "v":
                    iter = 0;
                    while iter < tiles:
                        board[index][column + iter][row] = 1
                        iter += 1;
                    break;
            
                elif i == "h":
                    iter = 0;
                    while iter < tiles:
                        board[index][column][row + iter] = 1
                        iter += 1;
                    break;
        
                else:
                    print("Invalid orientation input [h - v], Try again... ")

            except Exception:
                return "outOfBounds";

        return board[index];

    def coordinatesCheck(self):
        columns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9 }
        while True:
            columnInput = input("Enter column [A - J]: ").lower()
            if columnInput in columns:
                rowInput = int(input("Enter row [0 - 9]: ").lower())
                if rowInput in range(10):
                    break;
                else:
                    print("Row not in range [0 - 9], Try again")
            else:
                print("COLUMN not in range [A - J], Try again...")

        return list((columns[columnInput], rowInput));

class Game:
    def __init__(self):
        self.board = [[[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]], 

                    [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]]
        
    def setBoard(self, index, orientedBoard, shipInitial):
        for i, column in enumerate(orientedBoard):
            for ii, j in enumerate(column):
                if j == 1:
                    if isinstance(self.board[index][i][ii], str):
                        return True;
                    else:
                        self.board[index][i][ii] = shipInitial
    
    def getBoard(self):
        for layer in self.board:
            for row in layer:
                print(row)
            print();

    def registry(self):
        print("Welcome to Battleship!")
        self.p1 = Player(input("Player One nickname: "))
        self.p2 = Player(input("Player Two nickname: "))
        if self.p1.name == self.p2.name:
            self.p1.name += "_A"
            self.p2.name += "_B"

        print(f"...{self.p1.name} VS {self.p2.name}...")

    def shipSetUp(self):
        players = [self.p1.name, self.p2.name];
        iH = InputHandler();
        s = Ship();

        for index, p in enumerate(players):

            #Destructor
            while True:
                print(f"{p} Enter Destructor coordinates (3 tiles): ")
                destructorStartingTile = iH.coordinatesCheck();
                orientedBoard = iH.orientationCheck(index, destructorStartingTile[0], destructorStartingTile[1], s.ships["destructor"])
                if orientedBoard == "outOfBounds":
                    print("Invalid location, Try again...")
                else:
                    self.setBoard(index, orientedBoard, "D")
                    break;
            
            # Cruiser
            while True:
                print(f"{p} Enter Cruiser starting coordinates (2 tiles): ")
                cruiserStartingTile = iH.coordinatesCheck();
                orientedBoard = iH.orientationCheck(index, cruiserStartingTile[0], cruiserStartingTile[1], s.ships["cruiser"])
                if orientedBoard == "outOfBounds":
                    print("Invalid location, Try again...")
                else:
                    break;

            #Collision check
            if self.setBoard(index, orientedBoard, "C"):
                while True:
                    print("Ship Collision, Try another coordinates: ")
                    cruiserStartingTile = iH.coordinatesCheck();
                    orientedBoard = iH.orientationCheck(index, cruiserStartingTile[0], cruiserStartingTile[1], s.ships["cruiser"])
                    if self.setBoard(index, orientedBoard, "C") != True:
                        break;

            #AircrafCarrier
            while True:
                print(f"{p} Enter Aircraft Carrier starting coordinates (5 tiles): ")
                aircraftCarrierStartingTile = iH.coordinatesCheck();
                orientedBoard = iH.orientationCheck(index, aircraftCarrierStartingTile[0], aircraftCarrierStartingTile[1], s.ships["aircraftCarrier"])
                if orientedBoard == "outOfBounds":
                    print("Invalid location, Try again...")
                else:
                    break;

            #Collision check
            if self.setBoard(index, orientedBoard, "AC"):
                while True:
                    print("Ship Collision, Try another coordinates: ")
                    aircraftCarrierStartingTile = iH.coordinatesCheck();
                    orientedBoard = iH.orientationCheck(index, aircraftCarrierStartingTile[0], aircraftCarrierStartingTile[1], s.ships["aircraftCarrier"])
                    if self.setBoard(index, orientedBoard, "AC") != True:
                        break;
        
        print("--- Board Status ---")
        self.getBoard();

#Game start:
g = Game();
g.registry();
g.shipSetUp();

