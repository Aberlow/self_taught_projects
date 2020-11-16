#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:23:39 2020

@author: aaronberlow
"""
def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters*.25+dimes*.10+nickels*.05+pennies*.01
    print()
    print('The total value of your change is', total)

main()