from tabulate import tabulate
from colorama import Fore, Style
import emoji
import csv
import click
import datetime
import os

# Class for Expense Tracker application
class ExpenseTracker:

    # Lists to define income and expense categories
    income_categories = ["Salary", "Side Job", "Interest", "Gift", "Freelance", "Other"]
    expense_categories = ["Groceries", "Utilities", "Rent", "Mortgage", "Entertainment", "Transportation", "Health", "Clothing", "Gifts", "Other"]

    def __init__(self):
        # Empty list to store monthly income and expense data
        self.monthly_data = []

# Create new Expense Tracker
    def create_new_expense_tracker(self):
        print("Creating new expense tracker")

        # Data structure to store monthly income and expenses
        self.monthly_data = []

        while True: 
            # Sub-menu within options to navigate around application

            print("\nSub-menu:")
            print("1. Add income entry")
            print("2. Add expense entry")
            print("3. View your budget for this month")
            print("4. Save budget data")
            print("5. Delete an entry")
            print("6. Export budget to CSV")
            print("7. Return to main menu")

            sub_choice = input("Please enter which option you'd like to choose (1-7):")

            if sub_choice == "1":
                self.record_income()
            elif sub_choice == "2":
                self.record_expense()
            elif sub_choice == "3":
                self.view_budget()
            elif sub_choice == "4":
                expense_file_path = input("Enter file name to save budget data:")
                self.save_data_to_file(expense_file_path)
            elif sub_choice == "5":
                self.delete_entry()
            elif sub_choice == "6":
                csv_file_name = input("Enter file name to export budget to CSV file:")
                self.export_to_csv(csv_file_name)
            elif sub_choice == "7":
                print("Returning back to the main menu.")
                break

            else:
                print("Your input is invalid. Please choose a menu option between 1-7.")
            
# Load existing Expense Tracker from a file
    def load_expense_tracker(self):
        print("Loading existing expense tracker...")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        file_name = input("Enter the file name of the saved data:")

        full_file_path = os.path.join(desktop_path, file_name)
        
        try: 
            with open(full_file_path, 'r') as file:
                reader = csv.reader(file)

                self.monthly_data = []

                for row in reader:
                    name, amount, category, date = row
                    new_expense = Expense(name, float(amount), category, date)
                    self.monthly_data.append(new_expense)

            print(f"Data has been successfully loaded from {full_file_path}")

            loaded_successfully = True

        except FileNotFoundError: 
            print(f"Error: File {full_file_path} could not be found. Please check the file name and try again.")

            loaded_successfully = False
        
        except Exception as e:
            print(f"Error loading expense data: {e}")

            loaded_successfully = False
        
        if loaded_successfully:
            while True:
                print("\nSub-menu:")
                print("1. Add income entry")
                print("2. Add expense entry")
                print("3. View your budget for this month")
                print("4. Save budget data")
                print("5. Delete an entry")
                print("6. Export budget to CSV")
                print("7. Return to main menu")

                sub_choice = input("Please enter which option you'd like to choose (1-7):")

                if sub_choice == "1":
                    self.record_income()
                elif sub_choice == "2":
                    self.record_expense()
                elif sub_choice == "3":
                    self.view_budget()
                elif sub_choice == "4":
                    expense_file_path = input("Enter file name to save budget data:")
                    self.save_data_to_file(expense_file_path)
                elif sub_choice == "5":
                    self.delete_entry()
                elif sub_choice == "6":
                    csv_file_name = input("Enter file name to export budget to CSV file:")
                    self.export_to_csv(csv_file_name)
                elif sub_choice == "7":
                    print("Returning back to the main menu.")
                    break
                else:
                    print("Your input is invalid. Please choose a menu option between 1-7.")
        else:
            print("Returning to the main menu.")

