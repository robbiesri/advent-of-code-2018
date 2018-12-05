#!/usr/bin/env python3

import commonAOC
import re

def createSleepiestMinuteDict():
    sleepiestMin = {}
    for m in range(60):
        sleepiestMin[m] = 0
    return sleepiestMin

inputDataFile = commonAOC.loadInputData("d4.txt")
lines = list(inputDataFile)

lines.sort()

curGuardID = 0
curSleepStart = 0

perGuardSleepiestMinDict = {}

for entry in lines:
    if "begins shift" in entry:
        curGuardID = re.findall("#\d+", entry)
        curGuardID = curGuardID[0][1:]
    elif "falls asleep" in entry:
        curSleepStart = re.findall(":\d+", entry)[0][1:]
    elif "wakes up" in entry:
        curWakeTime = re.findall(":\d+", entry)[0][1:]
        sleepRange = [int(curSleepStart), int(curWakeTime)]

        if curGuardID not in perGuardSleepiestMinDict:
            perGuardSleepiestMinDict[curGuardID] = createSleepiestMinuteDict()

        for m in range(sleepRange[0], sleepRange[1]):
            perGuardSleepiestMinDict[curGuardID][m] += 1

# print(perGuardSleepiestMinDict)

maxSleepiestMinAmount = 0
maxSleepiestMin = 0
maxSleepiestMinGuardID = 0
for guardID in perGuardSleepiestMinDict:
    # print(guardID)
    # print(perGuardSleepiestMinDict[guardID])
    sleepiestMin = perGuardSleepiestMinDict[guardID]
    s = [(k, sleepiestMin[k]) for k in sorted(sleepiestMin, key=sleepiestMin.get, reverse=True)]
    # print(s)
    # print(s[0])
    
    if s[0][1] > maxSleepiestMinAmount:
        maxSleepiestMinGuardID = guardID
        maxSleepiestMinAmount = s[0][1]
        maxSleepiestMin = s[0][0]

print ("Guard chosen: " + str(maxSleepiestMinGuardID))
print ("    Sleepiest minute: " + str(maxSleepiestMin))
print ("    Amount slept that minute: " + str(maxSleepiestMinAmount))