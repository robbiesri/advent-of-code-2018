#!/usr/bin/env python3

import commonAOC

inputDataFile = commonAOC.loadInputData("d2.txt")

IDs = list(inputDataFile)

for testID in IDs:
    for otherID in IDs:
        delta = 0
        for c in range(len(testID)):
            if testID[c] != otherID[c]:
                delta += 1
        if delta == 1:
            commonSet = ""
            for c in range(len(testID)):
                if testID[c] == otherID[c]:
                    commonSet += testID[c]
            print (commonSet)
            print (testID)
            print (otherID)

            exit()