# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 18:00:04 2021

@author: joaoandre
"""
## Day 1.1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

## Day 1.2
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

## Day 1.3
print(len(input("What is your name?")))

## Day 1.4
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)