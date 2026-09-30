
expenses = []

small_expense = 0
medium_expense = 0
large_expense = 0

expense = 1

while expense != 0:
    expense = float(input("Enter an expense or 0 to finish: "))
    if expense > 0:
        expenses.append(float(expense))
    elif expense < 0:
        print("Invalid expense, please enter another.")

for i in expenses:
    if i < 25:
        small_expense += 1
    elif i >= 25 and i <= 100:
        medium_expense += 1
    else:
        large_expense += 1

total_expenses = len(expenses)
total_amount = sum(expenses)
average_expense = total_amount / total_expenses
smallest_expense = min(expenses)
largest_expense = max(expenses)

print(f"\nExpense Summary:")
print(f"Number of expenses: {total_expenses}")
print(f"Total: ${total_amount:,.2f}")
print(f"Average: ${average_expense:,.2f}")
print(f"Smallest expense: ${smallest_expense:,.2f}")
print(f"Largest expense: ${largest_expense:,.2f}")

print(f"\nSmall expenses: {small_expense}")
print(f"Moderate expenses: {medium_expense}")
print(f"Large expenses: {large_expense}")