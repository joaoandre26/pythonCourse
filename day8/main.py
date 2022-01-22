# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:28:38 2022

@author: Bea_S
"""
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount 
        if new_position > len(alphabet):
            new_position = new_position - position - 1
        
        end_text += alphabet[new_position]
        
    print(f"The {cipher_direction} word is {end_text}")
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction == "encode":
#     encript(plain_text = text, nr_shift = shift)
# else:
#     decrypt(cipher_text = text, shift_amount = shift)
print(art.logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= len(alphabet)
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    if input("Keep trying?").lower() == "no":
        should_continue = False
   
print("ByeBye")
