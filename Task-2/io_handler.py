import re
import os
import warnings
from board import Board


def readFromFile(filepath):

    row = None
    col = None
    aliveCells = []

    rowColRegex = re.compile(r'^Grid\((-?\d+),(-?\d+)\)$')
    aliveCellsRegex = re.compile(r'^\((-?\d+),(-?\d+)\)$')

    extractRowCol = re.compile(r'Grid\((\d+),\s*(\d+)\)')
    extractAliveCells = re.compile(r'\((\d+),\s*(\d+)\)')

    patternPath = os.path.join(os.path.dirname(__file__),"Patterns", filepath)
    if (not os.path.exists(patternPath)):
        raise FileExistsError("File does not exist!")

    with open(patternPath) as f:
        for line in f:
            if(re.match(rowColRegex, line)):
                if((row or col) is not None):
                    #warning
                    continue
                
                matchRowCol = extractRowCol.search(line)
                row, col = map(int, matchRowCol.groups())


            elif(re.match(aliveCellsRegex, line)):

                matchAliveCells = extractAliveCells.search(line)
                x, y = map(int,matchAliveCells.groups())

                aliveCells.append((x,y))

            else:

                #warning
                print("Feil ass")

    if((row or col) == None) or (len(aliveCells) == 0):

        # raise here
        print("Tarek Lein!")

    return row, col, aliveCells

def writeToFile(input, genNumber,genAmount, inBoard):
    
    row = inBoard.row
    col = inBoard.col

    if(input == None):
        #Raise here
        pass

    patternPath = os.path.join(os.path.dirname(__file__),"log", "state_snapshots.txt")
    with open(patternPath, "a+") as f:

        if(genNumber == 0):

            tmp = f"Conway Game of life snapshots"

            f.write(tmp + f"\nGrid {row} x {col}\n")

            f.write(lineSpace(tmp) + "\n")

            tmp = f"Initial Generation"
            
            f.write(tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")
        
        elif(genNumber == genAmount-1):

            tmp = f"Simulation ended with Gen: {genNumber}"
            f.write( tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")

        else:
            
            tmp =f"Generation: {genNumber}"
            f.write(tmp + f"\n{input}")
            f.write(lineSpace(tmp)+ "\n")


def lineSpace(string):

    stringOut = ""

    for _ in range(len(string)):
        stringOut += "-"

    return stringOut