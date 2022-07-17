from board import *
from time import time
from random import randint
import math

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

    while 'position' not in locals():
        y = int(input("Enter the column for 'O':  "))
        if y >= 0 and y < len(currentBoard.position[0]):
            for x in range(len(currentBoard.position)):
                if (currentBoard.position[len(currentBoard.position) - 1 - x][y] == ' '):
                    position = (len(currentBoard.position) - 1 - x,y)
                    break
            
                if len(currentBoard.position) - 1 - x == 0:
                    print("No more spots available, please choose another column")

        else:
            print("Invalid Entry, please enter a number")
        
    currentBoard.insertLetter(player, position)
    return

def compMove():
    bestScore = -800
    bestMoves = []
    for y in range(len(currentBoard.position[0])):
        for x in range(len(currentBoard.position)):
            if (currentBoard.position[len(currentBoard.position) - 1 - x][y] == ' '):
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = bot
                score = minimax(currentBoard, 0, -math.inf, math.inf, False)
                currentBoard.position[len(currentBoard.position) - 1 - x][y] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMoves = []
                    bestMoves.append((len(currentBoard.position) - 1 - x,y))
                elif (score == bestScore):
                    bestMoves.append((len(currentBoard.position) - 1 - x,y))
                break #break out of column

    bestMove = bestMoves[randint(0,len(bestMoves)-1)]
    print("Best Move Yielded: " + str(bestScore) + " Points")
    currentBoard.insertLetter(bot, bestMove)
    return

def minimax(board, depth, alpha, beta, isMaximizing):

    if (board.checkWhichMarkWon(bot)):
        return 500 - depth
    elif (board.checkWhichMarkWon(player)):
        return -500 + depth
    elif (board.checkForDraw()):
        return 0

    elif depth == 6:
        score = board.getScore()
        if isMaximizing: #player just moved
            return score
        else: #comp just moved
            return -score

    if (isMaximizing):
        bestScore = -math.inf
        for y in range(len(board.position[0])):
            for x in range(len(board.position)):
                if (board.position[len(board.position) - 1 - x][y] == ' '):
                    board.position[len(currentBoard.position) - 1 - x][y] = bot
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board.position[len(currentBoard.position) - 1 - x][y] = ' '
                    if (score > bestScore):
                        bestScore = score
                    if bestScore >= beta:
                        return bestScore
                    alpha = max(alpha, bestScore)

                    break #break out of column
        return bestScore

    else:
        bestScore = math.inf
        for y in range(len(board.position[0])):
            for x in range(len(board.position)):
                if (board.position[len(board.position) - 1 - x][y] == ' '):
                    board.position[len(currentBoard.position) - 1 - x][y] = player
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board.position[len(currentBoard.position) - 1 - x][y] = ' '
                    if (score < bestScore):
                        bestScore = score
                    if bestScore <= alpha:
                        return bestScore
                    beta = min(beta, bestScore)

                    break #break out of column
        return bestScore

while not currentBoard.checkForWin():
    starttime = time()
    compMove()
    print("Computer Move Time: " + str(time()-starttime) + " seconds")
    
    playerMove()

    