# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:10:55 2022

@author: joaoandre
"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_use = ["Rock", "Paper", "Scissors"]

use = int(input("Choose one? 0 Rock, 1 Paper or 2 Scissors"))
pc__use = random.randint(0,2)

if use > 2:
    print("Invalid Number, You Lose!\n")
else:
    if use == pc__use:
        print("Is a Draw")
    elif use == 0:
        print("You choose: \n")
        print(rock)
        print("\nComputer chose: \n")
        if pc__use == 1:
            print(paper)
            print("You Lose!")
        elif pc__use == 2:
            print(scissors)
            print("You «Win!")
    elif use == 1:
        print("You choose: \n")
        print(paper)
        print("\nComputer chose: \n")
        if pc__use == 0:
            print(rock)
            print("You Win!")
        elif pc__use == 2:
            print(scissors)
            print("You Lose!")
    elif use == 2:
        print("You choose: \n")
        print(scissors)
        print("\nComputer chose: \n")
        if pc__use == 0:
            print(rock)
            print("You Lose!")
        elif pc__use == 1:
            print(paper)
            print("You Win!")