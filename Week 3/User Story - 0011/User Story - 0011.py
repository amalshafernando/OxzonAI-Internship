'''
User Story - 0011 - Project 1 Personal Budget Tracker
● Objective : Help users track their income and expenses.
● Key Concepts
○ Lists and dictionaries for storing transactions.
○ Basic arithmetic for calculating totals.
○ File handling for saving and loading data.
● Features
○ Input income and expenses with categories.
○ Calculate total income, total expenses, and balance.
○ Save the budget history to a file and load it at the start.
● Bonus
○ Add date and time tracking for each transaction

'''

import os
import datetime

#initialize data structures
transactions = []

#Menu function
def show_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add income")
    print("2. Add expense")
    print("3. View Transactions")
    print("4. View Summary")
    print("5. Save data")
    print("6. Load data")
    print("7. Exit\n")
 
 
def add_transaction(transaction_type):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "timestamp": timestamp
     }
    transactions.append(transaction)
    print(f"{transaction_type} added successfully!")


# allow all users to see all recorded transactions
def view_transactions():
    if not transactions:
        print("No transactions recorded.")
        return
    print("\nTransactions:")
    for t in transactions:
        print(f"[{t['timestamp']}], {t['type']} - ${t['amount']} ({t['category']})")

def view_summary():
    total_income = sum(t['amount'] for t in transactions if t['type'] == "Income")
    total_expense = sum(t['amount'] for t in transactions if t['type'] =="Expense")
    balance = total_income - total_expense
    print("\nSummery")
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    print(f"Balance: ${balance}")
    
    
def save_data(filename="budget_data.txt"):
    with open(filename, "w") as file:
        for t in transactions:
            file.write(f"{t['type']},{t['amount']},{t['category']},{t['timestamp']}\n")
    print("Data saved successfully!")

def load_data(filename="budget_data.txt"):
    if not os.path.exists(filename):
        print("No saved data found.")
        return
    with open(filename, "r") as file:
        for line in file:
            t_type, amount, category, timestamp = line.strip().split(",")
            transactions.append({
                "type": t_type,
                "amount": float(amount),
                "category": category,
                "timestamp": timestamp
            })
    print("Data loaded successfully!")


     
# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice = ")
    if choice == "1":
        add_transaction("Income")
    elif choice == "2":
        add_transaction("Expense")
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        view_summary()
    elif choice == "5":
        save_data()
    elif choice == "6":
        load_data()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")   
        
        
      
    