#!/usr/bin/env python3

import commonAOC
import re

inputDataFile = commonAOC.loadInputData("d3.txt")

n = 1000
fabricArr = [[0] * n for i in range(n)]

for claimLine in inputDataFile:
    claim = claimLine.split()
    claimStart = list(map(int, re.findall("\d+", claim[2])))
    claimSize = list(map(int, re.findall("\d+", claim[3])))

    for x in range(claimStart[0], (claimStart[0]+claimSize[0])):
        for y in range(claimStart[1], (claimStart[1]+claimSize[1])):
            fabricArr[x][y] += 1

overlapCount = 0
for x in range(n):
    for y in range(n):
        if fabricArr[x][y] > 1:
            overlapCount += 1

print (overlapCount)