import os
from argparse import ArgumentParser, Namespace
from board import Board
from  io_handler import readFromFile, writeToFile

def main():

    parser = ArgumentParser()

    parser.add_argument('--filename', required=True, help="Pattern file name", type=str)
    parser.add_argument('--generations',required=True, help="Number of generation", type= int)

    args: Namespace = parser.parse_args()

    pattern = args.filename

    amountOfGeneration = args.generations + 1

    print(pattern)
    print(amountOfGeneration)

    row, col, aliveCells = readFromFile(pattern)

    newBoard = Board(row,col)

    for(gridX,gridY) in aliveCells:
        newBoard.updateCell(gridX,gridY)

    for genNumber in range(amountOfGeneration):

        if(genNumber == 0):
            print("OG grid: ")
        else:
            print("Gen",genNumber)
            newBoard.nextGen()

        writeToFile(newBoard.displayBoard(),genNumber,amountOfGeneration, newBoard)

        print(newBoard.displayBoard())

if __name__ == "__main__":
    main()