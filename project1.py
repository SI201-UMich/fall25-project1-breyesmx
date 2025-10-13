# Project 1 - Due Oct 10th.  
# Brandon Reyes Parra 
# UMID: 55887524
#Copy fail to a new vs code testing the commit with this comment
#Testing Commit 


import csv 
import unittest 

def csv_to_dict_list(self):

# Empty list to have the data
    data_list = []
# Step 1: I'm opening the file. 
    with open('SampleSuperstore.csv' 'r') as csvfile:
    sample_superstores_reader = csv.reader(csvfile)

#Step 2: Loop to get info from each row in the csv 

        for row in sample_superstores_reader:
            data_list.append(row) #Step 3: this would add the row to the list we created

# Step 4: we return the function 

    return data_list 

def calcualte_total_profit_by_category(data_list):

#Structure 
#Item = will be furniture which is a str
#Sales = will be the integer of the number of the sales 
#if statement if the item got sold