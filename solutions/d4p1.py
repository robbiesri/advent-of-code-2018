#!/usr/bin/env python3

import commonAOC
import re

inputDataFile = commonAOC.loadInputData("d4.txt")
lines = list(inputDataFile)

lines.sort()

# determine the guard that sleeps the most
guardMinutes = {}
curGuardID = 0
curSleepStart = 0

for entry in lines:
    if "begins shift" in entry:
        curGuardID = re.findall("#\d+", entry)
        curGuardID = curGuardID[0][1:]
    elif "falls asleep" in entry:
        curSleepStart = re.findall(":\d+", entry)[0][1:]
    elif "wakes up" in entry:
        curWakeTime = re.findall(":\d+", entry)[0][1:]
        addedSleepTime = int(curWakeTime) - int(curSleepStart)
        if curGuardID in guardMinutes:
            guardMinutes[curGuardID] += addedSleepTime
        else:
            guardMinutes[curGuardID] = addedSleepTime

#print (guardMinutes)
s = [(k, guardMinutes[k]) for k in sorted(guardMinutes, key=guardMinutes.get, reverse=True)]
#print (s)
print ("Sleepiest guard: " + s[0][0])
print ("    Total sleep time: " + str(s[0][1]))

sleepyGuardID = s[0][0]

# ok scan again, keeping map of minutes
sleepiestMin = {}
for m in range(60):
    sleepiestMin[m] = 0

#print (sleepiestMin)
for entry in lines:
    if "begins shift" in entry:
        curGuardID = re.findall("#\d+", entry)
        curGuardID = curGuardID[0][1:]
    elif "falls asleep" in entry:
        curSleepStart = re.findall(":\d+", entry)[0][1:]
    elif "wakes up" in entry:
        curWakeTime = re.findall(":\d+", entry)[0][1:]
        if curGuardID == sleepyGuardID:
            sleepRange = [int(curSleepStart), int(curWakeTime)]
            for m in range(sleepRange[0], sleepRange[1]):
                sleepiestMin[m] += 1

# print(sleepiestMin)
s = [(k, sleepiestMin[k]) for k in sorted(sleepiestMin, key=sleepiestMin.get, reverse=True)]
# print(s)
print("Sleepiest minute: " + str(s[0][0]))
print("   Minutes slept on target minute: " + str(s[0][1]))
