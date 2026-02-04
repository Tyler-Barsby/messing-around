# messing-around

## [Clean-Structure.py](https://github.com/Tyler-Barsby/messing-around/blob/c4eebde8afb0e8c036aa0ecc1b50552da4895bad/Clean-Structure.py)

The purpose of this script is scan file names and rename them according to a set **naming convention**.

#### get_target_folders()
The below function reads the **[folders.md](https://github.com/Tyler-Barsby/messing-around/blob/c4eebde8afb0e8c036aa0ecc1b50552da4895bad/folders.md)** file and determines which sub-directories to open and clean. 
![get target folders function](/Assets/get_target_folders.png "get_target_folders function")

#### clean_files_in_targets()
This function uses the array from the previous function to iterate through and rename the files within to the set convention.
![get target folders function](/Assets/clean_files_in_targets.png "clean_files_in_targets")


## [Cli-Personal-Finance-Tracker.py](LINK_PLACEHOLDER)

A command-line tool to track expenses and view reports by category.

#### capture_expenses()
Handles the user input process to capture expense amount, category, and date, then saves it to the CSV file.
![capture expenses function](IMAGE_PLACEHOLDER "capture_expenses")

#### report_expense_data()
Guides the user through filtering expenses by category, viewing all expenses, or generating a summary report.
![report expense data function](IMAGE_PLACEHOLDER "report_expense_data")

#### display_category_summary()
Aggregates total expenses for each category and displays them in a formatted summary table.
![display category summary function](IMAGE_PLACEHOLDER "display_category_summary")

### Example Output Data
Based on `Python/finance-tracker-assets/expenses.csv`:

| ID | Amount | Category | Date |
| :--- | :---: | :--- | :---: |
| 2026-01-22 19:53:49.242550 | 100.0 | General | 01/05/2007 |
| 20260204153637 | 1000.0 | Transfer | 04/02/2026 |

**Total**: 1100.0
