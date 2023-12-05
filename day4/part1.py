def sumAllPoints(fileName):
    sum = 0
    f = open(fileName, "r")
    for card in f:
        sum += getCardPoints(card)
    return sum

def getCardPoints(card):
    winningNums = set()
    points = 0
    [winningNumsList, ourNums] = card.split("|")
    for winningNum in winningNumsList.split():
        if winningNum.isdigit():
            winningNums.add(winningNum)
    for ourNum in ourNums.split():
        if ourNum in winningNums:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

print(sumAllPoints("input.txt"))