import re

def sortHands(hands):
    rank = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    # merge sort from https://www.geeksforgeeks.org/merge-sort/
    if len(hands) > 1:
 
         # Finding the mid of the array
        mid = len(hands)//2
 
        # Dividing the array elements
        left = hands[:mid]
 
        # Into 2 halves
        right = hands[mid:]
 
        # Sorting the first half
        sortHands(left)
 
        # Sorting the second half
        sortHands(right)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            leftHand = left[i]
            rightHand = right[j]
            for cardPos in range(len(left[i])):
                if rank[leftHand[cardPos]] < rank[rightHand[cardPos]]:
                    hands[k] = leftHand
                    i += 1
                    break
                if rank[leftHand[cardPos]] > rank[rightHand[cardPos]]:
                    hands[k] = rightHand
                    j += 1
                    break
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            hands[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            hands[k] = right[j]
            j += 1
            k += 1

def getTotalWinnings(fileName):
    f = open(fileName, "r")
    camelCards = f.read()
    hands = re.findall("(.{5}) ", camelCards)
    bids = re.findall(" (\d*)", camelCards)
    handsAndBidsDict = dict(zip(hands, bids))
    categorizedHands = categorizeHands(hands)
    for hand in categorizedHands:
        sortHands(categorizedHands[hand])
    total = 0
    rank = 1
    handCategories = ["highCard", "onePair", "twoPair", "threeOfAKind",
                        "fullHouse", "fourOfAKind", "fiveOfAKind"]
    for category in handCategories:
        for hand in categorizedHands[category]:
            total += rank * int(int(handsAndBidsDict[hand]))
            rank += 1
    return total


def getCardCounts(hand):
    cardCounts = {}
    for card in hand:
        cardCounts[card] = cardCounts.get(card, 0) + 1
    return cardCounts

def categorizeHands(hands):
    categorizedHands = {
        "fiveOfAKind": [],
        "fourOfAKind": [],
        "fullHouse": [],
        "threeOfAKind": [],
        "twoPair": [],
        "onePair": [],
        "highCard": []
    }
    for hand in hands:
        cardCounts = getCardCounts(hand)
        if len(cardCounts) == 1: # only one card value in hand
            categorizedHands["fiveOfAKind"].append(hand)
        elif len(cardCounts) == 2: # two card values in hand
            for card in cardCounts:
                if cardCounts[card] == 4 or cardCounts[card] == 1:
                    categorizedHands["fourOfAKind"].append(hand)
                    break
                if cardCounts[card] == 2 or cardCounts[card] == 3:
                    categorizedHands["fullHouse"].append(hand)
                    break
        elif len(cardCounts) == 3: # three card values in hand
            for card in cardCounts:
                if cardCounts[card] == 3:
                    categorizedHands["threeOfAKind"].append(hand)
                    break
                elif cardCounts[card] == 2:
                    categorizedHands["twoPair"].append(hand)
                    break
        elif len(cardCounts) == 4:
            categorizedHands["onePair"].append(hand)
        else:
            categorizedHands["highCard"].append(hand)
    return categorizedHands

print(getTotalWinnings("input.txt"))