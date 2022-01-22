# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 21:36:50 2022

@author: joaoandre
"""

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                           "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary)


# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
    
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "OutStanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)   
    
# Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany":{"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
#     }

# Nesting a Disctionary in a List
travel_Log = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
    },
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5,
    }
    ]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_Log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_Log)
