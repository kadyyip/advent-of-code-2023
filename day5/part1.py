import re

def convertSourceToDest(map, srcNums):
    map = map.strip().split("\n")
    destNums = []
    mappedNums = set()
    for i in range(1,len(map)):
        [destStart, srcStart, rangeLen] = map[i].split()
        destStart, srcStart, rangeLen = int(destStart), int(srcStart), int(rangeLen)
        offset = srcStart - destStart
        for srcNum in srcNums:
            if srcNum >= srcStart and srcNum < srcStart + rangeLen:
                mappedNums.add(srcNum)
                destNums.append(srcNum - offset)
    for srcNum in srcNums:
        if srcNum not in mappedNums:
            destNums.append(srcNum)
    return destNums

def getLowestLocationNum(fileName):
    f = open(fileName, "r")
    sections = f.read().split("\n\n")
    seeds = re.findall("\d+", sections[0])
    seeds = [int(seed) for seed in seeds]
    src = seeds
    for i in range(1, len(sections)):
        src = convertSourceToDest(sections[i], src)
    return min(src)
    
print(getLowestLocationNum("input.txt"))