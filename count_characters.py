#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:45:10 2020

@author: aaronberlow
"""
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c]+=1
        else:
            count_dict[c] = 1
    print(count_dict)
    

count_characters('mississippi')