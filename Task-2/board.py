from rules import rulesList, rules

class Board:

    def __init__(self, row, col, inRule ="default"):

        ## add exception
        self.row = row
        self.col = col
        self.inRule = inRule
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

        rule = rulesList[self.inRule]
        
        self.grid = rule(self.grid)
