"""
Created on Thu Apr 16 13:15:28 2020
Country test
@author: Willian Kroye Dapper
"""
import json
import numpy as np
import pandas as pd
import random as rd
#read our dataset
country_df = pd.read_csv('country-list.csv')
#get a random number
no_of_questions = 20
mark = 0

print("Country and Capital test")
print("Enter the capital of the country given to you")


for item in range(0, no_of_questions):
    randNum = rd.randint(0, 247)
    #assign random element to question
    question = country_df.iloc[randNum]
    answer = input("Capital of %s: " % question['country'])
    answer = answer.lower()
    if question['capital'].lower() == answer:
        mark +=1
    else:
        print("The correct answer is %s" % question['capital'] )
    item+=1
    
print("Score is %s " % mark)


