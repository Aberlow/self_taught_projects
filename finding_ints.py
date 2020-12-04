#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  25 01:05:43 2020

@author: aaronberlow
"""

def filter_list(l):
    number_list = []
    for i in l:
        if type(i) is int:
            number_list.append(i)
    return number_list
  
  
print(filter_list([1,2,'aasf','1','123',123]))

#test.assert_equals(filter_list([1,2,'a','b']),[1,2])
#test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
#test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])