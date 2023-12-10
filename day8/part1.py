import re

def getSteps(fileName):
    f = open(fileName, "r")
    map = f.read().split("\n\n")
    instructions = map[0]
    network = map[1].strip().split("\n")
    networkDict = getNodeNetwork(network)
    currNode = "AAA"
    currInd = 0
    numSteps = 0
    while currNode != "ZZZ":
        currInstruction = instructions[currInd]
        currNode = networkDict[currNode][currInstruction]
        if currInd == len(instructions) - 1: # need to repeat sequence
            currInd = 0
        else:
            currInd += 1
        numSteps += 1
    return numSteps
        

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
