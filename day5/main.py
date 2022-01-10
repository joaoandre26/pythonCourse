# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:18:40 2022

@author: joaoandre
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

characters = []
for i in range(1,nr_letters+1):
    characters.append(random.choice(letters))
    
for i in range(1,nr_symbols+1):
    characters.append(random.choice(symbols))
    
for i in range(1,nr_numbers+1):
    characters.append(random.choice(numbers))
    

s = ""
random.shuffle(characters)
for idx in range(0,len(characters)):
    s += characters[idx]
    
print(s)