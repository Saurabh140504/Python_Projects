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

#----------------------- DAY 2 -----------------------------------
# Budget Check & Expense Analytics

def check_budget():
    """
    Check whether total expense exceeds budget.
    """
    total = calculate_total()

    if total > BUDGET:
        print("Budget exceeded.")
    elif total == BUDGET:
        print("Budget fully utilized.")
    else:
        print("You are within budget.")


def category_summary():
    """
    Category-wise expense summary.
    """
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("Category Summary:")
    for key in summary:
        print(key, ":", summary[key])


def show_high_expenses():
    """
    Show expenses above user-defined amount.
    """
    threshold = float(input("Enter minimum amount: "))
    result = list(filter(lambda x: x["amount"] > threshold, expenses))

    if len(result) == 0:
        print("No high expenses found.")
    else:
        for exp in result:
            print(exp)


def unique_categories():
    """
    Display unique expense categories.
    """
    cat_set = set(map(lambda x: x["category"], expenses))
    print("Unique Categories:", cat_set)

# ----------------------- DAY 3 -------------------------------

# Date Analysis & Final Integration

def monthly_expense():
    """
    Calculate expense for a specific month.
    """
    month = int(input("Enter month (1-12): "))
    total = 0

    for exp in expenses:
        date_obj = datetime.strptime(exp["date"], "%Y-%m-%d")
        if date_obj.month == month:
            total += exp["amount"]

    print("Total expense for month:", total)


def generate_report():
    """
    Generate final expense report.
    """
    print("\n===== EXPENSE REPORT =====")
    print("Date:", datetime.now().strftime("%Y-%m-%d"))
    print("Total Expense:", calculate_total())
    category_summary()
    check_budget()
    print("==========================\n")


def main():
    while True:
        print("\n1.Add Expense  2.View Expenses  3.Total")
        print("4.Category Summary  5.Check Budget")
        print("6.High Expenses  7.Unique Categories")
        print("8.Monthly Expense  9.Generate Report")
        print("10.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Total:", calculate_total())
        elif choice == "4":
            category_summary()
        elif choice == "5":
            check_budget()
        elif choice == "6":
            show_high_expenses()
        elif choice == "7":
            unique_categories()
        elif choice == "8":
            monthly_expense()
        elif choice == "9":
            generate_report()
        elif choice == "10":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()