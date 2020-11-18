#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:24:17 2020

@author: aaronberlow
"""

def return_duplicates(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups

a_list = ['susan adams', 'kwame goodall', 'jill hampton', 'susan adams']
dups = return_duplicates(a_list)
print(dups)
    