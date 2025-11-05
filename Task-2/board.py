from rules import rules

class Board:

    def __init__(self, row, col):

        ## add exception
        self.row = row
        self.col = col
        self.grid = []

        for _ in range(self.row):
            tmpRow = []
            for _ in range(self.col):
                tmpRow.append(0)
            self.grid.append(tmpRow)
    
    def updateCell (self, row, col, cell=1):

        ## add exception
        self.grid[row][col] = cell

    def displayBoard(self):
        
        stringGrid =""

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                stringGrid += str(self.grid[i][j]) + " "
            stringGrid+= "\n"
            
        return stringGrid
    
    def nextGen(self):
        self.grid = rules(self.grid)
