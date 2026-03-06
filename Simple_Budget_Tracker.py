# Simple Budget Tracker

# Ask user for total monthly budget
total_budget = float(input("Enter your total monthly budget: "))

# Ask for 3 expenses
expense1 = float(input("Enter expense 1: "))
expense2 = float(input("Enter expense 2: "))
expense3 = float(input("Enter expense 3: "))

# Calculate total expenses
total_expenses = expense1 + expense2 + expense3

# Calculate remaining balance
remaining_balance = total_budget - total_expenses

# Display remaining balance
print("\n------------------------------")
print(f"Total Budget: ${total_budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
print("------------------------------")