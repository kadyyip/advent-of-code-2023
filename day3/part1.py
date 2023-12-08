def createGraph(fileName):
    f = open(fileName, "r")
    graph = []
    for line in f:
        graph.append(list(line.strip()))
    return graph

def isAdjacentToSymbol(row, col, graph):
    for i in range(-1, 2):
        for j in range(-1, 2):
            checkRow = row + i
            checkCol = col + j
            if ((checkRow >= 0 and checkRow < len(graph)) and 
                (checkCol>= 0 and checkCol < len(graph[0]))): # in bounds
                if (graph[checkRow][checkCol] != "." and 
                    not graph[checkRow][checkCol].isdigit()):
                    return True
    return False

def sumPartNums(fileName):
    graph = createGraph(fileName)
    sumPartNums = 0
    for row in range(len(graph)):
        currPartNum = ""
        isAdj = False
        for col in range(len(graph[0])):
            currChar = graph[row][col]
            if currChar.isdigit():
                currPartNum += currChar
                if isAdjacentToSymbol(row, col, graph):
                    isAdj = True
                # want to add numbers if we reach the end of row
                if isAdj and col == len(graph[0]) - 1:
                    sumPartNums += int(currPartNum)
            else:
                if isAdj:
                    sumPartNums += int(currPartNum)
                    isAdj = False
                currPartNum = ""
    return sumPartNums
            



print(sumPartNums("input.txt"))

