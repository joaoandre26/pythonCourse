# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 22:33:06 2022

@author: joaoandre
"""

#from replit import clear
import art

bids_dictionary = {}

print(art)
continue_bid = True

while continue_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids_dictionary[name] = bid
    
    keepGoing = input("Is there any one else to bid(Yes or No)? ").lower()
    if keepGoing == "no":
        continue_bid = False
    else:
        print("\x1B[2J")
        
name = ""
value = 0
for bidder in bids_dictionary:
    if bids_dictionary[bidder] > value:
        name = bidder
        value = bids_dictionary[bidder]
        
print(f"{name} Won! With a bid of ${value}")