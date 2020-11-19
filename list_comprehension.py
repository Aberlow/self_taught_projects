#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:31:47 2020

@author: aaronberlow
"""

#list comprehension

# long form 
num_list = [1,7,5,3,2]
new_list = []

for i in num_list:
    new_list.append(i*7)

print(new_list)

#short 
numbers = [1, 7, 5, 3, 2]
print([i* 7 for i in numbers])