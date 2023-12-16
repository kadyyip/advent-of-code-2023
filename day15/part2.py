import re

def getTotalFocusingPower(fileName):
    f = open(fileName, "r")
    initSeq = f.read().strip().split(",")
    sum = 0
    boxes = HASHMAP(initSeq)
    for box in boxes:
        for i in range(len(boxes[box])):
            slot = i + 1
            focalLen = boxes[box][i][1]
            focusingPower = (box + 1) * slot * focalLen
            sum += focusingPower
    return sum
    

def HASH(str):
    currentValue = 0
    for char in str:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    return currentValue

def HASHMAP(initSeq):
    boxes = {}
    for step in initSeq:
        label = re.search("\w*", step).group()
        operator = re.search("=|-", step).group()
        hash = HASH(label)
        if operator == "=":
            focalLen = int(re.search("\d+", step).group())
            if hash not in boxes:
                boxes[hash] = [[label, focalLen]]
            lensInBox = False
            for lens in boxes[hash]: 
                currLabel = lens[0]
                if currLabel == label:
                    lensInBox = True
                    lens[1] = focalLen
                    break
            if not lensInBox:
                boxes[hash].append([label, focalLen])
        elif operator == "-":
            if hash in boxes:
                for lens in boxes[hash]:
                    currLabel = lens[0]
                    if currLabel == label:
                        boxes[hash].remove(lens)
    return boxes



print(getTotalFocusingPower("input.txt"))