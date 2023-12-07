def createGraph(fileName):
    f = open(fileName, "r")
    graph = []
    for line in f:
        graph.append(list(line.strip()))
    return graph

def isAdjacentToAsterisk(row, col, graph):
    for i in range(-1, 2):
        for j in range(-1, 2):
            checkRow = row + i
            checkCol = col + j
            if ((checkRow >= 0 and checkRow < len(graph)) and 
                (checkCol>= 0 and checkCol < len(graph[0]))): # in bounds
                if graph[checkRow][checkCol] == "*":
                    return [True, (checkRow, checkCol)]
    return [False, (-1, -1)]

def sumPartNums(fileName):
    graph = createGraph(fileName)
    asteriskParts = {}
    sumGearRatios = 0
    for row in range(len(graph)):
        currPartNum = ""
        isAdj = False
        for col in range(len(graph[0])):
            currChar = graph[row][col]
            if currChar.isdigit():
                currPartNum += currChar
                isAdjacentToAsteriskRes = isAdjacentToAsterisk(row, col, graph)
                if isAdjacentToAsteriskRes[0]:
                    isAdj = True
                    asteriskInd = isAdjacentToAsteriskRes[1]
                # want to add numbers if we reach the end of row
                if isAdj and col == len(graph[0]) - 1:
                    if asteriskInd in asteriskParts:
                        gearRatio = asteriskParts[asteriskInd] * int(currPartNum)
                        sumGearRatios += gearRatio
                    else:
                        asteriskParts[asteriskInd] = int(currPartNum)
            else:
                if isAdj:
                    if asteriskInd in asteriskParts:
                        gearRatio = asteriskParts[asteriskInd] * int(currPartNum)
                        sumGearRatios += gearRatio
                        isAdj = False
                    else:
                        asteriskParts[asteriskInd] = int(currPartNum)
                        isAdj = False
                currPartNum = ""   
    return sumGearRatios
            



print(sumPartNums("input.txt"))

