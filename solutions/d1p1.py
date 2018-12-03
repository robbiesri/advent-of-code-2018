#!/usr/bin/env python3

import commonAOC

inputDataFile = commonAOC.loadInputData("d1.txt")
data = list(map(int, inputDataFile))

baseFreq = 0
for freqDelta in data:
    baseFreq += freqDelta

print("Final frequency: " + str(baseFreq))