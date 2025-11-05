import re
import os

def readFromFile(filepath):
    
    # Regex for the Grid header line
    grid_pattern = r"^Grid\(\s*(\d+)\s*,\s*(\d+)\s*\)$"
    
    # Regex for coordinate lines like (0,1)
    coord_pattern = r"^\(\s*(\d+)\s*,\s*(\d+)\s*\)$"

    patternPath = os.path.join(os.path.dirname(__file__), "Patterns", filepath)
    if not os.path.exists(patternPath):
        raise FileNotFoundError("File does not exist!")

    output = []
    with open(patternPath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            # First line should be the Grid(...) line
            grid_match = re.match(grid_pattern, line)
            if grid_match:
                rows, cols = map(int, grid_match.groups())
                output.append((rows,cols))
                continue  # move to next line

            # Coordinate lines
            coord_match = re.match(coord_pattern, line)
            if coord_match:
                x, y = map(int, coord_match.groups())
                output.append((x, y))

    return output


def writeToFile():
    pass