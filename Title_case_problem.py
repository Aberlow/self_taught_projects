#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:36:39 2020

@author: aaronberlow
"""
def title_case(title, minor_words=''):
       if title:
        title = title.lower().split()
        lower = minor_words.lower().split()
        final_title = []
        for word in title:
            if word in lower:
                final_title.append(word)
            else:
                final_title.append(word.capitalize())
        final_title[0] = final_title[0].capitalize()
        final_string = ' '.join([str(elem) for elem in final_title])
        return(final_string)
       return('')



print(title_case(''))
print(title_case('a clash of KINGS', 'a an the of'))# 'A Clash of Kings'
#title_case('THE WIND IN THE WILLOWS', 'The In')# 'The Wind in the Willows')
#Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')

#elegant solution
def title_case1(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])