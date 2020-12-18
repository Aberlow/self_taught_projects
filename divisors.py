#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:11:41 2020

@author: aaronberlow
"""


#counting the divisors of a number - long solution
def divisors(n):
    divisors = n
    count = 0 
    while divisors != 0:
        if n%divisors == 0:
            count += 1
        divisors -= 1
        
    return(count)
    

#elegant solution 
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);