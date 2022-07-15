from board import *
from time import time

#Initialize Game
position = [
    [" ", " ", " "," ", " ", " "," "],
    [" ", " ", " "," ", " ", " "," "],
    [" ", " ", " "," ", " ", " "," "],
    [" ", " ", " "," ", " ", " "," "],
    [" ", " ", " "," ", " ", " "," "],
    [" ", " ", " "," ", " ", " "," "]
]

bot = "X"
player = "O"
currentBoard = Board(player,position)

def playerMove():
    y = int(input("Enter the column for 'O':  "))
    for x in range(len(currentBoard.position)):
        if (currentBoard.position[len(currentBoard.position) - 1 - x][y] == ' '):
            position = (len(currentBoard.position) - 1 - x,y)
            break
    currentBoard.insertLetter(player, position)
    return

def compMove():
    bestScore = -800
    bestMove = (-1,-1)
    for y in range(len(currentBoard.position[0])):
        for x in range(len(currentBoard.position)):
            if (currentBoard.position[len(currentBoard.position) - 1 - x][y] == ' '):
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = bot
                score = minimax(currentBoard, 0, False)
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = (len(currentBoard.position) - 1 - x,y)
                break #break out of column

    currentBoard.insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):

    if (board.checkWhichMarkWon(bot)):
        return 100
    elif (board.checkWhichMarkWon(player)):
        return -100
    elif (board.checkForDraw()):
        return 0

    elif depth == 4:
        score = board.getScore()
        if isMaximizing:
            return score
        else:
            return -score

    if (isMaximizing):
        bestScore = -800
        for y in range(len(board.position[0])):
            for x in range(len(board.position)):
                if (board.position[len(board.position) - 1 - x][y] == ' '):
                    board.position[len(currentBoard.position) - 1 - x][y] = bot
                    score = minimax(board, depth + 1, False)
                    board.position[len(currentBoard.position) - 1 - x][y] = ' '
                    if (score > bestScore):
                        bestScore = score
                    break #break out of column
        return bestScore

    else:
        bestScore = 800
        for y in range(len(board.position[0])):
            for x in range(len(board.position)):
                if (board.position[len(board.position) - 1 - x][y] == ' '):
                    board.position[len(currentBoard.position) - 1 - x][y] = player
                    score = minimax(board, depth + 1, True)
                    board.position[len(currentBoard.position) - 1 - x][y] = ' '
                    if (score < bestScore):
                        bestScore = score
                    break #break out of column
        return bestScore

while not currentBoard.checkForWin():
    starttime = time()
    compMove()
    print("Computer Move Time: " + str(time()-starttime) + " seconds")
    playerMove()

    