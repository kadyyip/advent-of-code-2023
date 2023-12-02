import re

def getCalibrationValue(s):
    digits = re.findall("\d", s)
    firstDigit = digits[0]
    lastDigit = digits[len(digits) - 1]
    return int(firstDigit + lastDigit)

def addCalibrationValues(fileName):
    sum = 0
    f = open(fileName, "r")
    for line in f:
        sum += getCalibrationValue(line) 
    return sum

print(addCalibrationValues("day1/input.txt"))