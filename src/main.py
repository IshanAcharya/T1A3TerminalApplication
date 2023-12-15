from expense_tracker import ExpenseTracker
from colorama import Fore
import emoji

# Main function for application
def main():
    print(f"{Fore.BLACK}{emoji.emojize(':chart_with_upwards_trend:')} Welcome to Budget Buddy, helping you spend smart and live smarter!{Fore.RESET}")

    expense_tracker = ExpenseTracker()
    is_running = True

    while is_running:
        print(f"\n{Fore.GREEN}1. {emoji.emojize(':money_bag:')} Create new Expense Tracker{Fore.RESET}")
        print(f"{Fore.CYAN}2. {emoji.emojize(':open_file_folder:')} Load existing Expense Tracker{Fore.RESET}")
        print(f"{Fore.YELLOW}3. {emoji.emojize(':spiral_notepad:')}  View instructions{Fore.RESET}")
        print(f"{Fore.MAGENTA}4. {emoji.emojize(':door:')} Exit\n{Fore.RESET}")

        choice = input(f"{Fore.BLACK}{emoji.emojize(':input_numbers:')}To get started, please enter which option you'd like to choose (1-4):{Fore.RESET}")

        if choice == "1":
            expense_tracker.create_new_expense_tracker()
        elif choice == "2":
            expense_tracker.load_expense_tracker()
        elif choice == "3":
            expense_tracker.view_instructions()
        elif choice == "4":
            print(f"{Fore.YELLOW} {emoji.emojize(':waving_hand:')}Exiting Budget Buddy. Happy saving!{Fore.RESET}")
            is_running = False
        else:
            print(f"{Fore.RED}{emoji.emojize(':warning:')} Your input is invalid. Please choose a menu option between 1-4.{Fore.RESET}")

if __name__ == "__main__":
    main()