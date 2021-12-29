# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:08:21 2021

@author: joaoandre
"""

## Tip Calculator
#Welcome message
print("Welcome to the tip Calculator.")
#Bill
bill_value = float(input("What was the total bill? "))
#Tip
tip_percentage = int(input("What percentage tip would you like to give?10, 12, or 15? "))
#Number of persons
num_person = int(input("How many people to split the bill? "))

total_value = bill_value*(1+(tip_percentage/100))
value_per_person = round(total_value/num_person,2)

message = f"Each person should pay: ${value_per_person}"
print(message)
