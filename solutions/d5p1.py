#!/usr/bin/env python3

import commonAOC
import re

# def compressChar(char1, char2):
#     if char1.isupper():
#         if char2.islower() and (char2.upper() == char1):
#             return True

#     if char1.islower():
#         if char2.isupper() and (char2.lower() == char1):
#             return True

#     return False

def compressChar(char1, char2):
    return (char1 != char2) and (char1.lower() == char2.lower()) 

inputDataFile = commonAOC.loadInputData("d5.txt")

inputPolymer = list(inputDataFile)[0]
# print (inputPolymer)
# print (len(inputPolymer))
compressedPolymer = ""
compressedLen = 0
for inputPolymerChar in inputPolymer:
    # print(inputPolymerChar)
    compressedPolymer += inputPolymerChar
    compressedLen += 1

    while (True):
        if compressedLen > 1:
            curChar = compressedPolymer[-1]
            prevChar = compressedPolymer[-2]
            # print("Prev: " + prevChar + " Cur: " + curChar)
            if compressChar(prevChar, curChar):
                compressedPolymer = compressedPolymer[:-2]
                compressedLen -= 2
                # print(compressedPolymer)
            else:
                break
        else:
            break

print(compressedPolymer)
print (len(compressedPolymer))

def react(original):
    reacted = ""
    for c in original:
        if len(reacted) == 0:
            reacted = c
        elif compressChar(c, reacted[-1]):
            reacted = reacted[:-1]
        else:
            reacted += c
    return reacted

reactedPolymer = react(inputPolymer)
print (reactedPolymer)
print (len(reactedPolymer.strip()))