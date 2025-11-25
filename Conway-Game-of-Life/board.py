from rules import rulesList, rules
import warnings

class Board:

    def __init__(self, row, col, inRule):

        self.row = row
        self.col = col
        self.inRule = inRule
        self.grid = []

        for _ in range(self.row):
            tmpRow = []
            for _ in range(self.col):
                tmpRow.append(0)
            self.grid.append(tmpRow)
    
    def updateCell (self, gridRow, gridCol, cell=1):


        # Checks if the cell is inside of grid
        if (0 <= gridRow < self.row and 0 <= gridCol < self.col):
            self.grid[gridRow][gridCol] = cell

        else:
            warnings.warn(f"Grid is out of bound and will be skipped.")


    def displayBoard(self):
        
        stringGrid =""

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                stringGrid += str(self.grid[i][j]) + " "
            stringGrid+= "\n"
            
        return stringGrid
    
    def nextGen(self):
        
        rule = rulesList[self.inRule]
        
        self.grid = rule(self.grid)
