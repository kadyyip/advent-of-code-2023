def getSumShortestPaths(fileName):
    f = open(fileName, "r")
    grid = f.read().strip().split("\n")
    grid = [list(line) for line in grid]   
    galaxies = getGalaxies(grid)
    expandUniverse(grid, galaxies)
    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i, len(galaxies)):
            galaxyRow1, galaxyCol1 = galaxies[i]
            galaxyRow2, galaxyCol2 = galaxies[j]
            sum += getShortestPath(galaxyRow1, galaxyCol1, galaxyRow2, galaxyCol2)
    return sum

def getGalaxies(grid):
    galaxies = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                galaxies.append([row, col])
    return galaxies

def getShortestPath(galaxyRow1, galaxyCol1, galaxyRow2, galaxyCol2):
    return abs(galaxyRow1 - galaxyRow2) + abs(galaxyCol1 - galaxyCol2)

def expandUniverse(grid, galaxies):
    addRows = getRowsWithNoGalaxies(grid)
    addCols = getColsWithNoGalaxies(grid)
    expandLength = 1000000 - 1 # subtract 1 for the existing row / col
    for galaxy in galaxies:
        rowsToAdd = 0
        colsToAdd = 0
        for row in addRows:
            if galaxy[0] > row:
                rowsToAdd += expandLength
        for col in addCols:
            if galaxy[1] > col:
                colsToAdd += expandLength
        galaxy[0] += rowsToAdd
        galaxy[1] += colsToAdd

def getRowsWithNoGalaxies(grid):
    rows = []
    for row in range(len(grid)):
        hasGalaxy = False
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                hasGalaxy = True
                break
        if not hasGalaxy:
            rows.append(row)
    return rows

def getColsWithNoGalaxies(grid):
    cols = []
    for col in range(len(grid[0])):
        hasGalaxy = False
        for row in range(len(grid)):
            if grid[row][col] == "#":
                hasGalaxy = True
                break
        if not hasGalaxy:
            cols.append(col)
    return cols

print(getSumShortestPaths("input.txt"))
