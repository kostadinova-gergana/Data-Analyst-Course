# Personal Budget Tracker

# Define variables
monthly_budget = 0.0  # Initial budget set to 0.0
expenses = []  # List to store expenses

# Function to set the monthly budget
def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter your monthly budget: "))
    print(f"Monthly budget set to ${monthly_budget:.2f}")

# Function to add an expense ith a description and amount.
def add_expense():
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount of the expense: "))
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description} (${amount:.2f})")

# Function to display all expenses
def display_expenses():
    """
    Displays all the expenses.
    """
    print("\nExpenses:")
    for expense in expenses:
        print(f"- {expense['description']}: ${expense['amount']:.2f}")

# Function to calculate and display the remaining budget
def remaining_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    remaining = monthly_budget - total_expenses
    print(f"Remaining budget: ${remaining:.2f}")

# Main program loop at displays options to the user and performs actions based on the user's choice.
while True:
    print("\nOptions:")
    print("1. Set monthly budget")
    print("2. Add expense")
    print("3. Display all expenses")
    print("4. Calculate remaining budget")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        display_expenses()
    elif choice == '4':
        remaining_budget()
    elif choice == '5':
        print("Thank you for using the Personal Budget Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
