from board import Board
from  io_handler import readFromFile

def main():
    row, col, aliveCells = readFromFile("beehivepattern.txt")

    newBoard = Board(row,col)

    for(gridX,gridY) in aliveCells:
        newBoard.updateCell(gridX,gridY)
    

    for genNumber in range(21):

        if(genNumber == 0):
            print("OG grid: ")
        else:
            print("Gen",genNumber)
            newBoard.nextGen()

        print(newBoard.displayBoard())



if __name__ == "__main__":
    main()