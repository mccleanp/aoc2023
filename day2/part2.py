#!/usr/bin/env python3

import sys
import re


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()


lines = readLines(sys.argv[1])
powers = []
for line in lines:
    game, result = line.split(':')

    id = int(re.match(r'Game (\d+)', game).group(1))

    max = {}

    sets = result.split(';')
    for set in sets:
        results = set.split(',')
        for result in results:
            count, color = re.match(r'\s*(\d+) (\w+)', result).group(1,2)
            count = int(count)
            if color not in max or max[color] < count:
                max[color] = count 

    powers.append(max['red'] * max['green'] * max['blue'])

print(sum(powers))