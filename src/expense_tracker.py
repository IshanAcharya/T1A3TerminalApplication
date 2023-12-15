from tabulate import tabulate # Import tabulate to create tables when displaying data
from colorama import Fore # Import colorama to add coloured text within expense tracker
import emoji # Import emoji module to add emojis to expense tracker
import csv #Import csv module to handle csv files
import datetime #Import datetime to implement time and date within expense tracker
import os # Import os to define file path to save/load/export data to user's desktop

# Class for Expense Tracker application
class ExpenseTracker:

    # Lists to define income and expense categories
    income_categories = [
        emoji.emojize(":briefcase: Salary"),
        emoji.emojize(":toolbox: Side Job"),
        emoji.emojize(":chart_increasing: Interest"),
        emoji.emojize(":wrapped_gift: Gift"),
        emoji.emojize(":laptop: Freelance"),
        emoji.emojize(":green_circle: Other")]
    
    expense_categories = [
        emoji.emojize(":shopping_cart: Groceries"),
        emoji.emojize(":gear: Utilities"),
        emoji.emojize(":house: Rent"),
        emoji.emojize(":mortar_board: Mortgage"),
        emoji.emojize(":clapper: Entertainment"),
        emoji.emojize(":car: Transportation"),
        emoji.emojize(":hospital: Health"),
        emoji.emojize(":shirt: Clothing"),
        emoji.emojize(":wrapped_gift: Gifts"),
        emoji.emojize(":red_circle: Other")]

    def __init__(self):
        # Empty list to store monthly income and expense data
        self.monthly_data = []

# Create new Expense Tracker
    def create_new_expense_tracker(self):
        print(f"{Fore.GREEN}{emoji.emojize(':hourglass_not_done:')} Creating new expense tracker...{Fore.RESET}")

        # Data structure to store monthly income and expenses
        self.monthly_data = []

        while True: 
            # Sub-menu within options to navigate around application

            print("\nSub-menu:")
            print(f"{Fore.BLACK}1. {emoji.emojize(':money_bag:')} Add income entry{Fore.RESET}")
            print(f"{Fore.RED}2. {emoji.emojize(':credit_card:')} Add expense entry{Fore.RESET}")
            print(f"{Fore.BLUE}3. {emoji.emojize(':bar_chart:')} View your budget for this month{Fore.RESET}")
            print(f"{Fore.YELLOW}4. {emoji.emojize(':floppy_disk:')} Save budget data{Fore.RESET}")
            print(f"{Fore.CYAN}5. {emoji.emojize(':wastebasket:')} Delete an entry{Fore.RESET}")
            print(f"{Fore.MAGENTA}6. {emoji.emojize(':outbox_tray:')} Export budget to CSV{Fore.RESET}")
            print(f"{Fore.BLACK}7. {emoji.emojize(':backhand_index_pointing_left:')} Return to main menu{Fore.RESET}")

            sub_choice = input(f"{Fore.YELLOW}{emoji.emojize(':input_numbers:')} Please enter which option you'd like to choose (1-7):{Fore.RESET}")

            if sub_choice == "1":
                self.record_income()
            elif sub_choice == "2":
                self.record_expense()
            elif sub_choice == "3":
                self.view_budget()
            elif sub_choice == "4":
                expense_file_path = input(f"{Fore.YELLOW}{emoji.emojize(':file_folder:')} Enter file name to save budget data:{Fore.RESET}")
                self.save_data_to_file(expense_file_path)
            elif sub_choice == "5":
                self.delete_entry()
            elif sub_choice == "6":
                csv_file_name = input(f"{Fore.YELLOW}{emoji.emojize(':file_folder:')} Enter file name to export budget to CSV file:{Fore.RESET}")
                self.export_to_csv(csv_file_name)
            elif sub_choice == "7":
                print(f"{Fore.BLUE}{emoji.emojize(':backhand_index_pointing_left:')} Returning back to the main menu.{Fore.RESET}")
                break

            else:
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Your input is invalid. Please choose a menu option between 1-7.{Fore.RESET}")
            
