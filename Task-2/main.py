from board import Board
from io_handler import readFromFile

data = readFromFile("blinkerpattern.txt")
rows, cols = data[0]
liveBoard = data[1:]

newBoard = Board(rows, cols)

for row, col in liveBoard:
    newBoard.updateCell(row, col)

print("OG grid:")
print(newBoard.displayBoard())

for i in range(1, 5):
    newBoard.nextGen()
    print(f"Gen {i}")
    print(newBoard.displayBoard())
