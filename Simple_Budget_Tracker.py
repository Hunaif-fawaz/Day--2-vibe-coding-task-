# Budget Tracker with Multiple Expenses

# Ask user for total monthly budget
total_budget = float(input("Enter your total monthly budget (LKR): "))

# Initialize list to store expenses
expenses = []

# Loop to enter multiple expenses
while True:
    expense_input = input("Enter an expense (type 'done' to finish): ")
    if expense_input.lower() == "done":
        break
    try:
        expense_amount = float(expense_input)
        expenses.append(expense_amount)
    except ValueError:
        print("Please enter a valid number or 'done'.")

# Calculate total expenses
total_expenses = sum(expenses)

# Calculate remaining balance
remaining_balance = total_budget - total_expenses

# Display summary
print("\n------------------------------")
print(f"Total Budget: LKR {total_budget:.2f}")
print(f"Total Expenses: LKR {total_expenses:.2f}")
print(f"Remaining Balance: LKR {remaining_balance:.2f}")
print("------------------------------")

# Check for low funds
if remaining_balance < 500:
    print("Warning: Low Funds")