# Load existing Expense Tracker from a file
    def load_expense_tracker(self):
        print(f"{Fore.GREEN}{emoji.emojize(':hourglass_not_done:')}Loading existing expense tracker...{Fore.RESET}")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        file_name = input(f"{Fore.YELLOW}{emoji.emojize(':file_folder:')} Enter the file name of the saved data:{Fore.RESET}")

        full_file_path = os.path.join(desktop_path, file_name)
        
        try: 
            with open(full_file_path, 'r') as file:
                reader = csv.reader(file)

                self.monthly_data = []

                for row in reader:
                    name, amount, category, date_str = row
                    date_str = date_str.strip()
                    date_format_in_file = '%Y-%m-%d'
                    date = datetime.datetime.strptime(date_str, date_format_in_file).date()

                    if category in self.income_categories:
                        new_entry = Income(name, float(amount), category, date)
                    else:
                        new_entry = Expense(name, float(amount), category, date)
                    self.monthly_data.append(new_entry)

            print(f"{Fore.GREEN}{emoji.emojize(':check_mark_button:')} Data has been successfully loaded from {full_file_path}{Fore.RESET}")

            loaded_successfully = True

        except FileNotFoundError: 
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Error: File {full_file_path} could not be found. Please check the file name and try again.{Fore.RESET}")

            loaded_successfully = False
        
        except Exception as e:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Error loading expense data: {e}{Fore.RESET}")

            loaded_successfully = False
        
        if loaded_successfully:
            while True:
                print("\nSub-menu:")
                print(f"{Fore.GREEN}1. {emoji.emojize(':money_bag:')} Add income entry{Fore.RESET}")
                print(f"{Fore.RED}2. {emoji.emojize(':credit_card:')} Add expense entry{Fore.RESET}")
                print(f"{Fore.BLUE}3. {emoji.emojize(':bar_chart:')} View your budget for this month{Fore.RESET}")
                print(f"{Fore.YELLOW}4. {emoji.emojize(':floppy_disk:')} Save budget data{Fore.RESET}")
                print(f"{Fore.CYAN}5. {emoji.emojize(':wastebasket:')} Delete an entry{Fore.RESET}")
                print(f"{Fore.MAGENTA}6. {emoji.emojize(':outbox_tray:')} Export budget to CSV{Fore.RESET}")
                print(f"{Fore.BLACK}7. {emoji.emojize(':backhand_index_pointing_left:')} Return to main menu{Fore.RESET}")

                sub_choice = input(f"{Fore.YELLOW}{emoji.emojize(':input_numbers:')} Please enter which option you'd like to choose (1-7):{Fore.RESET}")

                if sub_choice == "1":
                    self.record_income()
                elif sub_choice == "2":
                    self.record_expense()
                elif sub_choice == "3":
                    self.view_budget()
                elif sub_choice == "4":
                    expense_file_path = input(f"{Fore.YELLOW}{emoji.emojize(':file_folder:')} Enter file name to save budget data:{Fore.RESET}")
                    self.save_data_to_file(expense_file_path)
                elif sub_choice == "5":
                    self.delete_entry()
                elif sub_choice == "6":
                    csv_file_name = input(f"{Fore.YELLOW}{emoji.emojize(':file_folder:')} Enter file name to export budget to CSV file:{Fore.RESET}")
                    self.export_to_csv(csv_file_name)
                elif sub_choice == "7":
                    print(f"{Fore.BLUE}{emoji.emojize(':backhand_index_pointing_left:')} Returning back to the main menu...{Fore.RESET}")
                    break
                else:
                    print(f"{Fore.RED}{emoji.emojize(':warning:')} Your input is invalid. Please choose a menu option between 1-7.{Fore.RESET}")
        else:
            print(f"{Fore.BLACK}{emoji.emojize(':backhand_index_pointing_left:')} Returning to the main menu...{Fore.RESET}")

# Display instructions on how to use the Expense Tracker application
    def view_instructions(self):
        print("Welcome to Budget Buddy!\n")
        print("To help you use this application, here are some simple instructions:\n")
        print("1. To create a new expense tracker and start recording your income and expenses, select option 1 from the main menu and follow the sub-menu options.")
        print("2. To load an existing expense tracker, select option 2 from the main menu and type in the file name of the existing expense tracker.")
        print("3. To exit the application, select option 4 from the main menu.\n")
        print("When creating an expense tracker for the first time:")
        print("- First add your income and expenses entries")
        print("- When adding your income, you will be prompted to enter the income name, income amount, and income category")
        print("- When adding your expenses, you will be prompted to enter the expense name, expense amount, and expense category")
        print("- You can then view all of your income and expense entries")
        print("- You can delete any income or expense entries as you see fit")
        print("- You can save all of your data and will be prompted to enter a file name to save the data")
        print("- You will also have the ability to export your data to a CSV file for external data keeping/analysis")
        print("- Thank you for using Budget Buddy. I hope you enjoy using it!")

        while True: 
            user_input = input(f"{Fore.YELLOW}{emoji.emojize(':input_latin_lowercase:')} Press r to return to the main menu:{Fore.RESET}").lower()

            if user_input == 'r':
                break
            else: 
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please enter r to return to the main menu.{Fore.RESET}")

