#!/usr/bin/env python3

import commonAOC
from collections import Counter
import string

inputDataFile = commonAOC.loadInputData("d2.txt")

total2count = 0
total3count = 0

for line in inputDataFile:
    count2 = False
    count3 = False
    
    counter = Counter(line)

    for k in string.ascii_lowercase:
        letterCount = counter[k]
        if letterCount == 2:
            count2 = True
        if letterCount == 3:
            count3 = True

    if count2:
        total2count += 1
    if count3:
        total3count += 1

checksum = total2count * total3count
print(checksum)