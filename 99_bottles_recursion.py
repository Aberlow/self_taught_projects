#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:27:15 2020

@author: aaronberlow
"""
# 99 bottles of beer 

def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer""")
        
        return 
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall, {} bottles of beer. 
          Take one down, pass it around, {} bottles of beer on the wall""".format(tmp, tmp, bob))
    bottles_of_beer(bob)
    

bottles_of_beer(6)