#------------------ DAY 1 -------------------------------
# Smart Expense Management System

from datetime import datetime
from functools import reduce

CATEGORIES = ("food", "transport", "shopping", "bills", "other")
expenses = []
BUDGET = 20000


def add_expense():
    """
    Add a new expense entered by user.
    """
    print("Available Categories:", CATEGORIES)

    amount = float(input("Enter amount: "))
    category = input("Enter category: ").strip().lower()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    description = input("Enter description: ").strip().lower()

    if category not in CATEGORIES:
        category = "other"

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    """
    Display all expenses.
    """
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for exp in expenses:
        print("--------------------------------")
        for key in exp:
            print(key.capitalize(), ":", exp[key])


def calculate_total():
    """
    Calculate total expense using reduce.
    """
    if len(expenses) == 0:
        return 0

    amounts = list(map(lambda x: x["amount"], expenses))
    return reduce(lambda x, y: x + y, amounts)