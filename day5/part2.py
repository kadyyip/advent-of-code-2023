import re

def convertSourceToDest(map, srcNums):
    map = map.strip().split("\n")
    destNums = []
    for i in range(1,len(map)):
        [destStart, srcStart, rangeLen] = map[i].split()
        destStart, srcStart, rangeLen = int(destStart), int(srcStart), int(rangeLen)
        srcEnd = srcStart + rangeLen - 1
        offset = srcStart - destStart
        removeInd = []
        for i in range(0,len(srcNums),2):
            srcNumStart = srcNums[i]
            srcNumRange = srcNums[i + 1]
            srcNumEnd = srcNumStart + srcNumRange - 1
            overlapStart = max(srcNumStart, srcStart)
            overlapEnd = min(srcNumEnd, srcEnd)
            if overlapStart <= overlapEnd: # valid overlap
                # add overlapping range to dest
                destNums.extend([overlapStart - offset, overlapEnd - overlapStart + 1])
                # add non-overlapping ranges in srcNums
                if srcNumStart < overlapStart:
                    srcNums.extend([srcNumStart, overlapStart - srcNumStart])
                if srcNumEnd > overlapEnd:
                    srcNums.extend([overlapEnd + 1, srcNumEnd - overlapEnd])
                removeInd.append(i)
        # remove the original ranges if overlapping range found
        numRemoved = 0
        if len(removeInd) > 0:
            for ind in removeInd:
                srcNums.pop(ind - numRemoved)
                srcNums.pop(ind - numRemoved)
                numRemoved += 2
    # add ranges for the ones that weren't mapped
    for i in range(0,len(srcNums),2):
        srcNumStart = srcNums[i]
        srcNumRange = srcNums[i + 1]
        destNums.extend([srcNumStart, srcNumRange])
    return destNums

def getLowestLocationNum(fileName):
    f = open(fileName, "r")
    sections = f.read().split("\n\n")
    seeds = re.findall("\d+", sections[0])
    seeds = [int(seed) for seed in seeds]
    src = seeds

    for i in range(1, len(sections)):
        src = convertSourceToDest(sections[i], src)
    # don't want to consider the range lengths
    return min([src[i] for i in range(0, len(src), 2)])
    
print(getLowestLocationNum("input.txt"))