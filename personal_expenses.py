#Empty list where inputs can be appended to
expenses = []

#Sets the count to 0
small_expense = 0
medium_expense = 0
large_expense = 0

#Allows the first while loop to run as the condition is not true
expense = 1

#While loop that will allow the user to input as many expenses as they would like and return an error if they enter 
#a negative number
while expense != 0:
    expense = float(input("Enter an expense or 0 to finish: "))
    if expense > 0:
        expenses.append(float(expense))
    elif expense < 0:
        print("Invalid expense, please enter another.")

#Sorts the inputted answers into small, medium, or large expenses and counts the amounts in each respective category
for i in expenses:
    if i < 25:
        small_expense += 1
    elif i >= 25 and i <= 100:
        medium_expense += 1
    else:
        large_expense += 1

#Uses different functions to find the length, sum, average, min, and max of the inputted values.
total_expenses = len(expenses)
total_amount = sum(expenses)
average_expense = total_amount / total_expenses
smallest_expense = min(expenses)
largest_expense = max(expenses)

#Prints out the results and formats inlcuding: total inputs, sum, average, min, max, and the amount in each category (S, M, L)
print(f"\nExpense Summary:")
print(f"Number of expenses: {total_expenses}")
print(f"Total: ${total_amount:,.2f}")
print(f"Average: ${average_expense:,.2f}")
print(f"Smallest expense: ${smallest_expense:,.2f}")
print(f"Largest expense: ${largest_expense:,.2f}")

print(f"\nSmall expenses: {small_expense}")
print(f"Moderate expenses: {medium_expense}")
print(f"Large expenses: {large_expense}")