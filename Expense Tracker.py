import json
import os
from datetime import datetime

# Function to load expense data from file
def load_expenses():
    if not os.path.exists('expenses.json'):
        return []
    with open('expenses.json', 'r') as file:
        return json.load(file)

# Function to save expense data to file
def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense():
    while(True):
        try:
            amount = float(input("Enter the amount spent: "))
            break
        except:
            print("Invalid input. Please enter a valid amount.")
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    date = datetime.now().strftime('%Y-%m-%d')

    return {'amount': amount, 'description': description, 'category': category, 'date': date}

# Function to display monthly summaries
def monthly_summary(expenses):
    # Group expenses by month
    monthly_expenses = {}
    for expense in expenses:
        month = expense['date'].split('-')[1]
        if month not in monthly_expenses:
            monthly_expenses[month] = 0
        monthly_expenses[month] += expense['amount']
    
    # Display summaries
    for month, total in monthly_expenses.items():
        print(f"Month: {month}, Total Expenses: ${total:.2f}")

# Function to display category-wise expenditure
def category_expenditure(expenses):
    # Group expenses by category
    category_expenses = {}
    for expense in expenses:
        category = expense['category']
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += expense['amount']
    
    # Display category-wise expenditure
    for category, total in category_expenses.items():
        print(f"Category: {category}, Total Expenses: ${total:.2f}")

# Main function to run the Expense Tracker
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summaries")
        print("3. View Category-wise Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            expense = add_expense()
            expenses.append(expense)
            save_expenses(expenses)
            print("Expense added successfully!")

        elif choice == '2':
            if expenses:
                monthly_summary(expenses)
            else:
                print("No expenses recorded yet!")

        elif choice == '3':
            if expenses:
                category_expenditure(expenses)
            else:
                print("No expenses recorded yet!")

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
