import json
from datetime import datetime

# Load expenses from a file


def load_expenses(file_name='expenses.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No existing expenses found, starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Error reading expenses file. Starting fresh.")
        return []

# Save expenses to a file


def save_expenses(expenses, file_name='expenses.json'):
    try:
        with open(file_name, 'w') as file:
            json.dump(expenses, file)
    except IOError:
        print("Error saving expenses. Please check file permissions.")

# Add an expense


def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category: ")
        date = datetime.now().strftime("%Y-%m-%d")
        expenses.append({"amount": amount, "description": description,
                        "category": category, "date": date})
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

# Show monthly summary of expenses


def monthly_summary(expenses):
    monthly_expenses = {}
    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM
        if month not in monthly_expenses:
            monthly_expenses[month] = 0
        monthly_expenses[month] += expense["amount"]
    for month, total in monthly_expenses.items():
        print(f"Total for {month}: ${total:.2f}")

# Show category-wise summary of expenses


def category_summary(expenses):
    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += expense["amount"]
    for category, total in category_expenses.items():
        print(f"Total for {category}: ${total:.2f}")

# Main menu to navigate through different functionalities


def main_menu():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            monthly_summary(expenses)
        elif choice == '3':
            category_summary(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point of the application
if __name__ == "__main__":
    main_menu()
