def getNumEnergizedTiles(fileName):
    f = open(fileName, "r")
    grid = f.read().strip().split("\n")
    grid = [list(row) for row in grid]
    energizedTiles = traverse(grid)
    return len(energizedTiles) 


def traverse(grid):
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
    # start from top-left corner and head right
    currRow, currCol, currDir = 0, 0, "right"
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
                if isInBounds(nextRow, nextCol, grid):
                    stack.append((nextRow, nextCol, directionChange))      
    return seen
            
        
def isInBounds(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

print(getNumEnergizedTiles("input.txt"))