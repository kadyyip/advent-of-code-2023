def getStepsToFarthesetPoint(fileName):
    f = open(fileName, "r")
    grid = f.read().split("\n")
    grid = [list(line) for line in grid]
    loop = findLoop(grid)
    return len(loop) // 2
    

def findLoop(grid):
    startRow, startCol = findStartPosition(grid)
    validMoves = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)], 
        "L": [(0, 1), (-1, 0)], 
        "J": [(-1, 0), (0, -1)], 
        "7": [(1, 0), (0, -1)], 
        "F": [(1, 0), (0, 1)], 
        "S": [(1, 0), (0, 1), (-1, 0), (0, -1)]
    }
    validConnectors = {
        (-1, 0): {"|", "7", "F"},
        (1, 0): {"|", "L", "J"},
        (0, -1): {"-", "L", "F"},
        (0, 1): {"-", "J", "7"}
    }

    seen = set()
    stack = [(startRow, startCol)]
    while len(stack) != 0:
        currRow, currCol = stack.pop()
        if (currRow, currCol) in seen:
            if (currRow, currCol) == (startRow, startCol):
                return seen
            continue
        seen.add((currRow, currCol))
        currTile = grid[currRow][currCol]
        if currTile != ".":
            for validMove in validMoves[currTile]:
                nextRow = currRow + validMove[0]
                nextCol = currCol + validMove[1]
                if isInBounds(grid, nextRow, nextCol):
                    nextTile = grid[nextRow][nextCol]
                    if nextTile in validConnectors[validMove]:
                        stack.append((nextRow, nextCol))
    return seen

def isInBounds(grid, row, col):
    return (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0]))

def findStartPosition(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                return (row, col)


print(getStepsToFarthesetPoint("input.txt"))