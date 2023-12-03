#!/usr/bin/env python3

import sys
import re


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def extractCalibrationValue(line):
    pattern = re.compile('\d')
    digits = pattern.findall(line)
    return int(digits[0]+digits[-1])


lines = readLines(sys.argv[1])
calVals = map(extractCalibrationValue, lines)
print(sum(calVals))
