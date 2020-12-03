#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 01:04:56 2020

@author: aaronberlow
"""

#Long solution
def sqInRect(lng, wdth):
    length = lng
    width = wdth
    blocks = length * width
    squares = []
    
    if length != width:
        while blocks != 0:
            if length < width:
                squares.append(length)
                width -= length
                blocks -= length * length
            else:
                squares.append(width)
                length -= width
                blocks -= width *width 
        return(squares)
    else:
        return None

print(sqInRect(5, 3))


#Best Solution
def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res