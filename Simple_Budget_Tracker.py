# Simple Budget Tracker with Warning

# Ask user for total monthly budget
total_budget = float(input("Enter your total monthly budget (LKR): "))

# Ask for 3 expenses
expense1 = float(input("Enter expense 1 (LKR): "))
expense2 = float(input("Enter expense 2 (LKR): "))
expense3 = float(input("Enter expense 3 (LKR): "))

# Calculate total expenses
total_expenses = expense1 + expense2 + expense3

# Calculate remaining balance
remaining_balance = total_budget - total_expenses

# Display remaining balance
print("\n------------------------------")
print(f"Total Budget: LKR {total_budget:.2f}")
print(f"Total Expenses: LKR {total_expenses:.2f}")
print(f"Remaining Balance: LKR {remaining_balance:.2f}")
print("------------------------------")

# Check for low funds
if remaining_balance < 500:
    print("Warning: Low Funds")