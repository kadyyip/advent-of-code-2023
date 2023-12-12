def getSumShortestPaths(fileName):
    f = open(fileName, "r")
    grid = f.read().strip().split("\n")
    grid = [list(line) for line in grid]   
    expandUniverse(grid)
    galaxies = getGalaxies(grid)
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

def expandUniverse(grid):
    addRows = getRowsWithNoGalaxies(grid)
    addCols = getColsWithNoGalaxies(grid)
    for i in range(len(addRows)):
        insertInd = addRows[len(addRows) - 1 - i]
        grid.insert(insertInd, ["." for i in range(len(grid[0]))])
    for i in range(len(addCols)):
        insertInd = addCols[len(addCols) - 1 - i]
        for row in grid:
            row.insert(insertInd, ".")

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
