#!/usr/bin/env python3

import sys
import re


def readLines(filename):
    with open(filename) as f:
        return f.read().splitlines()


limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

lines = readLines(sys.argv[1])
for line in lines:
    game, result = line.split(':')

    id = int(re.match(r'Game (\d+)', game).group(1))

    possible = True
    sets = result.split(';')
    for set in sets:
        colors = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        results = set.split(',')
        for result in results:
            count, color = re.match(r'\s*(\d+) (\w+)', result).group(1,2)
            colors[color] += int(count)

        for a, b in zip(colors.values(), limits.values()):
            if a > b:
                possible = False

    if possible:
        sum += id

print(sum)
