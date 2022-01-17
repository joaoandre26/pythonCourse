# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:38:20 2022

@author: joaoandre
"""

#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
wordIs = random.choice(word_list)
print(f"Pss. The chosen word is {wordIs}")

display = []
wordLength = len(wordIs)
lives = int(len(stages))-1
print(lives)

for i in range(wordLength):
    display += "_"
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
endOfGame = False
letterGuess = False
lostGame = False
print(stages[lives])
while not endOfGame:
    letterGuess = False
    letter = input("Guess a letter: ").lower()
    if letter in display:
        print("You already selected this letter, try again!")
    else:
        #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for j in range(wordLength):
            if wordIs[j] == letter:
                display[j] = letter
                letterGuess = True
        
        print(stages[lives])
        
        if not letterGuess:
            lives -= 1        
            if lives == 0:
                endOfGame = True
                lostGame = True

        if not "_" in display:
            endOfGame = True
        
        print(f"{' '.join(display)}")

if lostGame:
    print("You Lost!")
    print(stages[lives])
    print(f"The word was {wordIs}")
else:
    print("You Won!")