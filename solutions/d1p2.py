#!/usr/bin/env python3

import commonAOC

inputDataFile = commonAOC.loadInputData("d1.txt")
data = list(map(int, inputDataFile))

currentFreq = 0
freqSet = set()

repeatFreqFound = False
repeatFreq = 0

while repeatFreqFound == False:
    for freqChange in data:
        if currentFreq in freqSet:
            repeatFreqFound = True
            repeatFreq = currentFreq
            break

        freqSet.add(currentFreq)
        currentFreq += freqChange

print(repeatFreq)