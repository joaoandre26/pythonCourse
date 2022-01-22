# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 09:44:11 2022

@author: Bea_S
"""
import math
#Function with no input
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")
    
# greet()

#Function with one input
# def greet_with_names(name):
#     print("Hello")
#     print(f"How do you do {name}?")
    
# greet_with_names("Jack Bauer")



# #Function with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")


    
# greet_with(location = "Nowhere",name = "Jack Bauer")

######### EXERCISE 1
# #Write your code below this line 👇
# def paint_calc(height, width, cover):
#     area = height*width
#     nr_cans = math.ceil(area/cover)
#     print(f"You will need {nr_cans} to paint")






# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

################# Exercise 2
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2,number-1):
        if number%i == 0:
            is_prime = False
    
    if is_prime:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not a prime number!")
        
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)