# Display instructions on how to use the Expense Tracker application
    def view_instructions(self):
        print("Welcome to Budget Buddy!\n")
        print("To help you use this application, here are some simple instructions:\n")
        print("1. To create a new expense tracker and start recording your income and expenses, select option 1 from the main menu and follow the sub-menu options.")
        print("2. To load an existing expense tracker, select option 2 from the main menu and type in the filename of the existing expense tracker.")
        print("3. To exit the application, select option 4 from the main menu.\n")
        print("When creating an expense tracker for the first time:")
        print("- First add your income and expenses entries")
        print("- When adding your income, you will be prompted to enter the income name, income amount, income category, and income date")
        print("- When adding your expenses, you will be prompted to enter the expense name, expense amount, expense category, and expense date")
        print("- You can then view all of your income and expense entries")
        print("- You can delete any income or expense entries as you see fit")
        print("- You can save all of your data and will be prompted to enter a filepath to save the data")
        print("- You will also have the ability to export your data to a CSV file for external data keeping/analysis")
        print("- Thank you for using Budget Buddy. I hope you enjoy using it!")

        while True: 
            user_input = input("Press r to return to the main menu:").lower()

            if user_input == 'r':
                break
            else: 
                print("Invalid input. Please enter r to return to the main menu.")

# Record new income entry
    def record_income(self):
        print("You are now recording an income.")

        while True:
            income_name = input("Enter the income name: ")
            if income_name.replace(" ", "").isalpha():
                break
            else:
                print("Sorry your input is invalid. Please make sure the income name only contains text letters and no symbols or numbers.")

        income_amount = float(input("Enter income amount: ").replace(",", "").replace("$", ""))
        income_category = self.choose_category("income")
        income_date = datetime.date.today()

        new_income = Income(name=income_name, amount=income_amount, category=income_category, date=income_date)
        self.monthly_data.append(new_income)

        print(f"Income recorded: {new_income}")

# Record new expense entry
    def record_expense(self):
        print("You are now recording an expense.")

        while True:
            expense_name = input("Enter the expense name: ")
            if expense_name.replace(" ", "").isalpha():
                break
            else:
                print("Sorry your input is invalid. Please make sure the expense name only contains text letters and no symbols or numbers.")

        expense_amount = float(input("Enter expense amount: ").replace(",", "").replace("$", ""))
        expense_category = self.choose_category("expense")
        expense_date = datetime.date.today()

        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=expense_date)
        self.monthly_data.append(new_expense)

        print(f"Expense recorded: {new_expense}")

