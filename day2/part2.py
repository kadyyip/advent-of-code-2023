import re

def getMaxNumCubesOfGame(color, game):
    cubes = re.findall(f"(\d*) {color}", game)
    max = float("-inf")
    for numCubes in cubes:
        if int(numCubes) > max:
            max = int(numCubes)
    return max

def getPowerOfSet(game):
    # fewest num of cubes for possible game = max num of cubes in game
    minRed = getMaxNumCubesOfGame("red", game)
    minGreen = getMaxNumCubesOfGame("green", game)
    minBlue = getMaxNumCubesOfGame("blue", game)
    return minRed * minGreen * minBlue

def sumPowerOfSets(fileName):
    sum = 0
    f = open(fileName, "r")
    for game in f:
        power = getPowerOfSet(game)
        sum += power
    return sum


print(sumPowerOfSets("input.txt"))