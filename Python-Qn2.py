# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:56:53 2021

@author: Adarsh
"""
# =============================================================================
# The idea is to read the values of the Excel File into a pandas DataFrame, and create a dictionary mapping Country
# Code to Country Name, then accept input of country codes from user, find the location of key using index function
# list(dictionary.keys()), using this location append country names to an empty list for all items between the locations
# Sort this list and print 
# =============================================================================

import pandas as pd
data = pd.read_csv("DataByte - Task1 (Python).csv")
Country_dict = dict()
for index,rows in data.iterrows():
    Country_dict[rows.Code] = rows.Name
CC1 = input("Enter Country Code 1:")
CC2 = input("Enter Country Code 2:")
CC_result = list()
CC_Codes = list(Country_dict.keys())
index1 = CC_Codes.index(CC1)
index2 = CC_Codes.index(CC2)
if(index1 > index2):
    index1, index2 = index2, index1
for i in range(index1+1, index2):
    CC_result.append(Country_dict[CC_Codes[i]])
CC_result.sort()
print(CC_result)


    