# Choose income and expense entry categories
    def choose_category(self, entry_type):
        if entry_type == "income":
            categories = ExpenseTracker.income_categories
        elif entry_type == "expense":
            categories = ExpenseTracker.expense_categories
        else:
            return "Other"
        
        print("\nSelect a category:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        while True:
            try:
                selected_index = int(input("Enter your category:"))
                if 1 <= selected_index <= len(categories):
                    return categories[selected_index -1]
                else:
                    print("Invalid input. Please enter a valid category.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Save data to file
    def save_data_to_file(self, file_name):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        expense_file_path = os.path.join(desktop_path, file_name)

        try:
            with open(expense_file_path, 'w') as file:
                for expense in self.monthly_data:
                    file.write(f"{expense.name}, {expense.amount}, {expense.category}, {expense.date}\n")
        
            print(f"Budget data saved to {expense_file_path} successfully!")

        except FileNotFoundError:
            print("Error: File not found. Please check the file path and try again")
        
        except Exception as e:
            print(f"Error saving expense: {e}")

# View list of income and expense entries for specific month
    def view_budget(self):
        print("viewing budget")

        if not self.monthly_data:
            print("Sorry, no data available. Please add your income or expense entries first")
            return

        unique_month = set(entry.date.strftime("%B %Y") for entry in self.monthly_data)

        if not unique_month:
            print("You have no available entries available for any month! Please add your entries first.")
            return

        print("List of available months:")
        for index, month in enumerate(unique_month, start=1):
            print(f"{index}. {month}")

        selected_month_index = int(input("Please enter which month you would like to view:"))
        selected_month = list(unique_month)[selected_month_index - 1]

        month_entries = [entry for entry in self.monthly_data if entry.date.strftime("%B %Y") == selected_month]

        incomes = [entry for entry in month_entries if isinstance(entry, Income)]
        expenses = [entry for entry in month_entries if isinstance(entry, Expense)]

        print("\nView Options:")
        print("1. View your entries for a specific month")
        print("2. View your entries sorted by category for a specific month")

        option = input("Please enter your chocie (1 or 2):")

        if option == "1":
            print(f"\nEntries for {selected_month}:")

            print("\nIncomes:")
            for income in incomes:
                print(f"{income.name}: ${income.amount:.2f} ({income.date})")
            
            print("\nExpenses:")
            for expense in expenses:
                print(f"{expense.name}: ${expense.amount:.2f} ({expense.date})")

            self.display_entry_total(incomes, expenses)

        elif option == "2":
            self.view_by_category(selected_month, month_entries)
            self.display_entry_total(incomes, expenses)

        print("This is the end of your budget summary.")

    def display_entry_total(self, incomes, expenses):
        total_income = sum(income.amount for income in incomes)
        total_expense = sum(expense.amount for expense in expenses)

        print(f"\nTotal Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")

# View list of income and expense entries sorted by category for a specific month
    def view_by_category(self, selected_month, month_entries):

        income_categories = ExpenseTracker.income_categories
        expense_categories = ExpenseTracker.expense_categories

        print("\nIncome Categories:")
        for i, category in enumerate(income_categories, start=1):
            print(f"{i}. {category}")
                  
        print("\nExpense Categories:")
        for i, category in enumerate(expense_categories, start=1):
            print(f"{i}. {category}")

        selected_income_category = int(input("Select an income category to display:"))
        selected_expense_category = int(input("Select an expense category to display:"))

        filtered_entries = []
        for entry in month_entries:
            if selected_income_category == 0 and isinstance(entry, Income):
                filtered_entries.append(entry)
            elif selected_expense_category == 0 and isinstance(entry, Expense):
                filtered_entries.append(entry)
            elif isinstance(entry, Income) and entry.category == income_categories[selected_income_category -1]:
                filtered_entries.append(entry)
            elif isinstance(entry, Expense) and entry.category == expense_categories[selected_expense_category -1]:
                filtered_entries.append(entry)

        print(f"\nEntries for {selected_month} by category:")
        for entry in filtered_entries:
            print(entry)

# Delete income or expense entries
    def delete_entry(self):
        print("Deleting an entry:")

        for index, entry in enumerate(self.monthly_data, start=1):
            print(f"{index}. {entry}")

        while True:
            user_input = input("Enter the index of the entry you wish to delete. Or enter 0 if you wish to cancel.")

            if user_input == '0':
                print("Entry deletion cancelled!")
                return
            try:
                entry_index = int(user_input)

                if 1 <= entry_index <= len(self.monthly_data):
                    del self.monthly_data[entry_index - 1]
                    print("You have successfully deleted the entry!")
                    break
                else:
                    print("Invalid input. Please enter a valid input and try again.")

            except ValueError: 
                print("Invalid input, please enter a valid index and try again.")

        print("\nUpdated list of entries:")
        for index, expense in enumerate(self.monthly_data, start=1):
            print(f"{index}. {expense}")

# Export budget data to CSV file
    def export_to_csv(self, csv_file_name):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        csv_file_path = os.path.join(desktop_path, csv_file_name)

        try:
            with open(csv_file_path, 'w', newline='') as csvfile:
                fieldnames = ['Name', 'Amount','Category', 'Date']
                writer = csv.writer(csvfile)

                writer.writerow(fieldnames)

                for expense in self.monthly_data:
                    writer.writerow([expense.name, expense.amount, expense.category, expense.date])
        
            print(f"Your budget data has been exported to {csv_file_path} sucessfully!")

        except Exception as e:
            print("There was an error exporting your budget data. Please check the file name and try again.")

# Class for expense objects
class Expense:

    def __init__(self, name, amount, category, date) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"<Expense: {self.name}, {self.amount}, {self.category}, {self.date}>"

# Class for income objects
class Income:
    def __init__(self, name, amount, category, date) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"<Income: {self.name}, {self.amount}, {self.category}, {self.date}>"