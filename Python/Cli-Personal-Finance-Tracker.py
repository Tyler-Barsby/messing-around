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
from datetime import datetime

# Constants
CATEGORIES = ["General", "Expenses", "Transfer", "Food", "Transport", "Savings", "Other"]
FILE_PATH = "Python/finance-tracker-assets/expenses.csv"

def display_menu_categories():
    print(f"{'-'*4} Please select a category {'-'*4}")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}.  {category}")

def catch_menu_choice():
    display_menu_categories()
    while True:
        try:
            choice_idx = int(input(f"(1-{len(CATEGORIES)}):\t"))
            if 1 <= choice_idx <= len(CATEGORIES):
                return CATEGORIES[choice_idx - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def catch_expense_amount():
    print(f"Please provide the amount:")
    while True:
        try:
            amount = float(input(""))
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")

def catch_expense_date():
    print(f"Please provide the date:")
    while True:
        date_str = input(f"(DD/MM/YYYY) [Default: Today]:\t")
        if not date_str:
            return datetime.now().strftime("%d/%m/%Y")
        try:
            # Validate format
            datetime.strptime(date_str, "%d/%m/%Y")
            return date_str
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")

def create_expense_output(amount, category, date_str):
    output = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "amount": amount,
        "category": category,
        "date": date_str,
    }
    print(f"Please confirm the below details:\n{output}")
    # Simple pause for confirmation
    input("Press Enter to confirm and save...")
    return output

def store_data_csv(data):
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    file_exists = os.path.isfile(FILE_PATH)
    fieldnames = ["id", "amount", "category", "date"]

    try:
        with open(FILE_PATH, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            if isinstance(data, dict):
                writer.writerow(data)
                print("Success: Data stored.")
            elif isinstance(data, list):
                writer.writerows(data)
                print("Success: Data stored.")
    except IOError as e:
        print(f"Error saving data: {e}")

def capture_expenses():
    amount = catch_expense_amount()
    category = catch_menu_choice()
    date_str = catch_expense_date()
    output = create_expense_output(amount, category, date_str)
    store_data_csv(output)

# --- Reporting Functions ---

def display_reporting_menu():
    print(f"{'-'*4} Please select a category to filter by {'-'*4}")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}.  {category}")
    print(f"{len(CATEGORIES) + 1}.  All")
    print(f"{len(CATEGORIES) + 2}.  Summary Report")

def catch_reporting_choice():
    display_reporting_menu()
    while True:
        try:
            choice_idx = int(input(f"(1-{len(CATEGORIES) + 2}):\t"))
            if 1 <= choice_idx <= len(CATEGORIES):
                return CATEGORIES[choice_idx - 1]
            elif choice_idx == len(CATEGORIES) + 1:
                return "All"
            elif choice_idx == len(CATEGORIES) + 2:
                return "Summary"
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def read_expenses_csv():
    if not os.path.exists(FILE_PATH):
        print("No data file found.")
        return []

    data = []
    try:
        with open(FILE_PATH, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert amount to float for consistency
                try:
                    row['amount'] = float(row['amount'])
                except ValueError:
                    pass # Keep as string if fails, or handle error
                data.append(row)
    except IOError as e:
        print(f"Error reading data: {e}")
    return data

def report_expense_data():
    filter_choice = catch_reporting_choice()
    data = read_expenses_csv()
    
    if not data:
        print("No expenses recorded yet.")
        return

    if filter_choice == "Summary":
        display_category_summary(data)
    else:
        filtered_data = []
        if filter_choice == "All":
            filtered_data = data
        else:
            for row in data:
                if row['category'].lower() == filter_choice.lower():
                    filtered_data.append(row)
        display_expenses(filtered_data)

def display_category_summary(data):
    print(f"\n{'='*10} CATEGORY SUMMARY {'='*10}")
    summary = {cat: 0.0 for cat in CATEGORIES}
    
    for entry in data:
        cat = entry.get('category')
        amount = entry.get('amount')
        if cat in summary and isinstance(amount, (int, float)):
            summary[cat] += amount
            
    print(f"{'Category':<15} | {'Total':>10}")
    print("-" * 28)
    total_overall = 0
    for cat, total in summary.items():
        if total > 0:
            print(f"{cat:<15} | {total:>10.2f}")
            total_overall += total
    print("-" * 28)
    print(f"{'TOTAL':<15} | {total_overall:>10.2f}")
    print("=" * 28)


def display_expenses(data):
    if not data:
        print("No expenses found for this selection.")
        return

    print(f"\n{'='*10} EXPENSE REPORT {'='*10}")
    total = 0
    for entry in data:
        print("-" * 30)
        for key, value in entry.items():
            print(f"{key.title()}: {value}")
        if isinstance(entry.get('amount'), (int, float)):
            total += entry['amount']
    
    print("-" * 30)
    print(f"TOTAL: {total}")
    print("=" * 30)

def main():
    while True:
        print(f"\n{'='*5} PERSONAL FINANCE TRACKER {'='*5}")
        print("1. Add Expense")
        print("2. View Report")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            capture_expenses()
        elif choice == '2':
            report_expense_data()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
