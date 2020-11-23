#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:43:41 2020

@author: aaronberlow
"""
    
    
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

aq = Queue()
print(aq.is_empty())

for i in range(1,11):
    aq.enqueue(i)
print(aq.items)

for i in range(aq.size()+1):
    print(i)
    
