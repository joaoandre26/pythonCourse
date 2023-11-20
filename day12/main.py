# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 23:14:59 2022

@author: joaoandre
"""
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def game_mode():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == "easy":
        return 10
    else:
        return 5

def guess_a_number(number_to_guess):
    done = True
    number = int(input("Make a guess: "))
    if number == number_to_guess:
        print(f"You have won! Your number was {number}")
        done = False
    elif number < number_to_guess:
        print("To low")
    else:
        print("To high")
    return done

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
my_number = random.randrange(0,101,1)
attempts_left = game_mode()
keep_play = True
while keep_play:
    print(f"You have {attempts_left} attempts remaining to guess the number")
    keep_play = guess_a_number(my_number)
    attempts_left -= 1
    if attempts_left <= 0:
        if keep_play:
            print(f"You lost. Your number was {my_number}")
        keep_play = False
    else:
        print("Guess again.")
            
    