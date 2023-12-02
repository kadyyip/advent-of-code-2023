import re

def lessThanMaxColor(game, color, maxCubes):
    cubes = re.findall(f"(\d*) {color}", game)
    for numCubes in cubes:
        if int(numCubes) > maxCubes:
            return False
    return True

def isPossibleGame(game):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    return (lessThanMaxColor(game, "red", maxRed) and
            lessThanMaxColor(game, "green", maxGreen) and 
            lessThanMaxColor(game, "blue", maxBlue))

def sumPossibleGameIds(fileName):
    sum = 0
    f = open(fileName, "r")
    for game in f:
        if isPossibleGame(game):
            gameId = re.findall("Game (\d*)", game)
            sum += int(gameId[0])
    return sum


print(sumPossibleGameIds("input.txt"))