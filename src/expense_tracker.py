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

    
    def load_expense_tracker(self):
        print("Loading existing expense tracker")


    def view_instructions(self):
        print("Loading instructions")


    def get_user_income(self):
        print("Your income has been successfully recorded!")


    def get_user_expense(self):
        print("Your expense has been successfully recorded!")


    def save_expense_to_file(self, expense_file_path:
        print(f"Expenses saved to {expense_file_path} successfully!")


    def view_expenses(self):
        print("viewing expenses")


    def record_expense(self):
        print ("Recording expense:")

        expense_name = input("Enter the expense name:")
        epxense_amount = float(input("Enter expense amount:"))
        expense_category = input("Enter expense category:")
        expense_date = datetime.date.today()

        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=expense_date)
        self.weekly_data.append(new_expense)

        print(f"Expense recorded: {new_expense}")

class Expense:

    def __init__(self, name, amount, category, date) -> None:
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"<Expense: {self.name}", ${self.amount}, {self.category}, {self.date}>"

