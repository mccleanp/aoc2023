#!/usr/bin/env python3

import sys
import re


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()
    

def hasSymbolNeighbour(lines, lineno, chrno):
    for dx in range(-1,2):
        for dy in range(-1,2):
            x = chrno + dx
            y = lineno + dy
            if y >= 0 and y < len(lines):
                line = lines[y]
                if x >= 0 and x < len(line):
                    chr = line[x]
                    if not chr.isnumeric() and chr != '.':
                        return True
    return False

partNos = []
lines = readLines(sys.argv[1])
for lineno, line in enumerate(lines):
    num = ""
    isPartNumber = False
    for chrno, chr in enumerate(line):
        if chr.isnumeric():
            num += chr
            if not isPartNumber:
                isPartNumber = hasSymbolNeighbour(lines, lineno, chrno)
        else:
            if len(num) > 0 and isPartNumber:
                partNos.append(int(num))
            num = ""
            isPartNumber = False
    if len(num) > 0 and isPartNumber:
        partNos.append(int(num))
    
print(sum(partNos))
