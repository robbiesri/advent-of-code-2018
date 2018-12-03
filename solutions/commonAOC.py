#!/usr/bin/env python3

import os

def loadInputData(fileName):
    codeFolder = os.path.realpath(os.path.dirname(__file__))
    dataFolder = os.path.abspath(os.path.join(codeFolder, "..", "input"))

    inputDataFile = open(os.path.join(dataFolder, fileName))

    return inputDataFile