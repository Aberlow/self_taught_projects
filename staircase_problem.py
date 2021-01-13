#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:52:24 2021

@author: aaronberlow
"""

def staircase(n):
    stairs = 0
    steps = 1
    spaces = n-1
    
    while stairs != n:
       for i in range(spaces):
           print(" ", end=(""))
       for i in range(steps):
           print("#", end=(""))
       print()
       stairs += 1
       spaces -= 1
       steps += 1

staircase(6)