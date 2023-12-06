import re 
def getNumWaysToWin(time, dist):
    numWaysToWin = 0
    for i in range(time):
        timeLeft = time - i
        distTraveled = i * timeLeft
        if distTraveled > dist:
            numWaysToWin += 1
    return numWaysToWin

def getTotalNumWaysToWin(fileName):
    f = open(fileName, "r")
    raceInfo = f.read().split("\n")
    times = re.findall("\d+", raceInfo[0])
    distances = re.findall("\d+", raceInfo[1])
    total = 1
    for i in range(len(times)):
        time, dist = int(times[i]), int(distances[i])
        total *= getNumWaysToWin(time, dist)
    return total

print(getTotalNumWaysToWin("input.txt"))