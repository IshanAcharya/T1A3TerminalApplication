from expense_tracker import ExpenseTracker

def main():
    print("Welcome to Budget Buddy, helping you spend smart and live smarter!")

expense_tracker = ExpenseTracker()
is_running = True

while is_running:
    print("Main Menu:")
    print("1. Create new Expense Tracker")
    print("2. Load existing Expense Tracker")
    print("3. View instructions")
    print("4. Exit")

    choice = input("To get started, please enter which option you'd like to choose (1-4):")

    if choice == "1":
        expense_tracker.create_new_tracker()
    elif choice == "2":
        expense_tracker.load_existing_tracker()
    elif choice == "3":
        expense_tracker.view_instructions()
    elif choice == "4":
        print("Exiting Budget Buddy. Happy saving!")
        is_running = False
    else:
        print("Your input is invalid. Please choose a menu option between 1-4.")

if __name__ == "__main__":
    main()