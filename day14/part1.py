def getTotalLoad(fileName):
    f = open(fileName, "r")
    platform = f.read().split("\n")
    platform = [list(line) for line in platform]
    total = 0
    numRows, numCols = len(platform), len(platform[0])
    for col in range(numCols):
        numRoundRocks = 0
        maxNorthWeight = numRows
        for row in range(numCols):
            currPos = platform[row][col]
            if currPos == "O":
                numRoundRocks += 1
            elif currPos == "#":
                total += addRockLoad(numRoundRocks, maxNorthWeight)
                maxNorthWeight = numCols - row - 1 # row under the cube rock
                numRoundRocks = 0
            if row == numRows - 1: # if reach the end, want to add what we have
                total += addRockLoad(numRoundRocks, maxNorthWeight)
    return total

def addRockLoad(numRoundRocks, maxNorthWeight):
    total = 0
    for numRowsFromNorth in range(numRoundRocks):
        load = maxNorthWeight - numRowsFromNorth
        total += load
    return total

print(getTotalLoad("input.txt"))
