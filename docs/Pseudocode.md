# Pseudocode for T1A3 - Expense Tracker Terminal Application by Ishan Acharya
```
#Start application
Start application
Print("Welcome to Budget Buddy")

#Main menu for application
    DisplayMainMenu()
    UserInput = GetUserInput()
    Print("Choose option 1-4 below")

    #Main Menu
    If UserInput == 1:
        #Create option 1 to create a new expense tracker
        CreateNewExpenseTracker()
        Print("Create New Expense Tracker")
    ElseIf UserInput == 2:
        #Create option 2 to load an existing expense tracker
        LoadExistingExpenseTracker()
        Print("Load Expense Tracker")
    ElseIf UserInput == 3:
        #Create option 3 to view instructions
        ViewInstructions()
        Print("View Instructions")
    ElseIf UserInput == 4:
        #Create option 4 to exit the application
        ExitApplication()
        Print("Exiting application")
End

#Class to hold expense tracker objects
Class Expense_Tracker()

    #list to contain types of income categories
    List.income_categories[]
    List.expense_categories[]

    #list to contain income and expense data
    BudgetData = []

    #Function to create new expense tracker
    Function CreateNewExpenseTracker():
    Print("Creating new expense tracker")

        #Data structure to hold expense tracker data
        DataStructure()

        #Sub within new expense tracker
            #Display sub menu for user input
            SubMenu()
            SubMenuInput = GetUserInput()

            #Sub Menu options
            If SubMenuInput == 1:
                #Add income
                AddIncome()
                Print("Add income")
            ElseIf SubMenuInput == 2:
                #Add expense
                AddExpense()
                Print("Add expense")
            ElseIf SubMenuInput == 3:
                #View budget data
                ViewBudgetData()
                Print("View budget data")
            ElseIf SubMenuInput == 4:
                #Save data
                SaveData()
                Print("Save budget data")
            ElseIf SubMenuInput == 5:
                #Delete entry
                DeleteEntry()
                Print("Delete entry")
            ElseIf SubMenuInput == 6:
                #Export to CSV
                ExportToCSV()
                Print("Export to CSV")
            ElseIf SubMenuInput == 7:
                #Exit sub menu and return to the main menu
                ExitSubMenu()
                Print("Return to main menu")
    End

    #Function to load an existing expense tracker
    Function LoadExistingExpenseTracker():
        #Prompt user for the filename
        Print("Enter file name to load file")
        filename = GetUserInput()

        #Check if the file exists
        If FileExists(filename):
            #Load data from the file
            LoadDataFromFile(filename)
            Print("Data loaded successfully")
        Else:
            #Display error message if the file is not found
            Print("File not found, try again")
    End

    #Function to view instructions
    Function ViewInstructions():
        #Display instructions
        DisplayHelpInstructions()
        Print("view instructions")
        #Wait for user input before returning to the main menu
        WaitForUserInput()
        Print("Press r to return to main menu")
    End

    #Function to exit the application
    Function ExitApp():
        #Set isRunning to false
        isRunning = false
        #Terminate the app
        TerminateApplication()
    End

    #Function to add income
    Function AddIncome():
        #Get details of the income
        incomeDetails = GetIncomeDetails()

        #Validate income details
        If ValidateIncomeDetails(incomeDetails):
            #Add income
            AddIncome(incomeDetails)
            Print("Income added successfully.")
        Else:
            #Display an error message for invalid input
            Print("Invalid input. Please try again.")
    End

    #Function to add expense
    Function AddExpense():
        #Get details of the expense
        expenseDetails = GetExpenseDetails()

        #Validate expense details
        If ValidateExpenseDetails(expenseDetails):
            #Add expense
            AddExpense(expenseDetails)
            Print("Expense added successfully.")
        Else:
            #Display an error message for invalid input
            Print("Invalid input. Please try again.")
    End

    #Function to choose entry category for both income and expense
    Function ChooseDataCategory():
        #Initilaise list categories for income and expense
        If EntryType is "income":
            categories = ExpenseTracker.income_categories
        ElseIf EntryType is "expense":
            categories = ExpenseTracker.expense_categories
    End

    #Function to view budget data
    Function ViewBudgetData():
        #Display summary of recorded income and expenses
        ViewEntries()
        Print("View entries")
        #Wait for user input before returning to the sub menu
        WaitForUserInput()
    End

    #Function to view budget data by category
    Function ViewDataByCategory():
        #Display summary of recorded income and expenses by category
        ViewCategoryEntries()
        Print("View entries by category")
        #Wait for user input before returning to sub menu
        WaitForUserInput()

    # Function to save data
    Function SaveData():
        #Prompt user for a filename for saving
        filename = PromptForFileName()
        #Save current data to the specified file
        SaveDataToFile(filename)
        Print("Data saved successfully")
    End

    #Function to delete an entry
    Function DeleteEntry():
        #Display a list of entries (income and expenses) with indices
        DisplayEntryListWithIndices()
        Print("These are the current entries saved")
        #Get user input for the entry to delete
        entryIndex = GetUserInput()
        Print("Type index number of chosen entry to delete")

        #Validate entry index
        If ValidateEntryIndex(entryIndex):
            #Confirm deletion and update data
            ConfirmDeleteEntry(entryIndex)
            UpdatedEntries(entryIndex)
            Print("Entry has been deleted")
        Else:
            #Display an error message for invalid input
            Print("Invalid input. Please try again")
    End

    #Function to export data to CSV
    Function ExportToCSV():
        #Prompt user for a filename for exporting
        filename = PromptForFileName()
        Print("Enter filename to export data")
        #Export current data to a CSV file
        ExportDataToCSV(filename)
        Print("Data exported to CSV successfully")
    End
```