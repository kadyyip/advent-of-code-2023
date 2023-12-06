import re 
def getNumWaysToWin(fileName):
    f = open(fileName, "r")
    raceInfo = f.read().split("\n")
    time = "".join(re.findall("\d+", raceInfo[0]))
    distance = "".join(re.findall("\d+", raceInfo[1]))
    time, dist = int(time), int(distance)
    numWaysToWin = 0
    for i in range(time):
        timeLeft = time - i
        distTraveled = i * timeLeft
        if distTraveled > dist:
            numWaysToWin += 1
    return numWaysToWin

print(getNumWaysToWin("input.txt"))