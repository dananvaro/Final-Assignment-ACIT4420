from board import Board

newBoard = Board(3,3)

newBoard.updateCell(0,1,1)
newBoard.updateCell(1,1,1)
newBoard.updateCell(2,1,1)

for i in range(101):

    if(i == 0):
        print("OG grid: ")
    else:
        print("Gen",i)
        newBoard.nextGen()
    
    print(newBoard.displayBoard())
