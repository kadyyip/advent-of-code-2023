def getDifferenceBetweenSteps(sequence):
    difference = []
    for i in range(1, len(sequence)):
        difference.append(sequence[i] - sequence[i-1])
    return difference

def isSequenceOfZeroes(sequence):
    for num in sequence:
        if num != 0:
            return False
    return True

def predictNextValue(sequence):
    sequences = [sequence]
    currInd = 0
    while not isSequenceOfZeroes(sequences[currInd]):
        sequences.append(getDifferenceBetweenSteps(sequences[currInd]))
        currInd += 1
    print(sequences)
    sequences[-1].append(0)
    
    for i in range(len(sequences)-2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])
    return sequences[0][-1]

def sumPredictedValues(fileName):
    f = open(fileName, "r")
    sum = 0
    for line in f.readlines():
        sequence = [int(num) for num in line.split(" ")]
        sequence.reverse()
        sum += predictNextValue(sequence)
    return sum

print(sumPredictedValues("input.txt"))