from argparse import ArgumentParser, Namespace
from board import Board
from  io_handler import readFromFile, writeToFile

def main():

   

    



    row, col, aliveCells = readFromFile("beehivepattern.txt")

    newBoard = Board(row,col)

    for(gridX,gridY) in aliveCells:
        newBoard.updateCell(gridX,gridY)

    
    gens= 6
    

    for genNumber in range(gens):

        if(genNumber == 0):
            print("OG grid: ")
        else:
            print("Gen",genNumber)
            newBoard.nextGen()

        writeToFile(newBoard.displayBoard(),genNumber,gens, newBoard)

        print(newBoard.displayBoard())

if __name__ == "__main__":
    main()