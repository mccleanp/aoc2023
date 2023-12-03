#!/usr/bin/env python3

import sys
import re


numbers = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def wordToNumber(word):
    if (word in numbers):
        return str(numbers.index(word))
    else:
        return word


def extractCalibrationValue(line):
    pattern = re.compile('\d|'+'|'.join(numbers))
    digits = pattern.findall(line)
    digits = list(map(wordToNumber, digits))
    return int(digits[0]+digits[-1])


lines = readLines(sys.argv[1])
calVals = map(extractCalibrationValue, lines)
print(sum(calVals))
