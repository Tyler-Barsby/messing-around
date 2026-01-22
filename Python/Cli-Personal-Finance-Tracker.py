'''
# *Name: CLI Personal Finance Tracker

Deliverables:
    #TODO: Input module for capturing expense amount, category, and date (2 hours)
    #TODO: Data persistence module to save and load data from a file (3 hours)
    #TODO: Reporting module to display totals by category and overall balance (2 hours)
    #TODO: Input validation and error handling system (1 hour)

'''
import csv


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
        print(f"Please confirm the below details:")
        return output
    
    if __name__ == "__main__":
        create_expense_output(catch_expense_amount(), catch_menu_choice(), catch_expense_date(), output)






if __name__ == "__main__":
    capture_expenses()