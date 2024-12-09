import os
import json
from datetime import datetime

transactions = []

def add_transaction(trans_type, amount, category):
    transaction = {
        "type": trans_type,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)
    print(f"Transaction added: {transaction}")

def calculate_totals():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = total_income - total_expenses
    return total_income, total_expenses, balance

def save_to_file(filename="budget_data.json"):
    with open(filename, "w") as file:
        json.dump(transactions, file, indent=4)
    print(f"Data saved to {filename}.")

def load_from_file(filename="budget_data.json"):
    global transactions
    if os.path.exists(filename):
        with open(filename, "r") as file:
            transactions = json.load(file)
        print(f"Data loaded from {filename}.")
    else:
        print("No previous data found.")

def display_menu():
    print("\n--- Personal Budget Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Totals and Balance")
    print("4. View Transaction History")
    print("5. Save and Exit")

def main():
    load_from_file()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_transaction("Income", amount, category)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_transaction("Expense", amount, category)
        elif choice == "3":
            total_income, total_expenses, balance = calculate_totals()
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Balance: {balance}")
        elif choice == "4":
            for t in transactions:
                print(t)
        elif choice == "5":
            save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
