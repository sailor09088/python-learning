# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:23:20 2023

@author: pqi
"""
import sys

dictionary = {}

for line in open(sys.argv[1], encoding='utf-16'):
    splt = line.split()
    if len(splt) >= 2:
#two strings in a line: first as key, and second as value
        dictionary[splt[0]] = splt[1]


for line in open(sys.argv[2]):
    splt = line.split()
    if (len(splt) > 2):
        for i in range (0, len(splt)):
            if splt[i] == 'SIG_NAME' :
                key = splt[i+1]
                value = dictionary[key]
                line = line.replace(key, value)
    print(line)
            