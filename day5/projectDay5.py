# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:34:15 2022

@author: joaoandre
"""

fruits = ["Apple", "Peach", "Pear"]

for item in fruits:
    print(item+"\n")
    
# ## Exercise 1 - 
# students_heights = input("insert students height: ").split(",")

# average = 0
# for item in students_heights:
#     average += int(item)
    
# average = average /len(students_heights)

# print(f"Average height {average}")

## Exercise 2 

sum = 0
for i in range(0, 101):
    if i%2 == 0:
        sum += i
        
print(f"Even Sum: {sum}")

## Exercise 3 -
for i in range(1,101):
    if i%3 == 0:
        if i%5 == 0:
            print("FizzBuzz\n")
        else:
            print("Fizz\n")
    elif i%5 == 0:
        print("Buzz\n")
    else:
        print(f"{i}\n")
            
                