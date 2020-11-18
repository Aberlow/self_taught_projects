#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:13:06 2020

@author: aaronberlow
"""
# quadratic.py

import math

def main():
    print("This is a program finds the real solutions to a quadratic")
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    
    print()
    print("The solutions are:", root1, root2)
    
main()