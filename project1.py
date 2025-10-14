# Project 1 - Due Oct 10th.  
# Brandon Reyes Parra 
# UMID: 55887524
#Copy fail to a new vs code testing the commit with this comment
#Testing Commit 


import csv 
# ___read the file function___
def csv_to_dict_list(SampleSuperstore.csv):

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
    total_profit = 0 
    for row in data: 
        if row["Caterogy"] == category:
            total_profit += row["Profit"]
    return total_profit

# __Function 3: Get the total sales by category__
def calculate_total_sales_by_category(data, category):
    total_sales = 0
    for row in data: 
        if row["Category"] == category:
            total_sales += row["Sales"]
    return total_sales

#Structure 
#Item = will be furniture which is a str
#Sales = will be the integer of the number of the sales