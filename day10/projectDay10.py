# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:33:16 2022

@author: joaoandre
"""

# def my_function(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     name = f_name.title() + " " + l_name.title()
#     name1 = (f_name + " " + l_name).title()
#     return name1

# print(my_function("joao", "cruz"))



def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    """return the number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
      return "Invalid month"
    else:    
      if is_leap(year):
          if month == 2:
              return 29
          else:
              return month_days[month-1]
      else:
          return month_days[month-1]
          
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

