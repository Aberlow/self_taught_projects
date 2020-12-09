#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:57:52 2020

@author: aaronberlow
"""

name = input('enter file name: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

bigCount = None
bigword = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigword = word
        bigCount = count

print(bigword,bigCount)