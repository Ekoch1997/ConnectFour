

class Board():
    def __init__(self,currentPlayer,position):
        self.currentPlayer = currentPlayer
        self.position = position

    def printBoard(self):
        print("***********************************")
        for row in self.position:
            print(row)
        print("***********************************")

    def move(self,x,y):
        if self.position[x][y] != ' ':
            print("Illegal Move")
        
        self.position[x][y] = self.currentPlayer

    def checkForWin(self):
        
        #check across
        for row in self.position:
            for i in range(4):
                if row[0+i] == row[1+i] == row[2+i] == row[3+i] and row[0+i] != " ":
                    return True

        #check verical
        for i in range(len(self.position[0])):
            for j in range(3):
                if self.position[0+j][i] == self.position[1+j][i] == self.position[2+j][i] == self.position[3+j][i] and self.position[0+j][i] != " ":
                    return True

        #check down diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[0+j][0+i] == self.position[1+j][1+i] == self.position[2+j][2+i] == self.position[3+j][3+i] and self.position[0+j][0+i] != " ":
                    return True

        #check up diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[5-j][0+i] == self.position[4-j][1+i] == self.position[3-j][2+i] == self.position[2-j][3+i] and self.position[5-j][0+i] != " ":
                    return True
        
        return False

    def checkWhichMarkWon(self,mark):
        #check across
        for row in self.position:
            for i in range(4):
                if row[0+i] == row[1+i] == row[2+i] == row[3+i] and row[0+i] == mark:
                    return True

        #check verical
        for i in range(len(self.position[0])):
            for j in range(3):
                if self.position[0+j][i] == self.position[1+j][i] == self.position[2+j][i] == self.position[3+j][i] and self.position[0+j][i] == mark:
                    return True

        #check down diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[0+j][0+i] == self.position[1+j][1+i] == self.position[2+j][2+i] == self.position[3+j][3+i] and self.position[0+j][0+i] == mark:
                    return True

        #check up diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[5-j][0+i] == self.position[4-j][1+i] == self.position[3-j][2+i] == self.position[2-j][3+i] and self.position[5-j][0+i] == mark:
                    return True
        
        return False

    def checkForDraw(self):
        #check if spots available
        for row in self.position:
            for val in row:
                if val == " ":
                    return False
        return True

    def getScore(self):

        score = 0

        #Sum two in row
        #check across
        for row in self.position:
            for i in range(4):
                if row[0+i] != "O" and row[1+i] != "O" and row[2+i] != "O" and row[3+i] != "O": #Possible way to win for X
                    NumberInARow = 0
                    if row[0+i] == "X": NumberInARow += 1
                    if row[1+i] == "X": NumberInARow += 1
                    if row[2+i] == "X": NumberInARow += 1
                    if row[3+i] == "X": NumberInARow += 1
                    score += NumberInARow * NumberInARow

                if row[0+i] != "X" and row[1+i] != "X" and row[2+i] != "X" and row[3+i] != "X": #Possible way to win for O
                    NumberInARow = 0
                    if row[0+i] == "O": NumberInARow += 1
                    if row[1+i] == "O": NumberInARow += 1
                    if row[2+i] == "O": NumberInARow += 1
                    if row[3+i] == "O": NumberInARow += 1
                    score -= NumberInARow * NumberInARow

        #check verical
        for i in range(len(self.position[0])):
            for j in range(3):
                if self.position[0+j][i] != "O" and self.position[1+j][i] != "O" and self.position[2+j][i] != "O" and self.position[3+j][i] != "O":
                    NumberInARow = 0
                    if self.position[0+j][i] == "X": NumberInARow += 1
                    if self.position[1+j][i] == "X": NumberInARow += 1
                    if self.position[2+j][i] == "X": NumberInARow += 1
                    if self.position[3+j][i] == "X": NumberInARow += 1
                    score += NumberInARow * NumberInARow
                if self.position[0+j][i] != "X" and self.position[1+j][i] != "X" and self.position[2+j][i] != "X" and self.position[3+j][i] != "X":
                    NumberInARow = 0
                    if self.position[0+j][i] == "O": NumberInARow += 1
                    if self.position[1+j][i] == "O": NumberInARow += 1
                    if self.position[2+j][i] == "O": NumberInARow += 1
                    if self.position[3+j][i] == "O": NumberInARow += 1
                    score -= NumberInARow * NumberInARow

        #check down diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[0+j][0+i] != "O" and self.position[1+j][1+i] != "O" and self.position[2+j][2+i] != "O" and self.position[3+j][3+i] != "O":
                    NumberInARow = 0
                    if self.position[0+j][0+i] == "X": NumberInARow += 1
                    if self.position[1+j][1+i] == "X": NumberInARow += 1
                    if self.position[2+j][2+i] == "X": NumberInARow += 1
                    if self.position[3+j][3+i] == "X": NumberInARow += 1
                    score += NumberInARow * NumberInARow

        #check up diagonal
        for i in range(len(self.position[0])-3): #col
            for j in range(len(self.position)-3): #row
                if self.position[5-j][0+i] != "X" and self.position[4-j][1+i] != "X" and self.position[3-j][2+i] != "X" and self.position[2-j][3+i] != "X":
                    NumberInARow = 0
                    if self.position[5-j][0+i] == "O": NumberInARow += 1
                    if self.position[4-j][1+i] == "O": NumberInARow += 1
                    if self.position[3+j][2+i] == "O": NumberInARow += 1
                    if self.position[2+j][3+i] == "O": NumberInARow += 1
                    score -= NumberInARow * NumberInARow
        return score

            
    def spaceIsFree(self,x,y):
        if self.position[x][y] == ' ':
            return True
        else:
            return False
    
    def insertLetter(self,letter, position):
        x,y = position
        if self.spaceIsFree(x,y):
            self.position[x][y] = letter
            self.printBoard()
            if (self.checkForDraw()):
                print("Draw!")
                exit()
            if self.checkForWin():
                if letter == 'X':
                    print("Bot wins!")
                    exit()
                else:
                    print("Player wins!")
                    exit()

            return

        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            self.insertLetter(letter, position)
            return