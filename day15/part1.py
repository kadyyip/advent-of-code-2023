def getSumOfHashes(fileName):
    f = open(fileName, "r")
    initSeq = f.read().strip().split(",")
    sum = 0
    for step in initSeq:
        print(step, HASH(step))
        sum += HASH(step)
    return sum

def HASH(str):
    currentValue = 0
    for char in str:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    return currentValue

print(getSumOfHashes("input.txt"))