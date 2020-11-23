#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:37:15 2020

@author: aaronberlow
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) -1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
for i in range(1,11):
    stack.push(i)
    
print(stack.items)
print(stack.size())

stack.pop()
print(stack.items)

print(stack.peek())


hello = Stack()

for c in "Hello":
    hello.push(c)

reversed_string = ''
for i in range(len(hello.items)):
    reversed_string += hello.pop()

print(reversed_string)

