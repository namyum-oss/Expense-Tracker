end = False
expense_list = []
while end == False:

    print("\n Menu: \n 1. Add Expense \n 2. View all Expenses \n 3. View total Expenditure \n 4. View Expenses by Category \n 5. Exit")
    x = input("Enter your choice: ")
    print()
   
    if x == '1':
        print("Adding expense...\n")
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expense = {
            "Description": description,
            "Amount": amount,
            "Category": category
        }
        expense_list.append(expense)
        print("Expense added successfully!")
   
    elif x == '2':
        print("Displaying expenses...\n")
        if not expense_list:
            print("No expenses recorded.")
            continue
        for exp in expense_list:
                    print(f"Description: {exp['Description']}, Amount: {exp['Amount']}, Category: {exp['Category']}")

    elif x == '3':
        print("Calculating total expenditure...\n")
        total = 0
        for i in expense_list:
            total += i['Amount']
        print(f"Total Expenditure: {total}")                
   
    elif x == '5':
        print("Exiting...")
        end = True
   
    else:
        print("Invalid Choice. Please select a valid option from the menu.")

print("Thank you for using the Expense Tracker. Goodbye!")  
     