# Record new income entry
    def record_income(self):
        print(f"{Fore.GREEN}{emoji.emojize(':money_bag:')} You are now recording an income.{Fore.RESET}")

        while True:
            income_name = input(f"{Fore.GREEN}{emoji.emojize(':money_bag:')} Enter the income name: {Fore.RESET}")
            if income_name.replace(" ", "").isalpha():
                break
            else:
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Sorry your input is invalid. Please make sure the income name only contains text letters and no symbols or numbers.{Fore.RESET}")

        income_amount = float(input(f"{Fore.GREEN}Enter income amount: {Fore.RESET}").replace(",", "").replace("$", ""))
        income_category = self.choose_category("income")
        income_date = datetime.date.today()

        new_income = Income(name=income_name, amount=income_amount, category=income_category, date=income_date)
        self.monthly_data.append(new_income)

        print(f"{Fore.GREEN}{emoji.emojize(':money_bag:')}Income recorded:{Fore.RESET}")
        print(tabulate([(new_income.name, f"{new_income.amount:.2f}", new_income.date)], headers=["Name", "Amount", "Date"], tablefmt="fancy_grid"))


# Record new expense entry
    def record_expense(self):
        print(f"{Fore.RED}{emoji.emojize(':credit_card:')} You are now recording an expense...{Fore.RESET}")

        while True:
            expense_name = input(f"{Fore.YELLOW}{emoji.emojize(':credit_card:')} Enter the expense name: {Fore.RESET}")
            if expense_name.replace(" ", "").isalpha():
                break
            else:
                print(f"{Fore.RED}{emoji.emojize(':warning:')}Sorry your input is invalid. Please make sure the expense name only contains text letters and no symbols or numbers.{Fore.RESET}")

        expense_amount = float(input(f"{Fore.RED}Enter expense amount: {Fore.RESET}").replace(",", "").replace("$", ""))
        expense_category = self.choose_category("expense")
        expense_date = datetime.date.today()

        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category, date=expense_date)
        self.monthly_data.append(new_expense)

        print(f"{Fore.RED}{emoji.emojize(':credit_card:')} Expense recorded:{Fore.RESET}")
        print(tabulate([(new_expense.name, f"{new_expense.amount:.2f}", new_expense.date)], headers=["Name", "Amount", "Date"], tablefmt="fancy_grid"))


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
                selected_index = int(input(f"{Fore.BLUE}Enter your category:{Fore.RESET}"))
                if 1 <= selected_index <= len(categories):
                    return categories[selected_index -1]
                else:
                    print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please enter a valid category.{Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please enter a number.{Fore.RESET}")

# Save data to file
    def save_data_to_file(self, file_name):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        expense_file_path = os.path.join(desktop_path, file_name)

        try:
            with open(expense_file_path, 'w') as file:
                for expense in self.monthly_data:
                    file.write(f"{expense.name}, {expense.amount}, {expense.category}, {expense.date}\n")
        
            print(f"{Fore.GREEN}{emoji.emojize(':check_mark_button:')} Budget data saved to {expense_file_path} successfully!{Fore.RESET}")

        except FileNotFoundError:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Error: File not found. Please check the file path and try again{Fore.RESET}")
        
        except Exception as e:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Error saving expense: {e}{Fore.RESET}")

# View list of income and expense entries for specific month
    def view_budget(self):
        print(f"{Fore.CYAN}viewing budget...{Fore.RESET}")

        if not self.monthly_data:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Sorry, no data available. Please add your income or expense entries first.{Fore.RESET}")
            return

        unique_month = set(entry.date.strftime("%B %Y") for entry in self.monthly_data)

        if not unique_month:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} You have no available entries available for any month! Please add your entries first.{Fore.RESET}")
            return

        print(f"{Fore.CYAN}List of available months:{Fore.RESET}")
        for index, month in enumerate(unique_month, start=1):
            print(f"{index}. {month}")

        while True:
            try:
                selected_month_index = int(input(f"{Fore.CYAN}Please enter which month you would like to view:{Fore.RESET}"))
                selected_month = list(unique_month)[selected_month_index - 1]
            except  (ValueError, IndexError):
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please enter a valid number to select a month.{Fore.RESET}")
                continue

            month_entries = [entry for entry in self.monthly_data if entry.date.strftime("%B %Y") == selected_month]

            incomes = [entry for entry in month_entries if isinstance(entry, Income)]
            expenses = [entry for entry in month_entries if isinstance(entry, Expense)]

            print("\nView Options:")
            print(f"{Fore.YELLOW}1. View your entries for a specific month{Fore.RESET}")
            print(f"{Fore.GREEN}2. View your entries sorted by category for a specific month{Fore.RESET}")

            while True:
                option = input(f"{Fore.BLUE}Please enter your choice (1 or 2):{Fore.RESET}")
                if option in {"1", "2"}:
                    break
                else: 
                    print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please choose 1 or 2.{Fore.RESET}")

            if option == "1":
                print(f"\n{emoji.emojize(':spiral_notepad:')}Entries for {selected_month}:")

                print(f"{Fore.GREEN}{emoji.emojize(':money_bag:')} Incomes{Fore.RESET}")
                print(tabulate([(income.name, f"{income.amount:.2f}", income.date) for income in incomes], headers=["Name", "Amount", "Date"], tablefmt="fancy_grid"))
            
                print(f"\n{Fore.RED}{emoji.emojize(':credit_card:')} Expenses:{Fore.RESET}")
                print(tabulate([(expense.name, f"{expense.amount:.2f}", expense.date) for expense in expenses], headers=["Name", "Amount", "Date"], tablefmt="fancy_grid"))

                self.display_entry_total(incomes, expenses)

            elif option == "2":
                self.view_by_category(selected_month, month_entries)
                self.display_entry_total(incomes, expenses)

            print(f"{Fore.CYAN}{emoji.emojize(':bar_chart:')} This is the end of your budget summary.{Fore.RESET}")

    def display_entry_total(self, incomes, expenses):
        total_income = sum(income.amount for income in incomes)
        total_expense = sum(expense.amount for expense in expenses)

        print(f"\n{Fore.GREEN}{emoji.emojize(':money_bag:')} Total Income: ${total_income:.2f}{Fore.RESET}")
        print(f"{Fore.RED}{emoji.emojize(':credit_card:')} Total Expenses: ${total_expense:.2f}{Fore.RESET}")

