import os
from argparse import ArgumentParser, Namespace
from board import Board
from  io_handler import readFromFile, writeToFile

import warnings

warnings.simplefilter("always")
warnings.formatwarning = lambda message, category, filename, lineno, file: f"{category.__name__}: {message}\n"

def main():

    # Takes in command lines inputs from the user
    parser = ArgumentParser()

    parser.add_argument('--patternfile', required=True, help="Pattern file name with .txt", type=str)
    parser.add_argument('--generations',required=True, help="Number of generations", type= int)
    parser.add_argument('--ruleset',default="default", help="Choose a ruleset or default will be chosen",type=str)

    args: Namespace = parser.parse_args()

    # Assigns the patternname, generations and rule from the user to values
    pattern = args.patternfile
    amountOfGeneration = args.generations + 1
    rule = args.ruleset

    # Reads row, col and amout of alive cells from a file 
    
    #    Format: 
    #    Grid(3,3) # Grid size 
    #    (0,1) # Alive cells
    #    (1,1)
    #    (2,1)
    
    row, col, aliveCells = readFromFile(pattern)

    # Creates a Board object 
    newBoard = Board(row,col,rule)

    for(gridX,gridY) in aliveCells:
        newBoard.updateCell(gridX,gridY)

    for genNumber in range(amountOfGeneration):

        if(genNumber == 0):
            #print("OG grid: ")
            pass
        else:
            #print("Gen",genNumber)
            newBoard.nextGen()

        writeToFile(newBoard.displayBoard(),genNumber,amountOfGeneration, newBoard)

        #print(newBoard.displayBoard())

if __name__ == "__main__":
    main()