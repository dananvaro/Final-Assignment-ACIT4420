from rules import rulesList, rules
import warnings, time

class Board:

    def __init__(self, row, col, inRule):

        self.row = row
        self.col = col
        self.inRule = inRule
        self.grid = []

        # Creates an empty grid with the same grid size
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
            warnings.warn(f"Cell is out of bound: {(gridRow,gridCol)}")
            time.sleep(1)


    def displayBoard(self):
        

        stringGrid =""

        # Converts the grid into a string so it is easier to write to file
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                stringGrid += str(self.grid[i][j]) + " "
            stringGrid+= "\n"
            
        return stringGrid
    
    def nextGen(self):
        
        
        # Checks if rule is valid if it it it calls the rule and updates it to the new grid
        if (self.inRule) not in rulesList:
            raise ValueError(f"Rule {self.inRule} not found in rule list")

        rule = rulesList[self.inRule]
        
        self.grid = rule(self.grid)
