#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:33:33 2020

@author: aaronberlow
"""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])