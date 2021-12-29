# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:50:01 2021

@author: joaoandre
"""
## Day 2.1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(str(int(two_digit_number[0]) + int(two_digit_number[1])))

## Day 2.2
height = float(input("Insert your height: "))
weight = float(input("Insert your weight: "))

bmi = int(weight/(height ** 2))
bmif = round(weight/(height ** 2), 2)

print("Your BMI is: " + str(bmi) + ", " + str(bmif))

## Day 2.3
# 🚨 Don't change the code below 👇
age = input("What is your age? ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
age_int = int(age)

years_left = 90-age_int

months = int(years_left*12)
weeks = int(years_left*52)
days = int(years_left*365)
print(f"You have {days} days, {weeks} weeks and {months} months left.")