# View list of income and expense entries sorted by category for a specific month
    def view_by_category(self, selected_month, month_entries):

        income_categories = ExpenseTracker.income_categories
        expense_categories = ExpenseTracker.expense_categories

        print(f"\n{Fore.GREEN}{emoji.emojize(':money_bag:')} Income Categories:{Fore.RESET}")
        for i, category in enumerate(income_categories, start=1):
            print(f"{i}. {category}")
                  
        print(f"\n{Fore.RED}{emoji.emojize(':credit_card:')} Expense Categories:{Fore.RESET}")
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

        print(f"\n{emoji.emojize(':spiral_notepad:')}Entries for {selected_month} by category:")
        for entry in filtered_entries:
            print(entry)

# Delete income or expense entries
    def delete_entry(self):
        print(f"{Fore.RED}{emoji.emojize(':wastebasket:')} Deleting an entry:{Fore.RESET}")

        for index, entry in enumerate(self.monthly_data, start=1):
            print(f"{index}. {entry}")

        while True:
            user_input = input(f"{Fore.YELLOW}{emoji.emojize(':input_numbers:')} Enter the index of the entry you wish to delete. Or enter 0 if you wish to cancel.{Fore.RESET}")

            if user_input == '0':
                print(f"{Fore.RED}{emoji.emojize(':red_exclamation_mark:')}Entry deletion cancelled!{Fore.RESET}")
                return
            try:
                entry_index = int(user_input)

                if 1 <= entry_index <= len(self.monthly_data):
                    del self.monthly_data[entry_index - 1]
                    print(f"{Fore.GREEN}{emoji.emojize(':check_mark_button:')} You have successfully deleted the entry!{Fore.RESET}")
                    break
                else:
                    print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input. Please enter a valid input and try again.{Fore.RESET}")

            except ValueError: 
                print(f"{Fore.RED}{emoji.emojize(':warning:')} Invalid input, please enter a valid index and try again.{Fore.RESET}")

        print(f"\n{Fore.CYAN}{emoji.emojize(':spiral_notepad:')} Updated list of entries:{Fore.RESET}")
        for index, expense in enumerate(self.monthly_data, start=1):
            print(f"{index}. {expense}")

# Export budget data to CSV file
    def export_to_csv(self, csv_file_name):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        csv_file_path = os.path.join(desktop_path, csv_file_name + ".csv")

        try:
            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(['Name', 'Amount', 'Category', 'Date'])

                for income in self.monthly_data:
                    writer.writerow([income.name, income.amount, income.category, income.date])
                else: 
                    for expense in self.monthly_data:
                        writer.writerow([expense.name, expense.amount, expense.category, expense.date])
        
            print(f"{Fore.GREEN}{emoji.emojize(':outbox_tray:')} Your budget data has been exported to {csv_file_path} sucessfully!{Fore.RESET}")

        except Exception as e:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} There was an error exporting your budget data. Please check the file name and try again.{Fore.RESET}")

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
# String representation
    def __repr__(self):
        return f"<Income: {self.name}, {self.amount}, {self.category}, {self.date}>"