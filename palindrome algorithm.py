#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:37:41 2020

@author: aaronberlow
"""
def is_palindrome(word):
    word = word.lower()
    return word[::-1]==word