def getTotalCards(fileName):
    sum = 0
    cardNum = 1
    cardsDict = {}
    f = open(fileName, "r")
    for card in f:
        cardsDict[cardNum] = cardsDict.get(cardNum, 0) + 1
        numWinningNums = getNumWinningNums(card)
        for i in range(cardNum + 1, cardNum + numWinningNums + 1):
            cardsDict[i] = cardsDict.get(i, 0) + 1 * cardsDict.get(cardNum)
        cardNum += 1
    totalCards = 0
    for numCards in cardsDict.values():
        totalCards += numCards
    return totalCards

def getNumWinningNums(card):
    winningNums = set()
    numWinningNums = 0
    [winningNumsList, ourNums] = card.split("|")
    for winningNum in winningNumsList.split():
        if winningNum.isdigit():
            winningNums.add(winningNum)
    for ourNum in ourNums.split():
        if ourNum in winningNums:
            numWinningNums += 1
    return numWinningNums

print(getTotalCards("input.txt"))