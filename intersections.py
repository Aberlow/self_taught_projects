#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:21:12 2020

@author: aaronberlow
"""
#list intersection

#function solution
def intersecton(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [2,43,48,62,64,28,3]
list2 = [1,28,42,70,2,10,62,31,4,14]

print(intersecton(list1, list2))

#Intersection solution

def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

new_list = return_intersection(list1, list2)
print(new_list)