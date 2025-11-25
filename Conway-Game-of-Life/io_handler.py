import re, warnings, os, time
from board import Board


def readFromFile(filepath):

    # Intial values that are returned
    row = None
    col = None
    aliveCells = []

    # Used for validation in the format Grid(x,y) and alive cells (a,b)
    rowColRegex = re.compile(r'^Grid\((-?\d+),(-?\d+)\)$')
    aliveCellsRegex = re.compile(r'^\((-?\d+),(-?\d+)\)$')

    # Used to group and extract the values that are poistive
    extractRowCol = re.compile(r'Grid\((\d+),\s*(\d+)\)')
    extractAliveCells = re.compile(r'\((\d+),\s*(\d+)\)')

    patternPath = os.path.join(os.path.dirname(__file__),"Patterns", filepath)

    # Error handling for file name
    if (not os.path.exists(patternPath)):
        raise FileExistsError("File does not exist")

    with open(patternPath) as f:
        for line in f:

            # Used for formatting as it remove whitespace and \n
            line = line.strip()
            
            # Checks if the format is correct
            if(re.match(rowColRegex, line)):
                
                # Extract the values based on regex
                matchRowCol = extractRowCol.search(line)

                # If nothing is extracted it it hold the value None which is False
                if matchRowCol:
                    
                    # Assigns the row and col to the gourped objects
                    # Using map we can convert string into integers
                    row, col = map(int, matchRowCol.groups())    

                else: 
                    raise ValueError(f"Grid size cannot be: {line}")
                    
                

            elif(re.match(aliveCellsRegex, line)):

                matchAliveCells = extractAliveCells.search(line)

                if matchAliveCells:
                    x, y = map(int,matchAliveCells.groups())

                    # Appends it to a list of alive cells
                    aliveCells.append((x,y))
                else:
                    warnings.warn(f"Line cannot be of type None: {line}, line will be skipped.", category=UserWarning)
                    time.sleep(1)

            else:

                warnings.warn(f"Invalid line deteced: {line}, line will be skipped.", category=UserWarning)
                time.sleep(1)

    # If row/col is None there was an failed stage. If there are no alive cells the program stops
    if((row or col) == None) or (len(aliveCells) == 0):
        raise ValueError (f"Print row, col or amount of cells are invalid: row: {row}, col: {col} and alive cells: {aliveCells}")

    return row, col, aliveCells

def writeToFile(input, genNumber,genAmount, inBoard):


    # Gets the objects row and col
    row = inBoard.row
    col = inBoard.col

    # Appends to the state_snapshots text file
    patternPath = os.path.join(os.path.dirname(__file__),"data", "state_snapshots.txt")
    with open(patternPath, "a+") as f:

        # Appends the intial pattern to the file
        if(genNumber == 0):

            tmp = f"Conway Game of life snapshots"

            f.write(tmp + f"\nGrid {row} x {col}\n")

            f.write(lineSpace(tmp) + "\n")

            tmp = f"Initial Generation"
            
            f.write(tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")


        # Writes the final stage tot the file
        elif(genNumber == genAmount-1):

            tmp = f"Simulation ended with Gen: {genNumber}"
            f.write( tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")

        # Writes the new patterns to the file
        else:
            
            tmp =f"Generation: {genNumber}"
            f.write(tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")

# Style formatting for the file
def lineSpace(string):

    stringOut = ""

    for _ in range(len(string)):
        stringOut += "-"

    return stringOut