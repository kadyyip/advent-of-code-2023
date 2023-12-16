def getMaxNumEnergizedTiles(fileName):
    f = open(fileName, "r")
    grid = f.read().strip().split("\n")
    grid = [list(row) for row in grid]
    maxTiles = 0
    for col in range(len(grid[0])):
        # start from top row and go down
        currTiles = getNumEnergizedTiles(grid, 0, col, "down")
        if currTiles > maxTiles:
            maxTiles = currTiles
        # start from bottom row and go up
        currTiles = getNumEnergizedTiles(grid, len(grid) - 1, col, "up")
        if currTiles > maxTiles:
            maxTiles = currTiles
    
    for row in range(len(grid)):
        # start from left col and go right
        currTiles = getNumEnergizedTiles(grid, row, 0, "right")
        if currTiles > maxTiles:
            maxTiles = currTiles
        # start from right col and go left
        currTiles = getNumEnergizedTiles(grid, row, len(grid[0]) - 1, "left")
        if currTiles > maxTiles:
            maxTiles = currTiles
    return maxTiles

def getNumEnergizedTiles(grid, startRow, startCol, startDir):
    energizedTiles = traverse(grid, startRow, startCol, startDir)
    return len(energizedTiles) 

def traverse(grid, startRow, startCol, startDir):
    directionChanges = {
        "|": {"right": ["up", "down"],
              "left": ["up", "down"],
              "up": ["up"],
              "down": ["down"]
              },
        "-": {"right": ["right"],
              "left": ["left"],
              "up": ["left", "right"],
              "down": ["left", "right"],
              },
        "\\": {"right": ["down"],
              "left": ["up"],
              "up": ["left"],
              "down": ["right"],
              },
        "/": {"right": ["up"],
              "left": ["down"],
              "up": ["right"],
              "down": ["left"],
              },
        ".": {"right": ["right"],
              "left": ["left"],
              "up": ["up"],
              "down": ["down"],
              }
    }

    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }

    currRow, currCol, currDir = startRow, startCol, startDir
    stack = [(currRow, currCol, currDir)]
    seenPosDir = set()
    seen = set()
    while len(stack) > 0:
        currRow, currCol, currDir = stack.pop()
        tile = grid[currRow][currCol]
        if (currRow, currCol, currDir) in seenPosDir:
            continue
        seen.add((currRow, currCol))
        seenPosDir.add((currRow, currCol, currDir))
        if tile in directionChanges:
            for directionChange in directionChanges[tile][currDir]:
                nextRow = currRow + directions[directionChange][0]
                nextCol = currCol + directions[directionChange][1]
                if inBounds(nextRow, nextCol, grid):
                    stack.append((nextRow, nextCol, directionChange))      
    return seen
            
        
def inBounds(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

print(getMaxNumEnergizedTiles("input.txt"))