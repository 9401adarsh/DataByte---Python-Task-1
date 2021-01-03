# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:19:18 2021

@author: Adarsh
"""

for i in range(1, 101):
    if(i % 15 == 0):
        print("FizzBuzz")
    elif(i% 5 == 0):
        print("Fizz")
    elif(i % 3 == 0):
        print("Buzz")
    else:
        print(i)
