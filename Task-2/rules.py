


# Survival: A live cell with two or three live neighbors lives on to the next generation.
# Death by underpopulation: A live cell with fewer than two live neighbors dies.
# Death by overpopulation: A live cell with more than three live neighbors dies.
# Birth: A dead cell with exactly three live neighbors becomes a live cell in the next generation.

def rules(inGrid):

    # Save the row and column length
    arryRowLen = len(inGrid)
    arrColLen = len(inGrid[0])

    newGrid = []

    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

    # Create a new empty grid with the same size 
    for _ in range(arryRowLen):
        row =[]
        for _ in range(arrColLen):
            row.append(0)
        newGrid.append(row)

    for i in range(arryRowLen):
        for j in range(arrColLen):
            aliveNeigbour = 0
            
            # Counts arround the cell to find alive cells
            for row, col in directions:
                ix = row + i
                jy = col + j

                if((0 <= ix < arryRowLen and 0 <= jy < arrColLen) and (inGrid[ix][jy] == 1)):
                    aliveNeigbour+= 1

            # Death by underpopulation: A live cell with fewer than two live neighbors dies.
            # Death by overpopulation: A live cell with more than three live neighbors dies.
            if((aliveNeigbour < 2 or aliveNeigbour > 3) and inGrid[i][j] == 1):
                newGrid[i][j] = 0
            
            # Birth: A dead cell with exactly three live neighbors becomes a live cell in the next generation.
            elif(aliveNeigbour == 3 and inGrid[i][j] == 0):
                newGrid[i][j] = 1

            # Survival: A live cell with two or three live neighbors lives on to the next generation.
            elif((aliveNeigbour == 2 or aliveNeigbour == 3) and inGrid[i][j]== 1):
                newGrid[i][j] = 1

    return newGrid
    
        





testGrid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

for _ in range(25):
    newGrid = rules(testGrid)

    for row in newGrid: 
        print(row)

    print("---------")
    testGrid = newGrid