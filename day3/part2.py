#!/usr/bin/env python3

import sys
import re


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()
    

def findNumericNeighbours(lines, lineno, chrno):
    neighbours = []

    for dy in range(-1,2):
        dx = -1
        while dx < 2:
            x = chrno + dx
            y = lineno + dy
            if y >= 0 and y < len(lines):
                line = lines[y]
                if x >= 0 and x < len(line):
                    chr = line[x]
                    if chr.isnumeric():
                        post = ""
                        pre = ""
                        x += 1
                        while x < len(line) and line[x].isnumeric():
                            post += line[x]
                            x += 1
                        x = chrno + dx - 1 
                        while x >= 0 and line[x].isnumeric():
                            pre = line[x] + pre
                            x -= 1
                        print(pre, chr, post)
                        neighbours.append(int(pre+chr+post))
                        dx += len(post)
            dx+=1
    return neighbours
                        

ratios = []
lines = readLines(sys.argv[1])
for lineno, line in enumerate(lines):
    for chrno, chr in enumerate(line):
        if chr == '*':
            neighbours = findNumericNeighbours(lines, lineno, chrno)
            print(neighbours)
            if len(neighbours) == 2:
                ratios.append(neighbours[0] * neighbours[1])
    
print(sum(ratios))
