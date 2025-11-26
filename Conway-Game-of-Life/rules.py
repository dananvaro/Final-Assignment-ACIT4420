
# List of rules
rulesList = {}

# Gives the rule name wanted
def rules(ruleName):
    # Puts the rule in rules list and returns the rule function
    def addRule(func):
        rulesList[ruleName] = func
        return func
    # Further return the wanted function
    return addRule

@rules("default")
def defaultRules(inGrid):

    # Save the row and column length
    arryRowLen = len(inGrid)
    arrColLen = len(inGrid[0])

    newGrid = []

    # Directions around the targeted cell
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

    # Create a new empty grid with the same size 
    for _ in range(arryRowLen):
        row =[]
        for _ in range(arrColLen):
            row.append(0)
        newGrid.append(row)

    # Loops through the given Grid
    for i in range(arryRowLen):
        for j in range(arrColLen):
            aliveNeiggbour = 0
            
            # Counts arround the cell to find alive cells
            for row, col in directions:
                ix = row + i
                jy = col + j

                # Checks if cells are inside of the grid
                if((0 <= ix < arryRowLen and 0 <= jy < arrColLen) and (inGrid[ix][jy] == 1)):
                    aliveNeiggbour+= 1

            # If cell has less than two or more that 3 alive neighbors it dies
            if((aliveNeiggbour < 2 or aliveNeiggbour > 3) and inGrid[i][j] == 1):
                newGrid[i][j] = 0
            
            # If a cell has exactly 3 alive neighours it becomes alive
            elif(aliveNeiggbour == 3 and inGrid[i][j] == 0):
                newGrid[i][j] = 1

            # If a cell has exaclty 2 or 3 alive cells it stays alive
            elif((aliveNeiggbour == 2 or aliveNeiggbour == 3) and inGrid[i][j]== 1):
                newGrid[i][j] = 1

    return newGrid