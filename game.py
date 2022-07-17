from board import *
from time import time
from random import randint

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
        else:
            position = (len(currentBoard.position) - 1,y)
        
    currentBoard.insertLetter(player, position)
    return

def compMove():
    bestScore = -800
    bestMoves = []
    for y in range(len(currentBoard.position[0])):
        for x in range(len(currentBoard.position)):
            if (currentBoard.position[len(currentBoard.position) - 1 - x][y] == ' '):
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = bot
                score = minimax(currentBoard, 0, False)
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMoves = []
                    bestMoves.append((len(currentBoard.position) - 1 - x,y))
                elif (score == bestScore):
                    bestMoves.append((len(currentBoard.position) - 1 - x,y))
                break #break out of column

    bestMove = bestMoves[randint(0,len(bestMoves)-1)]
    print("Best Moves Yielded: " + str(score) + " Points")
    currentBoard.insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):

    if (board.checkWhichMarkWon(bot)):
        return 500 - depth
    elif (board.checkWhichMarkWon(player)):
        return -500 + depth
    elif (board.checkForDraw()):
        return 0

    elif depth == 4:
        score = board.getScore()
        if isMaximizing: #player just moved
            return -score
        else: #comp just moved
            return score

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

    