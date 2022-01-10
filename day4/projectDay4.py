# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:55:18 2022

@author: joaoandre
"""

import random
import module

# c = random.randint(1, 100)

# print(f"number {c} ")
# print(f"pi {module.pi}")

# fl = random.random()
# print(f"number {fl} ")


# ## Exercise 1

# head_tales = random.randint(0,1)

# if(head_tales == 1):
#     print("Head\n")
# else:
#     print("Tales\n")
    
# ## Exercise 2

# names = input("Insert names of people at the table: ")

# list_names = names.split(",")

# randnum = random.randint(0, len(list_names)-1)

# person = list_names[randnum]
# print(f"{person} is paying the dinner")

# print(random.choice(list_names)+" is paying the dinner")

## Exercise 3

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
vertical = int(position[0])-1
horizontal = int(position[1])-1

if(vertical < 3 and horizontal < 3):
    map[vertical][horizontal] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

            