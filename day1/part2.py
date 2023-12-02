import re

def getCalibrationValue(s):
    digits = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", s)
    print(digits)
    numsDict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }
    firstDigit = digits[0]
    lastDigit = digits[len(digits) - 1]
    if firstDigit in numsDict:
        firstDigit = numsDict[firstDigit]
    if lastDigit in numsDict:
        lastDigit = numsDict[lastDigit]
    return int(firstDigit + lastDigit)

def addCalibrationValues(fileName):
    sum = 0
    f = open(fileName, "r")
    for line in f:
        print(getCalibrationValue(line) )
        sum += getCalibrationValue(line) 
    return sum

print(addCalibrationValues("input.txt"))
