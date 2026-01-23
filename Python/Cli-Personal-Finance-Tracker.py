'''
# *Name: CLI Personal Finance Tracker

Deliverables:
    #TODO: Input module for capturing expense amount, category, and date (2 hours) //
    #TODO: Data persistence module to save and load data from a file (3 hours) //
    #TODO: Reporting module to display totals by category and overall balance (2 hours)
    #TODO: Input validation and error handling system (1 hour)

'''
import csv
import os


def capture_expenses():
    from datetime import datetime

    categories = ["General","Expenses","Transfer","Food","Transport","Savings","Other"]
    amount = 0
    category = categories[0]
    date = datetime.now()

    output = {
        "id":"",
        "amount":amount,
        "category": category,
        "date": date, 
    }

    def display_menu_categories():
        print(f"{'-'*4} Please select a category {'-'*4}")
        for index, category in enumerate(categories, start=1):
            print(f"{index}.  {category}")
    
    def catch_menu_choice():
        display_menu_categories()
        choice = int(input(f"(1-{len(categories)}):\t"))
        choice = categories[choice - 1]
        return choice
    
    def catch_expense_amount():
        print(f"Please provide the amount:")
        amount = int(input(""))
        return amount
    
    def catch_expense_date():
        print(f"Please provide the date:")
        date = input(f"(DD/MM/YYYY)\t")
        return date
    
    def create_expense_output(amount, category, date, output):
        output["id"] = datetime.now()
        output["amount"] = amount
        output["category"] = category
        output["date"] = date
        print(f"Please confirm the below details:\n{output}")
        input()
        return output
    
    def store_data_csv(data):
        file_path = "Python/finance-tracker-assets/expenses.csv"

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        file_exists = os.path.isfile(file_path)
        fieldnames = ["id", "amount", "category", "date"]

        with open(file_path, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            if isinstance(data, dict):
                writer.writerow(data)
                print("Success: Data stored.")
            elif isinstance(data, list):
                writer.writerows(data)
                print("Success: Data stored.")
    
    if __name__ == "__main__":
        return store_data_csv(create_expense_output(catch_expense_amount(), catch_menu_choice(), catch_expense_date(), output))

    
def report_expense_data():
    categories = ["General","Expenses","Transfer","Food","Transport","Savings","Other"]

    def display_reporting_menu():
        print(f"{'-'*4} Please select a category to filter by {'-'*4}")
        for index, category in enumerate(categories, start=1):
            print(f"{index}.  {category}")
        print(f"{len(categories) + 1}.  All")

    def catch_reporting_choice():
        display_reporting_menu()
        choice = int(input(f"(1-{len(categories) + 1}):\t"))
        if choice in range [1:len(categories)]:
            choice = categories[choice - 1]
        elif choice == len(categories) + 1:
            choice = "all"

    def get_filtered_expenses(category_filter=None):
        file_path = "Python/finance-tracker-assets/expenses.csv"
        filtered_data = []

        if not os.path.exists(file_path):
            print("No data file found.")
            return []

        with open(file_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 1. Convert data types immediately
                row['amount'] = float(row['amount']) 
                
                # 2. Apply filtering logic
                if category_filter:
                    if row['category'].lower() == category_filter.lower():
                        filtered_data.append(row)
                else:
                    # If no filter is provided, keep everything
                    filtered_data.append(row)
                    
        return filtered_data


    def read_data_csv():
        file_path = "Python/finance-tracker-assets/expenses.csv"
        data = []

        if not os.path.exists(file_path):
            print("No data file found.")
            return []

        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount']) 
                data.append(row)
        return data

    def display_expenses(data):
        if not data:
            print("No expenses recorded yet.")
            return

        print(f"\n{'='*10} EXPENSE REPORT {'='*10}")
        
        for entry in data:
            print("-" * 30)
            for key, value in entry.items():
                print(f"{key.title()}: {value}")
        
        print("-" * 30)

    if __name__ == "__main__":
        return 

if __name__ == "__main__":

