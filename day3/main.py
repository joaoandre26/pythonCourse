# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:03:52 2022

@author: joaoandre
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))


if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")


## Exercise 1 - Odd or Even
number = int(input("Odd or Even? "))

if number % 2 == 0:
    print("Odd number")
else:
    print(f"Even number, remainder of {number % 2}")
    
## Exercise 2 - BMI Calculator 2.0
weight = float(input("Introduce your weight(m): " ))
height = float(input("Introduce your height(kg): "))


bmi = round(weight/(height**2), 1)

print(f"Your BMI is {bmi}\n")
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("slightly overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")

## Exercise 2 - Leap Year
year = int(input("Which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year!")
        else:
            print("Not Leap Year!")
    else:
        print("Not Leap Year!")
else:
    print("Not a Leap Year")
    
## Exercise 3 
print("Welcome to automatic pizza order!")

size = input("Which size of pizza do you want? Small, Medium or Large?")

bill = 0
if size == "Small":
    bill += 15
elif size == "Medium":
    bill += 20
else: #Large
    bill += 25
    
peperonni = input("Do you want Peperoni? Y or N")
if peperonni == "Y":
    if size == "Small":
        bill += 2
    else:
        bill += 3
        
cheese = input("Extra cheese? Y or N")
if cheese == "Y":
    bill += 1

print(f"You have to pay ${bill}")

## Exercise 4 - Love Calculator
hername = input("Girl Name: \n")
hisname = input("Boy Name: \n")

hername = hername.lower()
hisname = hisname.lower()

names = hername + hisname

decimal = 0
unit = 0
decimal += names.count("t")
decimal += names.count("r")
decimal += names.count("e")
decimal += names.count("u")

unit += names.count("l")
unit += names.count("o")
unit += names.count("v")
unit += names.count("e")

Love_Score = decimal*10 + unit

if Love_Score < 10 or Love_Score > 90:
    print(f"You score is {Love_Score}, you go together like coke and mentos")
elif Love_Score >= 40 and Love_Score <= 50:
    print(f"You score is {Love_Score}, you are alright together")
else:
    print(f"You score is {Love_Score}")