from tabulate import tabulate
from colorama import Fore, Style
import emoji
import csv
import click
import datetime

class ExpenseTracker:

    def __init__(self):
        self.weekly_data = []


    def create_new_expense_tracker(self):
        print("Creating new expense tracker")

        # Data structure to store weekly income and expenses

        self.weekly_data = []

        while True: 
            # Sub-menu within options to navigate around application

            print("\nSub-menu:")
            print("1. Add income entry")
            print("2. Add expense entry")
            print("3. View weekly budget")
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
                self.save_expense_to_file(expense_file_path)
            elif sub_choice == "5":
                self.delete_entry()
            elif sub_choice == "6":
                csv_file_path = input("Enter file name to export budget to CSV file:")
                self.export_to_csv(csv_file_path)
            elif sub_choice == "7":
                print("Returning to the main menu.")
                break

            else:
                print("Your input is invalid. Please choose a menu option between 1-7.")
            

    def load_expense_tracker(self):
        print("Loading existing expense tracker")

        file_name = input("Enter the file name of the saved data:")
        
        try: 
            with open(file_name, 'r') as file:
                reader = csv.reader(file)

                for row in reader:
                    name, amount, category, date = row
                    new_expense = Expense(name, float(amount), category, date)
                    self.weekly_data.append(new_expense)
            print(f"Data has been successfully loaded from {file_name}")

        except FileNotFoundError: 
            print(f"Error: File {file_name} could not be found. Please check the file name and try again.")
        
        except Exception as e:
            print(f"Error loading expense data: {e}")
            

    def view_instructions(self):
        print("Welcome to Budget Buddy!\n")
        print("To help you use this application, here are some simple instructions:\n")
        print("1. To create a new expense tracker and start recording your income and expenses, select option 1 from the main menu and follow the sub-menu options.")
        print("2. To load an existing expense tracker, select option 2 from the main menu and type in the filename of the existing expense tracker.")
        print("3. To exit the application, select option 4 from the main menu.\n")
        print("When creating an expense tracker for the first time:")
        print("- First add your weekly income and expenses entries")
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


    def record_income(self):
        print("You are now recording an income.")

        income_name = input("Enter the income name:")
        income_amount = float(input("Enter income amount:").replace(",", ""))
        income_category = input("Enter income category:")
        income_date = datetime.date.today()

        new_income = Income(name=income_name, amount=income_amount, category=income_category, date=income_date)
        self.weekly_data.append(new_income)

        print(f"Income recorded: {new_income}")

    def record_expense(self):
        print("You are now recording an expense.")

        expense_name = input("Enter the expense name:")
        expense_amount = float(input("Enter expense amount:").replace(",", ""))
        expense_category = input("Enter expense category:")
        expense_date = datetime.date.today()

        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=expense_date)
        self.weekly_data.append(new_expense)

        print(f"Expense recorded: {new_expense}")

    def save_expense_to_file(self, expense_file_path):
        try:
            with open(expense_file_path, 'w') as file:
                for expense in self.weekly_data:
                    file.write(f"{expense.name}, {expense.amount}, {expense.category}, {expense.date}")
        
            print(f"Budget data saved to {expense_file_path} successfully!")

        except FileNotFoundError:
            print("Error: File not found. Please check the file path and try again")
        
        except Exception as e:
            print(f"Error saving expense: {e}")

    def view_budget(self):
        print("viewing budget")

        if not self.weekly_data:
            print("Sorry, no data available. Please add your income or expense entries firsst")
            return

        unique_month = set(entry.date.strftime("%B %Y") for entry in self.weekly_data)

        if not unique_month:
            print("You have no available entries available for any month! Please add your entries first.")
            return

        print("List of available months:")
        for index, month in enumerate(unique_month, start=1):
            print(f"{index}. {month}")

        selected_month_index = int(input("Please enter which month you would like to view:"))
        selected_month = list(unique_month)[selected_month_index - 1]

        month_entries = [entry for entry in self.weekly_data if entry.date.strftime("%B %Y") == selected_month]

        incomes = [entry for entry in month_entries if isinstance(entry, Income)]
        expenses = [entry for entry in month_entries if isinstance(entry, Expense)]

        print("\nIncomes:")
        for income in incomes:
            print(income)

        print("\nExpenses:")
        for expense in expenses:
            print(expense)

        print("This is the end of your budget summary.")


    def delete_entry(self):
        print("Deleting an entry:")

        for index, expense in enumerate(self.weekly_data, start=1):
            print(f"{index}. {expense}")

        while True:
            user_input = input("Enter the index of the entry you wish to delete. Or enter 0 if you wish to cancel.")

            if user_input == '0':
                print("Entry deletion cancelled!")
                break
        
        try:
            entry_index = int(user_input)

            if 1 <= entry_index <= len(self.weekly_data):
                del self.weekly_data [entry_index - 1]
                print("You have successfully deleted the entry!")
            else:
                print("Invalid index. Please enter a valid index and try again.")

        except ValueError: 
            print("Invalid input, please enter a valid index and try again.")

    def export_to_csv(self, csv_file_path):
        try:
            with open(csv_file_path, 'w', newline='') as csvfile:
                fieldnames = ['Name', 'Amount','Category', 'Date']
                writer = csv.writer(csvfile)

                writer.writerow(fieldnames)

                for expense in self.weekly_data:
                    writer.writerow([expense.name, expense.amount, expense.category, expense.date])
        
            print(f"Your budget data has been exported to {csv_file_path} sucessfully!")

        except:
            print("There was an error exporting your budget data. Please check the file name and try again.")


class Expense:

    def __init__(self, name, amount, category, date) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"<Expense: {self.name}, {self.amount}, {self.category}, {self.date}>"

class Income:
    def __init__(self, name, amount, category, date) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"<Income: {self.name}, {self.amount}, {self.category}, {self.date}>"