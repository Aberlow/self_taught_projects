#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:56:12 2020

@author: aaronberlow
"""
#Breaking string into components

abc = "With three words"
stuff = abc.split()
print(stuff)

print(len(stuff))

print(stuff[0])

print(stuff)

for w in stuff:
    print(w)