#!/usr/bin/env python3

import commonAOC
import re
import string

def reacts(char1, char2):
    return (char1 != char2) and (char1.lower() == char2.lower()) 

def react(original):
    reacted = ""
    for c in original:
        if len(reacted) == 0:
            reacted = c
        elif reacts(c, reacted[-1]):
            reacted = reacted[:-1]
        else:
            reacted += c
    return reacted

def reactStrip(original, targetChar):
    reacted = ""
    for c in original:
        if (c != targetChar) and (c != targetChar.upper()):
            if len(reacted) == 0:
                reacted = c
            elif reacts(c, reacted[-1]):
                reacted = reacted[:-1]
            else:
                reacted += c

    return reacted

inputDataFile = commonAOC.loadInputData("d5.txt")
inputPolymer = list(inputDataFile)[0]

minLen = 1000000
charForMinLen = 'a'

for c in list(string.ascii_lowercase):
    strippedReact = reactStrip(inputPolymer, c)
    if len(strippedReact) < minLen:
        minLen = len(strippedReact.strip())
        charForMinLen = c

print (charForMinLen)
print (minLen)