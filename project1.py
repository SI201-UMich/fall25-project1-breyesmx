# Project 1 - Due Oct 10th.  
# Brandon Reyes Parra 
# UMID: 55887524
#Copy fail to a new vs code testing the commit with this comment
#Testing Commit 


import csv 
import unittest
import os 

# ___read the file function___
def csv_to_dict_list(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, filename)

# Empty list to have the data
    data_list = []
# Step 1: I'm opening the file. / Update Indentions
    with open(full_path, 'r') as csvfile:
        superstores_reader = csv.DictReader(csvfile)

#Step 2: Loop to get info from each row in the csv / Update indentions 

        for row in superstores_reader:
            try:
                row["Sales"] = float(row["Sales"])
                row["Profit"] = float(row["Profit"])
                data_list.append(row) #Step 3: this would add the row to the list we created
            except ValueError:
                print(f'Skipping row that are non-numeric data: {row}')
    return data_list #AI debgging indention 

# Step 4: we return the function / update indentions

# ___Function number 2 get the total of the profit by category__
def calcualte_total_profit_by_category(data, category):
#created a a variable called total_profit to start at 0.
    total_profit = 0
# loop trough each row from the data. 
    for row in data:
# Check the if the category is matches the category we are calling
        if row.get("Category") == category: #missing the .get AI debug this code / parentheses instead of brackets
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
        if row.get("Category") == category: #missing .get AI debugg this code / parentheses instead of brackets
#if it matches then we add to the total_sales. 
            total_sales += row["Sales"]
    return total_sales

#Function number 4 get the the result of the file 
def write_results_to_file(filename, results_dict):
    with open(filename, 'w', newline='') as file: #error here AI debugg this missing comma 
        section_names = ['Category', 'Total Profit', 'Total Sales'] #debugging with AI wrong indention
        writer = csv.DictWriter(file, fieldnames = section_names) #debugging with AI wrong indention, syntax error
        writer.writeheader() #debugging with AI wrong indention
        writer.writerows(results_dict)

# Main
def main():
#Using this read function #this would be in the main
    data = csv_to_dict_list("SampleSuperstore.csv")
    print(f"Loaded {len(data)} rows from the file:")
 
# get a list of the categories 
    categories = set(row["Category"] for row in data if "Category" in row)
    print(F'Found categories: {list(categories)}')
# loop trough each of the category and get it's total
    final_result = []
    for category in categories:
        profit = calcualte_total_profit_by_category(data, category) #debugged by AI indentions 
        sales = calculate_total_sales_by_category(data, category) #debugged by AI indentions 

# get the results in csv writer / indention wrong here would not select all the categories at first.
        final_result.append({
            "Category": category,
            "Total Profit": round(profit, 2),
            "Total Sales": round(sales, 2)
        })

    print("\nResults by Category:")
    for result in final_result:
        print(f"{result["Category"]}: \nProfit = ${result["Total Profit"]:,.2f}, \nSales = ${result["Total Sales"]:,.2f}")
    print("\nAnalysis Complete:")
    #print(final_result)

# then final list to a new file 
    output_file = "category_summary.csv" 
    write_results_to_file(output_file, final_result) #syntax error / variable name
    print(f'\nResults have been completed to written to {output_file}')
# call the functions for each of the category
if __name__ == "__main__":
    main()

# Creating the Test-Case
class TestSuperstoreFunctions(unittest.TestCase):
    def setUp(self):
        #Will have the data load the test of the CSV file
        self.test_data = csv_to_dict_list("test_superstore.csv")
        #print(self.test_data)
# Test for the CSV csv_to_dict_list 
def test_csv_loads_valid_rows(self):


    
#trying to pull this info I'm using two laptops since my laptop was at the tech shop. Doing a pull and see if it works.
#I was able to pull succesfully my updates from the other laptop.
# Structure needs to be fixed 
#Item = will be furniture which is a str
#Sales = will be the integer of the number of the sales