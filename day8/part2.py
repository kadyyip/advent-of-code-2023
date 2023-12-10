import re
import math

def getSteps(fileName):
    f = open(fileName, "r")
    map = f.read().split("\n\n")
    instructions = map[0]
    network = map[1].strip().split("\n")
    networkDict = getNodeNetwork(network)
    currNodes = [node for node in networkDict.keys() if node[2] == "A"]
    currInd = 0
    numSteps = 0
    stepsToZ = dict()
    while True:
        numSteps += 1
        currInstruction = instructions[currInd]
        for i in range(len(currNodes)):
            currNode = currNodes[i]
            currNodes[i] = networkDict[currNode][currInstruction]
            if currNodes[i][2] == "Z":
                if currNode not in stepsToZ:
                    stepsToZ[currNode] = numSteps
        if len(stepsToZ) == len(currNodes):
            break
        if currInd == len(instructions) - 1: # need to repeat sequence
            currInd = 0
        else:
            currInd += 1
    return math.lcm(*stepsToZ.values())


def getNodeNetwork(network):
    networkDict = {}
    for line in network:
        nodes = re.findall("\w{3}", line)
        node = nodes[0]
        left = nodes[1]
        right = nodes[2]
        networkDict[node] = {"L": left, "R": right}
    return networkDict


print(getSteps("input.txt"))
