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

        self.weeky_data = []

        while True: 
            # Sub-menu within option 1

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


    def view_instructions(self):
        print("Loading instructions")


    def record_income(self):
        print("Your income has been successfully recorded!")

    def record_expense(self):
        print("Recording expense:")

        expense_name = input("Enter the expense name:")
        epxense_amount = float(input("Enter expense amount:"))
        expense_category = input("Enter expense category:")
        expense_date = datetime.date.today()

        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=expense_date)
        self.weekly_data.append(new_expense)

        print(f"Expense recorded: {new_expense}")

    def save_expense_to_file(self, expense_file_path:
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
            with open(csv_file_path, 'w', newline' ') as csvfile:
            fieldnames = ['Name', 'Amount', 'Category', Date']
            write = csv.writer(csvfile)

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
        return f"<Expense: {self.name}", ${self.amount}, {self.category}, {self.date}>"

