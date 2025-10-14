# Project 1 - Due Oct 10th.  
# Brandon Reyes Parra 
# UMID: 55887524
#Copy fail to a new vs code testing the commit with this comment
#Testing Commit 


import csv 
# ___read the file function___
def csv_to_dict_list():

# Empty list to have the data
    data_list = []
# Step 1: I'm opening the file. / Update Indentions
    with open('SampleSuperstore.csv' 'r') as csvfile:
        superstores_reader = csv.DictReader(csvfile)

#Step 2: Loop to get info from each row in the csv / Update indentions 

        for row in superstores_reader:
            row["Sales"] = float(row["Sales"])
            row["Profit"] = float(row["Profit"])
            data_list.append(row) #Step 3: this would add the row to the list we created
        return data_list 
#Using this read function
data = csv_to_dict_list("SampleSuperstore.csv")
print(f"Load {len(data)} rows")
print(data[0])

# Step 4: we return the function / update indentions

# ___Function number 2 get the total of the profit by category__
def calcualte_total_profit_by_category(data, category):
#created a a variable called total_profit to start at 0.
    total_profit = 0
# loop trough each row from the data. 
    for row in data:
# Check the if the category is matches the category we are calling
        if row["Caterogy"] == category:
# If it matches then we add to the total_profit 
            total_profit += row["Profit"]
    return total_profit

# __Function 3: Get the total sales by category__
def calculate_total_sales_by_category(data, category):
#created a varible called total_sales which start at 0.
    total_sales = 0
# Loop trough each row in the data.
    for row in data:
#Again it checks the value in the row that matches the one we are calling. 
        if row["Category"] == category:
#if it matches then we add to the total_sales. 
            total_sales += row["Sales"]
    return total_sales

#Function number 4 get the the result of the file 
def write_results_to_file(filename, results):
    with open(filename, 'w' as file):

#trying to pull this info I'm using two laptops since my laptop was at the tech shop. Doing a pull and see if it works.
#I was able to pull succesfully my updates from the other laptop.
# Structure 
#Item = will be furniture which is a str
#Sales = will be the integer of the number of the sales