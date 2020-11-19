#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:38:29 2020

@author: aaronberlow
"""


input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string if c.isdigit()][-1]
print(new_list)