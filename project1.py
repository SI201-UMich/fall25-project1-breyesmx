# Project 1 - Due Oct  15th 
# Brandon Reyes Parra 
# UMID: 55887524
# AI USage: I used AI assistatn for project structre gudidance, debugging (especially in indentions), and re-explaning some of the concepts that I forgot like try/except, and getting the ideas for the unitt test case. During this project I was able to create the functions with using the debugging of the syntax errors and typeerrors. 
#PLEASE READ THIS SECTION: #LINK to video will be here if you're having any problems please let me know. 

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
            except (ValueError, TypeError):
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

# Function 3: Get the total sales by category__
def calculate_total_sales_by_subcategory(data, subcategory):
#created a varible called total_sales which start at 0.
    total_sales = 0
# Loop trough each row in the data.
    for row in data:
#Again it checks the value in the row that matches the one we are calling. 
        if row.get("Sub-Category") == subcategory: #missing .get AI debugg this code / parentheses instead of brackets
#if it matches then we add to the total_sales. 
            total_sales += row["Sales"]
    return total_sales

#Function number 4 get the the result of the file 
def write_results_to_file(filename, results_list):
    with open(filename, 'w', newline='') as file: #error here AI debugg this missing comma 
        if not results_list:
            file.write("")
            return
        
        section_names = results_list[0].keys() #debugging with AI wrong indention
        writer = csv.DictWriter(file, fieldnames = section_names) #debugging with AI wrong indention, syntax error
        writer.writeheader() #debugging with AI wrong indention
        writer.writerows(results_list)

# Main
def main():
#Using this read function #this would be in the main
    data = csv_to_dict_list("SampleSuperstore.csv")
    print(f"Loaded {len(data)} rows from the file:")
 
# get a list of the categories 
    categories = sorted(list(set(row["Category"] for row in data if "Category" in row)))
    print(F'Found categories: {list(categories)}')
# loop trough each of the calculation category 
    profit_final_result = []
    for category in categories:
        profit = calcualte_total_profit_by_category(data, category) #debugged by AI indentions 

        profit_final_result.append({
            "Category": category,
            "Total Profit": round(profit, 2),            
        })

    output_file_1 = "category_profits.csv"
    write_results_to_file(output_file_1, profit_final_result)
    print(F'Analysis Completed: {output_file_1}')
# Loop trough each of the calculation by subcategory
    subcategories = sorted(list(set(row["Sub-Category"] for row in data if "Sub-Category" in row)))
    print(f'Selected: {len(subcategories)} sub-categories')
    total_sales_result = []
    for subcategory in subcategories:
        sales = calculate_total_sales_by_subcategory(data, subcategory)
        total_sales_result.append({
            "Sub-Category": subcategory,
            "Total Sales": round(sales, 2)
        })
    output_file_2 = "subcategory_sales.csv"
    write_results_to_file(output_file_2, total_sales_result)
    print(f'Sales Analysis:{output_file_2}')


# Creating the Test-Case
class TestSuperstoreFunctions(unittest.TestCase):
    def setUp(self):
        self.test_csv_file = "test_superstore.csv"
        with open(self.test_csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Category", "Sub-Category", "Profit", "Sales"])
            writer.writerow(["Office", "Paper", "10.00", "50.00"])
            writer.writerow(["Tech", "Phones", "10.00", "50.00"])
        self.test_data = csv_to_dict_list(self.test_csv_file)

    def tearDown(self):
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_profit_calculation(self):
        profit = calcualte_total_profit_by_category(self.test_data, "Tech")
        self.assertEqual(profit, 80.00)
    def test_sales_by_subcategory(self):
        sales = calculate_total_sales_by_subcategory(self.test_data, "Paper")
        self.assertEqual(sales, 50.00)
    def test_write_empty_list(self):
        output_file = "test_empty.csv"
        write_results_to_file(output_file, [])
        with open(output_file, 'r') as f:
            content = f.read()
            self.assertEqual(content, '')
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    main()
    print("\nRUNNING UNIT TEST\n")
    unittest.main(argv=[''], exit=False, verbosity=2)